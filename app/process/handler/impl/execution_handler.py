import time
import multiprocessing as mp
from multiprocessing import Pool
from app.process.context import Context
from app.process.handler.abstract_handler import AbstractHandler


def f(x):
    time.sleep(20)
    return x*x


class FaceVectorCalculatorHandler(AbstractHandler):
    def handle(self, context: Context):
        print("FaceVectorCalculatorHandler start")

        face_images_data_list = context.data_set

        cpu_count = mp.cpu_count()
        pool_size = min(cpu_count, len(face_images_data_list))
        with Pool(pool_size) as p:
            context.result = p.map(f, face_images_data_list)

        print("FaceVectorCalculatorHandler done")
        self.next.handle(context)