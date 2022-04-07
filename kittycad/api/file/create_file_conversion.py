from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.file_conversion_with_output import FileConversionWithOutput
from ...models.error import Error
from ...models.file_conversion_output_format import FileConversionOutputFormat
from ...models.file_conversion_source_format import FileConversionSourceFormat
from ...types import Response

def _get_kwargs(
	output_format: FileConversionOutputFormat,
	src_format: FileConversionSourceFormat,
	body: bytes,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/file/conversion/{src_format}/{output_format}".format(client.base_url, output_format=output_format, src_format=src_format)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
		"content": body,
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileConversionWithOutput, Error]]:
	if response.status_code == 201:
		response_201 = FileConversionWithOutput.from_dict(response.json())
		return response_201
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileConversionWithOutput, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	output_format: FileConversionOutputFormat,
	src_format: FileConversionSourceFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, FileConversionWithOutput, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
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
	output_format: FileConversionOutputFormat,
	src_format: FileConversionSourceFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, FileConversionWithOutput, Error]]:
	""" Convert a CAD file from one format to another. If the file being converted is larger than 30MB, it will be performed asynchronously.
If the conversion is performed synchronously, the contents of the converted file (`output`) will be returned as a base64 encoded string.
If the conversion is performed asynchronously, the `id` of the conversion will be returned. You can use the `id` returned from the request to get status information about the async conversion from the `/file/conversions/{id}` endpoint. """

	return sync_detailed(
		output_format=output_format,
		src_format=src_format,
		body=body,
		client=client,
	).parsed


async def asyncio_detailed(
	output_format: FileConversionOutputFormat,
	src_format: FileConversionSourceFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, FileConversionWithOutput, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
		src_format=src_format,
		body=body,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	output_format: FileConversionOutputFormat,
	src_format: FileConversionSourceFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, FileConversionWithOutput, Error]]:
	""" Convert a CAD file from one format to another. If the file being converted is larger than 30MB, it will be performed asynchronously.
If the conversion is performed synchronously, the contents of the converted file (`output`) will be returned as a base64 encoded string.
If the conversion is performed asynchronously, the `id` of the conversion will be returned. You can use the `id` returned from the request to get status information about the async conversion from the `/file/conversions/{id}` endpoint. """

	return (
		await asyncio_detailed(
			output_format=output_format,
			src_format=src_format,
			body=body,
			client=client,
		)
	).parsed
