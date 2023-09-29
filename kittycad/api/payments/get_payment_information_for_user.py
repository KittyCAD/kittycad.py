from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.customer import Customer
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    
    *,
    client: Client,
    
) -> Dict[str, Any]:
    url = "{}/user/payment".format(client.base_url, )  # noqa: E501
    


    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Customer, Error]] :
	if response.status_code == 200:
		response_200 = Customer.from_dict(response.json())
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
)  -> Response[Optional[Union[Customer, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    
    *,
    client: Client,
    
)  -> Response[Optional[Union[Customer, Error]]]:
    kwargs = _get_kwargs(
        
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    
    *,
    client: Client,
    
)  -> Optional[Union[Customer, Error]] :
    """This includes billing address, phone, and name.
This endpoint requires authentication by any KittyCAD user. It gets the payment information for the authenticated user."""  # noqa: E501

    return sync_detailed(
        
        client=client,
    ).parsed


async def asyncio_detailed(
    
    *,
    client: Client,
    
)  -> Response[Optional[Union[Customer, Error]]]:
    kwargs = _get_kwargs(
        
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    
    *,
    client: Client,
    
)  -> Optional[Union[Customer, Error]] :
    """This includes billing address, phone, and name.
This endpoint requires authentication by any KittyCAD user. It gets the payment information for the authenticated user."""  # noqa: E501

    return (
        await asyncio_detailed(
            
            client=client,
        )
    ).parsed
