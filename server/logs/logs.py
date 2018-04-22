from abc import ABC, ABCMeta, abstractmethod
from typing import Any
from server.files import TextFile, FlaskTextFile


class LogFile(ABC):
    """Represent abstraction for log file object."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, data: str) -> int:
        pass

    @abstractmethod
    def read(self) -> str:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    def __exit__(self, exc_type: Any = None, exc_val: Any = None, exc_tb: Any = None) -> None:
        self.close()

    def __enter__(self) -> Any:
        return self


class FlaskLogFile(LogFile):
    """Represent log file object for flask application."""

    def __init__(self, file: str, mode: str = 'r') -> None:
        self._flow = FlaskTextFile(file, mode)  # type: TextFile

    def write(self, data: str) -> int:
        return self._flow.open().write(data)

    def read(self) -> str:
        return ''.join(self._flow.open().readlines())

    def close(self) -> None:
        self._flow.close()
