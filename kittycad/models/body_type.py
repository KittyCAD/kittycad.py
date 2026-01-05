from enum import Enum


class BodyType(str, Enum):
    """Body type determining if the operation will create a solid or a surface."""  # noqa: E501

    """# Create a body that has two caps, creating a solid object."""  # noqa: E501

    SOLID = "solid"

    """# Create only the surface of the body without any caps."""  # noqa: E501

    SURFACE = "surface"

    def __str__(self) -> str:
        return str(self.value)
