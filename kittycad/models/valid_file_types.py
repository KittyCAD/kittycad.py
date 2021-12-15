from enum import Enum


class ValidFileTypes(str, Enum):
    STEP = "step"
    OBJ = "obj"
    STL = "stl"
    DXF = "dxf"
    DWG = "dwg"

    def __str__(self) -> str:
        return str(self.value)
