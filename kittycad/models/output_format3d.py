import datetime
from typing import Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.fbx_storage import FbxStorage
from ..models.gltf_presentation import GltfPresentation
from ..models.gltf_storage import GltfStorage
from ..models.ply_storage import PlyStorage
from ..models.selection import Selection
from ..models.stl_storage import StlStorage
from ..models.system import System
from ..models.unit_length import UnitLength
from .base import KittyCadBaseModel


class OptionFbx(KittyCadBaseModel):
    """Autodesk Filmbox (FBX) format."""

    created: Optional[datetime.datetime] = None

    storage: FbxStorage

    type: Literal["fbx"] = "fbx"


class OptionGltf(KittyCadBaseModel):
    """glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ASCII output, you can set that option for the export."""

    presentation: GltfPresentation

    storage: GltfStorage

    type: Literal["gltf"] = "gltf"


class OptionObj(KittyCadBaseModel):
    """Wavefront OBJ format."""

    coords: System

    type: Literal["obj"] = "obj"

    units: UnitLength


class OptionPly(KittyCadBaseModel):
    """The PLY Polygon File Format."""

    coords: System

    selection: Selection

    storage: PlyStorage

    type: Literal["ply"] = "ply"

    units: UnitLength


class OptionStep(KittyCadBaseModel):
    """ISO 10303-21 (STEP) format."""

    coords: System

    created: Optional[datetime.datetime] = None

    type: Literal["step"] = "step"


class OptionStl(KittyCadBaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    selection: Selection

    storage: StlStorage

    type: Literal["stl"] = "stl"

    units: UnitLength


OutputFormat3d = RootModel[
    Annotated[
        Union[
            OptionFbx,
            OptionGltf,
            OptionObj,
            OptionPly,
            OptionStep,
            OptionStl,
        ],
        Field(discriminator="type"),
    ]
]
