from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.point3d import Point3d


class OptionLocal(BaseModel):
    """Local Origin (center of object bounding box)."""

    type: Literal["local"] = "local"

    model_config = ConfigDict(protected_namespaces=())


class OptionGlobal(BaseModel):
    """Global Origin (0, 0, 0)."""

    type: Literal["global"] = "global"

    model_config = ConfigDict(protected_namespaces=())


class OptionCustom(BaseModel):
    """Custom Origin (user specified point)."""

    origin: Point3d

    type: Literal["custom"] = "custom"

    model_config = ConfigDict(protected_namespaces=())


OriginType = RootModel[
    Annotated[
        Union[
            OptionLocal,
            OptionGlobal,
            OptionCustom,
        ],
        Field(discriminator="type"),
    ]
]
