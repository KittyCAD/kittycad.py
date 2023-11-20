from enum import Enum


class CodeLanguage(str, Enum):
    """The language code is written in."""  # noqa: E501

    """# The `go` programming language. """  # noqa: E501
    GO = "go"
    """# The `python` programming language. """  # noqa: E501
    PYTHON = "python"
    """# The `node` programming language. """  # noqa: E501
    NODE = "node"

    def __str__(self) -> str:
        return str(self.value)
