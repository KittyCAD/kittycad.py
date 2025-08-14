from pydantic import BaseModel, ConfigDict

from ..models.input_format3d import InputFormat3d
from ..models.output_format3d import OutputFormat3d


class ConversionParams(BaseModel):
    """Describes the file to convert (src) and what it should be converted into (output)."""

    output_format: OutputFormat3d

    src_format: InputFormat3d

    model_config = ConfigDict(protected_namespaces=())
