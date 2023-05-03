from enum import Enum


class CodeLanguage(str, Enum):
    """The language code is written in."""  # noqa: E501

    GO = "go"
    PYTHON = "python"
    NODE = "node"

    def __str__(self) -> str:
        return str(self.value)
