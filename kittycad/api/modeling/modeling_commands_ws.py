from typing import Any, Dict

from websockets.client import WebSocketClientProtocol, connect as ws_connect_async
from websockets.sync.client import ClientConnection, connect as ws_connect

from ...client import Client
from ...models.error import Error


def _get_kwargs(
    
    
    fps: int,
    
    
    
    unlocked_framerate: bool,
    
    
    
    video_res_height: int,
    
    
    
    video_res_width: int,
    
    
    
    webrtc: bool,
    
    
    *,
    client: Client,
    
    
    
    
    
    
    
    
    
    
    
) -> Dict[str, Any]:
    url = "{}/ws/modeling/commands".format(client.base_url) # noqa: E501
    
    
    if fps is not None:
        if "?" in url:
            url = url + "&fps=" + str(fps)
        else:
            url = url + "?fps=" + str(fps)
    
    
    
    if unlocked_framerate is not None:
        if "?" in url:
            url = url + "&unlocked_framerate=" + str(unlocked_framerate)
        else:
            url = url + "?unlocked_framerate=" + str(unlocked_framerate)
    
    
    
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
            url = url + "&webrtc=" + str(webrtc)
        else:
            url = url + "?webrtc=" + str(webrtc)
    
    


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

    with ws_connect(kwargs["url"].replace("https://", "wss://"), additional_headers=kwargs["headers"]) as websocket:
        return websocket # type: ignore

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

    async with ws_connect_async(kwargs["url"].replace("https://", "wss://"), extra_headers=kwargs["headers"]) as websocket:
        return websocket

    # Return an error if we got here.
    return Error(message="An error occurred while connecting to the websocket.")
