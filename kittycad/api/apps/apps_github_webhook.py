from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response

def _get_kwargs(
	body: bytes,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/apps/github/webhook".format(client.base_url)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
		"content": body,
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
	if response.status_code == 204:
		response_204 = None
		return response_204
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, Error]]:
	kwargs = _get_kwargs(
		body=body,
		client=client,
	)

	response = httpx.post(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, Error]]:
	""" These come from the GitHub app. """

	return sync_detailed(
		body=body,
		client=client,
	).parsed


async def asyncio_detailed(
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, Error]]:
	kwargs = _get_kwargs(
		body=body,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, Error]]:
	""" These come from the GitHub app. """

	return (
		await asyncio_detailed(
		body=body,
			client=client,
		)
	).parsed