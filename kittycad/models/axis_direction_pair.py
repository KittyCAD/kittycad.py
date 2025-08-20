from ..models.axis import Axis
from ..models.direction import Direction
from .base import KittyCadBaseModel


class AxisDirectionPair(KittyCadBaseModel):
    """An [`Axis`] paired with a [`Direction`]."""

    axis: Axis

    direction: Direction
