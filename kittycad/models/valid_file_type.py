from enum import Enum


class ValidFileType(str, Enum):
    OBJ = "obj"
    STL = "stl"
    DAE= "dae"

    def __str__(self) -> str:
        return str(self.value)
