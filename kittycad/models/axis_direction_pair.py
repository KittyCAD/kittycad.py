from pydantic import BaseModel, ConfigDict

from ..models.axis import Axis
from ..models.direction import Direction


class Axisdirectionpair(BaseModel):
    """An [`Axis`] paired with a [`Direction`]."""

    axis: Axis

    direction: Direction

    model_config = ConfigDict(protected_namespaces=())
