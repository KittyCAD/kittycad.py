from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.file2_d_vector_conversion import File2DVectorConversion
from ...models.error import Error
from ...models.file2_d_vector_export_format import File2DVectorExportFormat
from ...models.file2_d_vector_import_format import File2DVectorImportFormat
from ...types import Response

def _get_kwargs(
	output_format: File2DVectorExportFormat,
	src_format: File2DVectorImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/file/2d/vector/conversion/{src_format}/{output_format}".format(client.base_url, output_format=output_format, src_format=src_format)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
		"content": body,
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, File2DVectorConversion, Error]]:
	if response.status_code == 201:
		response_201 = File2DVectorConversion.from_dict(response.json())
		return response_201
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, File2DVectorConversion, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	output_format: File2DVectorExportFormat,
	src_format: File2DVectorImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, File2DVectorConversion, Error]]:
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
	output_format: File2DVectorExportFormat,
	src_format: File2DVectorImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, File2DVectorConversion, Error]]:
	""" Convert a 2D Vector file from one format to another. If the file being converted is larger than 25MB, it will be performed asynchronously.
If the conversion is performed synchronously, the contents of the converted file (`output`) will be returned as a base64 encoded string.
If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint. """

	return sync_detailed(
		output_format=output_format,
		src_format=src_format,
		body=body,
		client=client,
	).parsed


async def asyncio_detailed(
	output_format: File2DVectorExportFormat,
	src_format: File2DVectorImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, File2DVectorConversion, Error]]:
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
	output_format: File2DVectorExportFormat,
	src_format: File2DVectorImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, File2DVectorConversion, Error]]:
	""" Convert a 2D Vector file from one format to another. If the file being converted is larger than 25MB, it will be performed asynchronously.
If the conversion is performed synchronously, the contents of the converted file (`output`) will be returned as a base64 encoded string.
If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint. """

	return (
		await asyncio_detailed(
		output_format=output_format,
		src_format=src_format,
		body=body,
			client=client,
		)
	).parsed