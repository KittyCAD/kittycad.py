from typing import Any, Dict, Type, TypeVar, Union

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

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


GY = TypeVar("GY", bound="InputFormat")


@attr.s(auto_attribs=True)
class InputFormat:

    """Input format specifier."""

    type: Union[
        fbx,
        gltf,
        obj,
        ply,
        sldprt,
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
            sldprt,
            step,
            stl,
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, fbx):
            JV: fbx = self.type
            return JV.model_dump()
        elif isinstance(self.type, gltf):
            FV: gltf = self.type
            return FV.model_dump()
        elif isinstance(self.type, obj):
            OY: obj = self.type
            return OY.model_dump()
        elif isinstance(self.type, ply):
            TM: ply = self.type
            return TM.model_dump()
        elif isinstance(self.type, sldprt):
            AH: sldprt = self.type
            return AH.model_dump()
        elif isinstance(self.type, step):
            JR: step = self.type
            return JR.model_dump()
        elif isinstance(self.type, stl):
            HK: stl = self.type
            return HK.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "fbx":
            IO: fbx = fbx(**d)
            return cls(type=IO)
        elif d.get("type") == "gltf":
            LE: gltf = gltf(**d)
            return cls(type=LE)
        elif d.get("type") == "obj":
            HO: obj = obj(**d)
            return cls(type=HO)
        elif d.get("type") == "ply":
            BS: ply = ply(**d)
            return cls(type=BS)
        elif d.get("type") == "sldprt":
            EG: sldprt = sldprt(**d)
            return cls(type=EG)
        elif d.get("type") == "step":
            LY: step = step(**d)
            return cls(type=LY)
        elif d.get("type") == "stl":
            VR: stl = stl(**d)
            return cls(type=VR)

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
                    sldprt,
                    step,
                    stl,
                ]
            ),
        )
