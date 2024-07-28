import datetime
from typing import Any, Dict, List, Literal, Optional, Type, TypeVar, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict, Field, RootModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing_extensions import Annotated

from ..models.system import System
from ..models.unit_length import UnitLength
from .base64data import Base64Data


class fbx(BaseModel):
    """Autodesk Filmbox (FBX) format."""

    type: Literal["fbx"] = "fbx"

    model_config = ConfigDict(protected_namespaces=())


class gltf(BaseModel):
    """Binary glTF 2.0. We refer to this as glTF since that is how our customers refer to it, but this can also import binary glTF (glb)."""

    type: Literal["gltf"] = "gltf"

    model_config = ConfigDict(protected_namespaces=())


class obj(BaseModel):
    """Wavefront OBJ format."""

    coords: System

    type: Literal["obj"] = "obj"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


class ply(BaseModel):
    """The PLY Polygon File Format."""

    coords: System

    type: Literal["ply"] = "ply"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


class sldprt(BaseModel):
    """SolidWorks part (SLDPRT) format."""

    type: Literal["sldprt"] = "sldprt"

    model_config = ConfigDict(protected_namespaces=())


class step(BaseModel):
    """ISO 10303-21 (STEP) format."""

    type: Literal["step"] = "step"

    model_config = ConfigDict(protected_namespaces=())


class stl(BaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    type: Literal["stl"] = "stl"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


InputFormat = RootModel[
    Annotated[
        Union[
            fbx,
            gltf,
            obj,
            ply,
            sldprt,
            step,
            stl,
        ],
        Field(discriminator="type"),
    ]
]
