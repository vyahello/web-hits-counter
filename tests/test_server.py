import requests

_url = 'http://127.0.0.1:9999'
_log = 'logs/data.log'


def test_server_url():
    response = requests.get(_url).text
    assert len(response) > 0


def test_server_logs():
    response = requests.get(_url + '/logs').text
    assert len(response) > 0
