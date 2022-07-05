from enum import Enum


class OAuth2GrantType(str, Enum):
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE = 'urn:ietf:params:oauth:grant-type:device_code'

    def __str__(self) -> str:
        return str(self.value)
