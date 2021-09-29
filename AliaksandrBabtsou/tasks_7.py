from contextlib import ContextDecorator
import logging
from contextlib import contextmanager
import tempfile
import os
import sys

__all__ = (
    'FileContex',
    'file_contex',
    'TrackEntryAndExit',
    'try_exc',
    'is_even'
)


class FileContex:
    def __init__(self, path: str, mode: str = 'w', encoding: str = 'utf-8'):
        self.path = path
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        if self.mode == 'w':
            self.temp_file = tempfile.NamedTemporaryFile(
                self.mode,
                encoding=self.encoding,
                delete=False,
            )
            return self.temp_file
        else:
            self.file = open(self.path, self.mode)
            return self.file

    def __exit__(self, exception, exception_msg, trace_back):
        if self.mode == 'w':
            self.temp_file.close()
            if exception is None:
                os.rename(self.temp_file.name, self.path)
            else:
                os.unlink(self.temp_file)
        else:
            self.file.close()


@contextmanager
def file_contex(path: str, mode: str, encoding: str = 'utf-8'):
    f = open(path, mode=mode, encoding=encoding)
    try:
        yield f
    except Exception as exc:
        print(exc)
    finally:
        f.close()


class TrackEntryAndExit(ContextDecorator):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __enter__(self):
        logging.info(f'{self.name} Entering: %s')
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        if exc_type:
            logging.error(f'{self.name} {exc} {exc_tb}')
        logging.info(f'{self.name} Exiting: %s')


logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )
def try_exc(fun):
    def wrapped(*args, **kwargs):
        try:
            result = fun(*args, **kwargs)
            logging.info(f'{fun.__name__} result {result}')
            return result            
        except Exception as e:            
            logging.error(f'{fun.__name__} {e}')
    return wrapped


class ErorrEven(ValueError):
    pass


class ValueNotEven(ErorrEven):
    pass


class ValueNotNumberInt(ErorrEven):
    pass



def is_even(number : int) -> bool:
    if not isinstance(number,int):
        raise ValueNotNumberInt('ValueNotNumberInt')
    if number % 2 !=0:
        raise ValueNotEven('ValueTooDamnNumber')
    return True


