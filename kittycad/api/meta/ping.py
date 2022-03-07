from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.pong_message import PongMessage
from ...types import Response

def _get_kwargs(
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/ping".format(client.base_url)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PongMessage]]:
	if response.status_code == 200:
		response_200 = PongMessage.from_dict(response.json())
		return response_200
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PongMessage]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	*,
	client: Client,
) -> Response[Union[Any, PongMessage]]:
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
) -> Optional[Union[Any, PongMessage]]:
	""" Simple ping to the server. """

	return sync_detailed(
		client=client,
	).parsed


async def asyncio_detailed(
	*,
	client: Client,
) -> Response[Union[Any, PongMessage]]:
	kwargs = _get_kwargs(
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	*,
	client: Client,
) -> Optional[Union[Any, PongMessage]]:
	""" Simple ping to the server. """

	return (
		await asyncio_detailed(
			client=client,
		)
	).parsed
