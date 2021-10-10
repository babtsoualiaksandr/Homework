import functools
import logging

formatt = "%(asctime)s; %(levelname)s; %(message)s"
logging.basicConfig(filename='rss_parser.log', filemode='a', level=logging.INFO, format=formatt)
logger = logging.getLogger()

log_stream = logging.StreamHandler()
log_stream.setLevel(logging.DEBUG)
formatter = logging.Formatter(formatt)
log_stream.setFormatter(formatter)


def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.info(f" function  {func.__name__}. args={args}, kwargs={kwargs} return  result {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__} args={args}, kwargs={kwargs}. exception: {str(e)}")

    return wrapper
