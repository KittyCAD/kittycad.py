from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.unit_conversion import UnitConversion
from ...models.error import Error
from ...models.unit_metric_format import UnitMetricFormat
from ...models.unit_metric_format import UnitMetricFormat
from ...types import Response

def _get_kwargs(
	output_format: UnitMetricFormat,
	src_format: UnitMetricFormat,
	value: float,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/unit/conversion/{src_format}/{output_format}?value={value}".format(client.base_url, output_format=output_format, src_format=src_format, value=value)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UnitConversion, Error]]:
	if response.status_code == 201:
		response_201 = UnitConversion.from_dict(response.json())
		return response_201
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UnitConversion, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	output_format: UnitMetricFormat,
	src_format: UnitMetricFormat,
	value: float,
	*,
	client: Client,
) -> Response[Union[Any, UnitConversion, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
		src_format=src_format,
		value=value,
		client=client,
	)

	response = httpx.post(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	output_format: UnitMetricFormat,
	src_format: UnitMetricFormat,
	value: float,
	*,
	client: Client,
) -> Optional[Union[Any, UnitConversion, Error]]:
	""" Convert a metric unit value to another metric unit value. This is a nice endpoint to use for helper functions. """

	return sync_detailed(
		output_format=output_format,
		src_format=src_format,
		value=value,
		client=client,
	).parsed


async def asyncio_detailed(
	output_format: UnitMetricFormat,
	src_format: UnitMetricFormat,
	value: float,
	*,
	client: Client,
) -> Response[Union[Any, UnitConversion, Error]]:
	kwargs = _get_kwargs(
		output_format=output_format,
		src_format=src_format,
		value=value,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	output_format: UnitMetricFormat,
	src_format: UnitMetricFormat,
	value: float,
	*,
	client: Client,
) -> Optional[Union[Any, UnitConversion, Error]]:
	""" Convert a metric unit value to another metric unit value. This is a nice endpoint to use for helper functions. """

	return (
		await asyncio_detailed(
		output_format=output_format,
		src_format=src_format,
		value=value,
			client=client,
		)
	).parsed
