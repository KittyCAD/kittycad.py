from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .base import KittyCadBaseModel


class DxfData(KittyCadBaseModel):
    """Export storage."""


class OptionDxf(KittyCadBaseModel):
    """AutoCAD drawing interchange format."""

    storage: DxfData

    type: Literal["dxf"] = "dxf"


OutputFormat2d = RootModel[Annotated[Union[OptionDxf,], Field(discriminator="type")]]
