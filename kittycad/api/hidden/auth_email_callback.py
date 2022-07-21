from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response

def _get_kwargs(
	callback_url: str,
	email: str,
	token: str,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/auth/email/callback?callback_url={callback_url}&email={email}&token={token}".format(client.base_url, callback_url=callback_url, email=email, token=token)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
	if response.status_code == 302:
		response_302 = None
		return response_302
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
	callback_url: str,
	email: str,
	token: str,
	*,
	client: Client,
) -> Response[Union[Any, Error]]:
	kwargs = _get_kwargs(
		callback_url=callback_url,
		email=email,
		token=token,
		client=client,
	)

	response = httpx.get(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	callback_url: str,
	email: str,
	token: str,
	*,
	client: Client,
) -> Optional[Union[Any, Error]]:

	return sync_detailed(
		callback_url=callback_url,
		email=email,
		token=token,
		client=client,
	).parsed


async def asyncio_detailed(
	callback_url: str,
	email: str,
	token: str,
	*,
	client: Client,
) -> Response[Union[Any, Error]]:
	kwargs = _get_kwargs(
		callback_url=callback_url,
		email=email,
		token=token,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	callback_url: str,
	email: str,
	token: str,
	*,
	client: Client,
) -> Optional[Union[Any, Error]]:

	return (
		await asyncio_detailed(
		callback_url=callback_url,
		email=email,
		token=token,
			client=client,
		)
	).parsed
