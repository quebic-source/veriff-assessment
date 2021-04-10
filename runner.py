from veriff.util.logger_util import logger
from veriff.pipeline import process_pipeline

if __name__ == "__main__":
    logger.info("start")
    process_pipeline.execute()
    logger.info("completed")
