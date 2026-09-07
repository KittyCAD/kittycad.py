from unittest.mock import AsyncMock, Mock
from urllib.parse import parse_qs, urlsplit

import pytest

import kittycad


@pytest.mark.parametrize("geometry_only", [None, False, True])
def test_sync_geometry_intent(geometry_only):
    client = kittycad.KittyCAD(token="test-token")
    factory = Mock()
    client.modeling.modeling_commands_ws(
        geometry_only=geometry_only, webrtc=False, ws_factory=factory
    )
    query = parse_qs(urlsplit(factory.call_args.args[0]).query)
    assert query.get("geometry_only") == (
        None if geometry_only is None else [str(geometry_only).lower()]
    )
    assert query["webrtc"] == ["false"]
    for unused in ["post_effect", "video_res_width", "video_res_height"]:
        assert unused not in query


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "group,method,kwargs,path",
    [
        ("executor", "create_executor_term", {}, "/ws/executor/term"),
        ("ml", "ml_copilot_ws", {"pr": 42}, "/ws/ml/copilot"),
        ("ml", "ml_reasoning_ws", {"id": "test-id"}, "/ws/ml/reasoning/test-id"),
    ],
)
async def test_shared_async_wrapper_returns_connection(
    monkeypatch, group, method, kwargs, path
):
    factory = AsyncMock()
    monkeypatch.setattr(kittycad, "ws_connect_async", factory)
    client = kittycad.AsyncKittyCAD(token="test-token")
    result = await getattr(getattr(client, group), method)(**kwargs)
    factory.assert_awaited_once()
    assert result is factory.return_value
    assert urlsplit(factory.call_args.args[0]).path == path
    assert "additional_headers" in factory.call_args.kwargs
    if "pr" in kwargs:
        assert parse_qs(urlsplit(factory.call_args.args[0]).query)["pr"] == ["42"]


@pytest.mark.asyncio
@pytest.mark.parametrize("geometry_only", [None, False, True])
async def test_async_geometry_intent(monkeypatch, geometry_only):
    factory = AsyncMock()
    monkeypatch.setattr(kittycad, "ws_connect_async", factory)
    client = kittycad.AsyncKittyCAD(token="test-token")
    result = await client.modeling.modeling_commands_ws(
        geometry_only=geometry_only, webrtc=False
    )
    factory.assert_awaited_once()
    assert result is factory.return_value
    query = parse_qs(urlsplit(factory.call_args.args[0]).query)
    assert query.get("geometry_only") == (
        None if geometry_only is None else [str(geometry_only).lower()]
    )
    assert query["webrtc"] == ["false"]
    assert "additional_headers" in factory.call_args.kwargs
    assert "extra_headers" not in factory.call_args.kwargs
    for unused in ["post_effect", "video_res_width", "video_res_height"]:
        assert unused not in query
