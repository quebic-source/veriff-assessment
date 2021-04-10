from veriff.data.context import Context
from veriff.handler import AbstractHandler
from veriff.util.logger_util import get_logger

logger = get_logger(__name__)


class ResultGenerateHandler(AbstractHandler):
    """
        ResultGenerateHandler is used to prepare result
    """
    def handle(self, context: Context):
        logger.info("ResultGenerateHandler start")
        logger.info("!!!! result !!!")
        logger.info(context.result)
        logger.info("ResultGenerateHandler done")
        raise ValueError()