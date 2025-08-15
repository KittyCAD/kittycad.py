from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.uuid import Uuid
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    provider_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/auth/saml/provider/{provider_id}/login".format(
        client.base_url,
        provider_id=provider_id,
    )  # noqa: E501

    if callback_url is not None:
        if "?" in url:
            url = url + "&callback_url=" + str(callback_url)
        else:
            url = url + "?callback_url=" + str(callback_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> None:
    return None
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[None]:
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
    provider_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Response[None]:
    kwargs = _get_kwargs(
        provider_id=provider_id,
        callback_url=callback_url,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    provider_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> None:
    """The UI uses this to avoid having to ask the API anything about the IdP. It already knows the SAML IdP ID from the path, so it can just link to this path and rely on the API to redirect to the actual IdP."""  # noqa: E501

    return sync_detailed(
        provider_id=provider_id,
        callback_url=callback_url,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Response[None]:
    kwargs = _get_kwargs(
        provider_id=provider_id,
        callback_url=callback_url,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    provider_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> None:
    """The UI uses this to avoid having to ask the API anything about the IdP. It already knows the SAML IdP ID from the path, so it can just link to this path and rely on the API to redirect to the actual IdP."""  # noqa: E501

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            callback_url=callback_url,
            client=client,
        )
    ).parsed
