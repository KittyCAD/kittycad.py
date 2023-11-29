from typing import Union

from pydantic import BaseModel, RootModel

from ..models.system import System
from ..models.unit_length import UnitLength


class fbx(BaseModel):
    """Autodesk Filmbox (FBX) format."""

    type: str = "fbx"


class gltf(BaseModel):
    """Binary glTF 2.0. We refer to this as glTF since that is how our customers refer to it, but this can also import binary glTF (glb)."""

    type: str = "gltf"


class obj(BaseModel):
    """Wavefront OBJ format."""

    coords: System

    type: str = "obj"

    units: UnitLength


class ply(BaseModel):
    """The PLY Polygon File Format."""

    coords: System

    type: str = "ply"

    units: UnitLength


class sldprt(BaseModel):
    """SolidWorks part (SLDPRT) format."""

    type: str = "sldprt"


class step(BaseModel):
    """ISO 10303-21 (STEP) format."""

    type: str = "step"


class stl(BaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    type: str = "stl"

    units: UnitLength


InputFormat = RootModel[
    Union[
        fbx,
        gltf,
        obj,
        ply,
        sldprt,
        step,
        stl,
    ]
]
