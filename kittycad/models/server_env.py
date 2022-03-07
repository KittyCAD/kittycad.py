from enum import Enum


class ServerEnv(str, Enum):
    PRODUCTION = 'production'
    DEVELOPMENT = 'development'
    PREVIEW = 'preview'

    def __str__(self) -> str:
        return str(self.value)
