import time
from veriff.helper.logger_util import get_logger
from veriff import pipeline

logger = get_logger(__name__)

if __name__ == "__main__":
    start_time = time.time()
    logger.info("application starting")
    status = pipeline.execute()
    logger.info("application stopped status:%s. took %r seconds"
                , "OK" if status else "FAILED"
                , (time.time() - start_time))
