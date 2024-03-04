from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

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

    type: Literal["fbx"] = "fbx"

    model_config = ConfigDict(protected_namespaces=())


class gltf(BaseModel):
    """glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ASCII output, you can set that option for the export."""

    presentation: GltfPresentation

    storage: GltfStorage

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

    selection: Selection

    storage: PlyStorage

    type: Literal["ply"] = "ply"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


class step(BaseModel):
    """ISO 10303-21 (STEP) format."""

    coords: System

    type: Literal["step"] = "step"

    model_config = ConfigDict(protected_namespaces=())


class stl(BaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    selection: Selection

    storage: StlStorage

    type: Literal["stl"] = "stl"

    units: UnitLength

    model_config = ConfigDict(protected_namespaces=())


OutputFormat = RootModel[
    Annotated[
        Union[
            fbx,
            gltf,
            obj,
            ply,
            step,
            stl,
        ],
        Field(discriminator="type"),
    ]
]
