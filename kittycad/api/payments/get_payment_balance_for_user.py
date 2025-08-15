from typing import Any, Dict

import httpx

from ...client import Client
from ...models.customer_balance import CustomerBalance
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    include_total_due: bool,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/payment/balance".format(
        client.base_url,
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


def _parse_response(*, response: httpx.Response) -> CustomerBalance:
    if response.status_code == 200:
        response_200 = CustomerBalance(**response.json())
        return response_200
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[CustomerBalance]:
    # Check for errors first - this will raise exceptions for non-success status codes
    # before we try to parse the response
    if not response.is_success:
        raise_for_status(response)

    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    include_total_due: bool,
    *,
    client: Client,
) -> Response[CustomerBalance]:
    kwargs = _get_kwargs(
        include_total_due=include_total_due,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    include_total_due: bool,
    *,
    client: Client,
) -> CustomerBalance:
    """This endpoint requires authentication by any Zoo user. It gets the balance information for the authenticated user."""  # noqa: E501

    return sync_detailed(
        include_total_due=include_total_due,
        client=client,
    ).parsed


async def asyncio_detailed(
    include_total_due: bool,
    *,
    client: Client,
) -> Response[CustomerBalance]:
    kwargs = _get_kwargs(
        include_total_due=include_total_due,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    include_total_due: bool,
    *,
    client: Client,
) -> CustomerBalance:
    """This endpoint requires authentication by any Zoo user. It gets the balance information for the authenticated user."""  # noqa: E501

    return (
        await asyncio_detailed(
            include_total_due=include_total_due,
            client=client,
        )
    ).parsed
