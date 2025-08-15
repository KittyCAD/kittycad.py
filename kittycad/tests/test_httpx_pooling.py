"""Tests for httpx client pooling functionality."""

import httpx
import pytest

from kittycad import AsyncKittyCAD, KittyCAD
from kittycad.client import AsyncClient, Client


def test_sync_client_pooling():
    """Test that sync client uses persistent httpx.Client for connection pooling."""
    client = Client(token="test_token_123")

    # Get the http client multiple times and verify it's the same instance
    http_client1 = client.get_http_client()
    http_client2 = client.get_http_client()

    assert http_client1 is http_client2, "Should reuse same httpx.Client instance"
    assert isinstance(http_client1, httpx.Client), "Should return httpx.Client instance"

    # Verify the client has expected configuration
    assert http_client1.timeout.read == 120.0, "Should use client timeout setting"

    client.close()


def test_sync_client_context_manager():
    """Test that sync client supports context manager for proper cleanup."""
    client = Client(token="test_token_123")

    # Get initial http client
    http_client1 = client.get_http_client()

    # Test context manager
    with client as ctx_client:
        assert ctx_client is client, "Context manager should return same client"
        # Client should still work inside context
        http_client_ctx = ctx_client.get_http_client()
        assert http_client_ctx is http_client1, "Should reuse same client in context"

    # After context manager exit, client should be closed but still usable
    # Get a new client - it should be a different instance since old one was closed
    http_client2 = client.get_http_client()
    assert http_client2 is not http_client1, "Should create new client after close"


def test_sync_client_manual_close():
    """Test that sync client close() method works correctly."""
    client = Client(token="test_token_123")

    # Get initial http client
    http_client1 = client.get_http_client()
    assert isinstance(http_client1, httpx.Client)

    # Close the client
    client.close()

    # Get new http client - should be different instance
    http_client2 = client.get_http_client()
    assert http_client2 is not http_client1, (
        "Should create new client after manual close"
    )


@pytest.mark.asyncio
async def test_async_client_pooling():
    """Test that async client uses persistent httpx.AsyncClient for connection pooling."""
    client = AsyncClient(token="test_token_123")

    # Get the http client multiple times and verify it's the same instance
    http_client1 = client.get_http_client()
    http_client2 = client.get_http_client()

    assert http_client1 is http_client2, "Should reuse same httpx.AsyncClient instance"
    assert isinstance(http_client1, httpx.AsyncClient), (
        "Should return httpx.AsyncClient instance"
    )

    # Verify the client has expected configuration
    assert http_client1.timeout.read == 120.0, "Should use client timeout setting"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_client_context_manager():
    """Test that async client supports async context manager for proper cleanup."""
    client = AsyncClient(token="test_token_123")

    # Get initial http client
    http_client1 = client.get_http_client()

    # Test async context manager
    async with client as ctx_client:
        assert ctx_client is client, "Context manager should return same client"
        # Client should still work inside context
        http_client_ctx = ctx_client.get_http_client()
        assert http_client_ctx is http_client1, "Should reuse same client in context"

    # After context manager exit, client should be closed but still usable
    # Get a new client - it should be a different instance since old one was closed
    http_client2 = client.get_http_client()
    assert http_client2 is not http_client1, "Should create new client after aclose"


@pytest.mark.asyncio
async def test_async_client_manual_close():
    """Test that async client aclose() method works correctly."""
    client = AsyncClient(token="test_token_123")

    # Get initial http client
    http_client1 = client.get_http_client()
    assert isinstance(http_client1, httpx.AsyncClient)

    # Close the client
    await client.aclose()

    # Get new http client - should be different instance
    http_client2 = client.get_http_client()
    assert http_client2 is not http_client1, (
        "Should create new client after manual aclose"
    )


def test_sync_client_custom_settings():
    """Test that sync client respects custom timeout and SSL settings."""
    client = Client(token="test_token_123", timeout=60.0, verify_ssl=False)

    http_client = client.get_http_client()

    assert http_client.timeout.read == 60.0, "Should use custom timeout setting"

    client.close()


@pytest.mark.asyncio
async def test_async_client_custom_settings():
    """Test that async client respects custom timeout and SSL settings."""
    client = AsyncClient(token="test_token_123", timeout=60.0, verify_ssl=False)

    http_client = client.get_http_client()

    assert http_client.timeout.read == 60.0, "Should use custom timeout setting"

    await client.aclose()


def test_main_kittycad_client_inheritance():
    """Test that KittyCAD class properly inherits from Client."""
    # This test doesn't require actual API calls, just verifies the structure
    try:
        client = KittyCAD(token="test_token")

        # Should inherit Client methods
        assert hasattr(client, "get_http_client"), "Should have get_http_client method"
        assert hasattr(client, "close"), "Should have close method"
        assert hasattr(client, "__enter__"), "Should have context manager entry"
        assert hasattr(client, "__exit__"), "Should have context manager exit"

        # Should be able to get httpx client
        http_client = client.get_http_client()
        assert isinstance(http_client, httpx.Client), "Should return httpx.Client"

        client.close()

    except Exception as e:
        pytest.fail(f"KittyCAD client creation failed: {e}")


