from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.unit_magnetic_flux_conversion import UnitMagneticFluxConversion
from ...models.unit_magnetic_flux_format import UnitMagneticFluxFormat
from ...types import Response


def _get_kwargs(
    output_format: UnitMagneticFluxFormat,
    src_format: UnitMagneticFluxFormat,
    value: float,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/unit/conversion/magnetic-flux/{src_format}/{output_format}".format(
        client.base_url, output_format=output_format, src_format=src_format
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
) -> Optional[Union[UnitMagneticFluxConversion, Error]]:
    if response.status_code == 200:
        response_200 = UnitMagneticFluxConversion.from_dict(response.json())
        return response_200
    if response.status_code == 400:
        response_4XX = Error.from_dict(response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error.from_dict(response.json())
        return response_5XX
    return Error.from_dict(response.json())


def _build_response(
    *, response: httpx.Response
) -> Response[Optional[Union[UnitMagneticFluxConversion, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    output_format: UnitMagneticFluxFormat,
    src_format: UnitMagneticFluxFormat,
    value: float,
    *,
    client: Client,
) -> Response[Optional[Union[UnitMagneticFluxConversion, Error]]]:
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
    output_format: UnitMagneticFluxFormat,
    src_format: UnitMagneticFluxFormat,
    value: float,
    *,
    client: Client,
) -> Optional[Union[UnitMagneticFluxConversion, Error]]:
    """Convert a magnetic flux unit value to another magnetic flux unit value. This is a nice endpoint to use for helper functions."""  # noqa: E501

    return sync_detailed(
        output_format=output_format,
        src_format=src_format,
        value=value,
        client=client,
    ).parsed


async def asyncio_detailed(
    output_format: UnitMagneticFluxFormat,
    src_format: UnitMagneticFluxFormat,
    value: float,
    *,
    client: Client,
) -> Response[Optional[Union[UnitMagneticFluxConversion, Error]]]:
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
    output_format: UnitMagneticFluxFormat,
    src_format: UnitMagneticFluxFormat,
    value: float,
    *,
    client: Client,
) -> Optional[Union[UnitMagneticFluxConversion, Error]]:
    """Convert a magnetic flux unit value to another magnetic flux unit value. This is a nice endpoint to use for helper functions."""  # noqa: E501

    return (
        await asyncio_detailed(
            output_format=output_format,
            src_format=src_format,
            value=value,
            client=client,
        )
    ).parsed
