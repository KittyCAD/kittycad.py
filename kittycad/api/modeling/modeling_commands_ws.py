from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ws/modeling/commands".format(client.base_url)  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response):
    return


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
):
    """Pass those commands to the engine via websocket, and pass responses back to the client. Basically, this is a websocket proxy between the frontend/client and the engine."""  # noqa: E501

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
):
    """Pass those commands to the engine via websocket, and pass responses back to the client. Basically, this is a websocket proxy between the frontend/client and the engine."""  # noqa: E501

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
