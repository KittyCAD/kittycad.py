from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.modeling_cmd_req import ModelingCmdReq
from ...types import Response


def _get_kwargs(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/modeling/cmd".format(client.base_url)  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[dict, Error]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Optional[Union[dict, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Response[Optional[Union[dict, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Optional[Union[dict, Error]]:
    """Response depends on which command was submitted, so unfortunately the OpenAPI schema can't generate the right response type."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Response[Optional[Union[dict, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Optional[Union[dict, Error]]:
    """Response depends on which command was submitted, so unfortunately the OpenAPI schema can't generate the right response type."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
