from enum import Enum


class ApiCallStatus(str, Enum):
    """The status of an async API call."""  # noqa: E501

    """# The async API call is queued. """  # noqa: E501
    QUEUED = "queued"
    """# The async API call was uploaded to be converted. """  # noqa: E501
    UPLOADED = "uploaded"
    """# The async API call is in progress. """  # noqa: E501
    IN_PROGRESS = "in_progress"
    """# The async API call has completed. """  # noqa: E501
    COMPLETED = "completed"
    """# The async API call has failed. """  # noqa: E501
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
