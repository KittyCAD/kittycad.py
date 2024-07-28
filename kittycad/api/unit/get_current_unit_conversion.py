from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.unit_current import UnitCurrent
from ...models.unit_current_conversion import UnitCurrentConversion
from ...types import Response


def _get_kwargs(
    input_unit: UnitCurrent,
    output_unit: UnitCurrent,
    value: float,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/unit/conversion/current/{input_unit}/{output_unit}".format(
        client.base_url,
        input_unit=input_unit,
        output_unit=output_unit,
    )  # noqa: E501

    if value is not None:

        if "?" in url:
            url = url + "&value=" + str(value)
        else:
            url = url + "?value=" + str(value)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[UnitCurrentConversion, Error]]:
    if response.status_code == 200:
        response_200 = UnitCurrentConversion(**response.json())
        return response_200
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(
    *, response: httpx.Response
) -> Response[Optional[Union[UnitCurrentConversion, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    input_unit: UnitCurrent,
    output_unit: UnitCurrent,
    value: float,
    *,
    client: Client,
) -> Response[Optional[Union[UnitCurrentConversion, Error]]]:
    kwargs = _get_kwargs(
        input_unit=input_unit,
        output_unit=output_unit,
        value=value,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    input_unit: UnitCurrent,
    output_unit: UnitCurrent,
    value: float,
    *,
    client: Client,
) -> Optional[Union[UnitCurrentConversion, Error]]:
    """Convert a current unit value to another current unit value. This is a nice endpoint to use for helper functions."""  # noqa: E501

    return sync_detailed(
        input_unit=input_unit,
        output_unit=output_unit,
        value=value,
        client=client,
    ).parsed


async def asyncio_detailed(
    input_unit: UnitCurrent,
    output_unit: UnitCurrent,
    value: float,
    *,
    client: Client,
) -> Response[Optional[Union[UnitCurrentConversion, Error]]]:
    kwargs = _get_kwargs(
        input_unit=input_unit,
        output_unit=output_unit,
        value=value,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    input_unit: UnitCurrent,
    output_unit: UnitCurrent,
    value: float,
    *,
    client: Client,
) -> Optional[Union[UnitCurrentConversion, Error]]:
    """Convert a current unit value to another current unit value. This is a nice endpoint to use for helper functions."""  # noqa: E501

    return (
        await asyncio_detailed(
            input_unit=input_unit,
            output_unit=output_unit,
            value=value,
            client=client,
        )
    ).parsed
