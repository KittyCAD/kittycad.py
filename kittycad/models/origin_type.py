from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class OptionLocal(KittyCadBaseModel):
    """Local Origin ([0, 0, 0] in object space)."""

    type: Literal["local"] = "local"


class OptionGlobal(KittyCadBaseModel):
    """Global Origin ([0, 0, 0] in world space)."""

    type: Literal["global"] = "global"


class OptionCustom(KittyCadBaseModel):
    """Custom Origin (user specified point in world space)."""

    origin: Point3d

    type: Literal["custom"] = "custom"


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
