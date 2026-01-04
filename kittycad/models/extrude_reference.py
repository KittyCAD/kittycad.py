from typing import Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class EntityReference(KittyCadBaseModel):
    """Extrudes along the normal of the top face until it is as close to the entity as possible. An entity can be a solid, a path, a face, etc."""

    entity_id: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "entity_reference" in data
            and isinstance(data["entity_reference"], dict)
        ):
            return data["entity_reference"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"entity_reference": payload}


class Axis(KittyCadBaseModel):
    """Extrudes until the top face is as close as possible to this given axis."""

    axis: Point3d

    point: Point3d = {"x": 0.0, "y": 0.0, "z": 0.0}  # type: ignore[assignment]

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


class Point(KittyCadBaseModel):
    """Extrudes until the top face is as close as possible to this given point."""

    point: Point3d

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "point" in data
            and isinstance(data["point"], dict)
        ):
            return data["point"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"point": payload}


ExtrudeReference = RootModel[
    Union[
        EntityReference,
        Axis,
        Point,
    ]
]
