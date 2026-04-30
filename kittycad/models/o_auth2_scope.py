from enum import Enum


class OAuth2Scope(str, Enum):
    """Supported OAuth 2.0 scopes."""  # noqa: E501

    """# Grants access to modeling APIs."""  # noqa: E501

    MODELING = "modeling"

    """# Grants write access to admin APIs."""  # noqa: E501

    ADMIN_WRITE = "admin:write"

    def __str__(self) -> str:
        return str(self.value)
