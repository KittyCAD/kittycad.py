from enum import Enum


class CreatedAtSortMode(str, Enum):
    """Supported set of sort modes for scanning by created_at only.

    Currently, we only support scanning in ascending order."""  # noqa: E501

    """# Sort in increasing order of "created_at". """  # noqa: E501
    CREATED_AT_ASCENDING = "created_at_ascending"
    """# Sort in decreasing order of "created_at". """  # noqa: E501
    CREATED_AT_DESCENDING = "created_at_descending"

    def __str__(self) -> str:
        return str(self.value)
