from enum import Enum


class AiPluginHttpAuthType(str, Enum):
    """AI plugin http auth type."""  # noqa: E501

    """# Basic. """  # noqa: E501
    BASIC = "basic"
    """# Bearer. """  # noqa: E501
    BEARER = "bearer"

    def __str__(self) -> str:
        return str(self.value)
