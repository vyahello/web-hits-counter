from server.servers import Server, WebServer
from server.counters import Counter, FlaskCounter
from server.files import LogFile

_server: Server = WebServer()
_counter: Counter = FlaskCounter()
_log: str = 'logs/data.log'


def _clear_logs() -> None:
    with LogFile(_log, mode='w') as lg:
        lg.write('')


@_server.route('/')
def hello() -> str:
    _counter.increment()
    response: str = 'Get request occurred {} time(s)\n'.format(_counter.total())
    with LogFile(_log, mode='a') as lg:
        lg.write(response)
    return response


@_server.route('/logs')
def logs() -> str:
    with LogFile(_log) as lg:
        return lg.read()


if __name__ == "__main__":
    _clear_logs()
    _server.run()
