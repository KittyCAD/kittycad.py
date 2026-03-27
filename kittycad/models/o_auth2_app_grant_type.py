from enum import Enum


class OAuth2AppGrantType(str, Enum):
    """An OAuth 2.0 grant type allowed for an app."""  # noqa: E501

    """# OAuth 2.0 Device Authorization Grant."""  # noqa: E501

    DEVICE_CODE = "device_code"

    """# OAuth 2.0 Authorization Code Grant."""  # noqa: E501

    AUTHORIZATION_CODE = "authorization_code"

    """# OAuth 2.0 Refresh Token Grant."""  # noqa: E501

    REFRESH_TOKEN = "refresh_token"

    """# OAuth 2.0 Client Credentials Grant."""  # noqa: E501

    CLIENT_CREDENTIALS = "client_credentials"

    def __str__(self) -> str:
        return str(self.value)
