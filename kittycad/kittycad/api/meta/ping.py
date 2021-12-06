from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.ping_response_200 import PingResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ping".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[PingResponse200]:
    if response.status_code == 200:
        response_200 = PingResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PingResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[PingResponse200]:
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
) -> Optional[PingResponse200]:
    """Simple ping to the server."""

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[PingResponse200]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[PingResponse200]:
    """Simple ping to the server."""

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
