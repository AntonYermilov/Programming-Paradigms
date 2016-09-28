from collections.abc import Iterator
from collections import Counter, OrderedDict
import logging
import sys

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting {} to {}'.format(key, value))
        super().__setitem__(key, value)

class OrderedLoggingDict(LoggingDict, OrderedDict):
    pass

class OrderedCounter(Counter, OrderedDict):
    pass

class ReversedIterator(Iterator):
    def __init__(self, container):
        self.container = container
        self.index = len(self.container)

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.container[self.index]

class Window:
    def __init__(self, *args):
        super().__init__()
        self.window = 42

class WithBorder:
    def border(self):
        return self.window

class WithSlider:
   def slider(self):
       ...
       return self.window

class MyWindow(WithSlider, WithBorder, Window):
    pass

class A: pass
class B(A): pass
class C(A): pass
class D(B, A): pass

if __name__ == '__main__':
    print(*ReversedIterator(range(10)))
    print(MyWindow().border())
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    l = LoggingDict()
    l[1] = 2
    d = D()
