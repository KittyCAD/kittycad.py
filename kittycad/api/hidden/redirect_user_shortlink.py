from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/shortlinks/{key}".format(
        client.base_url,
        key=key,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    return None
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(*, response: httpx.Response) -> Response[Optional[Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: Client,
) -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
) -> Optional[Error]:
    """This endpoint might require authentication by a Zoo user. It gets the shortlink for the user and redirects them to the URL. If the shortlink is owned by an org, the user must be a member of the org."""  # noqa: E501

    return sync_detailed(
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
) -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
) -> Optional[Error]:
    """This endpoint might require authentication by a Zoo user. It gets the shortlink for the user and redirects them to the URL. If the shortlink is owned by an org, the user must be a member of the org."""  # noqa: E501

    return (
        await asyncio_detailed(
            key=key,
            client=client,
        )
    ).parsed
