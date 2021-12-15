import pytest
import asyncio

from .client import AuthenticatedClientFromEnv
from .models import FileConversion, ValidFileTypes, AuthSession, InstanceMetadata, Message
from .api.file import file_convert_with_base64_helper
from .api.meta import meta_debug_session, meta_debug_instance, ping

def test_get_session():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the session.
    session: AuthSession = meta_debug_session.sync(client=client)

    assert session != None

    print(f"Session: {session}")

@pytest.mark.asyncio
async def test_get_session_async():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the session.
    session: AuthSession = await meta_debug_session.asyncio(client=client)

    assert session != None

    print(f"Session: {session}")

def test_get_instance():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the instance.
    instance: InstanceMetadata = meta_debug_instance.sync(client=client)

    assert instance != None

    print(f"Instance: {instance}")

@pytest.mark.asyncio
async def test_get_instance_async():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the instance.
    instance: InstanceMetadata = await meta_debug_instance.asyncio(client=client)

    assert instance != None

    print(f"Instance: {instance}")

def test_ping():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the message.
    message: Message = ping.sync(client=client)

    assert message != None

    print(f"Message: {message}")

@pytest.mark.asyncio
async def test_ping_async():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the message.
    message: Message = await ping.asyncio(client=client)

    assert message != None

    print(f"Message: {message}")
