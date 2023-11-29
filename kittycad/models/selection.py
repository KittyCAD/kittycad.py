from typing import Literal, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated



class default_scene(BaseModel):
    """Visit the default scene."""

    type: Literal["default_scene"] = "default_scene"


class scene_by_index(BaseModel):
    """Visit the indexed scene."""

    index: int

    type: Literal["scene_by_index"] = "scene_by_index"


class scene_by_name(BaseModel):
    """Visit the first scene with the given name."""

    name: str

    type: Literal["scene_by_name"] = "scene_by_name"


class mesh_by_index(BaseModel):
    """Visit the indexed mesh."""

    index: int

    type: Literal["mesh_by_index"] = "mesh_by_index"


class mesh_by_name(BaseModel):
    """Visit the first mesh with the given name."""

    name: str

    type: Literal["mesh_by_name"] = "mesh_by_name"


Selection = RootModel[
    Annotated[
        Union[
            default_scene,
            scene_by_index,
            scene_by_name,
            mesh_by_index,
            mesh_by_name,
        ],
        Field(discriminator="type"),
    ]
]
