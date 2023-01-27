from enum import Enum


class File3DImportFormat(str, Enum):
    DAE = 'dae'
    DXF = 'dxf'
    FBX = 'fbx'
    OBJ_ZIP = 'obj_zip'
    OBJ = 'obj'
    OBJ_NOMTL = 'obj_nomtl'
    PLY = 'ply'
    STEP = 'step'
    STL = 'stl'

    def __str__(self) -> str:
        return str(self.value)
