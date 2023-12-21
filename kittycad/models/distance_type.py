from typing import Literal, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from ..models.global_axis import GlobalAxis


class euclidean(BaseModel):
    """Euclidean Distance."""

    type: Literal["euclidean"] = "euclidean"


class on_axis(BaseModel):
    """The distance between objects along the specified axis"""

    axis: GlobalAxis

    type: Literal["on_axis"] = "on_axis"


DistanceType = RootModel[
    Annotated[
        Union[
            euclidean,
            on_axis,
        ],
        Field(discriminator="type"),
    ]
]
