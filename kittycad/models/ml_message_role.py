from enum import Enum


class MlMessageRole(str, Enum):
    """The role of the author of a chat message."""  # noqa: E501

    """# Client-authored input."""  # noqa: E501

    CLIENT = "client"

    """# Server-authored message."""  # noqa: E501

    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)
