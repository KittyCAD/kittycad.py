from enum import Enum


class File3DImportFormat(str, Enum):
    DAE = 'dae'
    FBX = 'fbx'
    OBJ = 'obj'
    OBJ_NOMTL = 'obj_nomtl'
    STEP = 'step'
    STL = 'stl'

    def __str__(self) -> str:
        return str(self.value)
