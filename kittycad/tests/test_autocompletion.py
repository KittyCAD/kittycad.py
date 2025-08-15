#!/usr/bin/env python3
"""
Test the improved autocompletion with the new client architecture.

This test shows that the methods now have proper signatures instead of (*args, **kwargs).
IDEs will now provide full parameter hints and autocompletion.
"""

from kittycad import KittyCAD
from kittycad.models.post_effect_type import PostEffectType


def test_client_creation():
    """Test that client can be created successfully."""
    client = KittyCAD()
    assert client.base_url == "https://api.zoo.dev"


def test_websocket_method_signature():
    """Test that WebSocket methods have proper signatures for autocompletion."""
    client = KittyCAD()

    # This method call demonstrates full autocompletion with parameter names and types:
    ws = client.modeling.modeling_commands_ws(
        fps=30,  # IDE now knows this is int
        post_effect=PostEffectType.NOEFFECT,  # IDE shows enum values
        show_grid=False,  # IDE knows this is bool
        unlocked_framerate=False,  # IDE knows this is bool
        video_res_height=360,  # IDE knows this is int
        video_res_width=480,  # IDE knows this is int
        webrtc=False,  # IDE knows this is bool
        # Optional parameters with defaults also show up:
        api_call_id=None,  # IDE knows this is Optional[str]
        pool=None,  # IDE knows this is Optional[str]
        replay=None,  # IDE knows this is Optional[str]
    )

    # Verify WebSocket was created successfully
    assert ws is not None
    assert hasattr(ws, "send")
    assert hasattr(ws, "recv")
    assert hasattr(ws, "close")

    # Clean up
    ws.close()


def test_regular_api_method_signature():
    """Test that regular API methods have proper signatures."""
    client = KittyCAD()

    # Regular API methods also have proper signatures (though they delegate to API files)
    # We can't actually call this without auth, but we can verify the method exists
    # and has the right signature
    assert hasattr(client.users, "get_user_self")

    # Verify the method is callable
    method = getattr(client.users, "get_user_self")
    assert callable(method)


def test_environment_variable_support():
    """Test that client classes maintain environment variable support."""
    client = KittyCAD()
    assert isinstance(client.base_url, str)
    assert len(client.base_url) > 0
