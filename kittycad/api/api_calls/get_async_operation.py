"""
This module should only be accessed through client.api.
Direct imports like 'from kittycad.api.module import function' are not supported.
Use: client = KittyCAD(); client.api.module.function() instead.
"""

from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.file_center_of_mass import FileCenterOfMass
from ...models.file_conversion import FileConversion
from ...models.file_density import FileDensity
from ...models.file_mass import FileMass
from ...models.file_surface_area import FileSurfaceArea
from ...models.file_volume import FileVolume
from ...models.text_to_cad import TextToCad
from ...models.text_to_cad_iteration import TextToCadIteration
from ...models.text_to_cad_multi_file_iteration import TextToCadMultiFileIteration
from ...response_helpers import raise_for_status
from ...types import Response

# Prevent direct imports - hide all public functions
__all__: list[str] = []


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


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[
        FileConversion,
        FileCenterOfMass,
        FileMass,
        FileVolume,
        FileDensity,
        FileSurfaceArea,
        TextToCad,
        TextToCadIteration,
        TextToCadMultiFileIteration,
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
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_text_to_cad_iteration = TextToCadIteration(**data)
            return option_text_to_cad_iteration
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_text_to_cad_multi_file_iteration = TextToCadMultiFileIteration(
                **data
            )
            return option_text_to_cad_multi_file_iteration
        except ValueError:
            raise
        except TypeError:
            raise
    # This should not be reached since we handle all known success responses above
    # and errors are handled by raise_for_status
    raise ValueError(f"Unexpected response status: {response.status_code}")


def _build_response(
    *, response: httpx.Response
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
            TextToCadIteration,
            TextToCadMultiFileIteration,
        ]
    ]
]:
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
        TextToCadIteration,
        TextToCadMultiFileIteration,
    ]
]:
    """Get the status and output of an async operation.

    This endpoint requires authentication by any Zoo user. It returns details of the requested async operation for the user.

    If the user is not authenticated to view the specified async operation, then it is not returned.

    Only Zoo employees with the proper access can view async operations for other users."""  # noqa: E501

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response).parsed


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
        TextToCadIteration,
        TextToCadMultiFileIteration,
    ]
]:
    """Get the status and output of an async operation.

    This endpoint requires authentication by any Zoo user. It returns details of the requested async operation for the user.

    If the user is not authenticated to view the specified async operation, then it is not returned.

    Only Zoo employees with the proper access can view async operations for other users."""  # noqa: E501

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response).parsed
