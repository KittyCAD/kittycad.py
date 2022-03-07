from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.gpu_device import GPUDevice
from ...models.error_message import ErrorMessage
from ...types import Response

def _get_kwargs(
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/_internal/gpu/devices".format(client.base_url)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, [GPUDevice], ErrorMessage]]:
	if response.status_code == 200:
		response_200 = [
			GPUDevice.from_dict(item)
			for item in response.json()
		]
		return response_200
	if response.status_code == 401:
		response_401 = ErrorMessage.from_dict(response.json())
		return response_401
	if response.status_code == 403:
		response_403 = ErrorMessage.from_dict(response.json())
		return response_403
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, [GPUDevice], ErrorMessage]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	*,
	client: Client,
) -> Response[Union[Any, [GPUDevice], ErrorMessage]]:
	kwargs = _get_kwargs(
		client=client,
	)

	response = httpx.get(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	*,
	client: Client,
) -> Optional[Union[Any, [GPUDevice], ErrorMessage]]:
	""" Get information about GPU devices on this server. This is primarily used for debugging. This endpoint can only be used by specific KittyCAD employees. """

	return sync_detailed(
		client=client,
	).parsed


async def asyncio_detailed(
	*,
	client: Client,
) -> Response[Union[Any, [GPUDevice], ErrorMessage]]:
	kwargs = _get_kwargs(
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	*,
	client: Client,
) -> Optional[Union[Any, [GPUDevice], ErrorMessage]]:
	""" Get information about GPU devices on this server. This is primarily used for debugging. This endpoint can only be used by specific KittyCAD employees. """

	return (
		await asyncio_detailed(
			client=client,
		)
	).parsed
