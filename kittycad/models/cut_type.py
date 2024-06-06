from enum import Enum


class CutType(str, Enum):
    """What kind of cut to do"""  # noqa: E501

    """# Round off an edge. """  # noqa: E501
    FILLET = "fillet"
    """# Cut away an edge. """  # noqa: E501
    CHAMFER = "chamfer"

    def __str__(self) -> str:
        return str(self.value)
