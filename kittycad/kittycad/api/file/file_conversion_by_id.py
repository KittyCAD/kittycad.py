from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.file_conversion import FileConversion
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/file/conversion/{id}".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileConversion]]:
    if response.status_code == 200:
        response_200 = FileConversion.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = None

        return response_400
    if response.status_code == 401:
        response_401 = None

        return response_401
    if response.status_code == 403:
        response_403 = None

        return response_403
    if response.status_code == 404:
        response_404 = None

        return response_404
    if response.status_code == 406:
        response_406 = None

        return response_406
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileConversion]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, FileConversion]]:
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
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Get the status of a file conversion."""

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, FileConversion]]:
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
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Get the status of a file conversion."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
