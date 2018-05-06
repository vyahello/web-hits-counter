import os
from server.files import TextFile, LogFile

_file: str = 'test.txt'
_input: str = 'data'


def test_file():
    with TextFile(_file, 'w') as f:
        f.write(_input)
    with TextFile(_file, 'r') as f:
        assert f.read() == _input
    os.remove(_file)


def test_log():
    with LogFile(_file, 'w') as log:
        log.write(_input)
    with LogFile(_file, 'r') as log:
        assert log.read() == _input
    os.remove(_file)
