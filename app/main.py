from app.process.context import Context
from app.process.handler.impl.data_loader_hander import DataLoaderHandler
from app.process.handler.impl.execution_handler import FaceVectorCalculatorHandler
from app.process.handler.impl.result_generate_handler import ResultGenerateHandler

if __name__ == "__main__":
    print("start")

    data_loader_handler = DataLoaderHandler()
    face_vector_calculator = FaceVectorCalculatorHandler()
    result_generator_handler = ResultGenerateHandler()
    data_loader_handler.set_next(face_vector_calculator).set_next(result_generator_handler)

    data_loader_handler.handle(Context())

    print("completed")
