from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    email: str,
    token: str,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/auth/email/callback".format(
        client.base_url,
    )  # noqa: E501

    if callback_url is not None:

        if "?" in url:
            url = url + "&callback_url=" + str(callback_url)
        else:
            url = url + "?callback_url=" + str(callback_url)

    if email is not None:

        if "?" in url:
            url = url + "&email=" + str(email)
        else:
            url = url + "?email=" + str(email)

    if token is not None:

        if "?" in url:
            url = url + "&token=" + str(token)
        else:
            url = url + "?token=" + str(token)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    return None
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(*, response: httpx.Response) -> Response[Optional[Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    email: str,
    token: str,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        callback_url=callback_url,
        email=email,
        token=token,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    email: str,
    token: str,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Optional[Error]:

    return sync_detailed(
        callback_url=callback_url,
        email=email,
        token=token,
        client=client,
    ).parsed


async def asyncio_detailed(
    email: str,
    token: str,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        callback_url=callback_url,
        email=email,
        token=token,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    email: str,
    token: str,
    *,
    client: Client,
    callback_url: Optional[str] = None,
) -> Optional[Error]:

    return (
        await asyncio_detailed(
            callback_url=callback_url,
            email=email,
            token=token,
            client=client,
        )
    ).parsed
