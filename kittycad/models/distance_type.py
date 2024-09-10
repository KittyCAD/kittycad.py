from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.global_axis import GlobalAxis


class OptionEuclidean(BaseModel):
    """Euclidean Distance."""

    type: Literal["option_euclidean"] = "option_euclidean"

    model_config = ConfigDict(protected_namespaces=())


class OptionOnAxis(BaseModel):
    """The distance between objects along the specified axis"""

    axis: GlobalAxis

    type: Literal["option_on_axis"] = "option_on_axis"

    model_config = ConfigDict(protected_namespaces=())


DistanceType = RootModel[
    Annotated[
        Union[
            OptionEuclidean,
            OptionOnAxis,
        ],
        Field(discriminator="type"),
    ]
]
