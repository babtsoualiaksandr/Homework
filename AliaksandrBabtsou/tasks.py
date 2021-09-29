from contextlib import ContextDecorator
import logging
from contextlib import contextmanager
import tempfile
import os
import sys

__all__ = [
    'FileContex',
    'file_contex',
    'TrackEntryAndExit',
    'try_exc',
    'is_even'
]


class FileContex:
    """
        Implement class-based context manager for opening and working with file, including handling 
        exceptions. Do not use 'with open()'. Pass filename and mode via constructor.
    """

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
    """
    file_contex [Implement context manager for opening and working with file, 
    including handling exceptions with @contextmanager decorator.]

    [Implement context manager for opening and working with file, 
    including handling exceptions with @contextmanager decorator.]

    :param path: [description]
    :type path: str
    :param mode: [description]
    :type mode: str
    :param encoding: [description], defaults to 'utf-8'
    :type encoding: str, optional
    :yield: [description]
    :rtype: [type]
    """
    f = open(path, mode=mode, encoding=encoding)
    try:
        yield f
    except Exception as exc:
        print(exc)
    finally:
        f.close()


class TrackEntryAndExit(ContextDecorator):
    """
        Implement decorator with context manager support for writing execution time to log-file. 
        See contextlib module.
    """
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
    """
    Implement decorator for supressing exceptions. If exception not occure write log to console.
    """
    def wrapped(*args, **kwargs):
        try:
            result = fun(*args, **kwargs)
            logging.info(f'{fun.__name__} result {result}')
            return result
        except Exception as e:
            logging.error(f'{fun.__name__} {e}')
    return wrapped



## Implement function for check that number is even and is greater than 2. Throw different exceptions for this errors. 
# Custom exceptions must be derived from custom base exception(not Base Exception class).

class ErorrEven(ValueError):
    pass


class ValueNotEven(ErorrEven):
    pass


class ValueNotNumberInt(ErorrEven):
    pass

class ValueisGreaterThanTwo(ErorrEven):
    pass


def is_even(number: int) -> bool:
    """
    is_even [check that number is even]

    [check that number is even]

    :param number: [description]
    :type number: int
    :raises ValueNotNumberInt: [description]
    :raises ValueNotEven: [description]
    :return: [description]
    :rtype: bool
    """
    if not isinstance(number, int):
        raise ValueNotNumberInt('Number not integer')
    if number < 3:
        raise ValueNotEven('Integer not greater than 2 ')
    if number % 2 != 0:
        raise ValueNotEven('Value Not Even')
    return True


## Create console program for proving Goldbach's conjecture. Program accepts number for input and print result. For pressing 'q' program succesfully close. 
## Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.

def goldbach():
    import math
    MAX = 10000

    primes = []
    
    def sieveSundaram():
        marked = [False] * (int(MAX / 2) + 100)
        for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
            for j in range((i * (i + 1)) << 1,
                            int(MAX / 2) + 1, 2 * i + 1):
                marked[j] = True
        primes.append(2)
        for i in range(1, int(MAX / 2) + 1):
            if (marked[i] == False):
                primes.append(2 * i + 1)
    
    def findPrimes(n):
        if not is_even(n):
            print("Invalid Input")
            return
        i = 0
        while (primes[i] <= n // 2):
            diff = n - primes[i]
            if diff in primes:
                print(primes[i], "+", diff, "=", n)
                return
            i += 1

    
    while True:
        input_number = input('Please enter an even number greater than 3, Break <q>')
        if input_number == 'q': 
            break

        try:
            if is_even(int(input_number)):
                sieveSundaram()
                findPrimes(int(input_number))
        except ValueError as exc:
            print(exc)
        finally:
            continue

            

