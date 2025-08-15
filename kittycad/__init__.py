"""A client library for accessing KittyCAD"""

import os
import ssl
from types import ModuleType
from typing import Any, Dict, Optional, Union

from .client import Client, ClientFromEnv
from .exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADConnectionError,
    KittyCADError,
    KittyCADServerError,
    KittyCADTimeoutError,
)


# Convenience client class
class APIModule:
    """Dynamic wrapper for API modules like client.api.users, client.api.ml"""

    def __init__(self, client: "Client", module_name: str):
        self.client = client
        self.module_name = module_name
        self._module: Optional[ModuleType] = None

    def __getattr__(self, name):
        # Dynamically import the API module
        if self._module is None:
            self._module = __import__(
                f"kittycad.api.{self.module_name}", fromlist=[name]
            )

        # Get the item from the module
        item = getattr(self._module, name)

        # Check if it's a class (like WebSocket)
        if isinstance(item, type):
            # For WebSocket classes, create a wrapper that injects the client
            if name == "WebSocket":
                # Capture the client in the closure to avoid attribute assignment issues
                client_to_inject = self.client

                class WebSocketWrapper:
                    def __init__(self, *args, **kwargs):
                        # Override the default client with our client
                        from kittycad import set_default_client

                        original_client = None
                        try:
                            from kittycad import get_default_client

                            original_client = get_default_client()
                        except ValueError:
                            pass  # No default client set

                        set_default_client(client_to_inject)
                        try:
                            self._ws = item(*args, **kwargs)
                        finally:
                            # Restore original client
                            if original_client:
                                set_default_client(original_client)
                            else:
                                import kittycad

                                kittycad._default_client = None

                    def __getattr__(self, attr):
                        return getattr(self._ws, attr)

                    def __enter__(self):
                        return self._ws.__enter__()

                    def __exit__(self, *args):
                        return self._ws.__exit__(*args)

                return WebSocketWrapper
            else:
                # Return other classes directly
                return item

        # Otherwise, treat it as a function module and create a wrapper
        func = item

        # Create a wrapper class that supports both sync calls and .asyncio attribute
        class APIFunction:
            def __init__(self, func, client):
                self.func = func
                self.client = client

            def __call__(self, *args, **kwargs):
                # Default sync behavior when called directly
                if "client" not in kwargs:
                    kwargs["client"] = self.client
                return self.func.sync(*args, **kwargs)

            async def asyncio(self, *args, **kwargs):
                # Async behavior when called with .asyncio
                if "client" not in kwargs:
                    kwargs["client"] = self.client
                return await self.func.asyncio(*args, **kwargs)

            def __getattr__(self, attr_name):
                # Support accessing classes like WebSocket from function modules
                if hasattr(self.func, attr_name):
                    attr = getattr(self.func, attr_name)
                    if isinstance(attr, type):
                        return attr
                return getattr(self.func, attr_name)

        return APIFunction(func, self.client)


class APICollection:
    """Collection of all API modules - accessed as client.api.users, client.api.ml, etc."""

    def __init__(self, client: "Client"):
        self.client = client

    def __getattr__(self, name):
        # Dynamically create API module wrappers
        return APIModule(self.client, name)


class KittyCAD(Client):
    """Main KittyCAD client class with modern API interface.

    Usage:
        client = KittyCAD(token="your-api-token")
        user = client.api.users.get_user_self()

    Or with environment variable:
        client = KittyCAD()  # Uses KITTYCAD_API_TOKEN or ZOO_API_TOKEN
    """

    def __init__(self, token: Optional[str] = None, **kwargs):
        if token is None:
            token = os.getenv("KITTYCAD_API_TOKEN") or os.getenv("ZOO_API_TOKEN")
            if token is None:
                raise ValueError(
                    "No API token provided. Either pass token parameter or set "
                    "KITTYCAD_API_TOKEN or ZOO_API_TOKEN environment variable."
                )
        super().__init__(token=token, **kwargs)
        # Add OpenAI-style API namespaces
        self.api = APICollection(self)


# Global default client instance
_default_client: Optional[Client] = None


def configure(
    api_token: Optional[str] = None,
    base_url: Optional[str] = None,
    timeout: Optional[float] = None,
    cookies: Optional[Dict[str, str]] = None,
    headers: Optional[Dict[str, str]] = None,
    verify_ssl: Optional[Union[str, bool, ssl.SSLContext]] = None,
) -> None:
    """Configure the global default client for KittyCAD.

    Args:
        api_token: Your API token. If None, will attempt to use environment variable.
        base_url: Base URL for the API. Defaults to https://api.zoo.dev
        timeout: Request timeout in seconds. Defaults to 120.0
        cookies: Additional cookies to send with requests
        headers: Additional headers to send with requests
        verify_ssl: SSL verification setting (bool, path to CA cert, or SSLContext)

    Examples:
        Configure with explicit token:
        >>> import kittycad
        >>> kittycad.configure(api_token="your-token-here")

        Configure using environment variables:
        >>> kittycad.configure()  # Uses KITTYCAD_API_TOKEN or ZOO_API_TOKEN

        Configure with custom base URL:
        >>> kittycad.configure(api_token="token", base_url="https://custom.api.url")
    """
    global _default_client

    if api_token is None:
        # Try to get from environment
        api_token = os.getenv("KITTYCAD_API_TOKEN") or os.getenv("ZOO_API_TOKEN")
        if api_token is None:
            raise ValueError(
                "No API token provided. Either pass api_token parameter or set "
                "KITTYCAD_API_TOKEN or ZOO_API_TOKEN environment variable."
            )

    client_kwargs: Dict[str, Any] = {}
    if base_url is not None:
        client_kwargs["base_url"] = base_url
    if timeout is not None:
        client_kwargs["timeout"] = timeout
    if cookies is not None:
        client_kwargs["cookies"] = cookies
    if headers is not None:
        client_kwargs["headers"] = headers
    if verify_ssl is not None:
        client_kwargs["verify_ssl"] = verify_ssl

    _default_client = Client(token=api_token, **client_kwargs)


def get_default_client() -> Client:
    """Get the global default client.

    If no client has been configured, attempts to create one from environment variables.

    Returns:
        The global default client

    Raises:
        ValueError: If no client has been configured and no environment variables are set
    """
    global _default_client

    if _default_client is None:
        # Try to auto-configure from environment
        try:
            _default_client = ClientFromEnv()
        except ValueError:
            raise ValueError(
                "No default client configured. Either call kittycad.configure() "
                "or set KITTYCAD_API_TOKEN or ZOO_API_TOKEN environment variable."
            )

    return _default_client


def set_default_client(client: Client) -> None:
    """Set the global default client directly.

    Args:
        client: Client instance to use as default
    """
    global _default_client
    _default_client = client


__all__ = [
    "KittyCAD",
    "KittyCADError",
    "KittyCADAPIError",
    "KittyCADClientError",
    "KittyCADServerError",
    "KittyCADConnectionError",
    "KittyCADTimeoutError",
]
