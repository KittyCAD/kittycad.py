from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.org_member import OrgMember
from ...models.uuid import Uuid
from ...types import Response


def _get_kwargs(
    user_id: Uuid,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/org/members/{user_id}".format(
        client.base_url,
        user_id=user_id,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[OrgMember, Error]]:
    if response.status_code == 200:
        response_200 = OrgMember(**response.json())
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
) -> Response[Optional[Union[OrgMember, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: Uuid,
    *,
    client: Client,
) -> Response[Optional[Union[OrgMember, Error]]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: Uuid,
    *,
    client: Client,
) -> Optional[Union[OrgMember, Error]]:
    """This endpoint requires authentication by an org admin. It gets the specified member of the authenticated user's org."""  # noqa: E501

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: Uuid,
    *,
    client: Client,
) -> Response[Optional[Union[OrgMember, Error]]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: Uuid,
    *,
    client: Client,
) -> Optional[Union[OrgMember, Error]]:
    """This endpoint requires authentication by an org admin. It gets the specified member of the authenticated user's org."""  # noqa: E501

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
