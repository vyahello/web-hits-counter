from server.connections.api import ApiSession
from server.connections.responses import HttpResponse


class _FakeSession:
    def __init__(self, response: object) -> None:
        self._response: object = response
        self.calls: list[dict[str, object]] = []

    def get(self, url: str, verify: bool = True) -> object:
        self.calls.append({"url": url, "verify": verify})
        return self._response


class _FakeRequestsResponse:
    def __init__(self, status_code: int = 200) -> None:
        self.status_code: int = status_code
        self.content: bytes = b""

    def json(self) -> dict[object, object]:
        return {}


def test_api_session_get_calls_verify_false() -> None:
    url = "http://localhost:9999"
    raw = _FakeRequestsResponse(status_code=200)
    fake_session = _FakeSession(raw)

    api = ApiSession(url, session=fake_session)  # type: ignore[arg-type]
    resp = api.get()

    assert isinstance(resp, HttpResponse)
    assert fake_session.calls == [{"url": url, "verify": False}]

