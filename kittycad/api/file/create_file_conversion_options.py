from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.conversion_params import ConversionParams
from ...models.error import Error
from ...models.file_conversion import FileConversion
from ...types import Response


def _get_kwargs(
    body: ConversionParams,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/file/conversion".format(
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[FileConversion, Error]]:
    if response.status_code == 201:
        response_201 = FileConversion(**response.json())
        return response_201
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(
    *, response: httpx.Response
) -> Response[Optional[Union[FileConversion, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: ConversionParams,
    *,
    client: Client,
) -> Response[Optional[Union[FileConversion, Error]]]:
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
    body: ConversionParams,
    *,
    client: Client,
) -> Optional[Union[FileConversion, Error]]:
    """This takes a HTTP multipart body with these fields in any order:

     - The input and output format options (as JSON), name is 'body'.  - The files to convert, in raw binary. Must supply filenames.

    This starts a conversion job and returns the `id` of the operation. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: ConversionParams,
    *,
    client: Client,
) -> Response[Optional[Union[FileConversion, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: ConversionParams,
    *,
    client: Client,
) -> Optional[Union[FileConversion, Error]]:
    """This takes a HTTP multipart body with these fields in any order:

     - The input and output format options (as JSON), name is 'body'.  - The files to convert, in raw binary. Must supply filenames.

    This starts a conversion job and returns the `id` of the operation. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
