import os
from server.counters import Counter, FlaskCounter
from server.files import clear_logs, LogFile
from server.servers import Server, WebServer

server: Server = WebServer()
_counter: Counter = FlaskCounter()
_log: str = os.path.abspath('logs/data.log')

clear_logs(_log)


@server.route('/')
def hello() -> str:
    _counter.increment()
    response: str = 'Get request occurred {} time(s)\n'.format(_counter.total())
    with LogFile(_log, mode='a') as lg:
        lg.write(response)
    return response


@server.route('/logs')
def logs() -> str:
    with LogFile(_log) as lg:
        return lg.read()
