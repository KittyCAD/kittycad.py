from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.code_language import CodeLanguage
from ...models.code_output import CodeOutput
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    lang: CodeLanguage,
    body: bytes,
    *,
    client: Client,
    output: Optional[str] = None,
) -> Dict[str, Any]:
    url = "{}/file/execute/{lang}".format(
        client.base_url,
        lang=lang,
    )  # noqa: E501

    if output is not None:

        if "?" in url:
            url = url + "&output=" + str(output)
        else:
            url = url + "?output=" + str(output)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CodeOutput, Error]]:
    if response.status_code == 201:
        response_201 = CodeOutput(**response.json())
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
) -> Response[Optional[Union[CodeOutput, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    lang: CodeLanguage,
    body: bytes,
    *,
    client: Client,
    output: Optional[str] = None,
) -> Response[Optional[Union[CodeOutput, Error]]]:
    kwargs = _get_kwargs(
        lang=lang,
        output=output,
        body=body,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    lang: CodeLanguage,
    body: bytes,
    *,
    client: Client,
    output: Optional[str] = None,
) -> Optional[Union[CodeOutput, Error]]:

    return sync_detailed(
        lang=lang,
        output=output,
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    lang: CodeLanguage,
    body: bytes,
    *,
    client: Client,
    output: Optional[str] = None,
) -> Response[Optional[Union[CodeOutput, Error]]]:
    kwargs = _get_kwargs(
        lang=lang,
        output=output,
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    lang: CodeLanguage,
    body: bytes,
    *,
    client: Client,
    output: Optional[str] = None,
) -> Optional[Union[CodeOutput, Error]]:

    return (
        await asyncio_detailed(
            lang=lang,
            output=output,
            body=body,
            client=client,
        )
    ).parsed
