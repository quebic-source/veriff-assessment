import time
import multiprocessing as mp
from multiprocessing import Pool
from veriff.data.context import Context
from veriff.handler import AbstractHandler
from veriff.util.logger_util import get_logger

logger = get_logger(__name__)


def f(x):
    time.sleep(1)
    return x*x


class FaceVectorCalculatorHandler(AbstractHandler):
    """
        FaceVectorCalculatorHandler is used to calculate average face vector
    """
    def handle(self, context: Context):
        logger.info("FaceVectorCalculatorHandler start")

        face_images_data_list = context.data_set

        cpu_count = mp.cpu_count()
        pool_size = min(cpu_count, len(face_images_data_list))
        with Pool(pool_size) as p:
            context.result = p.map(f, face_images_data_list)

        logger.info("FaceVectorCalculatorHandler done")
        self.next.handle(context)