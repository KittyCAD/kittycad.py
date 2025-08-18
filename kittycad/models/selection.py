from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .base import KittyCadBaseModel


class OptionDefaultScene(KittyCadBaseModel):
    """Visit the default scene."""

    type: Literal["default_scene"] = "default_scene"


class OptionSceneByIndex(KittyCadBaseModel):
    """Visit the indexed scene."""

    index: int

    type: Literal["scene_by_index"] = "scene_by_index"


class OptionSceneByName(KittyCadBaseModel):
    """Visit the first scene with the given name."""

    name: str

    type: Literal["scene_by_name"] = "scene_by_name"


class OptionMeshByIndex(KittyCadBaseModel):
    """Visit the indexed mesh."""

    index: int

    type: Literal["mesh_by_index"] = "mesh_by_index"


class OptionMeshByName(KittyCadBaseModel):
    """Visit the first mesh with the given name."""

    name: str

    type: Literal["mesh_by_name"] = "mesh_by_name"


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
