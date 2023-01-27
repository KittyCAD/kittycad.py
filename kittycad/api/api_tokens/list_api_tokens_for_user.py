from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_token_results_page import ApiTokenResultsPage
from ...models.error import Error
from ...models.created_at_sort_mode import CreatedAtSortMode
from ...types import Response

def _get_kwargs(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/user/api-tokens?limit={limit}&page_token={page_token}&sort_by={sort_by}".format(client.base_url, limit=limit, page_token=page_token, sort_by=sort_by)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiTokenResultsPage, Error]]:
	if response.status_code == 200:
		response_200 = ApiTokenResultsPage.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ApiTokenResultsPage, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	*,
	client: Client,
) -> Response[Union[Any, ApiTokenResultsPage, Error]]:
	kwargs = _get_kwargs(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
		client=client,
	)

	response = httpx.get(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	*,
	client: Client,
) -> Optional[Union[Any, ApiTokenResultsPage, Error]]:
	""" This endpoint requires authentication by any KittyCAD user. It returns the API tokens for the authenticated user.
The API tokens are returned in order of creation, with the most recently created API tokens first. """

	return sync_detailed(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
		client=client,
	).parsed


async def asyncio_detailed(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	*,
	client: Client,
) -> Response[Union[Any, ApiTokenResultsPage, Error]]:
	kwargs = _get_kwargs(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	*,
	client: Client,
) -> Optional[Union[Any, ApiTokenResultsPage, Error]]:
	""" This endpoint requires authentication by any KittyCAD user. It returns the API tokens for the authenticated user.
The API tokens are returned in order of creation, with the most recently created API tokens first. """

	return (
		await asyncio_detailed(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
			client=client,
		)
	).parsed
