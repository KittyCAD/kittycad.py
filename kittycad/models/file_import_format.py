from enum import Enum


class FileImportFormat(str, Enum):
    """The valid types of source file formats."""  # noqa: E501

    """# The COLLADA/DAE file format. <https://en.wikipedia.org/wiki/COLLADA> """  # noqa: E501
    DAE = "dae"
    """# The DXF file format. <https://en.wikipedia.org/wiki/AutoCAD_DXF> """  # noqa: E501
    DXF = "dxf"
    """# The FBX file format. <https://en.wikipedia.org/wiki/FBX> """  # noqa: E501
    FBX = "fbx"
    """# The OBJ file format. A zip file containing both the obj file itself and its associated mtl file for full processing. <https://en.wikipedia.org/wiki/Wavefront_.obj_file>> """  # noqa: E501
    OBJ_ZIP = "obj_zip"
    """# The OBJ file format. <https://en.wikipedia.org/wiki/Wavefront_.obj_file> It may or may not have an an attached material (mtl // mtllib) within the file, but we interact with it as if it does not. """  # noqa: E501
    OBJ = "obj"
    """# The PLY file format. <https://en.wikipedia.org/wiki/PLY_(file_format)> """  # noqa: E501
    PLY = "ply"
    """# The STEP file format. <https://en.wikipedia.org/wiki/ISO_10303-21> """  # noqa: E501
    STEP = "step"
    """# The STL file format. <https://en.wikipedia.org/wiki/STL_(file_format)> """  # noqa: E501
    STL = "stl"

    def __str__(self) -> str:
        return str(self.value)
