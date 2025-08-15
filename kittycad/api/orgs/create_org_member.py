from typing import Any, Dict

import httpx

from ...client import Client
from ...models.add_org_member import AddOrgMember
from ...models.org_member import OrgMember
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    body: AddOrgMember,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/org/members".format(
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


def _parse_response(*, response: httpx.Response) -> OrgMember:
    if response.status_code == 201:
        response_201 = OrgMember(**response.json())
        return response_201
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[OrgMember]:
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
    body: AddOrgMember,
    *,
    client: Client,
) -> Response[OrgMember]:
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
    body: AddOrgMember,
    *,
    client: Client,
) -> OrgMember:
    """If the user exists, this will add them to your org. If they do not exist, this will create a new user and add them to your org.

    In both cases the user gets an email that they have been added to the org.

    If the user is already in your org, this will return a 400 and a message.

    If the user is already in a different org, this will return a 400 and a message.

    This endpoint requires authentication by an org admin. It adds the specified member to the authenticated user's org."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: AddOrgMember,
    *,
    client: Client,
) -> Response[OrgMember]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: AddOrgMember,
    *,
    client: Client,
) -> OrgMember:
    """If the user exists, this will add them to your org. If they do not exist, this will create a new user and add them to your org.

    In both cases the user gets an email that they have been added to the org.

    If the user is already in your org, this will return a 400 and a message.

    If the user is already in a different org, this will return a 400 and a message.

    This endpoint requires authentication by an org admin. It adds the specified member to the authenticated user's org."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
