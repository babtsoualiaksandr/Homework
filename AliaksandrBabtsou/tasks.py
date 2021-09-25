from enum import Enum
from collections import OrderedDict
import string
from typing import List


__all__ = [
    'Counter',
    'HistoryDict',
    'Cipher',
    'Bird',
    'FlyingBird',
    'NonFlyingBird',
    'SuperBird',
    'Sun',
    'Money',
    'Pagination'

]


class Counter:

    def __init__(self, start: int = 0, stop: int = -1):
        self.__stop = stop
        self.__counter = start

    def get(self):
        if self.__stop == -1:
            return self.__counter
        else:
            return self.__counter if self.__counter < self.__stop else self.__stop

    def increment(self):
        if self.__stop == -1:
            self.__counter += 1
        else:
            self.__counter = self.__counter + 1 if self.__counter < self.__stop else self.__stop
            return 'Maximal value is reached.'


class HistoryDict(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__items = []

    def __setitem__(self, key, value):
        super(HistoryDict, self).__setitem__(key, value)
        self.__items.append(key)

    def set_value(self, key, value):
        self.__setitem__(key, value)

    def get_history(self):
        return self.__items[-10:]


class Cipher:
    def __init__(self, keyword):
        self._keyword = keyword

        def rem_val_from_str(is_str, val):
            for char in val:
                is_str = [value for value in is_str if value != char]
            return ''.join(is_str)
        alphabet = string.ascii_uppercase
        alphabet_cod = self._keyword.upper() + rem_val_from_str(alphabet,
                                                                self._keyword.upper())
        alphabet_cod = alphabet_cod + alphabet_cod.lower()+' '
        self.__encode = {iter[0]: iter[1] for iter in zip(
            alphabet+alphabet.lower()+' ', alphabet_cod)}
        self.__decode = {iter[1]: iter[0] for iter in zip(
            alphabet+alphabet.lower()+' ', alphabet_cod)}

    def encode(self, val):
        return ''.join([self.__encode[iter] for iter in val])

    def decode(self, val):
        return ''.join([self.__decode[iter] for iter in val])


# import antigravity


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f'{self.name} fly'

    def walk(self):
        return f'{self.name} bird can walk'


class FlyingBird(Bird):
    def __init__(self, name, *args):
        if not any(args):
            self.ration = 'grains'
        else:
            self.ration = args
        super().__init__(name)

    def eat(self):
        return f'It eats mostly {self.ration if isinstance(self.ration,str) else ",".join(self.ration)}'

    def __str__(self) -> str:
        return f'{self.name} can walk and fly'


class NonFlyingBird(Bird):
    def __init__(self, name, *args):
        if not any(args):
            self.ration = 'fish'
        else:
            self.ration = args
        super().__init__(name)

    def swim(self):
        return f'{self.name} bird can swim'

    def __getattribute__(self, name):
        if name in ['fly']:
            raise AttributeError(
                f'{self.name} nobject has no attribute {name!r}')
        return super(NonFlyingBird, self).__getattribute__(name)

    def __str__(self) -> str:
        return f'{self.name} can walk and fly'

    def eat(self):
        return f'It eats mostly {self.ration if isinstance(self.ration,str) else ",".join(self.ration)}'


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, *args):
        if not any(args):
            self.ration = 'fish'
        else:
            self.ration = args
        super().__init__(name)

    def swim(self):
        return f'{self.name} swim'

    def __str__(self) -> str:
        return f'{self.name} can walk, swim and fly'

    def eat(self):
        return f'It eats {self.ration if isinstance(self.ration,str) else ",".join(self.ration)}'


class Sun():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        print('instance created')

    @classmethod
    def inst(cls, *args, **kwargs):
        return cls.__new__(cls, *args, **kwargs)


class Money:
    exchange_rate = {
        'EUR': 0.93,
        'BYN': 2.1,
        'RUB': 70,
        'JPY': 0.0090,
        'USD': 1
    }

    def __init__(self, value: float, exchange: str = 'USD'):
        self._value = value
        self._extange = exchange

    def __str__(self) -> str:
        return f'{self._value:.2f} {self._extange}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__ }({self._value:.2f},{self._extange!r})'

    def __add__(self, other):
        try:
            rate = Money.exchange_rate[other._extange] / \
                Money.exchange_rate[self._extange]
            return Money(self._value + other._value / rate, self._extange)
        except AttributeError:
            print(self, other)
            return Money(self._value, self._extange)
    __radd__ = __add__

    def __iadd__(self, other):
        rate = Money.exchange_rate[other._extange] / \
            Money.exchange_rate[self._extange]
        return Money(self._value + other._value * rate, self._extange)

    def __sub__(self, other):
        return Money(self._value - other._value, self._extange)

    def __mul__(self, val):
        return Money(self._value * val, self._extange)

    def __rmul__(self, val):
        return Money(self._value * val, self._extange)

    def __truediv__(self, other):
        return Money(self._value / other._value, self._extange)

    # <
    def __lt__(self, other):
        rate = Money.exchange_rate[other._extange] / \
            Money.exchange_rate[self._extange]
        return self._value < other._value / rate
    # >

    def __gt__(self, other):
        rate = Money.exchange_rate[other._extange] / \
            Money.exchange_rate[self._extange]
        return self._value > other._value / rate
    # <=

    def __le__(self, other):
        rate = Money.exchange_rate[other._extange] / \
            Money.exchange_rate[self._extange]
        return self._value <= other._value / rate
    # >=

    def __ge__(self, other):
        rate = Money.exchange_rate[other._extange] / \
            Money.exchange_rate[self._extange]
        return self._value >= other._value / rate
    # ==

    def __eq__(self, other):
        rate = Money.exchange_rate[other._extange] / \
            Money.exchange_rate[self._extange]
        return self._value == other._value / rate
    #!=

    def __ne__(self, other):
        rate = Money.exchange_rate[other._extange] / \
            Money.exchange_rate[self._extange]
        return self._value != other._value / rate


class Pagination:
    def __init__(self, text: str, size_page: int) -> None:
        self.text = text
        self.size_page=size_page
        self.pages = [text[idx:idx+size_page]
                      for idx in range(0, len(text), size_page)]
        self.page_count = len(self.pages)
        self.item_count = len(text)

    def count_items_on_page(self, page_number: int) -> int:
        try:
            return len(self.pages[page_number])
        except IndexError:
            return f'Exception: Invalid index. Page is missing.'

    def find_page(self, search_str: str) -> List[int]:
        idxes_start = [i for i in range(len(self.text)) if self.text.startswith(search_str, i)]
        if not len(idxes_start):
            return f"Exception: '{search_str}' is missing on the pages"
        else:
            result=set()
            for idx in idxes_start:
                print(idx) 
                result.add(idx//self.size_page)
                result.add((idx+len(search_str))//self.size_page)
            return list(result)

    def display_page(self, page_number: int) -> str:
        return self.pages[page_number]

if __name__ == '__main__':
    s = SuperBird("Gull")
    SuperBird.__mro__
