from typing import Any, Dict, List

import httpx

from ...client import Client
from ...models.api_call_query_group import ApiCallQueryGroup
from ...models.api_call_query_group_by import ApiCallQueryGroupBy
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    group_by: ApiCallQueryGroupBy,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api-call-metrics".format(
        client.base_url,
    )  # noqa: E501

    if group_by is not None:
        if "?" in url:
            url = url + "&group_by=" + str(group_by)
        else:
            url = url + "?group_by=" + str(group_by)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> List[ApiCallQueryGroup]:
    if response.status_code == 200:
        response_200 = [ApiCallQueryGroup(**item) for item in response.json()]
        return response_200
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[List[ApiCallQueryGroup]]:
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
    group_by: ApiCallQueryGroupBy,
    *,
    client: Client,
) -> Response[List[ApiCallQueryGroup]]:
    kwargs = _get_kwargs(
        group_by=group_by,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    group_by: ApiCallQueryGroupBy,
    *,
    client: Client,
) -> List[ApiCallQueryGroup]:
    """This endpoint requires authentication by a Zoo employee. The API calls are grouped by the parameter passed."""  # noqa: E501

    return sync_detailed(
        group_by=group_by,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_by: ApiCallQueryGroupBy,
    *,
    client: Client,
) -> Response[List[ApiCallQueryGroup]]:
    kwargs = _get_kwargs(
        group_by=group_by,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_by: ApiCallQueryGroupBy,
    *,
    client: Client,
) -> List[ApiCallQueryGroup]:
    """This endpoint requires authentication by a Zoo employee. The API calls are grouped by the parameter passed."""  # noqa: E501

    return (
        await asyncio_detailed(
            group_by=group_by,
            client=client,
        )
    ).parsed
