import pytest
import requests

_url = 'http://127.0.0.1:9999'


@pytest.fixture(scope='module')
def url_setup() -> str:
    return requests.get(_url).text


@pytest.fixture(scope='module')
def log_setup() -> str:
    return requests.get(_url + '/logs').text


def test_server_url(url_setup: str) -> None:
    assert len(url_setup) > 0


def test_server_logs(log_setup: str) -> None:
    assert len(log_setup) > 0
