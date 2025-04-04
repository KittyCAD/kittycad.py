from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.text_to_cad_iteration import TextToCadIteration
from ...models.text_to_cad_iteration_body import TextToCadIterationBody
from ...types import Response


def _get_kwargs(
    body: TextToCadIterationBody,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ml/text-to-cad/iteration".format(
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[TextToCadIteration, Error]]:
    if response.status_code == 201:
        response_201 = TextToCadIteration(**response.json())
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
) -> Response[Optional[Union[TextToCadIteration, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: TextToCadIterationBody,
    *,
    client: Client,
) -> Response[Optional[Union[TextToCadIteration, Error]]]:
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
    body: TextToCadIterationBody,
    *,
    client: Client,
) -> Optional[Union[TextToCadIteration, Error]]:
    """Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

    You always get the whole code back, even if you only changed a small part of it.

    This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

    This endpoint will soon be deprecated in favor of the `/ml/text-to-cad/multi-file/iteration` endpoint. In that the endpoint path will remain but it will have the same behavior as `ml/text-to-cad/multi-file/iteration`."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: TextToCadIterationBody,
    *,
    client: Client,
) -> Response[Optional[Union[TextToCadIteration, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: TextToCadIterationBody,
    *,
    client: Client,
) -> Optional[Union[TextToCadIteration, Error]]:
    """Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

    You always get the whole code back, even if you only changed a small part of it.

    This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

    This endpoint will soon be deprecated in favor of the `/ml/text-to-cad/multi-file/iteration` endpoint. In that the endpoint path will remain but it will have the same behavior as `ml/text-to-cad/multi-file/iteration`."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
