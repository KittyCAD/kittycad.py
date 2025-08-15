"""Tests for global client functionality."""

import os
from unittest.mock import patch

import pytest

from kittycad import configure, get_default_client, set_default_client
from kittycad.client import Client, ClientFromEnv


class TestGlobalClientConfiguration:
    """Test global client configuration functionality."""

    def setup_method(self):
        """Clear any existing default client before each test."""
        import kittycad

        kittycad._default_client = None

    def test_configure_with_explicit_token(self):
        """Test configuring with explicit API token."""
        configure(api_token="test-token-123")
        client = get_default_client()

        assert client.token == "test-token-123"
        assert client.base_url == "https://api.zoo.dev"
        assert client.timeout == 120.0

    def test_configure_with_all_params(self):
        """Test configuring with all parameters."""
        configure(
            api_token="test-token-456",
            base_url="https://custom.url",
            timeout=60.0,
            headers={"X-Custom": "header"},
            cookies={"session": "abc123"},
            verify_ssl=False,
        )
        client = get_default_client()

        assert client.token == "test-token-456"
        assert client.base_url == "https://custom.url"
        assert client.timeout == 60.0
        assert client.headers == {"X-Custom": "header"}
        assert client.cookies == {"session": "abc123"}
        assert client.verify_ssl is False

    @patch.dict(os.environ, {"KITTYCAD_API_TOKEN": "env-token-123"}, clear=True)
    def test_configure_from_kittycad_env(self):
        """Test configuring from KITTYCAD_API_TOKEN environment variable."""
        configure()  # No explicit token
        client = get_default_client()

        assert client.token == "env-token-123"

    @patch.dict(os.environ, {"ZOO_API_TOKEN": "zoo-token-456"}, clear=True)
    def test_configure_from_zoo_env(self):
        """Test configuring from ZOO_API_TOKEN environment variable."""
        configure()  # No explicit token
        client = get_default_client()

        assert client.token == "zoo-token-456"

    @patch.dict(os.environ, {}, clear=True)
    def test_configure_no_token_raises_error(self):
        """Test that configure raises error when no token is available."""
        with pytest.raises(ValueError, match="No API token provided"):
            configure()

    def test_set_default_client_directly(self):
        """Test setting default client directly."""
        custom_client = Client(token="direct-token")
        set_default_client(custom_client)

        client = get_default_client()
        assert client is custom_client
        assert client.token == "direct-token"

    @patch.dict(os.environ, {"KITTYCAD_API_TOKEN": "fallback-token"})
    def test_get_default_client_auto_fallback(self):
        """Test that get_default_client falls back to ClientFromEnv when no config."""
        # Clear any existing default client
        import kittycad

        kittycad._default_client = None

        client = get_default_client()
        assert isinstance(client, ClientFromEnv)
        assert client.token == "fallback-token"

    @patch.dict(os.environ, {}, clear=True)
    def test_get_default_client_no_fallback_raises_error(self):
        """Test that get_default_client raises error when no fallback available."""
        # Clear any existing default client
        import kittycad

        kittycad._default_client = None

        with pytest.raises(ValueError, match="No default client configured"):
            get_default_client()

    def test_multiple_configure_calls_replace_client(self):
        """Test that multiple configure calls replace the previous client."""
        configure(api_token="first-token")
        first_client = get_default_client()
        assert first_client.token == "first-token"

        configure(api_token="second-token")
        second_client = get_default_client()
        assert second_client.token == "second-token"
        assert second_client is not first_client
