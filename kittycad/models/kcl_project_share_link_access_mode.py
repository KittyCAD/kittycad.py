from enum import Enum


class KclProjectShareLinkAccessMode(str, Enum):
    """Access policy for a shared project download link."""  # noqa: E501

    """# Anyone holding the URL can download the project."""  # noqa: E501

    ANYONE_WITH_LINK = "anyone_with_link"

    """# Only members of the owner's organization can use the URL."""  # noqa: E501

    ORGANIZATION_ONLY = "organization_only"

    def __str__(self) -> str:
        return str(self.value)
