from enum import Enum


class Environment(str, Enum):
    """The environment the server is running in."""  # noqa: E501

    DEVELOPMENT = "DEVELOPMENT"
    PREVIEW = "PREVIEW"
    PRODUCTION = "PRODUCTION"

    def __str__(self) -> str:
        return str(self.value)
