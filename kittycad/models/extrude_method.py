from enum import Enum


class ExtrudeMethod(str, Enum):
    """Extrusion method determining if the extrusion will be part of the existing object or an entirely new object."""  # noqa: E501

    """# Create a new object that is not connected to the object it is extruded from. This will result in two objects after the operation."""  # noqa: E501

    NEW = "new"

    """# This extrusion will be part of object it is extruded from. This will result in one object after the operation."""  # noqa: E501

    MERGE = "merge"

    def __str__(self) -> str:
        return str(self.value)
