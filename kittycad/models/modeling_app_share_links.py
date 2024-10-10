from enum import Enum


class ModelingAppShareLinks(str, Enum):
    """The options for sharable links through the modeling app."""  # noqa: E501

    """# Public. """  # noqa: E501
    PUBLIC = "public"
    """# Password protected. """  # noqa: E501
    PASSWORD_PROTECTED = "password_protected"
    """# Organization only. Links can be made only available to members of the organization. """  # noqa: E501
    ORGANIZATION_ONLY = "organization_only"

    def __str__(self) -> str:
        return str(self.value)
