from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.code_language import CodeLanguage
from ...models.code_output import CodeOutput
from ...response_helpers import raise_for_status
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


def _parse_response(*, response: httpx.Response) -> CodeOutput:
    if response.status_code == 201:
        response_201 = CodeOutput(**response.json())
        return response_201
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[CodeOutput]:
    # Check for errors first - this will raise exceptions for non-success status codes
    # before we try to parse the response
    if not response.is_success:
        raise_for_status(response)

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
) -> Response[CodeOutput]:
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
) -> CodeOutput:
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
) -> Response[CodeOutput]:
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
) -> CodeOutput:
    return (
        await asyncio_detailed(
            lang=lang,
            output=output,
            body=body,
            client=client,
        )
    ).parsed
