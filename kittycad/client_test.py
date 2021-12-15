import pytest
import asyncio

from .client import AuthenticatedClientFromEnv
from .models import FileConversion, ValidFileTypes, AuthSession, InstanceMetadata
from .api.file import file_convert_with_base64_helper
from .api.meta import meta_debug_session, meta_debug_instance

def test_get_session():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the session.
    session: AuthSession = meta_debug_session.sync(client=client)

    print(f"Session: {session}")

@pytest.mark.asyncio
async def test_get_session_async():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the session.
    session: AuthSession = meta_debug_session.asyncio(client=client)

    print(f"Session: {session}")

def test_get_instance():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the instance.
    instance: InstanceMetadata = meta_debug_instance.sync(client=client)
    print(f"Instance: {instance}")

@pytest.mark.asyncio
async def test_get_instance_async():
    # Create our client.
    client = AuthenticatedClientFromEnv()

    # Get the instance.
    instance: InstanceMetadata = await meta_debug_instance.asyncio(client=client)
    print(f"Instance: {instance}")
