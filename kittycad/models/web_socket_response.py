from typing import Union

from pydantic import RootModel

from .failure_web_socket_response import FailureWebSocketResponse
from .success_web_socket_response import SuccessWebSocketResponse

WebSocketResponse = RootModel[
    Union[
        SuccessWebSocketResponse,
        FailureWebSocketResponse,
    ]
]
