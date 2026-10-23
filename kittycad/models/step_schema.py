from enum import Enum


class StepSchema(str, Enum):
    """Specifies the STEP application protocol schema for export."""  # noqa: E501

    """# AP203 edition 2."""  # noqa: E501

    AP203 = "ap203"

    """# AP214."""  # noqa: E501

    AP214 = "ap214"

    """# AP242.

This is the default setting."""  # noqa: E501

    AP242 = "ap242"

    def __str__(self) -> str:
        return str(self.value)
