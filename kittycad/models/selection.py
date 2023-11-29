from typing import Union

from pydantic import BaseModel, RootModel



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


Selection = RootModel[
    Union[
        default_scene,
        scene_by_index,
        scene_by_name,
        mesh_by_index,
        mesh_by_name,
    ]
]
