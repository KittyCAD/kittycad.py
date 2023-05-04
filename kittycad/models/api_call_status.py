from enum import Enum


class ApiCallStatus(str, Enum):
    """The status of an async API call."""  # noqa: E501

    """# The async API call is queued. """  # noqa: E501
    QUEUED = "Queued"
    """# The async API call was uploaded to be converted. """  # noqa: E501
    UPLOADED = "Uploaded"
    """# The async API call is in progress. """  # noqa: E501
    IN_PROGRESS = "In Progress"
    """# The async API call has completed. """  # noqa: E501
    COMPLETED = "Completed"
    """# The async API call has failed. """  # noqa: E501
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
