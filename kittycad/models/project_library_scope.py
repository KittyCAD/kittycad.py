from enum import Enum


class ProjectLibraryScope(str, Enum):
    """Ownership of a new cloud project library."""  # noqa: E501

    """# Owned personally by the authenticated user."""  # noqa: E501

    PERSONAL = "personal"

    """# Owned by the active organization; requires organization-admin access."""  # noqa: E501

    ORGANIZATION = "organization"

    def __str__(self) -> str:
        return str(self.value)
