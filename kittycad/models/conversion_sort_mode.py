from enum import Enum


class ConversionSortMode(str, Enum):
    """Supported sort modes for org dataset conversions."""  # noqa: E501

    """# Sort by created_at in increasing order."""  # noqa: E501

    CREATED_AT_ASCENDING = "created_at_ascending"

    """# Sort by created_at in decreasing order."""  # noqa: E501

    CREATED_AT_DESCENDING = "created_at_descending"

    """# Sort by status in increasing order."""  # noqa: E501

    STATUS_ASCENDING = "status_ascending"

    """# Sort by status in decreasing order."""  # noqa: E501

    STATUS_DESCENDING = "status_descending"

    """# Sort by updated_at in increasing order."""  # noqa: E501

    UPDATED_AT_ASCENDING = "updated_at_ascending"

    """# Sort by updated_at in decreasing order."""  # noqa: E501

    UPDATED_AT_DESCENDING = "updated_at_descending"

    def __str__(self) -> str:
        return str(self.value)
