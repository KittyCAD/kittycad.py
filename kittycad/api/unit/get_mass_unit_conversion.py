"""
This module should only be accessed through client.api.
Direct imports like 'from kittycad.api.module import function' are not supported.
Use: client = KittyCAD(); client.api.module.function() instead.
"""

from typing import Any, Dict

import httpx

from ...client import Client
from ...models.unit_mass import UnitMass
from ...models.unit_mass_conversion import UnitMassConversion
from ...response_helpers import raise_for_status
from ...types import Response

# Prevent direct imports - hide all public functions
__all__: list[str] = []


def _get_kwargs(
    input_unit: UnitMass,
    output_unit: UnitMass,
    value: float,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/unit/conversion/mass/{input_unit}/{output_unit}".format(
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


def _parse_response(*, response: httpx.Response) -> UnitMassConversion:
    if response.status_code == 200:
        response_200 = UnitMassConversion(**response.json())
        return response_200
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[UnitMassConversion]:
    # Check for errors first - this will raise exceptions for non-success status codes
    # before we try to parse the response
    if not response.is_success:
        raise_for_status(response)

    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync(
    input_unit: UnitMass,
    output_unit: UnitMass,
    value: float,
    *,
    client: Client,
) -> UnitMassConversion:
    """Convert a mass unit value to another mass unit value. This is a nice endpoint to use for helper functions."""  # noqa: E501

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

    return _build_response(response=response).parsed


async def asyncio(
    input_unit: UnitMass,
    output_unit: UnitMass,
    value: float,
    *,
    client: Client,
) -> UnitMassConversion:
    """Convert a mass unit value to another mass unit value. This is a nice endpoint to use for helper functions."""  # noqa: E501

    kwargs = _get_kwargs(
        input_unit=input_unit,
        output_unit=output_unit,
        value=value,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response).parsed
