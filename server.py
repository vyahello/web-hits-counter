from flask import Flask
from server.counters.counters import Counter, FlaskCounter
from server.files.files import LogFile

_server = Flask(__name__)  # type: Flask
_counter = FlaskCounter()  # type: Counter
_log = 'logs/data.log'  # type: str


def _clear_logs() -> None:
    with LogFile(_log, mode='w') as lg:
        lg.write('')


@_server.route('/')
def hello() -> str:
    _counter.increment()
    response = 'Get request occurred {} time(s)\n'.format(_counter.total())
    with LogFile(_log, mode='a') as lg:
        lg.write(response)
    return response


@_server.route('/logs')
def logs() -> str:
    with LogFile(_log) as lg:
        return lg.read()


if __name__ == "__main__":
    _clear_logs()
    _server.run(host="0.0.0.0", port=9999, debug=True)
