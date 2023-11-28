from typing import Any, Dict, Union

from typing_extensions import Self

from .failure_web_socket_response import FailureWebSocketResponse
from .success_web_socket_response import SuccessWebSocketResponse


class WebSocketResponse:

    """Websocket responses can either be successful or unsuccessful. Slightly different schemas in either case."""

    type: Union[
        SuccessWebSocketResponse,
        FailureWebSocketResponse,
    ] = None

    def __init__(
        self,
        type: Union[
            type(SuccessWebSocketResponse),
            type(FailureWebSocketResponse),
        ],
    ):
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, SuccessWebSocketResponse):
            n: SuccessWebSocketResponse = self.type
            return n.to_dict()
        elif isinstance(self.type, FailureWebSocketResponse):
            n: FailureWebSocketResponse = self.type
            return n.to_dict()

        raise Exception("Unknown type")

    def from_dict(self, d) -> Self:
        if d.get("type") == "SuccessWebSocketResponse":
            n: SuccessWebSocketResponse = SuccessWebSocketResponse()
            n.from_dict(d)
            self.type = n
            return Self
        elif d.get("type") == "FailureWebSocketResponse":
            n: FailureWebSocketResponse = FailureWebSocketResponse()
            n.from_dict(d)
            self.type = n
            return self

        raise Exception("Unknown type")
