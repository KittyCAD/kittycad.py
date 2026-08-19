from enum import Enum


class ProjectAccessScope(str, Enum):
    """Ownership scope for an authenticated project response."""  # noqa: E501

    """# The project is owned personally by its creator."""  # noqa: E501

    PERSONAL = "personal"

    """# The project is owned by an organization."""  # noqa: E501

    ORGANIZATION = "organization"

    def __str__(self) -> str:
        return str(self.value)
