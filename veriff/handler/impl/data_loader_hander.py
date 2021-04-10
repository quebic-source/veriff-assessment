from veriff.util.logger_util import logger
from veriff.dto.context import Context
from veriff.handler.abstract_handler import AbstractHandler


class DataLoaderHandler(AbstractHandler):
    def handle(self, context: Context):
        logger.info("DataLoaderHandler start")
        context.data_set = [1,2,3,4,5]
        logger.info("DataLoaderHandler done")
        self.next.handle(context)