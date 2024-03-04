from enum import Enum


class UserOrgRole(str, Enum):
    """The roles for users in an organization."""  # noqa: E501

    """# Admins can do anything in the org. """  # noqa: E501
    ADMIN = "admin"
    """# Members of an org can not modify an org, but they belong in the org. """  # noqa: E501
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
