from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response

def _get_kwargs(
	token: str,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/user/api-tokens/{token}".format(client.base_url, token=token)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
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
	token: str,
	*,
	client: Client,
) -> Response[Union[Any, Error]]:
	kwargs = _get_kwargs(
		token=token,
		client=client,
	)

	response = httpx.delete(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	token: str,
	*,
	client: Client,
) -> Optional[Union[Any, Error]]:
	""" This endpoint requires authentication by any KittyCAD user. It deletes the requested API token for the user.
This endpoint does not actually delete the API token from the database. It merely marks the token as invalid. We still want to keep the token in the database for historical purposes. """

	return sync_detailed(
		token=token,
		client=client,
	).parsed


async def asyncio_detailed(
	token: str,
	*,
	client: Client,
) -> Response[Union[Any, Error]]:
	kwargs = _get_kwargs(
		token=token,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.delete(**kwargs)

	return _build_response(response=response)


async def asyncio(
	token: str,
	*,
	client: Client,
) -> Optional[Union[Any, Error]]:
	""" This endpoint requires authentication by any KittyCAD user. It deletes the requested API token for the user.
This endpoint does not actually delete the API token from the database. It merely marks the token as invalid. We still want to keep the token in the database for historical purposes. """

	return (
		await asyncio_detailed(
		token=token,
			client=client,
		)
	).parsed
