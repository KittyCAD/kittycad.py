from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.zoo_product_subscriptions import ZooProductSubscriptions
from ...models.zoo_product_subscriptions_user_request import (
    ZooProductSubscriptionsUserRequest,
)
from ...types import Response


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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ZooProductSubscriptions, Error]]:
    if response.status_code == 201:
        response_201 = ZooProductSubscriptions(**response.json())
        return response_201
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(
    *, response: httpx.Response
) -> Response[Optional[Union[ZooProductSubscriptions, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: ZooProductSubscriptionsUserRequest,
    *,
    client: Client,
) -> Response[Optional[Union[ZooProductSubscriptions, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    body: ZooProductSubscriptionsUserRequest,
    *,
    client: Client,
) -> Optional[Union[ZooProductSubscriptions, Error]]:
    """This endpoint requires authentication by any Zoo user. It creates the subscription for the user."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: ZooProductSubscriptionsUserRequest,
    *,
    client: Client,
) -> Response[Optional[Union[ZooProductSubscriptions, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: ZooProductSubscriptionsUserRequest,
    *,
    client: Client,
) -> Optional[Union[ZooProductSubscriptions, Error]]:
    """This endpoint requires authentication by any Zoo user. It creates the subscription for the user."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed