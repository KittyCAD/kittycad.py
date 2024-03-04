from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.ai_feedback import AiFeedback
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    feedback: AiFeedback,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/text-to-cad/{id}".format(
        client.base_url,
        id=id,
    )  # noqa: E501

    if feedback is not None:

        if "?" in url:
            url = url + "&feedback=" + str(feedback)
        else:
            url = url + "?feedback=" + str(feedback)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    return None
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(*, response: httpx.Response) -> Response[Optional[Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    feedback: AiFeedback,
    *,
    client: Client,
) -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        id=id,
        feedback=feedback,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    feedback: AiFeedback,
    *,
    client: Client,
) -> Optional[Error]:
    """This endpoint requires authentication by any Zoo user. The user must be the owner of the text-to-CAD model, in order to give feedback."""  # noqa: E501

    return sync_detailed(
        id=id,
        feedback=feedback,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    feedback: AiFeedback,
    *,
    client: Client,
) -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        id=id,
        feedback=feedback,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    feedback: AiFeedback,
    *,
    client: Client,
) -> Optional[Error]:
    """This endpoint requires authentication by any Zoo user. The user must be the owner of the text-to-CAD model, in order to give feedback."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            feedback=feedback,
            client=client,
        )
    ).parsed
