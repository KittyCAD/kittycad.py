from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.user import User
from ...models.error import Error
from ...types import Response

def _get_kwargs(
	id: str,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/users/{id}".format(client.base_url, id=id)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, User, Error]]:
	if response.status_code == 200:
		response_200 = User.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, User, Error]]:
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
) -> Response[Union[Any, User, Error]]:
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
) -> Optional[Union[Any, User, Error]]:
	""" To get information about yourself, use `/users/me` as the endpoint. By doing so you will get the user information for the authenticated user.
Alternatively, to get information about the authenticated user, use `/user` endpoint.
To get information about any KittyCAD user, you must be a KittyCAD employee. """

	return sync_detailed(
		id=id,
		client=client,
	).parsed


async def asyncio_detailed(
	id: str,
	*,
	client: Client,
) -> Response[Union[Any, User, Error]]:
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
) -> Optional[Union[Any, User, Error]]:
	""" To get information about yourself, use `/users/me` as the endpoint. By doing so you will get the user information for the authenticated user.
Alternatively, to get information about the authenticated user, use `/user` endpoint.
To get information about any KittyCAD user, you must be a KittyCAD employee. """

	return (
		await asyncio_detailed(
		id=id,
			client=client,
		)
	).parsed
