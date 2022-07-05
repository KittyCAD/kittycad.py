import os
import pytest
import asyncio

from .client import ClientFromEnv
from .models import FileConversion, FileOutputFormat, FileSourceFormat, User, Pong, ApiCallStatus, FileMass, FileVolume
from .api.file import create_file_conversion_with_base64_helper, create_file_mass, create_file_volume
from .api.meta import ping
from .api.users import get_user_self


def test_get_session():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: User = get_user_self.sync(client=client)

    assert session is not None

    print(f"Session: {session}")


@pytest.mark.asyncio
async def test_get_session_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: User = await get_user_self.asyncio(client=client)

    assert session is not None

    print(f"Session: {session}")


def test_ping():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Pong = ping.sync(client=client)

    assert message is not None

    print(f"Message: {message}")


@pytest.mark.asyncio
async def test_ping_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Pong = await ping.asyncio(client=client)

    assert message is not None

    print(f"Message: {message}")


def test_file_convert_stl():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    fc: FileConversion = create_file_conversion_with_base64_helper.sync(
        client=client,
        body=content,
        src_format=FileSourceFormat.STL,
        output_format=FileOutputFormat.OBJ)

    assert fc is not None

    print(f"FileConversion: {fc}")

    assert fc.id is not None

    assert fc.status == ApiCallStatus.COMPLETED

    print(f"FileConversion: {fc}")


@pytest.mark.asyncio
async def test_file_convert_stl_async():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    fc: FileConversion = await create_file_conversion_with_base64_helper.asyncio(client=client, body=content, src_format=FileSourceFormat.STL, output_format=FileOutputFormat.OBJ)

    assert fc is not None

    print(f"FileConversion: {fc}")

    assert fc.id is not None

    print(f"FileConversion: {fc}")


def test_file_mass():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    fm: FileMass = create_file_mass.sync(
        client=client,
        body=content,
        src_format=FileSourceFormat.OBJ,
        material_density=1.0)

    assert fm is not None

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
    fv: FileVolume = create_file_volume.sync(
        client=client,
        body=content,
        src_format=FileSourceFormat.OBJ)

    assert fv is not None

    print(f"FileVolume: {fv}")

    assert fv.id is not None
    assert fv.volume is not None

    assert fv.to_dict() is not None

    assert fv.status == ApiCallStatus.COMPLETED
