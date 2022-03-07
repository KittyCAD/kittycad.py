from enum import Enum


class ValidSourceFileFormat(str, Enum):
    STL = 'stl'
    OBJ = 'obj'
    DAE = 'dae'
    STEP = 'step'
    FBX = 'fbx'

    def __str__(self) -> str:
        return str(self.value)
