import pytest
from requests import get, Response


_url: str = 'http://127.0.0.1:9999'
_success: int = 200


@pytest.fixture(scope='module')
def url_setup() -> Response:
    return get(_url)


@pytest.fixture(scope='module')
def log_setup() -> Response:
    return get(_url + '/logs')


def test_server_url(url_setup: Response) -> None:
    assert len(url_setup.text) > 0


def test_url_status_code(url_setup: Response) -> None:
    assert url_setup.status_code == _success


def test_server_logs(log_setup: Response) -> None:
    assert len(log_setup.text) > 0


def test_logs_status_code(log_setup: Response) -> None:
    assert log_setup.status_code == _success
