from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.system import System
from ..models.unit_length import UnitLength


class OptionFbx(BaseModel):
    """Autodesk Filmbox (FBX) format."""

    type: Literal["fbx"] = "fbx"

    model_config = ConfigDict(protected_namespaces=())


class OptionGltf(BaseModel):
    """Binary glTF 2.0. We refer to this as glTF since that is how our customers refer to it, but this can also import binary glTF (glb)."""

    type: Literal["gltf"] = "gltf"

    model_config = ConfigDict(protected_namespaces=())


class OptionObj(BaseModel):
    """Wavefront OBJ format."""

    coords: System

    type: Literal["obj"] = "obj"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


class OptionPly(BaseModel):
    """The PLY Polygon File Format."""

    coords: System

    type: Literal["ply"] = "ply"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


class OptionSldprt(BaseModel):
    """SolidWorks part (SLDPRT) format."""

    split_closed_faces: bool = False

    type: Literal["sldprt"] = "sldprt"

    model_config = ConfigDict(protected_namespaces=())


class OptionStep(BaseModel):
    """ISO 10303-21 (STEP) format."""

    split_closed_faces: bool = False

    type: Literal["step"] = "step"

    model_config = ConfigDict(protected_namespaces=())


class OptionStl(BaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    type: Literal["stl"] = "stl"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


InputFormat = RootModel[
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
