from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.kcl_model import KclModel
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ml/convert/proprietary-to-kcl".format(
        client.base_url,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[KclModel, Error]]:
    if response.status_code == 201:
        response_201 = KclModel(**response.json())
        return response_201
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(
    *, response: httpx.Response
) -> Response[Optional[Union[KclModel, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Optional[Union[KclModel, Error]]]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[KclModel, Error]]:
    """This endpoint is used to convert a proprietary CAD format to KCL. The file passed MUST have feature tree data.

    A STEP file does not have feature tree data, so it will not work. A sldprt file does have feature tree data, so it will work."""  # noqa: E501

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Optional[Union[KclModel, Error]]]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[KclModel, Error]]:
    """This endpoint is used to convert a proprietary CAD format to KCL. The file passed MUST have feature tree data.

    A STEP file does not have feature tree data, so it will not work. A sldprt file does have feature tree data, so it will work."""  # noqa: E501

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
