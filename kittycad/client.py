import ssl
from typing import Dict, Optional, Self, Union

import attr
import httpx
import truststore

DEFAULT_BASE_URL = "https://api.zoo.dev"


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

    async def __aenter__(self) -> Self:
        """Async context manager entry"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit"""
        await self.aclose()
