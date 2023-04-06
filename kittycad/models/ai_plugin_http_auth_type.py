from enum import Enum


class AiPluginHttpAuthType(str, Enum):
    BASIC = 'basic'
    BEARER = 'bearer'

    def __str__(self) -> str:
        return str(self.value)
