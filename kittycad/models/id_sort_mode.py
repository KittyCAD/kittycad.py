from enum import Enum


class IdSortMode(str, Enum):
    """Supported set of sort modes for scanning by id only.

    Currently, we only support scanning in ascending order."""  # noqa: E501

    """# Sort in increasing order of "id"."""  # noqa: E501

    ID_ASCENDING = "id_ascending"

    """# Sort in decreasing order of "id","""  # noqa: E501

    ID_DESCENDING = "id_descending"

    def __str__(self) -> str:
        return str(self.value)
