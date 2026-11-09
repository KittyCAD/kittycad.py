import datetime
from typing import Dict, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.fbx_storage import FbxStorage
from ..models.gltf_presentation import GltfPresentation
from ..models.gltf_storage import GltfStorage
from ..models.named_view import NamedView
from ..models.ply_storage import PlyStorage
from ..models.selection import Selection
from ..models.step_presentation import StepPresentation
from ..models.step_schema import StepSchema
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

    include_uuids: Optional[bool] = False

    presentation: Optional[GltfPresentation] = "pretty"  # type: ignore[assignment]

    storage: Optional[GltfStorage] = "embedded"  # type: ignore[assignment]

    type: Literal["gltf"] = "gltf"

    views: Optional[Dict[str, NamedView]] = None


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

    coords: Optional[System] = {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }  # type: ignore[assignment]

    created: Optional[datetime.datetime] = None

    presentation: Optional[StepPresentation] = "pretty"  # type: ignore[assignment]

    schema_: Optional[StepSchema] = Field(default="ap242", alias="schema")  # type: ignore[assignment]

    type: Literal["step"] = "step"

    units: Optional[UnitLength] = "m"  # type: ignore[assignment]

    views: Optional[Dict[str, NamedView]] = None


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
