
from pydantic import BaseModel

from ..models.axis import Axis
from ..models.direction import Direction


class AxisDirectionPair(BaseModel):
    """An [`Axis`] paired with a [`Direction`]."""

    axis: Axis

    direction: Direction
