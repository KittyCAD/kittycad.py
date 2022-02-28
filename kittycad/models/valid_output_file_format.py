from enum import Enum


class ValidOutputFileFormat(str, Enum):
    STL = 'stl'
    OBJ = 'obj'
    DAE = 'dae'
    STEP = 'step'
    FBX = 'fbx'
    FBXB = 'fbxb'

    def __str__(self) -> str:
        return str(self.value)