@pytest.mark.asyncio
async def test_main_async_kittycad_client_inheritance():
    """Test that AsyncKittyCAD class properly inherits from AsyncClient."""
    # This test doesn't require actual API calls, just verifies the structure
    try:
        client = AsyncKittyCAD(token="test_token")

        # Should inherit AsyncClient methods
        assert hasattr(client, "get_http_client"), "Should have get_http_client method"
        assert hasattr(client, "aclose"), "Should have aclose method"
        assert hasattr(client, "__aenter__"), "Should have async context manager entry"
        assert hasattr(client, "__aexit__"), "Should have async context manager exit"

        # Should be able to get httpx async client
        http_client = client.get_http_client()
        assert isinstance(http_client, httpx.AsyncClient), (
            "Should return httpx.AsyncClient"
        )

        await client.aclose()

    except Exception as e:
        pytest.fail(f"AsyncKittyCAD client creation failed: {e}")


def test_sync_client_custom_httpx_injection():
    """Test that sync client supports custom httpx.Client injection."""
    custom_httpx_client = httpx.Client(timeout=30.0)

    # Inject custom httpx client
    client = Client(token="test_token", http_client=custom_httpx_client)

    # Should use the injected client
    http_client = client.get_http_client()
    assert http_client is custom_httpx_client, "Should use injected httpx.Client"
    assert http_client.timeout.read == 30.0, "Should preserve custom client settings"

    # Cleanup
    client.close()


@pytest.mark.asyncio
async def test_async_client_custom_httpx_injection():
    """Test that async client supports custom httpx.AsyncClient injection."""
    custom_httpx_client = httpx.AsyncClient(timeout=30.0)

    # Inject custom httpx client
    client = AsyncClient(token="test_token", http_client=custom_httpx_client)

    # Should use the injected client
    http_client = client.get_http_client()
    assert http_client is custom_httpx_client, "Should use injected httpx.AsyncClient"
    assert http_client.timeout.read == 30.0, "Should preserve custom client settings"

    # Cleanup
    await client.aclose()
    await custom_httpx_client.aclose()


def test_sync_client_headers_and_cookies():
    """Test that sync client properly configures headers and cookies."""
    client = Client(
        token="test_token",
        headers={"Custom-Header": "value"},
        cookies={"session": "abc123"},
    )

    # Verify headers
    headers = client.get_headers()
    assert "Authorization" in headers, "Should have Authorization header"
    assert headers["Authorization"] == "Bearer test_token", (
        "Should have correct auth header"
    )
    assert headers["Custom-Header"] == "value", "Should include custom headers"

    # Verify cookies
    cookies = client.get_cookies()
    assert cookies["session"] == "abc123", "Should include custom cookies"

    # Verify httpx client gets cookies
    http_client = client.get_http_client()
    assert http_client.cookies.get("session") == "abc123", (
        "httpx client should have cookies"
    )

    client.close()


@pytest.mark.asyncio
async def test_async_client_headers_and_cookies():
    """Test that async client properly configures headers and cookies."""
    client = AsyncClient(
        token="test_token",
        headers={"Custom-Header": "value"},
        cookies={"session": "abc123"},
    )

    # Verify headers
    headers = client.get_headers()
    assert "Authorization" in headers, "Should have Authorization header"
    assert headers["Authorization"] == "Bearer test_token", (
        "Should have correct auth header"
    )
    assert headers["Custom-Header"] == "value", "Should include custom headers"

    # Verify cookies
    cookies = client.get_cookies()
    assert cookies["session"] == "abc123", "Should include custom cookies"

    # Verify httpx client gets cookies
    http_client = client.get_http_client()
    assert http_client.cookies.get("session") == "abc123", (
        "httpx client should have cookies"
    )

    await client.aclose()


def test_sync_client_evolution_creates_separate_clients():
    """Test that client evolution methods work correctly."""
    client = Client(token="test_token")

    # Evolve client with new headers
    new_client = client.with_headers({"X-New-Header": "test"})

    # New client should be different instance
    assert new_client is not client, "Evolution should create new client instance"

    # Test that the new client has the updated headers
    assert new_client.headers["X-New-Header"] == "test", (
        "New client should have new headers"
    )
    assert "X-New-Header" not in client.headers, (
        "Original client should not have new headers"
    )

    # Note: attrs.evolve may share some references, which is expected behavior
    # Each client can independently manage its http client lifecycle

    # Cleanup both clients
    client.close()
    new_client.close()


@pytest.mark.asyncio
async def test_async_client_evolution_creates_separate_clients():
    """Test that async client evolution methods work correctly."""
    client = AsyncClient(token="test_token")

    # Evolve client with new headers
    new_client = client.with_headers({"X-New-Header": "test"})

    # New client should be different instance
    assert new_client is not client, "Evolution should create new client instance"

    # Test that the new client has the updated headers
    assert new_client.headers["X-New-Header"] == "test", (
        "New client should have new headers"
    )
    assert "X-New-Header" not in client.headers, (
        "Original client should not have new headers"
    )

    # Note: attrs.evolve may share some references, which is expected behavior
    # Each client can independently manage its http client lifecycle

    # Cleanup both clients
    await client.aclose()
    await new_client.aclose()
