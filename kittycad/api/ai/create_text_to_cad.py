from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.file_export_format import FileExportFormat
from ...models.text_to_cad import TextToCad
from ...models.text_to_cad_create_body import TextToCadCreateBody
from ...types import Response


def _get_kwargs(
    
    
    output_format: FileExportFormat,
    
    
    
    body: TextToCadCreateBody,
    
    
    *,
    client: Client,
    
    
    
    
    
) -> Dict[str, Any]:
    url = "{}/ai/text-to-cad/{output_format}".format(client.base_url, output_format=output_format,)  # noqa: E501
    
    
    
    
    


    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[TextToCad, Error]] :
	if response.status_code == 201:
		response_201 = TextToCad.from_dict(response.json())
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
)  -> Response[Optional[Union[TextToCad, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    
    
    output_format: FileExportFormat,
    
    
    
    body: TextToCadCreateBody,
    
    
    *,
    client: Client,
    
    
    
    
    
)  -> Response[Optional[Union[TextToCad, Error]]]:
    kwargs = _get_kwargs(
        
        output_format=output_format,
        
        body=body,
        
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    
    
    output_format: FileExportFormat,
    
    
    
    body: TextToCadCreateBody,
    
    
    *,
    client: Client,
    
    
    
    
    
)  -> Optional[Union[TextToCad, Error]] :
    """This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.
This is an alpha endpoint. It will change in the future. The current output is honestly pretty bad. So if you find this endpoint, you get what you pay for, which currently is nothing. But in the future will be made a lot better."""  # noqa: E501

    return sync_detailed(
        
        output_format=output_format,
        
        body=body,
        
        client=client,
    ).parsed


async def asyncio_detailed(
    
    
    output_format: FileExportFormat,
    
    
    
    body: TextToCadCreateBody,
    
    
    *,
    client: Client,
    
    
    
    
    
)  -> Response[Optional[Union[TextToCad, Error]]]:
    kwargs = _get_kwargs(
        
        output_format=output_format,
        
        body=body,
        
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    
    
    output_format: FileExportFormat,
    
    
    
    body: TextToCadCreateBody,
    
    
    *,
    client: Client,
    
    
    
    
    
)  -> Optional[Union[TextToCad, Error]] :
    """This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.
This is an alpha endpoint. It will change in the future. The current output is honestly pretty bad. So if you find this endpoint, you get what you pay for, which currently is nothing. But in the future will be made a lot better."""  # noqa: E501

    return (
        await asyncio_detailed(
            
            output_format=output_format,
            
            body=body,
            
            client=client,
        )
    ).parsed
