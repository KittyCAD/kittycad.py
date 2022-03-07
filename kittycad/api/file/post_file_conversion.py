from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.file_conversion import FileConversion
from ...models.error_message import ErrorMessage
from ...models.valid_source_file_format import ValidSourceFileFormat
from ...models.valid_output_file_format import ValidOutputFileFormat
from ...types import Response

def _get_kwargs(
	source_format: ValidSourceFileFormat,
	output_format: ValidOutputFileFormat,
	body: bytes,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/file/conversion/{sourceFormat}/{outputFormat}".format(client.base_url, sourceFormat=source_format, outputFormat=output_format)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
		"content": body,
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
	if response.status_code == 200:
		response_200 = FileConversion.from_dict(response.json())
		return response_200
	if response.status_code == 202:
		response_202 = FileConversion.from_dict(response.json())
		return response_202
	if response.status_code == 400:
		response_400 = ErrorMessage.from_dict(response.json())
		return response_400
	if response.status_code == 401:
		response_401 = ErrorMessage.from_dict(response.json())
		return response_401
	if response.status_code == 403:
		response_403 = ErrorMessage.from_dict(response.json())
		return response_403
	if response.status_code == 406:
		response_406 = ErrorMessage.from_dict(response.json())
		return response_406
	if response.status_code == 500:
		response_500 = ErrorMessage.from_dict(response.json())
		return response_500
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileConversion, ErrorMessage]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	source_format: ValidSourceFileFormat,
	output_format: ValidOutputFileFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, FileConversion, ErrorMessage]]:
	kwargs = _get_kwargs(
		source_format=source_format,
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
	source_format: ValidSourceFileFormat,
	output_format: ValidOutputFileFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
	""" Convert a CAD file from one format to another. If the file being converted is larger than 30MB, it will be performed asynchronously. """

	return sync_detailed(
		source_format=source_format,
		output_format=output_format,
		body=body,
		client=client,
	).parsed


async def asyncio_detailed(
	source_format: ValidSourceFileFormat,
	output_format: ValidOutputFileFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, FileConversion, ErrorMessage]]:
	kwargs = _get_kwargs(
		source_format=source_format,
		output_format=output_format,
		body=body,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	source_format: ValidSourceFileFormat,
	output_format: ValidOutputFileFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
	""" Convert a CAD file from one format to another. If the file being converted is larger than 30MB, it will be performed asynchronously. """

	return (
		await asyncio_detailed(
			source_format=source_format,
			output_format=output_format,
			body=body,
			client=client,
		)
	).parsed
