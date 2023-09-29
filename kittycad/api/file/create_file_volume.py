from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.file_import_format import FileImportFormat
from ...models.file_volume import FileVolume
from ...models.unit_volume import UnitVolume
from ...types import Response


def _get_kwargs(
    
    
    output_unit: UnitVolume,
    
    
    
    src_format: FileImportFormat,
    
    
    
    body: bytes,
    
    
    *,
    client: Client,
    
    
    
    
    
    
    
) -> Dict[str, Any]:
    url = "{}/file/volume".format(client.base_url, )  # noqa: E501
    
    
    if output_unit is not None:
        if "?" in url:
            url = url + "&output_unit=" + str(output_unit)
        else:
            url = url + "?output_unit=" + str(output_unit)
    
    
    
    if src_format is not None:
        if "?" in url:
            url = url + "&src_format=" + str(src_format)
        else:
            url = url + "?src_format=" + str(src_format)
    
    
    
    


    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[FileVolume, Error]] :
	if response.status_code == 201:
		response_201 = FileVolume.from_dict(response.json())
		return response_201
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return Error.from_dict(response.json())



def _build_response(
    *, response: httpx.Response
)  -> Response[Optional[Union[FileVolume, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    
    
    output_unit: UnitVolume,
    
    
    
    src_format: FileImportFormat,
    
    
    
    body: bytes,
    
    
    *,
    client: Client,
    
    
    
    
    
    
    
)  -> Response[Optional[Union[FileVolume, Error]]]:
    kwargs = _get_kwargs(
        
        output_unit=output_unit,
        
        src_format=src_format,
        
        body=body,
        
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    
    
    output_unit: UnitVolume,
    
    
    
    src_format: FileImportFormat,
    
    
    
    body: bytes,
    
    
    *,
    client: Client,
    
    
    
    
    
    
    
)  -> Optional[Union[FileVolume, Error]] :
    """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.
This endpoint returns the cubic measure units.
In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.
Get the volume of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.
If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""  # noqa: E501

    return sync_detailed(
        
        output_unit=output_unit,
        
        src_format=src_format,
        
        body=body,
        
        client=client,
    ).parsed


async def asyncio_detailed(
    
    
    output_unit: UnitVolume,
    
    
    
    src_format: FileImportFormat,
    
    
    
    body: bytes,
    
    
    *,
    client: Client,
    
    
    
    
    
    
    
)  -> Response[Optional[Union[FileVolume, Error]]]:
    kwargs = _get_kwargs(
        
        output_unit=output_unit,
        
        src_format=src_format,
        
        body=body,
        
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    
    
    output_unit: UnitVolume,
    
    
    
    src_format: FileImportFormat,
    
    
    
    body: bytes,
    
    
    *,
    client: Client,
    
    
    
    
    
    
    
)  -> Optional[Union[FileVolume, Error]] :
    """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.
This endpoint returns the cubic measure units.
In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.
Get the volume of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.
If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""  # noqa: E501

    return (
        await asyncio_detailed(
            
            output_unit=output_unit,
            
            src_format=src_format,
            
            body=body,
            
            client=client,
        )
    ).parsed
