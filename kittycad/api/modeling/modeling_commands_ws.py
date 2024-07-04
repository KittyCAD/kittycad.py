import json
from typing import Any, Dict, Iterator, Optional

import bson
from websockets.client import WebSocketClientProtocol, connect as ws_connect_async
from websockets.sync.client import ClientConnection, connect as ws_connect

from ...client import Client
from ...models.post_effect_type import PostEffectType
from ...models.web_socket_request import WebSocketRequest
from ...models.web_socket_response import WebSocketResponse


def _get_kwargs(
    fps: int,
    post_effect: PostEffectType,
    show_grid: bool,
    unlocked_framerate: bool,
    video_res_height: int,
    video_res_width: int,
    webrtc: bool,
    *,
    client: Client,
    pool: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/ws/modeling/commands".format(client.base_url)  # noqa: E501

    if fps is not None:

        if "?" in url:
            url = url + "&fps=" + str(fps)
        else:
            url = url + "?fps=" + str(fps)

    if pool is not None:

        if "?" in url:
            url = url + "&pool=" + str(pool)
        else:
            url = url + "?pool=" + str(pool)

    if post_effect is not None:

        if "?" in url:
            url = url + "&post_effect=" + str(post_effect)
        else:
            url = url + "?post_effect=" + str(post_effect)

    if show_grid is not None:

        if "?" in url:
            url = url + "&show_grid=" + str(show_grid).lower()
        else:
            url = url + "?show_grid=" + str(show_grid).lower()

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
    post_effect: PostEffectType,
    show_grid: bool,
    unlocked_framerate: bool,
    video_res_height: int,
    video_res_width: int,
    webrtc: bool,
    *,
    client: Client,
    pool: Optional[str] = None,
) -> ClientConnection:
    """Pass those commands to the engine via websocket, and pass responses back to the client. Basically, this is a websocket proxy between the frontend/client and the engine."""  # noqa: E501

    kwargs = _get_kwargs(
        fps=fps,
        pool=pool,
        post_effect=post_effect,
        show_grid=show_grid,
        unlocked_framerate=unlocked_framerate,
        video_res_height=video_res_height,
        video_res_width=video_res_width,
        webrtc=webrtc,
        client=client,
    )

    return ws_connect(kwargs["url"].replace("http", "ws"), additional_headers=kwargs["headers"], close_timeout=120, max_size=None)  # type: ignore


async def asyncio(
    fps: int,
    post_effect: PostEffectType,
    show_grid: bool,
    unlocked_framerate: bool,
    video_res_height: int,
    video_res_width: int,
    webrtc: bool,
    *,
    client: Client,
    pool: Optional[str] = None,
) -> WebSocketClientProtocol:
    """Pass those commands to the engine via websocket, and pass responses back to the client. Basically, this is a websocket proxy between the frontend/client and the engine."""  # noqa: E501

    kwargs = _get_kwargs(
        fps=fps,
        pool=pool,
        post_effect=post_effect,
        show_grid=show_grid,
        unlocked_framerate=unlocked_framerate,
        video_res_height=video_res_height,
        video_res_width=video_res_width,
        webrtc=webrtc,
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

    ws: ClientConnection

    def __init__(
        self,
        fps: int,
        post_effect: PostEffectType,
        show_grid: bool,
        unlocked_framerate: bool,
        video_res_height: int,
        video_res_width: int,
        webrtc: bool,
        client: Client,
        pool: Optional[str] = None,
    ):
        self.ws = sync(
            fps,
            post_effect,
            show_grid,
            unlocked_framerate,
            video_res_height,
            video_res_width,
            webrtc,
            client=client,
            pool=pool,
        )

    def __enter__(
        self,
    ):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self) -> Iterator[WebSocketResponse]:
        """
        Iterate on incoming messages.

        The iterator calls :meth:`recv` and yields messages in an infinite loop.

        It exits when the connection is closed normally. It raises a
        :exc:`~websockets.exceptions.ConnectionClosedError` exception after a
        protocol error or a network failure.

        """
        for message in self.ws:
            yield WebSocketResponse(**json.loads(message))

    def send(self, data: WebSocketRequest):
        """Send data to the websocket."""
        self.ws.send(json.dumps(data.model_dump()))

    def send_binary(self, data: WebSocketRequest):
        """Send data as bson to the websocket."""
        self.ws.send(bson.encode(data.model_dump()))  # type: ignore

    def recv(self) -> WebSocketResponse:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=60)
        return WebSocketResponse(**json.loads(message))

    def close(self):
        """Close the websocket."""
        self.ws.close()
