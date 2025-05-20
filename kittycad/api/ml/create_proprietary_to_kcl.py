from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.code_option import CodeOption
from ...models.error import Error
from ...models.kcl_model import KclModel
from ...types import Response


def _get_kwargs(
    code_option: CodeOption,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ml/convert/proprietary-to-kcl".format(
        client.base_url,
    )  # noqa: E501

    if code_option is not None:
        if "?" in url:
            url = url + "&code_option=" + str(code_option)
        else:
            url = url + "?code_option=" + str(code_option)

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
    code_option: CodeOption,
    *,
    client: Client,
) -> Response[Optional[Union[KclModel, Error]]]:
    kwargs = _get_kwargs(
        code_option=code_option,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    code_option: CodeOption,
    *,
    client: Client,
) -> Optional[Union[KclModel, Error]]:
    """This endpoint is used to convert a proprietary CAD format to KCL. The file passed MUST have feature tree data.

    A STEP file does not have feature tree data, so it will not work. A sldprt file does have feature tree data, so it will work.

    Input filepaths will be normalized and re-canonicalized to be under the current working directory -- so returned paths may differ from provided paths, and care must be taken when handling user provided paths."""  # noqa: E501

    return sync_detailed(
        code_option=code_option,
        client=client,
    ).parsed


async def asyncio_detailed(
    code_option: CodeOption,
    *,
    client: Client,
) -> Response[Optional[Union[KclModel, Error]]]:
    kwargs = _get_kwargs(
        code_option=code_option,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    code_option: CodeOption,
    *,
    client: Client,
) -> Optional[Union[KclModel, Error]]:
    """This endpoint is used to convert a proprietary CAD format to KCL. The file passed MUST have feature tree data.

    A STEP file does not have feature tree data, so it will not work. A sldprt file does have feature tree data, so it will work.

    Input filepaths will be normalized and re-canonicalized to be under the current working directory -- so returned paths may differ from provided paths, and care must be taken when handling user provided paths."""  # noqa: E501

    return (
        await asyncio_detailed(
            code_option=code_option,
            client=client,
        )
    ).parsed
