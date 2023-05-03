from enum import Enum


class AsyncApiCallType(str, Enum):
    FILE_CONVERSION = "FileConversion"
    FILE_VOLUME = "FileVolume"
    FILE_CENTER_OF_MASS = "FileCenterOfMass"
    FILE_MASS = "FileMass"
    FILE_DENSITY = "FileDensity"
    FILE_SURFACE_AREA = "FileSurfaceArea"

    def __str__(self) -> str:
        return str(self.value)
