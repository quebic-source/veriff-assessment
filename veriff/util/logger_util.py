import logging
import time


def measure_time(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('%r (%r, %r) %2.2f sec' % (f.__name__, args, kw, te - ts))
        return result


def get_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # '%(asctime)s - {%(pathname)s:%(lineno)d} - %(name)s - %(levelname)s - %(message)s',
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s',
        datefmt='%Y/%m/%d %I:%M:%S %p'
    )

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


logger = get_logger(__name__)
