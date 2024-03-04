from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.file_center_of_mass import FileCenterOfMass
from ...models.file_conversion import FileConversion
from ...models.file_density import FileDensity
from ...models.file_mass import FileMass
from ...models.file_surface_area import FileSurfaceArea
from ...models.file_volume import FileVolume
from ...models.text_to_cad import TextToCad
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/async/operations/{id}".format(
        client.base_url,
        id=id,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[
    Union[
        FileConversion,
        FileCenterOfMass,
        FileMass,
        FileVolume,
        FileDensity,
        FileSurfaceArea,
        TextToCad,
        Error,
    ]
]:
    if response.status_code == 200:
        data = response.json()
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_file_conversion = FileConversion(**data)
            return option_file_conversion
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_file_center_of_mass = FileCenterOfMass(**data)
            return option_file_center_of_mass
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_file_mass = FileMass(**data)
            return option_file_mass
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_file_volume = FileVolume(**data)
            return option_file_volume
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_file_density = FileDensity(**data)
            return option_file_density
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_file_surface_area = FileSurfaceArea(**data)
            return option_file_surface_area
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_text_to_cad = TextToCad(**data)
            return option_text_to_cad
        except ValueError:
            raise
        except TypeError:
            raise
    if response.status_code == 400:
        response_4XX = Error(**response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error(**response.json())
        return response_5XX
    return Error(**response.json())


def _build_response(*, response: httpx.Response) -> Response[
    Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            Error,
        ]
    ]
]:
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
) -> Response[
    Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            Error,
        ]
    ]
]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[
    Union[
        FileConversion,
        FileCenterOfMass,
        FileMass,
        FileVolume,
        FileDensity,
        FileSurfaceArea,
        TextToCad,
        Error,
    ]
]:
    """Get the status and output of an async operation.
    This endpoint requires authentication by any Zoo user. It returns details of the requested async operation for the user.
    If the user is not authenticated to view the specified async operation, then it is not returned.
    Only Zoo employees with the proper access can view async operations for other users.
    """  # noqa: E501

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[
    Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            Error,
        ]
    ]
]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[
    Union[
        FileConversion,
        FileCenterOfMass,
        FileMass,
        FileVolume,
        FileDensity,
        FileSurfaceArea,
        TextToCad,
        Error,
    ]
]:
    """Get the status and output of an async operation.
    This endpoint requires authentication by any Zoo user. It returns details of the requested async operation for the user.
    If the user is not authenticated to view the specified async operation, then it is not returned.
    Only Zoo employees with the proper access can view async operations for other users.
    """  # noqa: E501

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
