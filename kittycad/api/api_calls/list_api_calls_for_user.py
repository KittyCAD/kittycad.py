from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.api_call_with_price_results_page import ApiCallWithPriceResultsPage
from ...models.created_at_sort_mode import CreatedAtSortMode
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/users/{id}/api-calls".format(
        client.base_url,
        id=id,
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
) -> Optional[Union[ApiCallWithPriceResultsPage, Error]]:
    if response.status_code == 200:
        response_200 = ApiCallWithPriceResultsPage(**response.json())
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
) -> Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Optional[Union[ApiCallWithPriceResultsPage, Error]]:
    """This endpoint requires authentication by any Zoo user. It returns the API calls for the authenticated user if "me" is passed as the user id.
    Alternatively, you can use the `/user/api-calls` endpoint to get the API calls for your user.
    If the authenticated user is a Zoo employee, then the API calls are returned for the user specified by the user id.
    The API calls are returned in order of creation, with the most recently created API calls first.
    """  # noqa: E501

    return sync_detailed(
        id=id,
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]]:
    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Optional[Union[ApiCallWithPriceResultsPage, Error]]:
    """This endpoint requires authentication by any Zoo user. It returns the API calls for the authenticated user if "me" is passed as the user id.
    Alternatively, you can use the `/user/api-calls` endpoint to get the API calls for your user.
    If the authenticated user is a Zoo employee, then the API calls are returned for the user specified by the user id.
    The API calls are returned in order of creation, with the most recently created API calls first.
    """  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            client=client,
        )
    ).parsed
