from enum import Enum


class ExecutionLogStream(str, Enum):
    """A retained binary stream; live tailing is not part of this protocol."""  # noqa: E501

    """# Standard output."""  # noqa: E501

    STDOUT = "stdout"

    """# Standard error."""  # noqa: E501

    STDERR = "stderr"

    def __str__(self) -> str:
        return str(self.value)
