from enum import Enum


class OAuth2TokenGrantType(str, Enum):
    """The OAuth 2.0 token endpoint grant types supported by the general token endpoint."""  # noqa: E501

    """# The authorization code grant."""  # noqa: E501

    AUTHORIZATION_CODE = "authorization_code"

    """# The refresh token grant."""  # noqa: E501

    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)
