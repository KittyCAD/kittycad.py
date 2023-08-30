from enum import Enum


class GltfStorage(str, Enum):
    """Describes the storage format of a glTF 2.0 scene."""  # noqa: E501

    """# Binary glTF 2.0.

This is a single binary with .glb extension. """  # noqa: E501
    BINARY = "binary"
    """# Standard glTF 2.0.

This is a JSON file with .gltf extension paired with a separate binary blob file with .bin extension. """  # noqa: E501
    STANDARD = "standard"
    """# Embedded glTF 2.0.

Single JSON file with .gltf extension binary data encoded as base64 data URIs.

This is the default setting. """  # noqa: E501
    EMBEDDED = "embedded"

    def __str__(self) -> str:
        return str(self.value)
