"""
This module should only be accessed through client.api.
Direct imports like 'from kittycad.api.module import function' are not supported.
Use: client = KittyCAD(); client.api.module.function() instead.
"""

from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.uuid import Uuid
from ...response_helpers import raise_for_status
from ...types import Response

# Prevent direct imports - hide all public functions
__all__: list[str] = []


def _get_kwargs(
    org_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/auth/saml/org/{org_id}/login".format(
        client.base_url,
        org_id=org_id,
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


def _parse_response(*, response: httpx.Response):
    if response.status_code == 302:
        return None
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Any]:
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


def sync(
    org_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
):
    """Redirects the browser straight to the org’s SAML IdP."""  # noqa: E501

    kwargs = _get_kwargs(
        org_id=org_id,
        callback_url=callback_url,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response).parsed


async def asyncio(
    org_id: Uuid,
    *,
    client: Client,
    callback_url: Optional[str] = None,
):
    """Redirects the browser straight to the org’s SAML IdP."""  # noqa: E501

    kwargs = _get_kwargs(
        org_id=org_id,
        callback_url=callback_url,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response).parsed
