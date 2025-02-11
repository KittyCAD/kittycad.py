from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.text_to_cad_multi_file_iteration import TextToCadMultiFileIteration
from ...models.text_to_cad_multi_file_iteration_body import (
    TextToCadMultiFileIterationBody,
)
from ...types import Response


def _get_kwargs(
    body: TextToCadMultiFileIterationBody,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ml/text-to-cad/multi-file/iteration".format(
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
) -> Optional[Union[TextToCadMultiFileIteration, Error]]:
    if response.status_code == 201:
        response_201 = TextToCadMultiFileIteration(**response.json())
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
) -> Response[Optional[Union[TextToCadMultiFileIteration, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: TextToCadMultiFileIterationBody,
    *,
    client: Client,
) -> Response[Optional[Union[TextToCadMultiFileIteration, Error]]]:
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
    body: TextToCadMultiFileIterationBody,
    *,
    client: Client,
) -> Optional[Union[TextToCadMultiFileIteration, Error]]:
    """This endpoint can iterate on multi-file models.

    Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

    You always get the whole code back, even if you only changed a small part of it. This endpoint will always return all the code back, including files that were not changed. If your original source code imported a stl/gltf/step/etc file, the output will not include that file since the model will never change non-kcl files. The endpoint will only return the kcl files that were changed.

    This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: TextToCadMultiFileIterationBody,
    *,
    client: Client,
) -> Response[Optional[Union[TextToCadMultiFileIteration, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: TextToCadMultiFileIterationBody,
    *,
    client: Client,
) -> Optional[Union[TextToCadMultiFileIteration, Error]]:
    """This endpoint can iterate on multi-file models.

    Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

    You always get the whole code back, even if you only changed a small part of it. This endpoint will always return all the code back, including files that were not changed. If your original source code imported a stl/gltf/step/etc file, the output will not include that file since the model will never change non-kcl files. The endpoint will only return the kcl files that were changed.

    This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
