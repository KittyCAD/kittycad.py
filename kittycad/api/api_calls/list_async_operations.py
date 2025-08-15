from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.api_call_status import ApiCallStatus
from ...models.async_api_call_results_page import AsyncApiCallResultsPage
from ...models.created_at_sort_mode import CreatedAtSortMode
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    sort_by: CreatedAtSortMode,
    status: ApiCallStatus,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/async/operations".format(
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

    if status is not None:
        if "?" in url:
            url = url + "&status=" + str(status)
        else:
            url = url + "?status=" + str(status)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> AsyncApiCallResultsPage:
    if response.status_code == 200:
        response_200 = AsyncApiCallResultsPage(**response.json())
        return response_200
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[AsyncApiCallResultsPage]:
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
    sort_by: CreatedAtSortMode,
    status: ApiCallStatus,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Response[AsyncApiCallResultsPage]:
    kwargs = _get_kwargs(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        status=status,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sort_by: CreatedAtSortMode,
    status: ApiCallStatus,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> AsyncApiCallResultsPage:
    """For async file conversion operations, this endpoint does not return the contents of converted files (`output`). To get the contents use the `/async/operations/{id}` endpoint.

    This endpoint requires authentication by a Zoo employee."""  # noqa: E501

    return sync_detailed(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        status=status,
        client=client,
    ).parsed


async def asyncio_detailed(
    sort_by: CreatedAtSortMode,
    status: ApiCallStatus,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Response[AsyncApiCallResultsPage]:
    kwargs = _get_kwargs(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        status=status,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sort_by: CreatedAtSortMode,
    status: ApiCallStatus,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> AsyncApiCallResultsPage:
    """For async file conversion operations, this endpoint does not return the contents of converted files (`output`). To get the contents use the `/async/operations/{id}` endpoint.

    This endpoint requires authentication by a Zoo employee."""  # noqa: E501

    return (
        await asyncio_detailed(
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            status=status,
            client=client,
        )
    ).parsed
