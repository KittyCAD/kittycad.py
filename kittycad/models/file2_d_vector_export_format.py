from enum import Enum


class File2DVectorExportFormat(str, Enum):
    DXF = 'dxf'
    JSON = 'json'
    SVG = 'svg'

    def __str__(self) -> str:
        return str(self.value)
