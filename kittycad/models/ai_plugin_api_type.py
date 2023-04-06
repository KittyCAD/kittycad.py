from enum import Enum


class AiPluginApiType(str, Enum):
    OPENAPI = 'openapi'

    def __str__(self) -> str:
        return str(self.value)
