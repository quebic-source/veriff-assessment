import logging


def get_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # '%(asctime)s - {%(pathname)s:%(lineno)d} - %(name)s - %(levelname)s - %(message)s',
    formatter = logging.Formatter(
        '%(asctime)s - {%(pathname)s:%(lineno)d} - %(levelname)s - %(message)s',
        datefmt='%Y/%m/%d %I:%M:%S %p'
    )

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


logger = get_logger(__name__)