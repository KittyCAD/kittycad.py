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


AnnotationMbdLeaderPosition = RootModel[
    Union[
        NormalizedPos,
        Centroid,
    ]
]
