from typing import Union

from pydantic import BaseModel, RootModel

from ..models.fbx_storage import FbxStorage
from ..models.gltf_presentation import GltfPresentation
from ..models.gltf_storage import GltfStorage
from ..models.ply_storage import PlyStorage
from ..models.selection import Selection
from ..models.stl_storage import StlStorage
from ..models.system import System
from ..models.unit_length import UnitLength


class fbx(BaseModel):
    """Autodesk Filmbox (FBX) format."""

    storage: FbxStorage

    type: str = "fbx"


class gltf(BaseModel):
    """glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ascii output, you can set that option for the export."""

    presentation: GltfPresentation

    storage: GltfStorage

    type: str = "gltf"


class obj(BaseModel):
    """Wavefront OBJ format."""

    coords: System

    type: str = "obj"

    units: UnitLength


class ply(BaseModel):
    """The PLY Polygon File Format."""

    coords: System

    selection: Selection

    storage: PlyStorage

    type: str = "ply"

    units: UnitLength


class step(BaseModel):
    """ISO 10303-21 (STEP) format."""

    coords: System

    type: str = "step"


class stl(BaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    selection: Selection

    storage: StlStorage

    type: str = "stl"

    units: UnitLength


OutputFormat = RootModel[
    Union[
        fbx,
        gltf,
        obj,
        ply,
        step,
        stl,
    ]
]
