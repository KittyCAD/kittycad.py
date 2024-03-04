from .success_web_socket_response import SuccessWebSocketResponse
from .failure_web_socket_response import FailureWebSocketResponse
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




WebSocketResponse = RootModel[Union[
        
        SuccessWebSocketResponse,
        
        FailureWebSocketResponse,
        
    ]]

