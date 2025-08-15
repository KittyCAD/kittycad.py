from typing import Any, Dict

import httpx

from ...client import Client
from ...models.create_shortlink_request import CreateShortlinkRequest
from ...models.create_shortlink_response import CreateShortlinkResponse
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    body: CreateShortlinkRequest,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/shortlinks".format(
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


def _parse_response(*, response: httpx.Response) -> CreateShortlinkResponse:
    if response.status_code == 201:
        response_201 = CreateShortlinkResponse(**response.json())
        return response_201
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[CreateShortlinkResponse]:
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
    body: CreateShortlinkRequest,
    *,
    client: Client,
) -> Response[CreateShortlinkResponse]:
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
    body: CreateShortlinkRequest,
    *,
    client: Client,
) -> CreateShortlinkResponse:
    """This endpoint requires authentication by any Zoo user. It creates a shortlink for the user."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: CreateShortlinkRequest,
    *,
    client: Client,
) -> Response[CreateShortlinkResponse]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: CreateShortlinkRequest,
    *,
    client: Client,
) -> CreateShortlinkResponse:
    """This endpoint requires authentication by any Zoo user. It creates a shortlink for the user."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
