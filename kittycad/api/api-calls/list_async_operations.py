from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.async_api_call_results_page import AsyncApiCallResultsPage
from ...models.error import Error
from ...models.created_at_sort_mode import CreatedAtSortMode
from ...models.api_call_status import APICallStatus
from ...types import Response

def _get_kwargs(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	status: APICallStatus,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/async/operations?limit={limit}&page_token={page_token}&sort_by={sort_by}&status={status}".format(client.base_url, limit=limit, page_token=page_token, sort_by=sort_by, status=status)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AsyncApiCallResultsPage, Error]]:
	if response.status_code == 200:
		response_200 = AsyncApiCallResultsPage.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AsyncApiCallResultsPage, Error]]:
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
	status: APICallStatus,
	*,
	client: Client,
) -> Response[Union[Any, AsyncApiCallResultsPage, Error]]:
	kwargs = _get_kwargs(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
		status=status,
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
	status: APICallStatus,
	*,
	client: Client,
) -> Optional[Union[Any, AsyncApiCallResultsPage, Error]]:
	""" For async file conversion operations, this endpoint does not return the contents of converted files (`output`). To get the contents use the `/async/operations/{id}` endpoint.
This endpoint requires authentication by a KittyCAD employee. """

	return sync_detailed(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
		status=status,
		client=client,
	).parsed


async def asyncio_detailed(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	status: APICallStatus,
	*,
	client: Client,
) -> Response[Union[Any, AsyncApiCallResultsPage, Error]]:
	kwargs = _get_kwargs(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
		status=status,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	limit: int,
	page_token: str,
	sort_by: CreatedAtSortMode,
	status: APICallStatus,
	*,
	client: Client,
) -> Optional[Union[Any, AsyncApiCallResultsPage, Error]]:
	""" For async file conversion operations, this endpoint does not return the contents of converted files (`output`). To get the contents use the `/async/operations/{id}` endpoint.
This endpoint requires authentication by a KittyCAD employee. """

	return (
		await asyncio_detailed(
		limit=limit,
		page_token=page_token,
		sort_by=sort_by,
		status=status,
			client=client,
		)
	).parsed
