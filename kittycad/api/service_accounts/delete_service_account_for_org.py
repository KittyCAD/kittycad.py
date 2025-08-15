"""
This module should only be accessed through client.api.
Direct imports like 'from kittycad.api.module import function' are not supported.
Use: client = KittyCAD(); client.api.module.function() instead.
"""

from typing import Any, Dict

import httpx

from ...client import Client
from ...models.service_account_uuid import ServiceAccountUuid
from ...response_helpers import raise_for_status
from ...types import Response

# Prevent direct imports - hide all public functions
__all__: list[str] = []


def _get_kwargs(
    token: ServiceAccountUuid,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/org/service-accounts/{token}".format(
        client.base_url,
        token=token,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response):
    if response.status_code == 204:
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
    token: ServiceAccountUuid,
    *,
    client: Client,
):
    """This endpoint requires authentication by an org admin. It deletes the requested service account for the organization.

    This endpoint does not actually delete the service account from the database. It merely marks the token as invalid. We still want to keep the service account in the database for historical purposes."""  # noqa: E501

    kwargs = _get_kwargs(
        token=token,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response).parsed


async def asyncio(
    token: ServiceAccountUuid,
    *,
    client: Client,
):
    """This endpoint requires authentication by an org admin. It deletes the requested service account for the organization.

    This endpoint does not actually delete the service account from the database. It merely marks the token as invalid. We still want to keep the service account in the database for historical purposes."""  # noqa: E501

    kwargs = _get_kwargs(
        token=token,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response).parsed
