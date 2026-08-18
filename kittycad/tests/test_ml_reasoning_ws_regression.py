import json
from typing import cast

from websockets.sync.client import ClientConnection as ClientConnectionSync

from kittycad import WebSocketMlReasoningWs
from kittycad.models.ml_copilot_server_message import Reasoning, SessionData
from kittycad.models.reasoning_message import OptionText


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
