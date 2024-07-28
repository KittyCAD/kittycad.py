from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.api_token import ApiToken
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    token: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/api-tokens/{token}".format(
        client.base_url,
        token=token,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ApiToken, Error]]:
    if response.status_code == 200:
        response_200 = ApiToken(**response.json())
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
) -> Response[Optional[Union[ApiToken, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    token: str,
    *,
    client: Client,
) -> Response[Optional[Union[ApiToken, Error]]]:
    kwargs = _get_kwargs(
        token=token,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    token: str,
    *,
    client: Client,
) -> Optional[Union[ApiToken, Error]]:
    """This endpoint requires authentication by any Zoo user. It returns details of the requested API token for the user."""  # noqa: E501

    return sync_detailed(
        token=token,
        client=client,
    ).parsed


async def asyncio_detailed(
    token: str,
    *,
    client: Client,
) -> Response[Optional[Union[ApiToken, Error]]]:
    kwargs = _get_kwargs(
        token=token,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    token: str,
    *,
    client: Client,
) -> Optional[Union[ApiToken, Error]]:
    """This endpoint requires authentication by any Zoo user. It returns details of the requested API token for the user."""  # noqa: E501

    return (
        await asyncio_detailed(
            token=token,
            client=client,
        )
    ).parsed
