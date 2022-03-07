from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.file_conversion import FileConversion
from ...models.error_message import ErrorMessage
from ...types import Response

def _get_kwargs(
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/_internal/async/conversions/stop".format(client.base_url)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
	if response.status_code == 200:
		response_200 = FileConversion.from_dict(response.json())
		return response_200
	if response.status_code == 401:
		response_401 = ErrorMessage.from_dict(response.json())
		return response_401
	if response.status_code == 403:
		response_403 = ErrorMessage.from_dict(response.json())
		return response_403
	if response.status_code == 404:
		response_404 = ErrorMessage.from_dict(response.json())
		return response_404
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileConversion, ErrorMessage]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	*,
	client: Client,
) -> Response[Union[Any, FileConversion, ErrorMessage]]:
	kwargs = _get_kwargs(
		client=client,
	)

	response = httpx.post(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	*,
	client: Client,
) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
	""" Stop all async conversions that are currently running. This endpoint can only be used by specific KittyCAD employees. """

	return sync_detailed(
		client=client,
	).parsed


async def asyncio_detailed(
	*,
	client: Client,
) -> Response[Union[Any, FileConversion, ErrorMessage]]:
	kwargs = _get_kwargs(
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	*,
	client: Client,
) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
	""" Stop all async conversions that are currently running. This endpoint can only be used by specific KittyCAD employees. """

	return (
		await asyncio_detailed(
			client=client,
		)
	).parsed
