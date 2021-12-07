from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.file_conversion import FileConversion
from ...models.valid_file_types import ValidFileTypes
from ...types import Response


def _get_kwargs(
    source_format: ValidFileTypes,
    output_format: ValidFileTypes,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/file/conversion/{sourceFormat}/{outputFormat}".format(
        client.base_url, sourceFormat=source_format, outputFormat=output_format
    )

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
    if response.status_code == 202:
        response_202 = FileConversion.from_dict(response.json())

        return response_202
    if response.status_code == 400:
        response_400 = None

        return response_400
    if response.status_code == 401:
        response_401 = None

        return response_401
    if response.status_code == 403:
        response_403 = None

        return response_403
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
    source_format: ValidFileTypes,
    output_format: ValidFileTypes,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, FileConversion]]:
    kwargs = _get_kwargs(
        source_format=source_format,
        output_format=output_format,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    source_format: ValidFileTypes,
    output_format: ValidFileTypes,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously."""

    return sync_detailed(
        source_format=source_format,
        output_format=output_format,
        client=client,
    ).parsed


async def asyncio_detailed(
    source_format: ValidFileTypes,
    output_format: ValidFileTypes,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, FileConversion]]:
    kwargs = _get_kwargs(
        source_format=source_format,
        output_format=output_format,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    source_format: ValidFileTypes,
    output_format: ValidFileTypes,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously."""

    return (
        await asyncio_detailed(
            source_format=source_format,
            output_format=output_format,
            client=client,
        )
    ).parsed
