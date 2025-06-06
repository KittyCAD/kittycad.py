from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.enterprise_subscription_tier_price import EnterpriseSubscriptionTierPrice
from ...models.error import Error
from ...models.uuid import Uuid
from ...models.zoo_product_subscriptions import ZooProductSubscriptions
from ...types import Response


def _get_kwargs(
    id: Uuid,
    body: EnterpriseSubscriptionTierPrice,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{id}/enterprise/pricing".format(
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
        "content": body.model_dump_json(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ZooProductSubscriptions, Error]]:
    if response.status_code == 200:
        response_200 = ZooProductSubscriptions(**response.json())
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
) -> Response[Optional[Union[ZooProductSubscriptions, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: Uuid,
    body: EnterpriseSubscriptionTierPrice,
    *,
    client: Client,
) -> Response[Optional[Union[ZooProductSubscriptions, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        body=body,
        client=client,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: Uuid,
    body: EnterpriseSubscriptionTierPrice,
    *,
    client: Client,
) -> Optional[Union[ZooProductSubscriptions, Error]]:
    """You must be a Zoo admin to perform this request."""  # noqa: E501

    return sync_detailed(
        id=id,
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: Uuid,
    body: EnterpriseSubscriptionTierPrice,
    *,
    client: Client,
) -> Response[Optional[Union[ZooProductSubscriptions, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: Uuid,
    body: EnterpriseSubscriptionTierPrice,
    *,
    client: Client,
) -> Optional[Union[ZooProductSubscriptions, Error]]:
    """You must be a Zoo admin to perform this request."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            body=body,
            client=client,
        )
    ).parsed
