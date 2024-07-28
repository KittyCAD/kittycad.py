import datetime
from typing import Any, Dict, List, Literal, Optional, Type, TypeVar, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict, Field, RootModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing_extensions import Annotated

from ..models.global_axis import GlobalAxis
from .base64data import Base64Data


class euclidean(BaseModel):
    """Euclidean Distance."""

    type: Literal["euclidean"] = "euclidean"

    model_config = ConfigDict(protected_namespaces=())


class on_axis(BaseModel):
    """The distance between objects along the specified axis"""

    axis: GlobalAxis

    type: Literal["on_axis"] = "on_axis"

    model_config = ConfigDict(protected_namespaces=())


DistanceType = RootModel[
    Annotated[
        Union[
            euclidean,
            on_axis,
        ],
        Field(discriminator="type"),
    ]
]
