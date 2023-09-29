from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.created_at_sort_mode import CreatedAtSortMode
from ...models.error import Error
from ...models.extended_user_results_page import ExtendedUserResultsPage
from ...types import Response


def _get_kwargs(
    
    
    
    
    
    
    sort_by: CreatedAtSortMode,
    
    
    *,
    client: Client,
    
    
    limit: Optional[int] = None,
    
    
    
    page_token: Optional[str] = None,
    
    
    
    
) -> Dict[str, Any]:
    url = "{}/users-extended".format(client.base_url, )  # noqa: E501
    
    
    if limit is not None:
        if "?" in url:
            url = url + "&limit=" + str(limit)
        else:
            url = url + "?limit=" + str(limit)
    
    
    
    if page_token is not None:
        if "?" in url:
            url = url + "&page_token=" + str(page_token)
        else:
            url = url + "?page_token=" + str(page_token)
    
    
    
    if sort_by is not None:
        if "?" in url:
            url = url + "&sort_by=" + str(sort_by)
        else:
            url = url + "?sort_by=" + str(sort_by)
    
    


    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExtendedUserResultsPage, Error]] :
	if response.status_code == 200:
		response_200 = ExtendedUserResultsPage.from_dict(response.json())
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
)  -> Response[Optional[Union[ExtendedUserResultsPage, Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    
    
    
    
    
    
    sort_by: CreatedAtSortMode,
    
    
    *,
    client: Client,
    
    
    limit: Optional[int] = None,
    
    
    
    page_token: Optional[str] = None,
    
    
    
    
)  -> Response[Optional[Union[ExtendedUserResultsPage, Error]]]:
    kwargs = _get_kwargs(
        
        limit=limit,
        
        page_token=page_token,
        
        sort_by=sort_by,
        
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    
    
    
    
    
    
    sort_by: CreatedAtSortMode,
    
    
    *,
    client: Client,
    
    
    limit: Optional[int] = None,
    
    
    
    page_token: Optional[str] = None,
    
    
    
    
)  -> Optional[Union[ExtendedUserResultsPage, Error]] :
    """This endpoint required authentication by a KittyCAD employee. The users are returned in order of creation, with the most recently created users first."""  # noqa: E501

    return sync_detailed(
        
        limit=limit,
        
        page_token=page_token,
        
        sort_by=sort_by,
        
        client=client,
    ).parsed


async def asyncio_detailed(
    
    
    
    
    
    
    sort_by: CreatedAtSortMode,
    
    
    *,
    client: Client,
    
    
    limit: Optional[int] = None,
    
    
    
    page_token: Optional[str] = None,
    
    
    
    
)  -> Response[Optional[Union[ExtendedUserResultsPage, Error]]]:
    kwargs = _get_kwargs(
        
        limit=limit,
        
        page_token=page_token,
        
        sort_by=sort_by,
        
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    
    
    
    
    
    
    sort_by: CreatedAtSortMode,
    
    
    *,
    client: Client,
    
    
    limit: Optional[int] = None,
    
    
    
    page_token: Optional[str] = None,
    
    
    
    
)  -> Optional[Union[ExtendedUserResultsPage, Error]] :
    """This endpoint required authentication by a KittyCAD employee. The users are returned in order of creation, with the most recently created users first."""  # noqa: E501

    return (
        await asyncio_detailed(
            
            limit=limit,
            
            page_token=page_token,
            
            sort_by=sort_by,
            
            client=client,
        )
    ).parsed
