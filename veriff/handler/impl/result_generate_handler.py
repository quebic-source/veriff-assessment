from veriff.dto.context import Context
from veriff.handler.abstract_handler import AbstractHandler
from veriff.util.logger_util import get_logger

logger = get_logger(__name__)


class ResultGenerateHandler(AbstractHandler):
    def handle(self, context: Context):
        logger.info("ResultGenerateHandler start")
        logger.info("!!!! result !!!")
        logger.info(context.result)
        logger.info("ResultGenerateHandler done")