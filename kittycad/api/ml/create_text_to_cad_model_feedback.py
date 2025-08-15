from typing import Any, Dict

import httpx

from ...client import Client
from ...models.ml_feedback import MlFeedback
from ...response_helpers import raise_for_status
from ...types import Response


def _get_kwargs(
    id: str,
    feedback: MlFeedback,
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


def _parse_response(*, response: httpx.Response):
    if response.status_code == 204:
        return None
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Any]:
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
    id: str,
    feedback: MlFeedback,
    *,
    client: Client,
) -> Response[Any]:
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
    feedback: MlFeedback,
    *,
    client: Client,
):
    """This can be a text-to-CAD creation or iteration.

    This endpoint requires authentication by any Zoo user. The user must be the owner of the ML response, in order to give feedback."""  # noqa: E501

    return sync_detailed(
        id=id,
        feedback=feedback,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    feedback: MlFeedback,
    *,
    client: Client,
) -> Response[Any]:
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
    feedback: MlFeedback,
    *,
    client: Client,
):
    """This can be a text-to-CAD creation or iteration.

    This endpoint requires authentication by any Zoo user. The user must be the owner of the ML response, in order to give feedback."""  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            feedback=feedback,
            client=client,
        )
    ).parsed
