from abc import abstractmethod, ABC
import requests
import urllib3
from server.connections.responses import Response, HttpResponse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Session(ABC):
    """The abstraction of an API session."""

    @abstractmethod
    def get(self) -> Response:
        """Send a GET request."""
        pass


class ApiSession(Session):
    """Represent standard API session."""

    def __init__(self, url: str, session: requests.Session = requests.Session()) -> None:
        self._session: requests.Session = session
        self._url: str = url

    def get(self) -> Response:
        return HttpResponse(self._session.get(self._url, verify=False))
