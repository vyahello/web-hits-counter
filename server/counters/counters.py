from abc import ABC, ABCMeta, abstractmethod


class Counter(ABC):
    """Represent abstraction for some counter object."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def increment(self) -> None:
        pass

    @abstractmethod
    def total(self) -> int:
        pass


class FlaskCounter(Counter):
    """Represent counter for flask application."""

    def __init__(self):
        self._occurrence = 0

    def increment(self) -> None:
        self._occurrence += 1

    def total(self) -> int:
        return self._occurrence
