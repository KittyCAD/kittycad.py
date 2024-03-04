from enum import Enum


class SceneSelectionType(str, Enum):
    """The type of scene selection change"""  # noqa: E501

    """# Replaces the selection """  # noqa: E501
    REPLACE = "replace"
    """# Adds to the selection """  # noqa: E501
    ADD = "add"
    """# Removes from the selection """  # noqa: E501
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
