

__all__ = [
    'Counter'
]


class Counter:

    def __init__(self, start: int = 0, stop: int = -1):
        self.__stop = stop
        self.__counter = start

    def setMaxPrice(self, price):
        self.__maxprice = price

    def get(self):
        if self.__stop == -1:
            return self.__counter
        else:
            return self.__counter if self.__counter < self.__stop else self.__stop
 
    def increment(self):
        if self.__stop == -1:
            self.__counter += 1
        else:
            self.__counter =  self.__counter +1 if self.__counter < self.__stop else self.__stop
            return 'Maximal value is reached.'

if __name__ == '__main__':
    pass
