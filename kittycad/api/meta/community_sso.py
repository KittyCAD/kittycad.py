from typing import Any, Dict

import httpx

from ...client import Client
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    sig: str,
    sso: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/community/sso".format(
        client.base_url,
    )  # noqa: E501

    if sig is not None:
        if "?" in url:
            url = url + "&sig=" + str(sig)
        else:
            url = url + "?sig=" + str(sig)

    if sso is not None:
        if "?" in url:
            url = url + "&sso=" + str(sso)
        else:
            url = url + "?sso=" + str(sso)

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


def sync_detailed(
    sig: str,
    sso: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        sig=sig,
        sso=sso,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sig: str,
    sso: str,
    *,
    client: Client,
):
    return sync_detailed(
        sig=sig,
        sso=sso,
        client=client,
    ).parsed


async def asyncio_detailed(
    sig: str,
    sso: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        sig=sig,
        sso=sso,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sig: str,
    sso: str,
    *,
    client: Client,
):
    return (
        await asyncio_detailed(
            sig=sig,
            sso=sso,
            client=client,
        )
    ).parsed
