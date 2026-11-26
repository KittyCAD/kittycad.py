from enum import Enum


class CompressionType(str, Enum):
    """Compression requested for a binary command response. Small or incompressible responses may remain uncompressed."""  # noqa: E501

    """# Zstandard framing, detected by magic bytes `28 b5 2f fd`, around the complete MessagePack response."""  # noqa: E501

    ZSTD = "zstd"

    def __str__(self) -> str:
        return str(self.value)
