from typing import Any, Dict, Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.point2d import Point2d
from .base import KittyCadBaseModel


class NormalizedPos(KittyCadBaseModel):
    """Normalized position within the entity to position the annotation leader from"""

    pos: Point2d

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):

        if (
            isinstance(data, dict)
            and "normalized_pos" in data
            and isinstance(data["normalized_pos"], dict)
        ):
            return data["normalized_pos"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):

        payload = handler(self, info)

        return {"normalized_pos": payload}


class Centroid(KittyCadBaseModel):
    """Geometric Center of the entity (such as on the center axis for a cylinder)"""

    centroid: Dict[str, Any]


class StepFrom(KittyCadBaseModel):
    """Used in dimension measurements for the to_entity_leader_pos field. Determines the position using the previous \"from\" position stepped back (projected) onto the planar entity (via planar projection or vector dot product)"""

    step_from: Dict[str, Any]


class Auto(KittyCadBaseModel):
    """Used in dimension measurements for the to_entity_leader_pos field. Automatically determines which type of leader position to use. If the entity is planar and this is a to_entity_leader_pos dimension field, then StepFrom is used. If the entity is circular or cylindrical, Centroid is used. If the entity is a linear edge NormalizedPos { 0.5, N/A } is used If no other cases apply, then NormalizedPos { 0.5, 0.5 } is used"""

    auto: Dict[str, Any]


AnnotationMbdLeaderPosition = RootModel[
    Union[
        NormalizedPos,
        Centroid,
        StepFrom,
        Auto,
    ]
]
