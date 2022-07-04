import abc
from typing import Callable


class Worker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def task(self, fn: Callable = None, *args, **kwargs):
        pass
