import os

import pytest

from kittycad import KittyCAD
from kittycad.models import MlCopilotClientMessage
from kittycad.models.ml_copilot_client_message import OptionUser
from kittycad.models.ml_copilot_server_message import (
    ConversationId,
    Delta,
    EndOfStream,
    Error,
)


def test_ml_copilot_ws_round_trip() -> None:
    token = os.getenv("KITTYCAD_API_TOKEN")
    if not token:
        pytest.skip("requires KITTYCAD_API_TOKEN")

    client = KittyCAD()
    client.headers["Cache-Control"] = "no-cache"

    prompt = "Explain why reliable CAD tooling matters in one sentence."

    with client.ml.ml_copilot_ws(conversation_id=None, replay=None) as websocket:
        websocket.send(MlCopilotClientMessage(OptionUser(content=prompt)))

        deltas: list[str] = []
        conversation_id: str | None = None
        end_of_stream = False

        for _ in range(200):
            message = websocket.recv()
            root = message.root

            if isinstance(root, ConversationId):
                conversation_id = root.conversation_id
            elif isinstance(root, Delta):
                deltas.append(root.delta)
            elif isinstance(root, EndOfStream):
                end_of_stream = True
                break
            elif isinstance(root, Error):
                pytest.fail(f"ml_copilot_ws returned error: {root.detail}")
        else:
            pytest.fail("ml_copilot_ws did not emit EndOfStream within 200 messages")

    response_text = "".join(deltas).strip()

    assert conversation_id, "Expected ConversationId message from ml_copilot_ws"
    assert end_of_stream, "Expected EndOfStream message from ml_copilot_ws"
    assert response_text, "Expected non-empty streamed response from ml_copilot_ws"
