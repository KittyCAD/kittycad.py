"""
This module should only be accessed through client.api.
Direct imports like 'from kittycad.api.module import function' are not supported.
Use: client = KittyCAD(); client.api.module.function() instead.
"""

from typing import Any, Dict

import httpx

from ...client import Client
from ...models.zoo_product_subscriptions import ZooProductSubscriptions
from ...models.zoo_product_subscriptions_user_request import (
    ZooProductSubscriptionsUserRequest,
)
from ...response_helpers import raise_for_status
from ...types import Response

# Prevent direct imports - hide all public functions
__all__: list[str] = []


def _get_kwargs(
    body: ZooProductSubscriptionsUserRequest,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/payment/subscriptions".format(
        client.base_url,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body.model_dump_json(),
    }


def _parse_response(*, response: httpx.Response) -> ZooProductSubscriptions:
    if response.status_code == 200:
        response_200 = ZooProductSubscriptions(**response.json())
        return response_200
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[ZooProductSubscriptions]:
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


def sync(
    body: ZooProductSubscriptionsUserRequest,
    *,
    client: Client,
) -> ZooProductSubscriptions:
    """This endpoint requires authentication by any Zoo user. It updates the subscription for the user."""  # noqa: E501

    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response).parsed


async def asyncio(
    body: ZooProductSubscriptionsUserRequest,
    *,
    client: Client,
) -> ZooProductSubscriptions:
    """This endpoint requires authentication by any Zoo user. It updates the subscription for the user."""  # noqa: E501

    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response).parsed
