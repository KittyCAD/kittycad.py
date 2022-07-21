from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.app_client_info import AppClientInfo
from ...models.error import Error
from ...types import Response

def _get_kwargs(
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/apps/github/consent".format(client.base_url)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AppClientInfo, Error]]:
	if response.status_code == 200:
		response_200 = AppClientInfo.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AppClientInfo, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	*,
	client: Client,
) -> Response[Union[Any, AppClientInfo, Error]]:
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
) -> Optional[Union[Any, AppClientInfo, Error]]:
	""" This is different than OAuth 2.0 authentication for users. This endpoint grants access for KittyCAD to access user's repos.
The user doesn't need KittyCAD OAuth authorization for this endpoint, this is purely for the GitHub permissions to access repos. """

	return sync_detailed(
		client=client,
	).parsed


async def asyncio_detailed(
	*,
	client: Client,
) -> Response[Union[Any, AppClientInfo, Error]]:
	kwargs = _get_kwargs(
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	*,
	client: Client,
) -> Optional[Union[Any, AppClientInfo, Error]]:
	""" This is different than OAuth 2.0 authentication for users. This endpoint grants access for KittyCAD to access user's repos.
The user doesn't need KittyCAD OAuth authorization for this endpoint, this is purely for the GitHub permissions to access repos. """

	return (
		await asyncio_detailed(
			client=client,
		)
	).parsed
