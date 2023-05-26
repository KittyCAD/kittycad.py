from enum import Enum


class AsyncApiCallType(str, Enum):
    """The type of async API call."""  # noqa: E501

    """# File conversion. """  # noqa: E501
    FILE_CONVERSION = "FileConversion"
    """# File volume. """  # noqa: E501
    FILE_VOLUME = "FileVolume"
    """# File center of mass. """  # noqa: E501
    FILE_CENTER_OF_MASS = "FileCenterOfMass"
    """# File mass. """  # noqa: E501
    FILE_MASS = "FileMass"
    """# File density. """  # noqa: E501
    FILE_DENSITY = "FileDensity"
    """# File surface area. """  # noqa: E501
    FILE_SURFACE_AREA = "FileSurfaceArea"

    def __str__(self) -> str:
        return str(self.value)
