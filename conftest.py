"""Pytest configuration for stable doctests.

This keeps doctest examples deterministic by intercepting network calls to
example.com that appear in documentation snippets.
"""

from __future__ import annotations

from typing import Any
from urllib.parse import urlparse

import httpx
import pytest
from _pytest.doctest import DoctestItem


def _is_example_com(url: str) -> bool:
    """Return True for doctest placeholder URLs."""
    parsed = urlparse(url)
    return parsed.netloc == "example.com"


def _mock_example_response(method: str, url: str) -> httpx.Response:
    """Build a fake HTTPX response for example.com doctest URLs."""
    request = httpx.Request(method=method.upper(), url=url)
    path = urlparse(url).path

    headers: dict[str, str] = {}
    content = b"ok"

    if path == "/download/file.pdf":
        content = b"%PDF-1.7 fake"
        headers["content-disposition"] = 'attachment; filename="file.pdf"'
    elif path == "/download/file":
        content = b"file-bytes"
        headers["content-disposition"] = 'attachment; filename="file"'
    elif path in {"/upload", "/upload-binary"}:
        content = b'{"ok": true}'
        headers["content-type"] = "application/json"

    return httpx.Response(
        status_code=200, headers=headers, content=content, request=request
    )


@pytest.fixture(autouse=True)
def _mock_example_network_for_doctests(
    monkeypatch: pytest.MonkeyPatch, request: pytest.FixtureRequest
) -> None:
    """Mock example.com calls only while running doctests."""
    if not isinstance(request.node, DoctestItem):
        return

    original_sync_request = httpx.Client.request
    original_async_request = httpx.AsyncClient.request

    def mocked_sync_request(
        self: httpx.Client,
        method: str,
        url: str | httpx.URL,
        *args: Any,
        **kwargs: Any,
    ) -> httpx.Response:
        url_str = str(url)
        if _is_example_com(url_str):
            return _mock_example_response(method=method, url=url_str)
        return original_sync_request(self, method, url, *args, **kwargs)

    async def mocked_async_request(
        self: httpx.AsyncClient,
        method: str,
        url: str | httpx.URL,
        *args: Any,
        **kwargs: Any,
    ) -> httpx.Response:
        url_str = str(url)
        if _is_example_com(url_str):
            return _mock_example_response(method=method, url=url_str)
        return await original_async_request(self, method, url, *args, **kwargs)

    monkeypatch.setattr(httpx.Client, "request", mocked_sync_request)
    monkeypatch.setattr(httpx.AsyncClient, "request", mocked_async_request)
