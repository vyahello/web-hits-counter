from server.connections.responses import HttpResponse


class _FakeRequestsResponse:
    def __init__(self, status_code: int, content: bytes, json_data: dict[str, int]) -> None:
        self.status_code: int = status_code
        self.content: bytes = content
        self._json_data: dict[str, int] = json_data

    def json(self) -> dict[str, int]:
        return self._json_data


def test_http_response_adapts_requests_response() -> None:
    raw = _FakeRequestsResponse(status_code=201, content=b"ok", json_data={"a": 1})
    resp = HttpResponse(raw)  # type: ignore[arg-type]

    assert resp.status_code() == 201
    assert resp.as_str() == str(b"ok")
    assert resp.as_dict() == {"a": 1}

