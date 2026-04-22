from enum import Enum


class OAuth2AuthorizationResponseType(str, Enum):
    """The OAuth 2.0 authorization response type."""  # noqa: E501

    """# The authorization code response type."""  # noqa: E501

    CODE = "code"

    def __str__(self) -> str:
        return str(self.value)
