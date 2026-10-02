from enum import Enum


class KclProjectVersionAncestryStatus(str, Enum):
    """Whether a project's version ancestry is known."""  # noqa: E501

    """# The first version of a new project, with no parent."""  # noqa: E501

    ROOT = "root"

    """# The version has a recorded parent relationship."""  # noqa: E501

    RECORDED = "recorded"

    """# The version's parent was not recorded."""  # noqa: E501

    LEGACY_UNKNOWN = "legacy_unknown"

    def __str__(self) -> str:
        return str(self.value)
