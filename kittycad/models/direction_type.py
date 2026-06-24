from typing import Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class Edge(KittyCadBaseModel):
    """Uses the direction of an edge, if linear"""

    id: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if isinstance(data, dict) and "edge" in data and isinstance(data["edge"], dict):
            return data["edge"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"edge": payload}


class Axis(KittyCadBaseModel):
    """Uses the provided vector as the direction."""

    direction: Point3d

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if isinstance(data, dict) and "axis" in data and isinstance(data["axis"], dict):
            return data["axis"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"axis": payload}


DirectionType = RootModel[
    Union[
        Edge,
        Axis,
    ]
]
