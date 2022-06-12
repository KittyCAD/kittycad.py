from enum import Enum


class CodeLanguage(str, Enum):
    GO = 'go'
    RUST = 'rust'
    PYTHON = 'python'
    NODE = 'node'

    def __str__(self) -> str:
        return str(self.value)
