import time
import multiprocessing as mp
from multiprocessing import Pool
import numpy as np
import face_recognition
from veriff.data.context import Context
from veriff.handler import AbstractHandler
from veriff.helper.logger_util import get_logger

logger = get_logger(__name__)


def face_encodings(image_path):
    start_time = time.time()
    logger.info("face_encodings start %r", image_path)
    image_data = face_recognition.load_image_file(image_path)

    face_vectors = face_recognition.face_encodings(image_data)
    if not face_vectors:
        logger.error("face_encodings failed. not found vector. took %r seconds", (time.time() - start_time))
        return None

    face_vector = face_vectors[0]
    logger.info("face_encodings completed. took %r seconds", (time.time() - start_time))
    return face_vector


def average_of_vector(vectors):
    # TODO
    return vectors


class FaceVectorCalculatorHandler(AbstractHandler):
    """
        FaceVectorCalculatorHandler is used to calculate average face vector
    """
    def handle(self, context: Context):
        start_time = time.time()
        logger.info("face-vector calculator start")

        face_images_data_list = context.data_set

        # cpu_count = mp.cpu_count()
        # pool_size = min(cpu_count, len(face_images_data_list))
        # with Pool(pool_size) as p:
        #     face_vectors = p.map(face_encodings, face_images_data_list)
        #     context.result = len(face_vectors)
        #     logger.info("face-vector calculator completed. took %r seconds", (time.time() - start_time))
        #     self.next.handle(context)

        face_vectors = []
        for face_image_path in face_images_data_list:
            vector = face_encodings(face_image_path)
            if vector is not None:
                face_vectors.append(vector)

        context.result = len(face_vectors)
        logger.info("face-vector calculator completed. took %r seconds", (time.time() - start_time))
        self.next.handle(context)
