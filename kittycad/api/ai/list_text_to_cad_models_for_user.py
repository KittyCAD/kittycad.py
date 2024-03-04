from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.created_at_sort_mode import CreatedAtSortMode
from ...models.error import Error
from ...models.text_to_cad_results_page import TextToCadResultsPage
from ...types import Response


def _get_kwargs(
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
    no_models: Optional[bool] = None,
) -> Dict[str, Any]:
    url = "{}/user/text-to-cad".format(
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

    if no_models is not None:

        if "?" in url:
            url = url + "&no_models=" + str(no_models)
        else:
            url = url + "?no_models=" + str(no_models)

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
) -> Optional[Union[TextToCadResultsPage, Error]]:
    if response.status_code == 200:
        response_200 = TextToCadResultsPage(**response.json())
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
) -> Response[Optional[Union[TextToCadResultsPage, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
    no_models: Optional[bool] = None,
) -> Response[Optional[Union[TextToCadResultsPage, Error]]]:
    kwargs = _get_kwargs(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        no_models=no_models,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
    no_models: Optional[bool] = None,
) -> Optional[Union[TextToCadResultsPage, Error]]:
    """This will always return the STEP file contents as well as the format the user originally requested.
    This endpoint requires authentication by any Zoo user. It returns the text-to-CAD models for the authenticated user.
    The text-to-CAD models are returned in order of creation, with the most recently created text-to-CAD models first.
    """  # noqa: E501

    return sync_detailed(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        no_models=no_models,
        client=client,
    ).parsed


async def asyncio_detailed(
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
    no_models: Optional[bool] = None,
) -> Response[Optional[Union[TextToCadResultsPage, Error]]]:
    kwargs = _get_kwargs(
        limit=limit,
        page_token=page_token,
        sort_by=sort_by,
        no_models=no_models,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sort_by: CreatedAtSortMode,
    *,
    client: Client,
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
    no_models: Optional[bool] = None,
) -> Optional[Union[TextToCadResultsPage, Error]]:
    """This will always return the STEP file contents as well as the format the user originally requested.
    This endpoint requires authentication by any Zoo user. It returns the text-to-CAD models for the authenticated user.
    The text-to-CAD models are returned in order of creation, with the most recently created text-to-CAD models first.
    """  # noqa: E501

    return (
        await asyncio_detailed(
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            no_models=no_models,
            client=client,
        )
    ).parsed
