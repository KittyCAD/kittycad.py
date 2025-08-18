from ..models.input_format3d import InputFormat3d
from ..models.output_format3d import OutputFormat3d
from .base import KittyCadBaseModel


class ConversionParams(KittyCadBaseModel):
    """Describes the file to convert (src) and what it should be converted into (output)."""

    output_format: OutputFormat3d

    src_format: InputFormat3d
