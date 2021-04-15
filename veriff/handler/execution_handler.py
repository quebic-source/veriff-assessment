import time
import os
import numpy as np
import face_recognition
from veriff.data.context import Context
from veriff.handler import AbstractHandler
from veriff.helper.logger_util import get_logger
import ray
from veriff.consts import RUNNING_MODE_ENV, HEAD_SERVICE_IP_ENV, HEAD_SERVICE_CLIENT_PORT_ENV


logger = get_logger(__name__)


@ray.remote
def face_encodings(image_path):
    image_data = face_recognition.load_image_file(image_path)

    face_vectors = face_recognition.face_encodings(image_data)
    if not face_vectors:
        logger.warning("face encodings failed. vector not found for image %r", image_path)
        # return empty array
        return np.empty((128,), dtype=int)

    return face_vectors[0]


class FaceVectorCalculatorHandler(AbstractHandler):
    """
        FaceVectorCalculatorHandler is used to calculate average face vector
    """
    def handle(self, context: Context):
        start_time = time.time()
        logger.info("face-vector calculator start")

        face_images_data_list = context.data_set

        # ray init
        running_mode = os.getenv(RUNNING_MODE_ENV, 'local')
        if running_mode == 'local':
            ray.init()
        else:
            # Kubernetes inject ip address of ray cluster head service into head_svc env variable
            head_service_ip = os.environ[os.environ[HEAD_SERVICE_IP_ENV]]
            client_port = os.environ[os.environ[HEAD_SERVICE_CLIENT_PORT_ENV]]
            ray.util.connect(f"{head_service_ip}:{client_port}")
        logger.info("ray init done")

        refs = [face_encodings.remote(image_path) for image_path in face_images_data_list]
        face_vectors = ray.get(refs)
        logger.info("face-encoding jobs completed")

        # average operation on vectors
        context.result = np.mean(face_vectors, axis=0)
        logger.info("face-vector calculator completed. took %r seconds", (time.time() - start_time))
        self.next.handle(context)

