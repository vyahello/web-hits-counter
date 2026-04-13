import pytest

from server.connections.requests import SafeGet
from server.connections.responses import HttpResponseError, Response


class _StubResponse(Response):
    def __init__(self, code: int) -> None:
        self._code: int = code

    def status_code(self) -> int:  # type: ignore[override]
        return self._code

    def as_str(self) -> str:
        return "x"

    def as_dict(self) -> dict[str, int]:
        return {"x": 1}


class _StubRequest:
    def __init__(self, response: Response) -> None:
        self._response = response

    def response(self) -> Response:
        return self._response


def test_safe_get_returns_response_when_status_ok() -> None:
    sg = SafeGet("http://example", status_code=200)
    ok = _StubResponse(200)
    sg._req = _StubRequest(ok)  # type: ignore[attr-defined]

    assert sg.response() is ok


def test_safe_get_raises_when_status_not_ok() -> None:
    sg = SafeGet("http://example", status_code=200)
    bad = _StubResponse(500)
    sg._req = _StubRequest(bad)  # type: ignore[attr-defined]

    with pytest.raises(HttpResponseError):
        sg.response()

