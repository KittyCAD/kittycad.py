from enum import Enum


class ErrorCode(str, Enum):
    """The type of errorcode."""  # noqa: E501

    """# User requested something impossible or invalid """  # noqa: E501
    BAD_REQUEST = "bad_request"
    """# Engine failed to complete request, consider retrying """  # noqa: E501
    INTERNAL_ENGINE = "internal_engine"

    def __str__(self) -> str:
        return str(self.value)
