from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.mesh import Mesh
from ...models.error import Error
from ...models.file_export_format import FileExportFormat
from ...types import Response

def _get_kwargs(
	output_format: FileExportFormat,
	prompt: str,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/ai/text-to-3d/{output_format}?prompt={prompt}".format(client.base_url, output_format=output_format, prompt=prompt)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Mesh, Error]]:
	if response.status_code == 200:
		response_200 = Mesh.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Mesh, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	output_format: FileExportFormat,
	prompt: str,
	*,
	client: Client,
) -> Response[Union[Any, Mesh, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
		prompt=prompt,
		client=client,
	)

	response = httpx.post(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	output_format: FileExportFormat,
	prompt: str,
	*,
	client: Client,
) -> Optional[Union[Any, Mesh, Error]]:

	return sync_detailed(
		output_format=output_format,
		prompt=prompt,
		client=client,
	).parsed


async def asyncio_detailed(
	output_format: FileExportFormat,
	prompt: str,
	*,
	client: Client,
) -> Response[Union[Any, Mesh, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
		prompt=prompt,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	output_format: FileExportFormat,
	prompt: str,
	*,
	client: Client,
) -> Optional[Union[Any, Mesh, Error]]:

	return (
		await asyncio_detailed(
		output_format=output_format,
		prompt=prompt,
			client=client,
		)
	).parsed
