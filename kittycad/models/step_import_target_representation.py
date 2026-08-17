from enum import Enum


class StepImportTargetRepresentation(str, Enum):
    """After importing, how should this model's data be represented?"""  # noqa: E501

    """# Mesh of 2D geometry"""  # noqa: E501

    MESH = "mesh"

    """# Boundary representation"""  # noqa: E501

    BREP = "brep"

    def __str__(self) -> str:
        return str(self.value)
