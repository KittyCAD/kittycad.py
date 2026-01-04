from typing import Optional, Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.angle import Angle
from ..models.length_unit import LengthUnit
from .base import KittyCadBaseModel


class Fillet(KittyCadBaseModel):
    """Round off an edge."""

    radius: LengthUnit

    second_length: Optional[LengthUnit] = None

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "fillet" in data
            and isinstance(data["fillet"], dict)
        ):
            return data["fillet"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"fillet": payload}


class Chamfer(KittyCadBaseModel):
    """Cut away an edge."""

    angle: Optional[Angle] = None

    distance: LengthUnit

    second_distance: Optional[LengthUnit] = None

    swap: bool

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "chamfer" in data
            and isinstance(data["chamfer"], dict)
        ):
            return data["chamfer"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"chamfer": payload}


class Custom(KittyCadBaseModel):
    """A custom cut profile."""

    path: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "custom" in data
            and isinstance(data["custom"], dict)
        ):
            return data["custom"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"custom": payload}


CutTypeV2 = RootModel[
    Union[
        Fillet,
        Chamfer,
        Custom,
    ]
]
