from typing import Any, Dict

from websockets.client import WebSocketClientProtocol, connect as ws_connect_async
from websockets.sync.client import ClientConnection, connect as ws_connect

from ...client import Client


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ws/executor/term".format(client.base_url)  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def sync(
    *,
    client: Client,
) -> ClientConnection:
    """Attach to a docker container to create an interactive terminal."""  # noqa: E501

    kwargs = _get_kwargs(
        client=client,
    )

    return ws_connect(kwargs["url"].replace("http", "ws"), additional_headers=kwargs["headers"], close_timeout=120, max_size=None)  # type: ignore


async def asyncio(
    *,
    client: Client,
) -> WebSocketClientProtocol:
    """Attach to a docker container to create an interactive terminal."""  # noqa: E501

    kwargs = _get_kwargs(
        client=client,
    )

    return await ws_connect_async(
        kwargs["url"].replace("http", "ws"),
        extra_headers=kwargs["headers"],
        close_timeout=120,
        max_size=None,
    )
