from enum import Enum


class File2DVectorExportFormat(str, Enum):
    DXF = 'dxf'
    JSON = 'json'
    PNG = 'png'
    PS = 'ps'
    SVG = 'svg'

    def __str__(self) -> str:
        return str(self.value)
