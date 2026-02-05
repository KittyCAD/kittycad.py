from enum import Enum


class BodyType(str, Enum):
    """Body type determining if the operation will create a manifold (solid) body or a non-manifold collection of surfaces."""  # noqa: E501

    """# Defines a body that is manifold."""  # noqa: E501

    SOLID = "solid"

    """# Defines a body that is non-manifold (an open collection of connected surfaces)."""  # noqa: E501

    SURFACE = "surface"

    def __str__(self) -> str:
        return str(self.value)
