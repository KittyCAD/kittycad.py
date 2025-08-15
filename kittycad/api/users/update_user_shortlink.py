from typing import Any, Dict

import httpx

from ...client import Client
from ...models.update_shortlink_request import UpdateShortlinkRequest
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    key: str,
    body: UpdateShortlinkRequest,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/user/shortlinks/{key}".format(
        client.base_url,
        key=key,
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


def _parse_response(*, response: httpx.Response) -> None:
    return None
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[None]:
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
    key: str,
    body: UpdateShortlinkRequest,
    *,
    client: Client,
) -> Response[None]:
    kwargs = _get_kwargs(
        key=key,
        body=body,
        client=client,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    body: UpdateShortlinkRequest,
    *,
    client: Client,
) -> None:
    """This endpoint requires authentication by any Zoo user. It updates a shortlink for the user.

    This endpoint really only allows you to change the `restrict_to_org` setting of a shortlink. Thus it is only useful for folks who are part of an org. If you are not part of an org, you will not be able to change the `restrict_to_org` status."""  # noqa: E501

    return sync_detailed(
        key=key,
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    key: str,
    body: UpdateShortlinkRequest,
    *,
    client: Client,
) -> Response[None]:
    kwargs = _get_kwargs(
        key=key,
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    body: UpdateShortlinkRequest,
    *,
    client: Client,
) -> None:
    """This endpoint requires authentication by any Zoo user. It updates a shortlink for the user.

    This endpoint really only allows you to change the `restrict_to_org` setting of a shortlink. Thus it is only useful for folks who are part of an org. If you are not part of an org, you will not be able to change the `restrict_to_org` status."""  # noqa: E501

    return (
        await asyncio_detailed(
            key=key,
            body=body,
            client=client,
        )
    ).parsed
