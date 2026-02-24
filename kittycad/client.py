import ssl
import time
from typing import Any, Dict, Optional, Self, Tuple, Union

import attr
import httpx
import truststore

DEFAULT_BASE_URL = "https://api.zoo.dev"


def _normalize_operation_status(status_value: Any) -> str:
    """Normalize async operation status values to lowercase strings."""

    if hasattr(status_value, "value"):
        status_value = status_value.value

    if status_value is None:
        return "unknown"

    return str(status_value).lower()


def _extract_operation_payload_and_status(result: Any) -> Tuple[Any, str]:
    """Extract operation payload and normalized status from model/dict/RootModel."""

    if isinstance(result, dict):
        return result, _normalize_operation_status(result.get("status"))

    payload = result.root if hasattr(result, "root") else result

    if isinstance(payload, dict):
        return payload, _normalize_operation_status(payload.get("status"))

    if hasattr(payload, "status"):
        return payload, _normalize_operation_status(getattr(payload, "status"))

    return payload, "unknown"


@attr.s(auto_attribs=True)
class Client:
    """A Client which has been authenticated for use on secured endpoints of the KittyCAD API."""  # noqa: E501

    token: str = attr.ib(kw_only=True)
    base_url: str = attr.ib(default=DEFAULT_BASE_URL)
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(120.0, kw_only=True)
    websocket_recv_timeout: Optional[float] = attr.ib(60.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext, truststore.SSLContext] = attr.ib(
        True, kw_only=True
    )
    http_client: Optional[httpx.Client] = attr.ib(default=None, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        headers = {**self.headers}
        if getattr(self, "token", None):
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)

    def get_websocket_recv_timeout(self) -> Optional[float]:
        return self.websocket_recv_timeout

    def with_websocket_recv_timeout(self, timeout: Optional[float]) -> "Client":
        """Get a new client matching this one with a new websocket recv timeout"""
        return attr.evolve(self, websocket_recv_timeout=timeout)

    def with_base_url(self, url: str) -> "Client":
        """Get a new client matching this one with a new base url"""
        return attr.evolve(self, base_url=url)

    def get_http_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, creating it if necessary"""
        if self.http_client is None:
            self.http_client = httpx.Client(
                timeout=self.timeout,
                verify=self.verify_ssl,
                cookies=self.cookies,
            )
        return self.http_client

    def close(self) -> None:
        """Close the underlying HTTP client"""
        if self.http_client is not None:
            self.http_client.close()
            self.http_client = None

    def wait_for_async_operation(
        self,
        operation_id: str,
        timeout_seconds: float = 60.0,
        poll_interval_seconds: float = 2.0,
    ) -> Any:
        """Poll `/async/operations/{id}` until status is completed/failed or timeout.

        Returns the unwrapped operation payload model when available.
        """

        api_calls = getattr(self, "api_calls", None)
        if api_calls is None or not hasattr(api_calls, "get_async_operation"):
            raise RuntimeError(
                "`wait_for_async_operation` requires a KittyCAD client instance."
            )

        end_time = time.time() + timeout_seconds
        result = api_calls.get_async_operation(id=operation_id)
        payload, status = _extract_operation_payload_and_status(result)

        while status not in {"completed", "failed"} and time.time() < end_time:
            time.sleep(poll_interval_seconds)
            result = api_calls.get_async_operation(id=operation_id)
            payload, status = _extract_operation_payload_and_status(result)

        return payload

    def __enter__(self) -> Self:
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit"""
        self.close()


@attr.s(auto_attribs=True)
class AsyncClient:
    """An Async Client which has been authenticated for use on secured endpoints of the KittyCAD API."""  # noqa: E501

    token: str = attr.ib(kw_only=True)
    base_url: str = attr.ib(default=DEFAULT_BASE_URL)
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(120.0, kw_only=True)
    websocket_recv_timeout: Optional[float] = attr.ib(60.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext, truststore.SSLContext] = attr.ib(
        True, kw_only=True
    )
    http_client: Optional[httpx.AsyncClient] = attr.ib(default=None, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        headers = {**self.headers}
        if getattr(self, "token", None):
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def with_headers(self, headers: Dict[str, str]) -> "AsyncClient":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "AsyncClient":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "AsyncClient":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)

    def get_websocket_recv_timeout(self) -> Optional[float]:
        return self.websocket_recv_timeout

    def with_websocket_recv_timeout(self, timeout: Optional[float]) -> "AsyncClient":
        """Get a new client matching this one with a new websocket recv timeout"""
        return attr.evolve(self, websocket_recv_timeout=timeout)

    def with_base_url(self, url: str) -> "AsyncClient":
        """Get a new client matching this one with a new base url"""
        return attr.evolve(self, base_url=url)

    def get_http_client(self) -> httpx.AsyncClient:
        """Get the underlying httpx.AsyncClient, creating it if necessary"""
        if self.http_client is None:
            self.http_client = httpx.AsyncClient(
                timeout=self.timeout,
                verify=self.verify_ssl,
                cookies=self.cookies,
            )
        return self.http_client

    async def aclose(self) -> None:
        """Close the underlying HTTP client"""
        if self.http_client is not None:
            await self.http_client.aclose()
            self.http_client = None

    async def wait_for_async_operation(
        self,
        operation_id: str,
        timeout_seconds: float = 60.0,
        poll_interval_seconds: float = 2.0,
    ) -> Any:
        """Async poll `/async/operations/{id}` until status is completed/failed or timeout.

        Returns the unwrapped operation payload model when available.
        """

        import asyncio

        api_calls = getattr(self, "api_calls", None)
        if api_calls is None or not hasattr(api_calls, "get_async_operation"):
            raise RuntimeError(
                "`wait_for_async_operation` requires an AsyncKittyCAD client instance."
            )

        end_time = time.time() + timeout_seconds
        result = await api_calls.get_async_operation(id=operation_id)
        payload, status = _extract_operation_payload_and_status(result)

        while status not in {"completed", "failed"} and time.time() < end_time:
            await asyncio.sleep(poll_interval_seconds)
            result = await api_calls.get_async_operation(id=operation_id)
            payload, status = _extract_operation_payload_and_status(result)

        return payload

    async def __aenter__(self) -> Self:
        """Async context manager entry"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit"""
        await self.aclose()
