from typing import Any, Dict, Type, TypeVar, Union

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

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


GY = TypeVar("GY", bound="OutputFormat")


@attr.s(auto_attribs=True)
class OutputFormat:

    """Output format specifier."""

    type: Union[
        fbx,
        gltf,
        obj,
        ply,
        step,
        stl,
    ]

    def __init__(
        self,
        type: Union[
            fbx,
            gltf,
            obj,
            ply,
            step,
            stl,
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, fbx):
            FC: fbx = self.type
            return FC.model_dump()
        elif isinstance(self.type, gltf):
            EI: gltf = self.type
            return EI.model_dump()
        elif isinstance(self.type, obj):
            JE: obj = self.type
            return JE.model_dump()
        elif isinstance(self.type, ply):
            JW: ply = self.type
            return JW.model_dump()
        elif isinstance(self.type, step):
            AS: step = self.type
            return AS.model_dump()
        elif isinstance(self.type, stl):
            YQ: stl = self.type
            return YQ.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "fbx":
            OA: fbx = fbx(**d)
            return cls(type=OA)
        elif d.get("type") == "gltf":
            CQ: gltf = gltf(**d)
            return cls(type=CQ)
        elif d.get("type") == "obj":
            RD: obj = obj(**d)
            return cls(type=RD)
        elif d.get("type") == "ply":
            KZ: ply = ply(**d)
            return cls(type=KZ)
        elif d.get("type") == "step":
            IU: step = step(**d)
            return cls(type=IU)
        elif d.get("type") == "stl":
            NQ: stl = stl(**d)
            return cls(type=NQ)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
                Union[
                    fbx,
                    gltf,
                    obj,
                    ply,
                    step,
                    stl,
                ]
            ),
        )
