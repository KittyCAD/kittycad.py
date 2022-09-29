from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.file_density import FileDensity
from ...models.error import Error
from ...models.file3_d_import_format import File3DImportFormat
from ...types import Response

def _get_kwargs(
	material_mass: float,
	src_format: File3DImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/file/density?material_mass={material_mass}&src_format={src_format}".format(client.base_url, material_mass=material_mass, src_format=src_format)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
		"content": body,
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileDensity, Error]]:
	if response.status_code == 201:
		response_201 = FileDensity.from_dict(response.json())
		return response_201
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileDensity, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	material_mass: float,
	src_format: File3DImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, FileDensity, Error]]:
	kwargs = _get_kwargs(
		material_mass=material_mass,
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
	material_mass: float,
	src_format: File3DImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, FileDensity, Error]]:
	""" Get the density of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.
If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint. """

	return sync_detailed(
		material_mass=material_mass,
		src_format=src_format,
		body=body,
		client=client,
	).parsed


async def asyncio_detailed(
	material_mass: float,
	src_format: File3DImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, FileDensity, Error]]:
	kwargs = _get_kwargs(
		material_mass=material_mass,
		src_format=src_format,
		body=body,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	material_mass: float,
	src_format: File3DImportFormat,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, FileDensity, Error]]:
	""" Get the density of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.
If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint. """

	return (
		await asyncio_detailed(
		material_mass=material_mass,
		src_format=src_format,
		body=body,
			client=client,
		)
	).parsed
