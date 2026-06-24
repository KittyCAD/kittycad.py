from enum import Enum


class FileImportFormat(str, Enum):
    """The valid types of source file formats."""  # noqa: E501

    """# ACIS part format."""  # noqa: E501

    ACIS = "acis"

    """# CATIA part format."""  # noqa: E501

    CATIA = "catia"

    """# PTC Creo part format."""  # noqa: E501

    CREO = "creo"

    """# Autodesk Filmbox (FBX) format. <https://en.wikipedia.org/wiki/FBX>"""  # noqa: E501

    FBX = "fbx"

    """# glTF 2.0."""  # noqa: E501

    GLTF = "gltf"

    """# Autodesk Inventor part format."""  # noqa: E501

    INVENTOR = "inventor"

    """# Siemens NX part format."""  # noqa: E501

    NX = "nx"

    """# The OBJ file format. <https://en.wikipedia.org/wiki/Wavefront_.obj_file> It may or may not have an an attached material (mtl // mtllib) within the file, but we interact with it as if it does not."""  # noqa: E501

    OBJ = "obj"

    """# Parasolid part format."""  # noqa: E501

    PARASOLID = "parasolid"

    """# The PLY file format. <https://en.wikipedia.org/wiki/PLY_(file_format)>"""  # noqa: E501

    PLY = "ply"

    """# SolidWorks part (SLDPRT) format."""  # noqa: E501

    SLDPRT = "sldprt"

    """# The STEP file format. <https://en.wikipedia.org/wiki/ISO_10303-21>"""  # noqa: E501

    STEP = "step"

    """# The STL file format. <https://en.wikipedia.org/wiki/STL_(file_format)>"""  # noqa: E501

    STL = "stl"

    def __str__(self) -> str:
        return str(self.value)
