from enum import Enum


class ModelingAppEventType(str, Enum):
    """Type for modeling-app events"""  # noqa: E501

    """# This event is sent before the modeling app or project is closed. The attachment should contain the contents of the most recent successful compile. """  # noqa: E501
    SUCCESSFUL_COMPILE_BEFORE_CLOSE = "successful_compile_before_close"

    def __str__(self) -> str:
        return str(self.value)
