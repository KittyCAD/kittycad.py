from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = 'DEVELOPMENT'
    PREVIEW = 'PREVIEW'
    PRODUCTION = 'PRODUCTION'

    def __str__(self) -> str:
        return str(self.value)
