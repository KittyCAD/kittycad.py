from enum import Enum


class ErrorCode(str, Enum):
    """The type of error sent by the KittyCAD API."""  # noqa: E501

    """# Graphics engine failed to complete request, consider retrying """  # noqa: E501
    INTERNAL_ENGINE = "internal_engine"
    """# API failed to complete request, consider retrying """  # noqa: E501
    INTERNAL_API = "internal_api"
    """# User requested something geometrically or graphically impossible. Don't retry this request, as it's inherently impossible. Instead, read the error message and change your request. """  # noqa: E501
    BAD_REQUEST = "bad_request"
    """# Auth token is missing from the request """  # noqa: E501
    AUTH_TOKEN_MISSING = "auth_token_missing"
    """# Auth token is invalid in some way (expired, incorrect format, etc) """  # noqa: E501
    AUTH_TOKEN_INVALID = "auth_token_invalid"
    """# Client sent invalid JSON. """  # noqa: E501
    INVALID_JSON = "invalid_json"
    """# Client sent invalid BSON. """  # noqa: E501
    INVALID_BSON = "invalid_bson"
    """# Client sent a message which is not accepted over this protocol. """  # noqa: E501
    WRONG_PROTOCOL = "wrong_protocol"
    """# Problem sending data between client and KittyCAD API. """  # noqa: E501
    CONNECTION_PROBLEM = "connection_problem"
    """# Client sent a Websocket message type which the KittyCAD API does not handle. """  # noqa: E501
    MESSAGE_TYPE_NOT_ACCEPTED = "message_type_not_accepted"
    """# Client sent a Websocket message intended for WebRTC but it was configured as a WebRTC connection. """  # noqa: E501
    MESSAGE_TYPE_NOT_ACCEPTED_FOR_WEB_R_T_C = "message_type_not_accepted_for_web_r_t_c"

    def __str__(self) -> str:
        return str(self.value)
