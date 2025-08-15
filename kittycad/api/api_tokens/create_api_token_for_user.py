from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.api_token import ApiToken
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    label: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/user/api-tokens".format(
        client.base_url,
    )  # noqa: E501

    if label is not None:
        if "?" in url:
            url = url + "&label=" + str(label)
        else:
            url = url + "?label=" + str(label)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> ApiToken:
    if response.status_code == 201:
        response_201 = ApiToken(**response.json())
        return response_201
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[ApiToken]:
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
    *,
    client: Client,
    label: Optional[str] = None,
) -> Response[ApiToken]:
    kwargs = _get_kwargs(
        label=label,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    label: Optional[str] = None,
) -> ApiToken:
    """This endpoint requires authentication by any Zoo user. It creates a new API token for the authenticated user."""  # noqa: E501

    return sync_detailed(
        label=label,
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    label: Optional[str] = None,
) -> Response[ApiToken]:
    kwargs = _get_kwargs(
        label=label,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    label: Optional[str] = None,
) -> ApiToken:
    """This endpoint requires authentication by any Zoo user. It creates a new API token for the authenticated user."""  # noqa: E501

    return (
        await asyncio_detailed(
            label=label,
            client=client,
        )
    ).parsed
