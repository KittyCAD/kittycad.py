from typing import Any, Dict, Type, TypeVar, Union

import attr

from .failure_web_socket_response import FailureWebSocketResponse
from .success_web_socket_response import SuccessWebSocketResponse

GY = TypeVar("GY", bound="WebSocketResponse")


@attr.s(auto_attribs=True)
class WebSocketResponse:

    """Websocket responses can either be successful or unsuccessful. Slightly different schemas in either case."""

    type: Union[
        SuccessWebSocketResponse,
        FailureWebSocketResponse,
    ]

    def __init__(
        self,
        type: Union[
            SuccessWebSocketResponse,
            FailureWebSocketResponse,
        ],
    ):
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, SuccessWebSocketResponse):
            XP: SuccessWebSocketResponse = self.type
            return XP.to_dict()
        elif isinstance(self.type, FailureWebSocketResponse):
            QM: FailureWebSocketResponse = self.type
            return QM.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "SuccessWebSocketResponse":
            VT: SuccessWebSocketResponse = SuccessWebSocketResponse()
            VT.from_dict(d)
            return cls(type=VT)
        elif d.get("type") == "FailureWebSocketResponse":
            UR: FailureWebSocketResponse = FailureWebSocketResponse()
            UR.from_dict(d)
            return cls(type=UR)

        raise Exception("Unknown type")
