from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.api_call_with_price import ApiCallWithPrice
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/org/api-calls/{id}".format(
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
) -> Optional[Union[ApiCallWithPrice, Error]]:
    if response.status_code == 200:
        response_200 = ApiCallWithPrice(**response.json())
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
) -> Response[Optional[Union[ApiCallWithPrice, Error]]]:
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
) -> Response[Optional[Union[ApiCallWithPrice, Error]]]:
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
) -> Optional[Union[ApiCallWithPrice, Error]]:
    """This endpoint requires authentication by an org admin. It returns details of the requested API call for the user's org."""  # noqa: E501

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Optional[Union[ApiCallWithPrice, Error]]]:
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
) -> Optional[Union[ApiCallWithPrice, Error]]:
    """This endpoint requires authentication by an org admin. It returns details of the requested API call for the user's org."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
