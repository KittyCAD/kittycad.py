from typing import Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class Edge(KittyCadBaseModel):
    """Reflect across an edge If used with a 3D mirror, the edge will define the normal of the mirror plane."""

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
    """Reflect across an axis (that goes through a point) If used with a 3D mirror, the axis will define the normal of the mirror plane."""

    axis: Point3d

    point: Point3d

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


class Plane(KittyCadBaseModel):
    """Reflect across a plane (which gives two axes) Cannot be used with 2D mirrors."""

    id: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "plane" in data
            and isinstance(data["plane"], dict)
        ):
            return data["plane"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"plane": payload}


MirrorAcross = RootModel[
    Union[
        Edge,
        Axis,
        Plane,
    ]
]
