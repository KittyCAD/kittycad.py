import json
from typing import Any, Dict, Iterator

import bson
from websockets.asyncio.client import (
    ClientConnection as ClientConnectionAsync,
    connect as ws_connect_async,
)
from websockets.sync.client import (
    ClientConnection as ClientConnectionSync,
    connect as ws_connect,
)

from ...client import Client
from ...models.ml_copilot_client_message import MlCopilotClientMessage
from ...models.ml_copilot_server_message import MlCopilotServerMessage


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ws/ml/copilot".format(client.base_url)  # noqa: E501

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
) -> ClientConnectionSync:
    kwargs = _get_kwargs(
        client=client,
    )

    return ws_connect(
        kwargs["url"].replace("http", "ws"),
        additional_headers=kwargs["headers"],
        close_timeout=120,
        max_size=None,
    )  # type: ignore


async def asyncio(
    *,
    client: Client,
) -> ClientConnectionAsync:
    kwargs = _get_kwargs(
        client=client,
    )

    return await ws_connect_async(
        kwargs["url"].replace("http", "ws"),
        extra_headers=kwargs["headers"],
        close_timeout=120,
        max_size=None,
    )


class WebSocket:
    """A websocket connection to the API endpoint."""

    ws: ClientConnectionSync

    def __init__(
        self,
        client: Client,
    ):
        self.ws = sync(
            client=client,
        )

    def __enter__(
        self,
    ):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self) -> Iterator[MlCopilotServerMessage]:
        """
        Iterate on incoming messages.

        The iterator calls :meth:`recv` and yields messages in an infinite loop.

        It exits when the connection is closed normally. It raises a
        :exc:`~websockets.exceptions.ConnectionClosedError` exception after a
        protocol error or a network failure.

        """
        for message in self.ws:
            yield MlCopilotServerMessage(**json.loads(message))

    def send(self, data: MlCopilotClientMessage):
        """Send data to the websocket."""
        self.ws.send(json.dumps(data.model_dump()))

    def send_binary(self, data: MlCopilotClientMessage):
        """Send data as bson to the websocket."""
        self.ws.send(bson.encode(data.model_dump()))  # type: ignore

    def recv(self) -> MlCopilotServerMessage:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=60)
        return MlCopilotServerMessage(**json.loads(message))

    def close(self):
        """Close the websocket."""
        self.ws.close()
