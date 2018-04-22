import os
from server.logs.logs import FlaskLogFile

_file = 'test.txt'
_input = 'data'


def test_log():
    with FlaskLogFile(_file, 'w') as log:
        log.write(_input)
    with FlaskLogFile(_file, 'r') as log:
        assert log.read() == _input
    os.remove(_file)
