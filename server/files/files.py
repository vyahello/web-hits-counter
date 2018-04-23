from abc import abstractmethod
from typing import Any, ContextManager


class File(ContextManager):
    """Represent abstraction for log file object."""

    @abstractmethod
    def write(self, data: str) -> None:
        pass

    @abstractmethod
    def read(self) -> str:
        pass


class TextFile(File):
    """Represent simple text file object."""

    def __init__(self, file: str, mode: str) -> None:
        self._stream = open(file, mode)

    def write(self, data: str) -> None:
        self._stream.write(data)

    def read(self) -> str:
        return ''.join(self._stream.readlines())

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any = None, exc_val: Any = None, exc_tb: Any = None) -> None:
        return self._stream.close()


class LogFile(File):
    """Represent log file object for flask application."""

    def __init__(self, file: str, mode: str = 'r') -> None:
        self._file = TextFile(file, mode)  # type: File

    def write(self, data: str) -> None:
        self._file.write(data)

    def read(self) -> str:
        return self._file.read()

    def __enter__(self) -> Any:
        return self._file.__enter__()

    def __exit__(self, exc_type: Any = None, exc_val: Any = None, exc_tb: Any = None) -> None:
        return self._file.__exit__(exc_type, exc_val, exc_tb)
