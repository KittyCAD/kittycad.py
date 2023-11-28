import json
from typing import Any, Dict, Optional

import bson
from websockets.client import WebSocketClientProtocol, connect as ws_connect_async
from websockets.sync.client import ClientConnection, connect as ws_connect

from ...client import Client
from ...models.error import Error
from ...models.web_socket_request import WebSocketRequest
from ...models.web_socket_response import WebSocketResponse


def _get_kwargs(
    fps: int,
    unlocked_framerate: bool,
    video_res_height: int,
    video_res_width: int,
    webrtc: bool,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ws/modeling/commands".format(client.base_url)  # noqa: E501

    if fps is not None:
        if "?" in url:
            url = url + "&fps=" + str(fps)
        else:
            url = url + "?fps=" + str(fps)

    if unlocked_framerate is not None:
        if "?" in url:
            url = url + "&unlocked_framerate=" + str(unlocked_framerate).lower()
        else:
            url = url + "?unlocked_framerate=" + str(unlocked_framerate).lower()

    if video_res_height is not None:
        if "?" in url:
            url = url + "&video_res_height=" + str(video_res_height)
        else:
            url = url + "?video_res_height=" + str(video_res_height)

    if video_res_width is not None:
        if "?" in url:
            url = url + "&video_res_width=" + str(video_res_width)
        else:
            url = url + "?video_res_width=" + str(video_res_width)

    if webrtc is not None:
        if "?" in url:
            url = url + "&webrtc=" + str(webrtc).lower()
        else:
            url = url + "?webrtc=" + str(webrtc).lower()

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def sync(
    fps: int,
    unlocked_framerate: bool,
    video_res_height: int,
    video_res_width: int,
    webrtc: bool,
    *,
    client: Client,
) -> ClientConnection:
    """Pass those commands to the engine via websocket, and pass responses back to the client. Basically, this is a websocket proxy between the frontend/client and the engine."""  # noqa: E501

    kwargs = _get_kwargs(
        fps=fps,
        unlocked_framerate=unlocked_framerate,
        video_res_height=video_res_height,
        video_res_width=video_res_width,
        webrtc=webrtc,
        client=client,
    )

    with ws_connect(
        kwargs["url"].replace("https://", "wss://"),
        additional_headers=kwargs["headers"],
    ) as websocket:
        return websocket  # type: ignore

    # Return an error if we got here.
    return Error(message="An error occurred while connecting to the websocket.")


async def asyncio(
    fps: int,
    unlocked_framerate: bool,
    video_res_height: int,
    video_res_width: int,
    webrtc: bool,
    *,
    client: Client,
) -> WebSocketClientProtocol:
    """Pass those commands to the engine via websocket, and pass responses back to the client. Basically, this is a websocket proxy between the frontend/client and the engine."""  # noqa: E501

    kwargs = _get_kwargs(
        fps=fps,
        unlocked_framerate=unlocked_framerate,
        video_res_height=video_res_height,
        video_res_width=video_res_width,
        webrtc=webrtc,
        client=client,
    )

    async with ws_connect_async(
        kwargs["url"].replace("https://", "wss://"), extra_headers=kwargs["headers"]
    ) as websocket:
        return websocket

    # Return an error if we got here.
    return Error(message="An error occurred while connecting to the websocket.")


class WebSocket:
    """A websocket connection to the API endpoint."""

    ws: ClientConnection

    def __init__(
        self,
        fps: int,
        unlocked_framerate: bool,
        video_res_height: int,
        video_res_width: int,
        webrtc: bool,
        client: Client,
    ):
        self.ws = sync(
            fps,
            unlocked_framerate,
            video_res_height,
            video_res_width,
            webrtc,
            client=client,
        )

    def send(self, data: WebSocketRequest):
        """Send data to the websocket."""
        self.ws.send(json.dumps(data.to_dict()))

    def send_binary(self, data: WebSocketRequest):
        """Send data as bson to the websocket."""
        self.ws.send(bson.BSON.encode(data.to_dict()))

    def recv(self) -> Optional[WebSocketResponse]:
        """Receive data from the websocket."""
        message = self.ws.recv()
        return Optional[WebSocketResponse].from_dict(json.loads(message))
