from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.physics_constant import PhysicsConstant
from ...models.physics_constant_name import PhysicsConstantName
from ...types import Response


def _get_kwargs(
    constant: PhysicsConstantName,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/constant/physics/{constant}".format(
        client.base_url, constant=constant
    )  # noqa: E501

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
) -> Optional[Union[PhysicsConstant, Error]]:
    if response.status_code == 200:
        response_200 = PhysicsConstant.from_dict(response.json())
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
) -> Response[Optional[Union[PhysicsConstant, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    constant: PhysicsConstantName,
    *,
    client: Client,
) -> Response[Optional[Union[PhysicsConstant, Error]]]:
    kwargs = _get_kwargs(
        constant=constant,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    constant: PhysicsConstantName,
    *,
    client: Client,
) -> Optional[Union[PhysicsConstant, Error]]:

    return sync_detailed(
        constant=constant,
        client=client,
    ).parsed


async def asyncio_detailed(
    constant: PhysicsConstantName,
    *,
    client: Client,
) -> Response[Optional[Union[PhysicsConstant, Error]]]:
    kwargs = _get_kwargs(
        constant=constant,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    constant: PhysicsConstantName,
    *,
    client: Client,
) -> Optional[Union[PhysicsConstant, Error]]:

    return (
        await asyncio_detailed(
            constant=constant,
            client=client,
        )
    ).parsed
