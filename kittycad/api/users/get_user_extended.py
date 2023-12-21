from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.extended_user import ExtendedUser
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users-extended/{id}".format(
        client.base_url,
        id=id,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ExtendedUser, Error]]:
    if response.status_code == 200:
        response_200 = ExtendedUser(**response.json())
        return response_200
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(
    *, response: httpx.Response
) -> Response[Optional[Union[ExtendedUser, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Optional[Union[ExtendedUser, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[Union[ExtendedUser, Error]]:
    """To get information about yourself, use `/users-extended/me` as the endpoint. By doing so you will get the user information for the authenticated user.
    Alternatively, to get information about the authenticated user, use `/user/extended` endpoint.
    To get information about any Zoo user, you must be a Zoo employee."""  # noqa: E501

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Optional[Union[ExtendedUser, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[Union[ExtendedUser, Error]]:
    """To get information about yourself, use `/users-extended/me` as the endpoint. By doing so you will get the user information for the authenticated user.
    Alternatively, to get information about the authenticated user, use `/user/extended` endpoint.
    To get information about any Zoo user, you must be a Zoo employee."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
