from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.file_conversion import FileConversion
from ...models.file_mass import FileMass
from ...models.file_volume import FileVolume
from ...models.file_density import FileDensity
from ...models.error import Error
from ...types import Response

def _get_kwargs(
	id: str,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/user/file/conversions/{id}".format(client.base_url, id=id)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileConversion, FileMass, FileVolume, FileDensity, Error]]:
	if response.status_code == 200:
		data = response.json()
		try:
			if not isinstance(data, dict):
				raise TypeError()
			option = FileConversion.from_dict(data)
			return option
		except:
			pass
		try:
			if not isinstance(data, dict):
				raise TypeError()
			option = FileMass.from_dict(data)
			return option
		except:
			pass
		try:
			if not isinstance(data, dict):
				raise TypeError()
			option = FileVolume.from_dict(data)
			return option
		except:
			pass
		try:
			if not isinstance(data, dict):
				raise TypeError()
			option = FileDensity.from_dict(data)
			return option
		except:
			raise
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileConversion, FileMass, FileVolume, FileDensity, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	id: str,
	*,
	client: Client,
) -> Response[Union[Any, FileConversion, FileMass, FileVolume, FileDensity, Error]]:
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
	client: Client,
) -> Optional[Union[Any, FileConversion, FileMass, FileVolume, FileDensity, Error]]:
	""" Get the status and output of an async file conversion. If completed, the contents of the converted file (`output`) will be returned as a base64 encoded string.
This endpoint requires authentication by any KittyCAD user. It returns details of the requested file conversion for the user. """

	return sync_detailed(
		id=id,
		client=client,
	).parsed


async def asyncio_detailed(
	id: str,
	*,
	client: Client,
) -> Response[Union[Any, FileConversion, FileMass, FileVolume, FileDensity, Error]]:
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
	client: Client,
) -> Optional[Union[Any, FileConversion, FileMass, FileVolume, FileDensity, Error]]:
	""" Get the status and output of an async file conversion. If completed, the contents of the converted file (`output`) will be returned as a base64 encoded string.
This endpoint requires authentication by any KittyCAD user. It returns details of the requested file conversion for the user. """

	return (
		await asyncio_detailed(
		id=id,
			client=client,
		)
	).parsed
