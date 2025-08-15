from typing import Any, Dict

import httpx

from ...client import Client
from ...models.enterprise_subscription_tier_price import EnterpriseSubscriptionTierPrice
from ...models.uuid import Uuid
from ...models.zoo_product_subscriptions import ZooProductSubscriptions
from ...response_helpers import raise_for_status
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


def sync_detailed(
    id: Uuid,
    body: EnterpriseSubscriptionTierPrice,
    *,
    client: Client,
) -> Response[ZooProductSubscriptions]:
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
) -> ZooProductSubscriptions:
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
) -> Response[ZooProductSubscriptions]:
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
) -> ZooProductSubscriptions:
    """You must be a Zoo admin to perform this request."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            body=body,
            client=client,
        )
    ).parsed
