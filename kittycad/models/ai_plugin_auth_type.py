from enum import Enum


class AiPluginAuthType(str, Enum):
    NONE = 'none'
    USER_HTTP = 'user_http'
    SERVICE_HTTP = 'service_http'
    OAUTH = 'oauth'

    def __str__(self) -> str:
        return str(self.value)
