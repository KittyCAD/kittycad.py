from enum import Enum


class AsyncApiCallType(str, Enum):
    FILE_CONVERSION = 'FileConversion'
    FILE2_D_VECTOR_CONVERSION = 'File2DVectorConversion'
    FILE3_D_CONVERSION = 'File3DConversion'
    FILE_VOLUME = 'FileVolume'
    FILE_CENTER_OF_MASS = 'FileCenterOfMass'
    FILE_CENTER_OF_MASS_WITH_UNIFORM_DENSITY = 'FileCenterOfMassWithUniformDensity'
    FILE_MASS = 'FileMass'
    FILE_DENSITY = 'FileDensity'
    FILE_SURFACE_AREA = 'FileSurfaceArea'

    def __str__(self) -> str:
        return str(self.value)
