from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    
    
    id: str,
    
    
    *,
    client: Client,
    
    
    
) -> Dict[str, Any]:
    url = "{}/user/payment/methods/{id}".format(client.base_url, id=id,)  # noqa: E501
    
    
    


    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error] :
	return None
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return Error.from_dict(response.json())



def _build_response(
    *, response: httpx.Response
)  -> Response[Optional[Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    
    
    id: str,
    
    
    *,
    client: Client,
    
    
    
)  -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        
        id=id,
        
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    
    
    id: str,
    
    
    *,
    client: Client,
    
    
    
)  -> Optional[Error] :
    """This endpoint requires authentication by any KittyCAD user. It deletes the specified payment method for the authenticated user."""  # noqa: E501

    return sync_detailed(
        
        id=id,
        
        client=client,
    ).parsed


async def asyncio_detailed(
    
    
    id: str,
    
    
    *,
    client: Client,
    
    
    
)  -> Response[Optional[Error]]:
    kwargs = _get_kwargs(
        
        id=id,
        
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    
    
    id: str,
    
    
    *,
    client: Client,
    
    
    
)  -> Optional[Error] :
    """This endpoint requires authentication by any KittyCAD user. It deletes the specified payment method for the authenticated user."""  # noqa: E501

    return (
        await asyncio_detailed(
            
            id=id,
            
            client=client,
        )
    ).parsed
