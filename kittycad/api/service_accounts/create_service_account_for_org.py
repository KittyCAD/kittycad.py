from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.service_account import ServiceAccount
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    label: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/org/service-accounts".format(
        client.base_url,
    )  # noqa: E501

    if label is not None:
        if "?" in url:
            url = url + "&label=" + str(label)
        else:
            url = url + "?label=" + str(label)

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
) -> Optional[Union[ServiceAccount, Error]]:
    if response.status_code == 201:
        response_201 = ServiceAccount(**response.json())
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
) -> Response[Optional[Union[ServiceAccount, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    label: Optional[str] = None,
) -> Response[Optional[Union[ServiceAccount, Error]]]:
    kwargs = _get_kwargs(
        label=label,
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
    label: Optional[str] = None,
) -> Optional[Union[ServiceAccount, Error]]:
    """This endpoint requires authentication by an org admin. It creates a new service account for the organization."""  # noqa: E501

    return sync_detailed(
        label=label,
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    label: Optional[str] = None,
) -> Response[Optional[Union[ServiceAccount, Error]]]:
    kwargs = _get_kwargs(
        label=label,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    label: Optional[str] = None,
) -> Optional[Union[ServiceAccount, Error]]:
    """This endpoint requires authentication by an org admin. It creates a new service account for the organization."""  # noqa: E501

    return (
        await asyncio_detailed(
            label=label,
            client=client,
        )
    ).parsed
