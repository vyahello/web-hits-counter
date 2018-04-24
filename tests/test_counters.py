import pytest
from server.counters.counters import Counter, FlaskCounter

_counts: int = 5


@pytest.fixture(scope='module')
def counter():
    return FlaskCounter()


def test_counter(counter: Counter):
    for _ in range(_counts):
        counter.increment()
    assert counter.total() == _counts
