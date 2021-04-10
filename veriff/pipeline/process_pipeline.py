from veriff.dto.context import Context
from veriff.handler.impl.data_loader_hander import DataLoaderHandler
from veriff.handler.impl.execution_handler import FaceVectorCalculatorHandler
from veriff.handler.impl.result_generate_handler import ResultGenerateHandler


def execute():
    data_loader_handler = DataLoaderHandler()
    face_vector_calculator = FaceVectorCalculatorHandler()
    result_generator_handler = ResultGenerateHandler()
    # define chain execution of handlers
    data_loader_handler.set_next(face_vector_calculator).set_next(result_generator_handler)
    data_loader_handler.handle(Context())
