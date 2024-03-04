from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.email_authentication_form import EmailAuthenticationForm
from ...models.error import Error
from ...models.verification_token_response import VerificationTokenResponse
from ...types import Response


def _get_kwargs(
    body: EmailAuthenticationForm,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/auth/email".format(
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
) -> Optional[Union[VerificationTokenResponse, Error]]:
    if response.status_code == 201:
        response_201 = VerificationTokenResponse(**response.json())
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
) -> Response[Optional[Union[VerificationTokenResponse, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: EmailAuthenticationForm,
    *,
    client: Client,
) -> Response[Optional[Union[VerificationTokenResponse, Error]]]:
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
    body: EmailAuthenticationForm,
    *,
    client: Client,
) -> Optional[Union[VerificationTokenResponse, Error]]:

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: EmailAuthenticationForm,
    *,
    client: Client,
) -> Response[Optional[Union[VerificationTokenResponse, Error]]]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: EmailAuthenticationForm,
    *,
    client: Client,
) -> Optional[Union[VerificationTokenResponse, Error]]:

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
