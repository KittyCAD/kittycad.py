from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.created_at_sort_mode import CreatedAtSortMode
from ...models.error import Error
from ...models.org_member_results_page import OrgMemberResultsPage
from ...models.org_role import OrgRole
from ...types import Response


def _get_kwargs(
    sort_by: CreatedAtSortMode,
    role: OrgRole,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/org/members".format(
        client.base_url,
    )  # noqa: E501

    if limit is not None:
        if "?" in url:
            url = url + "&limit=" + str(limit)
        else:
            url = url + "?limit=" + str(limit)

    if page_token is not None:
        if "?" in url:
            url = url + "&page_token=" + str(page_token)
        else:
            url = url + "?page_token=" + str(page_token)

    if sort_by is not None:
        if "?" in url:
            url = url + "&sort_by=" + str(sort_by)
        else:
            url = url + "?sort_by=" + str(sort_by)

    if role is not None:
        if "?" in url:
            url = url + "&role=" + str(role)
        else:
            url = url + "?role=" + str(role)

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
) -> Optional[Union[OrgMemberResultsPage, Error]]:
    if response.status_code == 200:
        response_200 = OrgMemberResultsPage(**response.json())
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
) -> Response[Optional[Union[OrgMemberResultsPage, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    sort_by: CreatedAtSortMode,
    role: OrgRole,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Response[Optional[Union[OrgMemberResultsPage, Error]]]:
    kwargs = _get_kwargs(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        role=role,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sort_by: CreatedAtSortMode,
    role: OrgRole,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Optional[Union[OrgMemberResultsPage, Error]]:
    """This endpoint requires authentication by an org admin. It lists the members of the authenticated user's org."""  # noqa: E501

    return sync_detailed(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        role=role,
        client=client,
    ).parsed


async def asyncio_detailed(
    sort_by: CreatedAtSortMode,
    role: OrgRole,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Response[Optional[Union[OrgMemberResultsPage, Error]]]:
    kwargs = _get_kwargs(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        role=role,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sort_by: CreatedAtSortMode,
    role: OrgRole,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Optional[Union[OrgMemberResultsPage, Error]]:
    """This endpoint requires authentication by an org admin. It lists the members of the authenticated user's org."""  # noqa: E501

    return (
        await asyncio_detailed(
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            role=role,
            client=client,
        )
    ).parsed
