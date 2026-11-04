"""Exercise generated WebSocket clients against the installed transport."""

import asyncio
import json
import warnings
from collections.abc import Iterator
from contextlib import ExitStack
from threading import Thread

import bson
import pytest
from websockets.sync.client import connect
from websockets.sync.server import ServerConnection, serve

from kittycad import AsyncKittyCAD, KittyCAD
from kittycad.models.ml_copilot_client_message import MlCopilotClientMessage, OptionUser
from kittycad.models.ml_copilot_server_message import Delta, MlCopilotServerMessage


@pytest.fixture
def websocket_server() -> Iterator[str]:
    def echo(connection: ServerConnection) -> None:
        for message in connection:
            payload = (
                bson.decode(message)
                if isinstance(message, bytes)
                else json.loads(message)
            )
            response = json.dumps({"delta": {"delta": payload["content"]}})
            # Exercise fragmented responses as well as text and BSON requests.
            connection.send([response[:10], response[10:]])

    with serve(echo, "127.0.0.1", 0) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{server.socket.getsockname()[1]}"
        finally:
            server.shutdown()
            thread.join(timeout=5)


@pytest.mark.parametrize("custom_factory", [False, True])
def test_sync_websocket_round_trip(websocket_server: str, custom_factory: bool) -> None:
    # Keep a strict factory signature to catch new transport options leaking into
    # the public ws_factory interface.
    def factory(uri, *, additional_headers, close_timeout, max_size):
        return connections.enter_context(
            connect(
                uri,
                additional_headers=additional_headers,
                close_timeout=close_timeout,
                max_size=max_size,
            )
        )

    client = KittyCAD(token="test-token", base_url=websocket_server)
    with ExitStack() as connections, warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        with client.ml.ml_reasoning_ws(
            id="test", recv_timeout=5, ws_factory=factory if custom_factory else None
        ) as websocket:
            request = MlCopilotClientMessage(OptionUser(content="hello"))
            websocket.send(request)
            response = websocket.recv()
            assert isinstance(response.root, Delta)
            assert response.root.delta == "hello"

            websocket.send_binary(request)
            response = next(iter(websocket))
            assert isinstance(response.root, Delta)
            assert response.root.delta == "hello"

        assert websocket.ws.close_code == 1000


@pytest.mark.asyncio
async def test_async_websocket_round_trip(websocket_server: str) -> None:
    client = AsyncKittyCAD(token="test-token", base_url=websocket_server)
    websocket = await client.ml.ml_reasoning_ws(id="test")
    try:
        request = MlCopilotClientMessage(OptionUser(content="hello"))
        await websocket.send(request.model_dump_json(exclude_none=True))
        response = MlCopilotServerMessage.model_validate_json(
            await asyncio.wait_for(websocket.recv(), timeout=5)
        )
        assert isinstance(response.root, Delta)
        assert response.root.delta == "hello"
    finally:
        await websocket.close()

    assert websocket.close_code == 1000
