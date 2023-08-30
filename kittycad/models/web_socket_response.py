from typing import Union

from .failure_web_socket_response import FailureWebSocketResponse
from .success_web_socket_response import SuccessWebSocketResponse

WebSocketResponse = Union[SuccessWebSocketResponse, FailureWebSocketResponse]
