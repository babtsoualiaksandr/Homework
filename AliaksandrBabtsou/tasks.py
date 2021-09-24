from collections import OrderedDict
import string


__all__ = [
    'Counter',
    'HistoryDict',
    'Cipher',
    'Bird',
    'FlyingBird',
    'NonFlyingBird',
    'SuperBird',

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

class NonFlyingBird(FlyingBird):
    def __init__(self, name, *args):
        super().__init__(name, *args)
    
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



class SuperBird(Bird):
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


if __name__ == '__main__':
    pass
