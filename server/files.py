from abc import ABC, ABCMeta, abstractmethod
from typing import TextIO


class TextFile(ABC):
    """Represent abstraction for a text file object."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def open(self) -> TextIO:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class FlaskTextFile(TextFile):
    """Represent text file for a flask application."""

    def __init__(self, file: str, mode: str) -> None:
        self._file = open(file, mode)

    def open(self) -> TextIO:
        return self._file

    def close(self) -> None:
        self._file.close()
