from enum import Enum


class CodeLanguage(str, Enum):
    GO = "go"
    PYTHON = "python"
    NODE = "node"

    def __str__(self) -> str:
        return str(self.value)
