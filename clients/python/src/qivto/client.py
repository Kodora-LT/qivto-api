from __future__ import annotations

import json as jsonlib
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class QivtoApiError(RuntimeError):
    def __init__(self, message: str, status: int, response: dict[str, Any] | None = None):
        super().__init__(message)
        self.status = status
        self.response = response


class QivtoClient:
    def __init__(self, base_url: str = "https://qivto.com/api/v1", timeout: float = 20.0, transport: Any = None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.transport = transport or urlopen

    def tools(self, language: str = "en") -> dict[str, Any]:
        return self._request("GET", "/tools", params={"lang": "lt" if language == "lt" else "en"})

    def uuid(self, count: int = 1) -> dict[str, Any]:
        return self._request("POST", "/uuid", json={"count": max(1, min(100, count))})

    def hash(self, text: str, algorithm: str = "sha256") -> dict[str, Any]:
        return self._request("POST", "/hash", json={"text": text, "algorithm": algorithm})

    def format_json(self, value: Any) -> dict[str, Any]:
        return self._request("POST", "/json-format", json={"json": value})

    def status(self) -> dict[str, Any]:
        return self._request("GET", "/status")

    def _request(self, method: str, path: str, params: dict[str, Any] | None = None, json: Any = None) -> dict[str, Any]:
        url = self.base_url + path
        if params:
            url += "?" + urlencode(params)
        body = None if json is None else jsonlib.dumps(json).encode("utf-8")
        request = Request(
            url,
            data=body,
            method=method,
            headers={"Accept": "application/json", "Content-Type": "application/json"},
        )
        try:
            with self.transport(request, timeout=self.timeout) as response:
                return self._decode(response.read(), response.status)
        except HTTPError as error:
            data = self._decode(error.read(), error.code, allow_error=True)
            raise QivtoApiError(str(data.get("error", "API request failed.")), error.code, data) from error
        except URLError as error:
            raise QivtoApiError(f"Unable to reach QIVTO: {error.reason}", 0) from error

    @staticmethod
    def _decode(raw: bytes, status: int, allow_error: bool = False) -> dict[str, Any]:
        try:
            data = jsonlib.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, jsonlib.JSONDecodeError) as error:
            raise QivtoApiError("QIVTO returned invalid JSON.", status) from error
        if not isinstance(data, dict):
            raise QivtoApiError("QIVTO returned an unexpected response.", status)
        if status >= 400 and not allow_error:
            raise QivtoApiError(str(data.get("error", "API request failed.")), status, data)
        return data
