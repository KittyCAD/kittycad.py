import os
import ssl
from typing import Dict, Optional, Union

import attr


@attr.s(auto_attribs=True)
class Client:
    """A Client which has been authenticated for use on secured endpoints of the KittyCAD API."""  # noqa: E501

    token: str = attr.ib(kw_only=True)
    base_url: str = attr.ib(default="https://api.kittycad.io")
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(120.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {"Authorization": f"Bearer {self.token}", **self.headers}

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

    def with_base_url(self, url: str) -> "Client":
        """Get a new client matching this one with a new base url"""
        return attr.evolve(self, base_url=url)


@attr.s(auto_attribs=True)
class ClientFromEnv(Client):
    """A Client which has been authenticated for use on secured endpoints that uses the KITTYCAD_API_TOKEN environment variable for the authentication token."""  # noqa: E501

    token: str = attr.field()

    @token.default
    def set_token(self):
        maybe_token: Optional[str] = os.getenv("KITTYCAD_API_TOKEN")
        if maybe_token is None:
            raise ValueError(
                "KITTYCAD_API_TOKEN environment variable must be set to use ClientFromEnv"
            )
        token: str = maybe_token
        return token

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        return {"Authorization": f"Bearer {self.token}", **self.headers}
