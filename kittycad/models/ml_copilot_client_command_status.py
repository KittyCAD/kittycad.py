from enum import Enum


class MlCopilotClientCommandStatus(str, Enum):
    """Lifecycle state reported by a client for a requested command."""  # noqa: E501

    """# The client accepted the request and execution is still in progress."""  # noqa: E501

    ACCEPTED = "accepted"

    """# The command completed successfully."""  # noqa: E501

    SUCCEEDED = "succeeded"

    """# The client or user declined the request before execution completed."""  # noqa: E501

    REJECTED = "rejected"

    """# The command failed during execution."""  # noqa: E501

    FAILED = "failed"

    """# Execution was cancelled after it started."""  # noqa: E501

    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)
