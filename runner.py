from veriff.util.logger_util import get_logger
from veriff import pipeline

logger = get_logger(__name__)

if __name__ == "__main__":
    logger.info("Application starting")
    status = pipeline.execute()
    logger.info("Application stopped status:%r", status)
