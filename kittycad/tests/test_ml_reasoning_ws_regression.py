import json
import os
from typing import cast

import pytest
from websockets.sync.client import ClientConnection as ClientConnectionSync

from kittycad import KittyCAD, WebSocketMlReasoningWs
from kittycad.models import FileExportFormat, TextToCadCreateBody
from kittycad.models.ml_copilot_server_message import (
    EndOfStream,
    Reasoning,
    SessionData,
)
from kittycad.models.reasoning_message import OptionText, ReasoningMessage


class FakeWS:
    def __init__(self, messages):
        self._messages = iter(messages)
        self.timeouts = []

    def recv(self, timeout=None):  # pragma: no cover - tiny helper
        self.timeouts.append(timeout)
        try:
            return next(self._messages)
        except StopIteration as exc:
            raise AssertionError("unexpected recv() after messages exhausted") from exc


def test_ml_reasoning_ws_recv_parses_reasoning_messages():
    reasoning_content = ":mag: Querying relevant KCL code examples..."

    fake_ws = FakeWS(
        [
            json.dumps({"session_data": {"api_call_id": "abc123"}}),
            json.dumps(
                {
                    "reasoning": {
                        "type": "text",
                        "content": reasoning_content,
                    }
                }
            ),
        ]
    )

    websocket = cast(
        WebSocketMlReasoningWs, WebSocketMlReasoningWs.__new__(WebSocketMlReasoningWs)
    )
    websocket.ws = cast(ClientConnectionSync, fake_ws)
    websocket._recv_timeout = 60

    session_message = websocket.recv()
    assert isinstance(session_message.root, SessionData)
    assert session_message.root.api_call_id == "abc123"
    assert fake_ws.timeouts[-1] == 60

    reasoning_message = websocket.recv()
    assert isinstance(reasoning_message.root, Reasoning)
    resolved_reasoning = reasoning_message.root.reasoning.root
    assert isinstance(resolved_reasoning, OptionText)
    assert resolved_reasoning.content == reasoning_content
    assert fake_ws.timeouts[-1] == 60


def test_ml_reasoning_ws_real_round_trip() -> None:
    token = os.getenv("KITTYCAD_API_TOKEN")
    if not token:
        pytest.skip("requires KITTYCAD_API_TOKEN")

    client = KittyCAD()
    client.headers["Cache-Control"] = "no-cache"

    prompt = "Create 8x8x8 cube"
    t2c = client.ml.create_text_to_cad(
        output_format=FileExportFormat.STEP,
        kcl=True,
        body=TextToCadCreateBody(
            prompt=prompt,
        ),
    )

    reasoning_chunks: list[ReasoningMessage] = []
    end_of_stream_received = False

    with client.ml.ml_reasoning_ws(id=t2c.id) as websocket:
        for _ in range(200):
            message = websocket.recv()
            root = message.root
            if isinstance(root, Reasoning):
                reasoning_chunks.append(root.reasoning)
            if isinstance(root, EndOfStream):
                end_of_stream_received = True
                break
        else:
            pytest.fail("ml_reasoning_ws did not emit EndOfStream within 200 messages")

    assert end_of_stream_received
    assert reasoning_chunks

    text_chunks = [
        chunk.root for chunk in reasoning_chunks if isinstance(chunk.root, OptionText)
    ]
    assert any(chunk.content.strip() for chunk in text_chunks)
