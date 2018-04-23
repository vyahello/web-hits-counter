from abc import ABC, ABCMeta, abstractmethod
from typing import Any


class ContextManager(ABC):
    """Represent context manager object.
    :Example:
        with Object(...) as obj:
            obj.do_some(...)
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __enter__(self) -> Any:
        pass

    @abstractmethod
    def __exit__(self, exc_type: Any = None, exc_val: Any = None, exc_tb: Any = None) -> None:
        pass
