from typing import Any, Dict

import httpx

from ...client import Client
from ...models.text_to_cad_response import TextToCadResponse
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/text-to-cad/{id}".format(
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
    }


def _parse_response(*, response: httpx.Response) -> TextToCadResponse:
    if response.status_code == 200:
        response_200 = TextToCadResponse(**response.json())
        return response_200
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[TextToCadResponse]:
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
    id: str,
    *,
    client: Client,
) -> Response[TextToCadResponse]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> TextToCadResponse:
    """This endpoint requires authentication by any Zoo user. The user must be the owner of the text-to-CAD model."""  # noqa: E501

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[TextToCadResponse]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> TextToCadResponse:
    """This endpoint requires authentication by any Zoo user. The user must be the owner of the text-to-CAD model."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
