from enum import Enum


class GltfExportExtra(str, Enum):
    """Additional data that can be included in a glTF 2.0 export."""  # noqa: E501

    """# Sketch geometry and metadata."""  # noqa: E501

    SKETCHES = "sketches"

    """# Sketch regions and their resolver metadata."""  # noqa: E501

    REGIONS = "regions"

    """# Original imported files."""  # noqa: E501

    IMPORTED_FILES = "imported_files"

    """# Model-based definition (MBD) annotations."""  # noqa: E501

    MBD = "mbd"

    """# UUIDs and source UUIDs on boundary-representation solids, edges, faces, and surfaces."""  # noqa: E501

    GEOMETRY_UUIDS = "geometry_uuids"

    def __str__(self) -> str:
        return str(self.value)
