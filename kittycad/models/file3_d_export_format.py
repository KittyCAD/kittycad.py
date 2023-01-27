from enum import Enum


class File3DExportFormat(str, Enum):
    DAE = 'dae'
    FBX = 'fbx'
    FBXB = 'fbxb'
    OBJ = 'obj'
    OBJ_NOMTL = 'obj_nomtl'
    PLY = 'ply'
    STEP = 'step'
    STL = 'stl'

    def __str__(self) -> str:
        return str(self.value)
