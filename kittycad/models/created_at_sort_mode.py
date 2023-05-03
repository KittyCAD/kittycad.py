from enum import Enum


class CreatedAtSortMode(str, Enum):
    """Supported set of sort modes for scanning by created_at only.

    Currently, we only support scanning in ascending order."""  # noqa: E501

    """# sort in increasing order of "created_at" """  # noqa: E501
    CREATED_AT_ASCENDING = "created-at-ascending"
    """# sort in decreasing order of "created_at" """  # noqa: E501
    CREATED_AT_DESCENDING = "created-at-descending"

    def __str__(self) -> str:
        return str(self.value)
