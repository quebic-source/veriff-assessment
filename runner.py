from veriff.util.logger_util import get_logger
from veriff.pipeline import process_pipeline

logger = get_logger(__name__)

if __name__ == "__main__":
    logger.info("start")
    process_pipeline.execute()
    logger.info("completed")
