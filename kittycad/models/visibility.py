from enum import Enum


class Visibility(str, Enum):
    """Identifies the visibility of entities."""  # noqa: E501

    """# The entity is visible."""  # noqa: E501

    SHOW = "show"

    """# The entity is hidden."""  # noqa: E501

    HIDE = "hide"

    def __str__(self) -> str:
        return str(self.value)
