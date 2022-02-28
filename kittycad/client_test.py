import os
import pytest
import asyncio

from .client import AuthenticatedClientFromEnv
from .models import FileConversion, ValidOutputFileFormat, ValidSourceFileFormat, AuthSession, InstanceMetadata, Message
from .api.file import post_file_conversion_with_base64_helper
from .api.meta import auth_session, instance_metadata, ping


def test_get_session():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: AuthSession = auth_session.sync(client=client)

    assert session is not None

    print(f"Session: {session}")


@pytest.mark.asyncio
async def test_get_session_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: AuthSession = await auth_session.asyncio(client=client)

    assert session is not None

    print(f"Session: {session}")


def test_get_instance():
    # Create our client.
    client = ClientFromEnv()

    # Get the instance.
    instance: InstanceMetadata = instance_metadata.sync(client=client)

    assert instance is not None

    print(f"Instance: {instance}")


@pytest.mark.asyncio
async def test_get_instance_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the instance.
    instance: InstanceMetadata = await instance_metadata.asyncio(client=client)

    assert instance is not None

    print(f"Instance: {instance}")


def test_ping():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Message = ping.sync(client=client)

    assert message is not None

    print(f"Message: {message}")


@pytest.mark.asyncio
async def test_ping_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Message = await ping.asyncio(client=client)

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
    fc: FileConversion = post_file_convertsion_with_base64_helper.sync(
        client=client,
        content=content,
        source_format=ValidSourceFileFormat.STL,
        output_format=ValidOutputFileFormat.OBJ)

    assert fc is not None

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
    fc: FileConversion = await post_file_convertsion_with_base64_helper.asyncio(client=client, content=content, source_format=ValidSourceFileFormat.STL, output_format=ValidOutputFileFormat.OBJ)

    assert fc is not None

    print(f"FileConversion: {fc}")
