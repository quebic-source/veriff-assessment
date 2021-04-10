from veriff.data.context import Context
from veriff.handler.data_loader_hander import DataLoaderHandler
from veriff.handler.execution_handler import FaceVectorCalculatorHandler
from veriff.handler.result_generate_handler import ResultGenerateHandler
from veriff.util.logger_util import get_logger

logger = get_logger(__name__)


def execute() -> bool:
    """
    Execution point of process pipeline
    :return: bool
    """
    try:
        data_loader_handler = DataLoaderHandler()
        face_vector_calculator = FaceVectorCalculatorHandler()
        result_generator_handler = ResultGenerateHandler()
        # define chain execution of handlers
        data_loader_handler.set_next(face_vector_calculator).set_next(result_generator_handler)
        data_loader_handler.handle(Context())
        return True
    except Exception:
        logger.exception("pipeline execution failed")
        return False
