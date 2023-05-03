from enum import Enum


class FileImportFormat(str, Enum):
    DAE = "dae"
    DXF = "dxf"
    FBX = "fbx"
    OBJ_ZIP = "obj_zip"
    OBJ = "obj"
    PLY = "ply"
    STEP = "step"
    STL = "stl"

    def __str__(self) -> str:
        return str(self.value)
