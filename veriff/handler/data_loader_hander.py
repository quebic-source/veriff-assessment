import os
import time

from veriff.consts import DATA_SET_URL_ENV
from veriff.consts import DATA_SET_DIR_ENV
from veriff.data.context import Context
from veriff.handler import AbstractHandler
from veriff.helper.exception import ConfigurationMissingError
from veriff.helper.file_util import download_and_unzip, list_files
from veriff.helper.logger_util import get_logger

logger = get_logger(__name__)


class DataLoaderHandler(AbstractHandler):
    """
        DataLoaderHandler is used to prepare data set
    """
    def handle(self, context: Context):
        start_time = time.time()
        logger.info("data-set loading start")

        data_set_url = os.getenv(DATA_SET_URL_ENV)
        if not data_set_url:
            raise ConfigurationMissingError("please config {} environment variable".format(DATA_SET_URL_ENV))

        data_set_dir = os.getenv(DATA_SET_DIR_ENV, "data_set")
        download_and_unzip(data_set_url, data_set_dir)

        # get list by the file pattern data_set_dir/<unzip_dir>/<name_dir>/<image>.<ext>
        context.data_set = list_files(data_set_dir + "/*/*/*.*")

        logger.info("data-set loading completed. took %r seconds", (time.time() - start_time))
        self.next.handle(context)
