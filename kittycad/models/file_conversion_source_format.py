from enum import Enum


class FileConversionSourceFormat(str, Enum):
    STL = 'stl'
    OBJ = 'obj'
    DAE = 'dae'
    STEP = 'step'
    FBX = 'fbx'

    def __str__(self) -> str:
        return str(self.value)
