from enum import Enum


class FileExportFormat(str, Enum):
    DAE = 'dae'
    DXF = 'dxf'
    FBX = 'fbx'
    FBXB = 'fbxb'
    OBJ = 'obj'
    PLY = 'ply'
    STEP = 'step'
    STL = 'stl'

    def __str__(self) -> str:
        return str(self.value)
