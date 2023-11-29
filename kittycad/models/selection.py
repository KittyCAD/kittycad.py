from typing import Any, Dict, Type, TypeVar, Union

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema



class default_scene(BaseModel):
    """Visit the default scene."""

    type: str = "default_scene"


class scene_by_index(BaseModel):
    """Visit the indexed scene."""

    index: int

    type: str = "scene_by_index"


class scene_by_name(BaseModel):
    """Visit the first scene with the given name."""

    name: str

    type: str = "scene_by_name"


class mesh_by_index(BaseModel):
    """Visit the indexed mesh."""

    index: int

    type: str = "mesh_by_index"


class mesh_by_name(BaseModel):
    """Visit the first mesh with the given name."""

    name: str

    type: str = "mesh_by_name"


GY = TypeVar("GY", bound="Selection")


@attr.s(auto_attribs=True)
class Selection:

    """Data item selection."""

    type: Union[
        default_scene,
        scene_by_index,
        scene_by_name,
        mesh_by_index,
        mesh_by_name,
    ]

    def __init__(
        self,
        type: Union[
            default_scene,
            scene_by_index,
            scene_by_name,
            mesh_by_index,
            mesh_by_name,
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, default_scene):
            JO: default_scene = self.type
            return JO.model_dump()
        elif isinstance(self.type, scene_by_index):
            TE: scene_by_index = self.type
            return TE.model_dump()
        elif isinstance(self.type, scene_by_name):
            WY: scene_by_name = self.type
            return WY.model_dump()
        elif isinstance(self.type, mesh_by_index):
            QV: mesh_by_index = self.type
            return QV.model_dump()
        elif isinstance(self.type, mesh_by_name):
            BP: mesh_by_name = self.type
            return BP.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "default_scene":
            OF: default_scene = default_scene(**d)
            return cls(type=OF)
        elif d.get("type") == "scene_by_index":
            OV: scene_by_index = scene_by_index(**d)
            return cls(type=OV)
        elif d.get("type") == "scene_by_name":
            FK: scene_by_name = scene_by_name(**d)
            return cls(type=FK)
        elif d.get("type") == "mesh_by_index":
            PE: mesh_by_index = mesh_by_index(**d)
            return cls(type=PE)
        elif d.get("type") == "mesh_by_name":
            FP: mesh_by_name = mesh_by_name(**d)
            return cls(type=FP)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
                Union[
                    default_scene,
                    scene_by_index,
                    scene_by_name,
                    mesh_by_index,
                    mesh_by_name,
                ]
            ),
        )
