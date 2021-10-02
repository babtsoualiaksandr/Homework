import functools
import logging

formatt = "%(asctime)s; %(levelname)s; %(message)s"
logging.basicConfig(filename='log.log', filemode='w', level = logging.INFO, format=formatt)
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
            logger.info(f" function  {func.__name__}. return  result {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
            
    return wrapper