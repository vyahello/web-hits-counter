import pytest
from server.connections.requests import SafeGet
from server.connections.responses import Response, HttpResponseError

_url: str = 'http://localhost:9999'
_success: int = 200


@pytest.fixture(scope='module')
def url_response() -> Response:
    return SafeGet(_url).response()


@pytest.fixture(scope='module')
def log_response() -> Response:
    return SafeGet(_url + '/logs').response()


def test_server_url(url_response: Response) -> None:
    assert len(url_response.as_str()) > 0


def test_url_status_code(url_response: Response) -> None:
    assert url_response.status_code() == _success


def test_server_logs(log_response: Response) -> None:
    assert len(log_response.as_str()) > 0


def test_logs_status_code(log_response: Response) -> None:
    assert log_response.status_code() == _success


def test_server_url_not_exists() -> None:
    with pytest.raises(HttpResponseError):
        SafeGet(_url + '/not_exists').response()
