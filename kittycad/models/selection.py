from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class OptionDefaultScene(BaseModel):
    """Visit the default scene."""

    type: Literal["default_scene"] = "default_scene"

    model_config = ConfigDict(protected_namespaces=())


class OptionSceneByIndex(BaseModel):
    """Visit the indexed scene."""

    index: int

    type: Literal["scene_by_index"] = "scene_by_index"

    model_config = ConfigDict(protected_namespaces=())


class OptionSceneByName(BaseModel):
    """Visit the first scene with the given name."""

    name: str

    type: Literal["scene_by_name"] = "scene_by_name"

    model_config = ConfigDict(protected_namespaces=())


class OptionMeshByIndex(BaseModel):
    """Visit the indexed mesh."""

    index: int

    type: Literal["mesh_by_index"] = "mesh_by_index"

    model_config = ConfigDict(protected_namespaces=())


class OptionMeshByName(BaseModel):
    """Visit the first mesh with the given name."""

    name: str

    type: Literal["mesh_by_name"] = "mesh_by_name"

    model_config = ConfigDict(protected_namespaces=())


Selection = RootModel[
    Annotated[
        Union[
            OptionDefaultScene,
            OptionSceneByIndex,
            OptionSceneByName,
            OptionMeshByIndex,
            OptionMeshByName,
        ],
        Field(discriminator="type"),
    ]
]
