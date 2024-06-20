from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class LinearTransform(BaseModel):
    """Ways to transform each solid being replicated in a repeating pattern."""

    replicate: Optional[bool] = None

    scale: Optional[Point3d] = None

    translate: Optional[Point3d] = None

    model_config = ConfigDict(protected_namespaces=())
