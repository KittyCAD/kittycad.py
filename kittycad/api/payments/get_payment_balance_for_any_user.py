from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.customer_balance import CustomerBalance
from ...models.error import Error
from ...models.user_identifier import UserIdentifier
from ...types import Response


def _get_kwargs(
    id: UserIdentifier,
    include_total_due: bool,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{id}/payment/balance".format(
        client.base_url,
        id=id,
    )  # noqa: E501

    if include_total_due is not None:
        if "?" in url:
            url = url + "&include_total_due=" + str(include_total_due).lower()
        else:
            url = url + "?include_total_due=" + str(include_total_due).lower()

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
) -> Optional[Union[CustomerBalance, Error]]:
    if response.status_code == 200:
        response_200 = CustomerBalance(**response.json())
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
) -> Response[Optional[Union[CustomerBalance, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: UserIdentifier,
    include_total_due: bool,
    *,
    client: Client,
) -> Response[Optional[Union[CustomerBalance, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        include_total_due=include_total_due,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: UserIdentifier,
    include_total_due: bool,
    *,
    client: Client,
) -> Optional[Union[CustomerBalance, Error]]:
    """This endpoint requires authentication by a Zoo employee. It gets the balance information for the specified user."""  # noqa: E501

    return sync_detailed(
        id=id,
        include_total_due=include_total_due,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UserIdentifier,
    include_total_due: bool,
    *,
    client: Client,
) -> Response[Optional[Union[CustomerBalance, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        include_total_due=include_total_due,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: UserIdentifier,
    include_total_due: bool,
    *,
    client: Client,
) -> Optional[Union[CustomerBalance, Error]]:
    """This endpoint requires authentication by a Zoo employee. It gets the balance information for the specified user."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            include_total_due=include_total_due,
            client=client,
        )
    ).parsed
