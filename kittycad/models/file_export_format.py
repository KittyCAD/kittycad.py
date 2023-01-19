from enum import Enum


class FileExportFormat(str, Enum):
    DAE = 'dae'
    DXF = 'dxf'
    FBX = 'fbx'
    FBXB = 'fbxb'
    JSON = 'json'
    OBJ = 'obj'
    OBJ_NOMTL = 'obj_nomtl'
    PLY = 'ply'
    STEP = 'step'
    STL = 'stl'
    SVG = 'svg'

    def __str__(self) -> str:
        return str(self.value)
