from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.update_user import UpdateUser
from ...models.user import User
from ...types import Response


def _get_kwargs(
    
    
    body: UpdateUser,
    
    
    *,
    client: Client,
    
    
    
) -> Dict[str, Any]:
    url = "{}/user".format(client.base_url, )  # noqa: E501
    
    
    


    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[User, Error]] :
	if response.status_code == 200:
		response_200 = User.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return Error.from_dict(response.json())



def _build_response(
    *, response: httpx.Response
)  -> Response[Optional[Union[User, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    
    
    body: UpdateUser,
    
    
    *,
    client: Client,
    
    
    
)  -> Response[Optional[Union[User, Error]]]:
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
    
    
    body: UpdateUser,
    
    
    *,
    client: Client,
    
    
    
)  -> Optional[Union[User, Error]] :
    """This endpoint requires authentication by any KittyCAD user. It updates information about the authenticated user."""  # noqa: E501

    return sync_detailed(
        
        body=body,
        
        client=client,
    ).parsed


async def asyncio_detailed(
    
    
    body: UpdateUser,
    
    
    *,
    client: Client,
    
    
    
)  -> Response[Optional[Union[User, Error]]]:
    kwargs = _get_kwargs(
        
        body=body,
        
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    
    
    body: UpdateUser,
    
    
    *,
    client: Client,
    
    
    
)  -> Optional[Union[User, Error]] :
    """This endpoint requires authentication by any KittyCAD user. It updates information about the authenticated user."""  # noqa: E501

    return (
        await asyncio_detailed(
            
            body=body,
            
            client=client,
        )
    ).parsed
