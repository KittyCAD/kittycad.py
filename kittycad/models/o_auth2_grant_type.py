from enum import Enum


class OAuth2GrantType(str, Enum):
    """An OAuth 2.0 Grant Type. These are documented here: <https://oauth.net/2/grant-types/>."""  # noqa: E501

    """# An OAuth 2.0 Device Authorization Grant. """  # noqa: E501
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE = (
        "urn:ietf:params:oauth:grant-type:device_code"
    )

    def __str__(self) -> str:
        return str(self.value)
