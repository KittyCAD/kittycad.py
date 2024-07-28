from typing import Any, Dict, Type, TypeVar, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .failure_web_socket_response import FailureWebSocketResponse
from .success_web_socket_response import SuccessWebSocketResponse

WebSocketResponse = RootModel[
    Union[
        SuccessWebSocketResponse,
        FailureWebSocketResponse,
    ]
]
