from enum import Enum


class ModelingAppShareLinks(str, Enum):
    """Modeling App share link capabilities."""  # noqa: E501

    """# Publicly accessible share links."""  # noqa: E501

    PUBLIC = "public"

    """# Share links guarded by a password."""  # noqa: E501

    PASSWORD_PROTECTED = "password_protected"

    """# Share links restricted to members of the organization."""  # noqa: E501

    ORGANIZATION_ONLY = "organization_only"

    def __str__(self) -> str:
        return str(self.value)
