from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_call_query_group import ApiCallQueryGroup
from ...models.error import Error
from ...models.api_call_query_group_by import ApiCallQueryGroupBy
from ...types import Response

def _get_kwargs(
	group_by: ApiCallQueryGroupBy,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/api-call-metrics?group_by={group_by}".format(client.base_url, group_by=group_by)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, [ApiCallQueryGroup], Error]]:
	if response.status_code == 200:
		response_200 = [
			ApiCallQueryGroup.from_dict(item)
			for item in response.json()
		]
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, [ApiCallQueryGroup], Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	group_by: ApiCallQueryGroupBy,
	*,
	client: Client,
) -> Response[Union[Any, [ApiCallQueryGroup], Error]]:
	kwargs = _get_kwargs(
		group_by=group_by,
		client=client,
	)

	response = httpx.get(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	group_by: ApiCallQueryGroupBy,
	*,
	client: Client,
) -> Optional[Union[Any, [ApiCallQueryGroup], Error]]:
	""" This endpoint requires authentication by a KittyCAD employee. The API calls are grouped by the parameter passed. """

	return sync_detailed(
		group_by=group_by,
		client=client,
	).parsed


async def asyncio_detailed(
	group_by: ApiCallQueryGroupBy,
	*,
	client: Client,
) -> Response[Union[Any, [ApiCallQueryGroup], Error]]:
	kwargs = _get_kwargs(
		group_by=group_by,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	group_by: ApiCallQueryGroupBy,
	*,
	client: Client,
) -> Optional[Union[Any, [ApiCallQueryGroup], Error]]:
	""" This endpoint requires authentication by a KittyCAD employee. The API calls are grouped by the parameter passed. """

	return (
		await asyncio_detailed(
		group_by=group_by,
			client=client,
		)
	).parsed
