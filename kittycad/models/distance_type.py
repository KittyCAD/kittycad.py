from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.global_axis import GlobalAxis
from .base import KittyCadBaseModel


class OptionEuclidean(KittyCadBaseModel):
    """Euclidean Distance."""

    type: Literal["euclidean"] = "euclidean"


class OptionOnAxis(KittyCadBaseModel):
    """The distance between objects along the specified axis"""

    axis: GlobalAxis

    type: Literal["on_axis"] = "on_axis"


DistanceType = RootModel[
    Annotated[
        Union[
            OptionEuclidean,
            OptionOnAxis,
        ],
        Field(discriminator="type"),
    ]
]
