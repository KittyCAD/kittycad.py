from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class DxfData(BaseModel):
    """Export storage."""

    model_config = ConfigDict(protected_namespaces=())


class OptionDxf(BaseModel):
    """AutoCAD drawing interchange format."""

    storage: DxfData

    type: Literal["dxf"] = "dxf"

    model_config = ConfigDict(protected_namespaces=())


OutputFormat2d = RootModel[Annotated[Union[OptionDxf,], Field(discriminator="type")]]
