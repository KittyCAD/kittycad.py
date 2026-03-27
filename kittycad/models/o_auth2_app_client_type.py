from enum import Enum


class OAuth2AppClientType(str, Enum):
    """The type of an OAuth 2.0 client."""  # noqa: E501

    """# A public client."""  # noqa: E501

    PUBLIC = "public"

    """# A confidential client."""  # noqa: E501

    CONFIDENTIAL = "confidential"

    def __str__(self) -> str:
        return str(self.value)
