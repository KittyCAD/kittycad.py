from enum import Enum


class FileExportFormat(str, Enum):
    """The valid types of output file formats."""  # noqa: E501

    """# Autodesk Filmbox (FBX) format. <https://en.wikipedia.org/wiki/FBX> """  # noqa: E501
    FBX = "fbx"
    """# Binary glTF 2.0.

This is a single binary with .glb extension.

This is better if you want a compressed format as opposed to the human readable glTF that lacks compression. """  # noqa: E501
    GLB = "glb"
    """# glTF 2.0. Embedded glTF 2.0 (pretty printed).

Single JSON file with .gltf extension binary data encoded as base64 data URIs.

The JSON contents are pretty printed.

It is human readable, single file, and you can view the diff easily in a git commit. """  # noqa: E501
    GLTF = "gltf"
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
