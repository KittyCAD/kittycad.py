from enum import Enum


class File2DVectorImportFormat(str, Enum):
    DXF = 'dxf'
    SVG = 'svg'

    def __str__(self) -> str:
        return str(self.value)
