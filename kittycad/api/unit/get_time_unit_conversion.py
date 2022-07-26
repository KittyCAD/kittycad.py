from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.unit_time_conversion import UnitTimeConversion
from ...models.error import Error
from ...models.unit_time_format import UnitTimeFormat
from ...models.unit_time_format import UnitTimeFormat
from ...types import Response

def _get_kwargs(
	output_format: UnitTimeFormat,
	src_format: UnitTimeFormat,
	value: float,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/unit/conversion/time/{src_format}/{output_format}?value={value}".format(client.base_url, output_format=output_format, src_format=src_format, value=value)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UnitTimeConversion, Error]]:
	if response.status_code == 200:
		response_200 = UnitTimeConversion.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UnitTimeConversion, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	output_format: UnitTimeFormat,
	src_format: UnitTimeFormat,
	value: float,
	*,
	client: Client,
) -> Response[Union[Any, UnitTimeConversion, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
		src_format=src_format,
		value=value,
		client=client,
	)

	response = httpx.get(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	output_format: UnitTimeFormat,
	src_format: UnitTimeFormat,
	value: float,
	*,
	client: Client,
) -> Optional[Union[Any, UnitTimeConversion, Error]]:
	""" Convert a time unit value to another time unit value. This is a nice endpoint to use for helper functions. """

	return sync_detailed(
		output_format=output_format,
		src_format=src_format,
		value=value,
		client=client,
	).parsed


async def asyncio_detailed(
	output_format: UnitTimeFormat,
	src_format: UnitTimeFormat,
	value: float,
	*,
	client: Client,
) -> Response[Union[Any, UnitTimeConversion, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
		src_format=src_format,
		value=value,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.get(**kwargs)

	return _build_response(response=response)


async def asyncio(
	output_format: UnitTimeFormat,
	src_format: UnitTimeFormat,
	value: float,
	*,
	client: Client,
) -> Optional[Union[Any, UnitTimeConversion, Error]]:
	""" Convert a time unit value to another time unit value. This is a nice endpoint to use for helper functions. """

	return (
		await asyncio_detailed(
		output_format=output_format,
		src_format=src_format,
		value=value,
			client=client,
		)
	).parsed
