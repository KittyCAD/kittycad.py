from enum import Enum


class FileImportFormat(str, Enum):
    DAE = 'dae'
    DXF = 'dxf'
    FBX = 'fbx'
    OBJ_ZIP = 'obj_zip'
    OBJ = 'obj'
    OBJ_NOMTL = 'obj_nomtl'
    PLY = 'ply'
    STEP = 'step'
    STL = 'stl'
    SVG = 'svg'

    def __str__(self) -> str:
        return str(self.value)
