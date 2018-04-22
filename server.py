from flask import Flask
from server.counters.counters import Counter, FlaskCounter
from server.logs.logs import FlaskLogFile

_server = Flask(__name__)  # type: Flask
_counter = FlaskCounter()  # type: Counter
_log = 'logs/data.log'


def _clear_logs() -> None:
    with FlaskLogFile(_log, mode='w') as lg:
        lg.write('')


@_server.route('/')
def hello() -> str:
    _counter.increment()
    response = 'Get request occurred {} time(s)\n'.format(_counter.total())
    with FlaskLogFile(_log, mode='a') as lg:
        lg.write(response)
    return response


@_server.route('/logs')
def logs() -> str:
    with FlaskLogFile(_log) as lg:
        return lg.read()


if __name__ == "__main__":
    _clear_logs()
    _server.run(host="0.0.0.0", port=9999, debug=True)
