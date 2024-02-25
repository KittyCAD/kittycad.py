from enum import Enum


class OrgRole(str, Enum):
    """The roles in an organization."""  # noqa: E501

    """# Admins can do anything in the org. """  # noqa: E501
    ADMIN = "admin"
    """# Members of an org can not modify an org, but they belong in the org. """  # noqa: E501
    MEMBER = "member"
    """# A service account role. """  # noqa: E501
    SERVICE_ACCOUNT = "service_account"

    def __str__(self) -> str:
        return str(self.value)
