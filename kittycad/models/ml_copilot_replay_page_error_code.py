from enum import Enum


class MlCopilotReplayPageErrorCode(str, Enum):
    """Machine-readable failures for paginated client history, independent of generation."""  # noqa: E501

    """# Pagination is not available on this connection."""  # noqa: E501

    UNAVAILABLE = "unavailable"

    """# The connection query does not satisfy pagination requirements."""  # noqa: E501

    INVALID_REQUEST = "invalid_request"

    """# The continuation expired, belongs to another connection, or its boundary no longer exists. The client must start a new replay instead of retrying it."""  # noqa: E501

    INVALID_CURSOR = "invalid_cursor"

    """# A transient page load failure; the same request may be retried."""  # noqa: E501

    LOAD_FAILED = "load_failed"

    def __str__(self) -> str:
        return str(self.value)
