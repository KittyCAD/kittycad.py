from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class Projectpointstoplane(BaseModel):
    """The response from the `ProjectPointsToPlane` command."""

    projected_points: List[Point3d]

    model_config = ConfigDict(protected_namespaces=())
