from veriff.dto.context import Context
from veriff.handler.abstract_handler import AbstractHandler
from veriff.util.logger_util import get_logger

logger = get_logger(__name__)


class DataLoaderHandler(AbstractHandler):
    """
        DataLoaderHandler is used to prepare data set
    """
    def handle(self, context: Context):
        logger.info("DataLoaderHandler start")
        context.data_set = [1,2,3,4,5]
        logger.info("DataLoaderHandler done")
        self.next.handle(context)
