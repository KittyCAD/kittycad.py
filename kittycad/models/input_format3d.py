from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.system import System
from ..models.unit_length import UnitLength
from .base import KittyCadBaseModel


class OptionFbx(KittyCadBaseModel):
    """Autodesk Filmbox (FBX) format."""

    type: Literal["fbx"] = "fbx"


class OptionGltf(KittyCadBaseModel):
    """Binary glTF 2.0. We refer to this as glTF since that is how our customers refer to it, but this can also import binary glTF (glb)."""

    type: Literal["gltf"] = "gltf"


class OptionObj(KittyCadBaseModel):
    """Wavefront OBJ format."""

    coords: System

    type: Literal["obj"] = "obj"

    units: UnitLength


class OptionPly(KittyCadBaseModel):
    """The PLY Polygon File Format."""

    coords: System

    type: Literal["ply"] = "ply"

    units: UnitLength


class OptionSldprt(KittyCadBaseModel):
    """SolidWorks part (SLDPRT) format."""

    split_closed_faces: bool = False

    type: Literal["sldprt"] = "sldprt"


class OptionStep(KittyCadBaseModel):
    """ISO 10303-21 (STEP) format."""

    split_closed_faces: bool = False

    type: Literal["step"] = "step"


class OptionStl(KittyCadBaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    type: Literal["stl"] = "stl"

    units: UnitLength


InputFormat3d = RootModel[
    Annotated[
        Union[
            OptionFbx,
            OptionGltf,
            OptionObj,
            OptionPly,
            OptionSldprt,
            OptionStep,
            OptionStl,
        ],
        Field(discriminator="type"),
    ]
]
