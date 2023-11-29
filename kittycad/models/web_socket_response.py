from typing import Any, Dict, Type, TypeVar, Union

import attr
from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

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

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, SuccessWebSocketResponse):
            HV: SuccessWebSocketResponse = self.type
            return HV.model_dump()
        elif isinstance(self.type, FailureWebSocketResponse):
            CL: FailureWebSocketResponse = self.type
            return CL.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("success") is True:
            CD: SuccessWebSocketResponse = SuccessWebSocketResponse(**d)
            return cls(type=CD)
        elif d.get("success") is False:
            ZO: FailureWebSocketResponse = FailureWebSocketResponse(**d)
            return cls(type=ZO)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
                Union[
                    SuccessWebSocketResponse,
                    FailureWebSocketResponse,
                ]
            ),
        )
