import os
from typing import Dict, Optional, Union

import pytest

from .api.api_tokens import list_api_tokens_for_user
from .api.file import create_file_conversion, create_file_mass, create_file_volume
from .api.meta import ping
from .api.users import get_user_self, list_users_extended
from .client import ClientFromEnv
from .models import (
    ApiCallStatus,
    ApiTokenResultsPage,
    Base64Data,
    CreatedAtSortMode,
    Error,
    ExtendedUserResultsPage,
    FileConversion,
    FileExportFormat,
    FileImportFormat,
    FileMass,
    FileVolume,
    Pong,
    UnitDensity,
    UnitMass,
    UnitVolume,
    User,
)
from .types import Unset


def test_get_session():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: Union[User, Error, None] = get_user_self.sync(client=client)

    assert isinstance(session, User)

    print(f"Session: {session}")


@pytest.mark.asyncio
async def test_get_api_tokens_async():
    # Create our client.
    client = ClientFromEnv()

    # List API tokens.
    fc: Union[ApiTokenResultsPage, Error, None] = list_api_tokens_for_user.sync(
        client=client, sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING
    )

    assert isinstance(fc, ApiTokenResultsPage)

    print(f"fc: {fc}")


@pytest.mark.asyncio
async def test_get_session_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: Union[User, Error, None] = await get_user_self.asyncio(client=client)

    assert isinstance(session, User)

    print(f"Session: {session}")


def test_ping():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Union[Pong, Error, None] = ping.sync(client=client)

    assert isinstance(message, Pong)

    print(f"Message: {message}")


@pytest.mark.asyncio
async def test_ping_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Union[Pong, Error, None] = await ping.asyncio(client=client)

    assert isinstance(message, Pong)

    print(f"Message: {message}")


def test_file_convert_stl():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[Union[FileConversion, Error]] = create_file_conversion.sync(
        client=client,
        body=content,
        src_format=FileImportFormat.STL,
        output_format=FileExportFormat.OBJ,
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    assert fc.status == ApiCallStatus.COMPLETED

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)

    outputs: Dict[str, Base64Data] = fc.outputs
    # Make sure the bytes are not empty.
    for key, value in outputs.items():
        assert len(value.get_decoded()) > 0


@pytest.mark.asyncio
async def test_file_convert_stl_async():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[
        Union[FileConversion, Error]
    ] = await create_file_conversion.asyncio(
        client=client,
        body=content,
        src_format=FileImportFormat.STL,
        output_format=FileExportFormat.OBJ,
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    assert fc.status == ApiCallStatus.COMPLETED

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)

    outputs: Dict[str, Base64Data] = fc.outputs
    # Make sure the bytes are not empty.
    for key, value in outputs.items():
        assert len(value.get_decoded()) > 0


@pytest.mark.asyncio
async def test_file_convert_obj_async():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/ORIGINALVOXEL-3.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[
        Union[FileConversion, Error]
    ] = await create_file_conversion.asyncio(
        client=client,
        body=content,
        src_format=FileImportFormat.OBJ,
        output_format=FileExportFormat.STL,
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    assert fc.status == ApiCallStatus.COMPLETED

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)

    outputs: Dict[str, Base64Data] = fc.outputs
    # Make sure the bytes are not empty.
    for key, value in outputs.items():
        assert len(value.get_decoded()) > 0


def test_file_mass():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Union[FileMass, Error, None] = create_file_mass.sync(
        client=client,
        body=content,
        src_format=FileImportFormat.OBJ,
        material_density=1.0,
        material_density_unit=UnitDensity.KG_M3,
        output_unit=UnitMass.G,
    )

    assert isinstance(result, FileMass)

    fm: FileMass = result

    print(f"FileMass: {fm}")

    assert fm.id is not None
    assert fm.mass is not None

    assert fm.to_dict() is not None

    assert fm.status == ApiCallStatus.COMPLETED


def test_file_volume():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Union[FileVolume, Error, None] = create_file_volume.sync(
        client=client,
        body=content,
        src_format=FileImportFormat.OBJ,
        output_unit=UnitVolume.CM3,
    )

    assert isinstance(result, FileVolume)

    fv: FileVolume = result

    print(f"FileVolume: {fv}")

    assert fv.id is not None
    assert fv.volume is not None

    assert fv.to_dict() is not None

    assert fv.status == ApiCallStatus.COMPLETED


def test_list_users():
    # Create our client.
    client = ClientFromEnv()

    response: Union[ExtendedUserResultsPage, Error, None] = list_users_extended.sync(
        sort_by=CreatedAtSortMode.CREATED_AT_DESCENDING, client=client, limit=10
    )

    assert isinstance(response, ExtendedUserResultsPage)

    print(f"ExtendedUserResultsPage: {response}")
