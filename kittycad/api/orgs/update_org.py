from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.org import Org
from ...models.org_details import OrgDetails
from ...types import Response


def _get_kwargs(
    body: OrgDetails,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/org".format(
        client.base_url,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body.model_dump_json(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Org, Error]]:
    if response.status_code == 200:
        response_200 = Org(**response.json())
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
) -> Response[Optional[Union[Org, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: OrgDetails,
    *,
    client: Client,
) -> Response[Optional[Union[Org, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    body: OrgDetails,
    *,
    client: Client,
) -> Optional[Union[Org, Error]]:
    """This endpoint requires authentication by an org admin. It updates the authenticated user's org."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: OrgDetails,
    *,
    client: Client,
) -> Response[Optional[Union[Org, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: OrgDetails,
    *,
    client: Client,
) -> Optional[Union[Org, Error]]:
    """This endpoint requires authentication by an org admin. It updates the authenticated user's org."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
