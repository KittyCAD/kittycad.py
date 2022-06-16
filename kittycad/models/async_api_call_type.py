from enum import Enum


class AsyncAPICallType(str, Enum):
    FILE_CONVERSION = 'FileConversion'
    FILE_VOLUME = 'FileVolume'
    FILE_MASS = 'FileMass'
    FILE_DENSITY = 'FileDensity'

    def __str__(self) -> str:
        return str(self.value)
