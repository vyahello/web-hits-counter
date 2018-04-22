import os
from io import TextIOWrapper
from server.files import FlaskTextFile

_file = 'test.txt'


def test_file():
    assert FlaskTextFile(_file, 'w').open().__class__ == TextIOWrapper
    os.remove(_file)
