import json

from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d
from ..models.rotation import Rotation


class Transform(BaseModel):
    """Ways to transform each solid being replicated in a repeating pattern."""

    replicate: bool = True

    rotation: Rotation = Rotation(
        **json.loads(
            """{'angle': {'unit': 'degrees', 'value': 0.0}, 'axis': {'x': 0.0, 'y': 0.0, 'z': 1.0}, 'origin': {'type': 'local'}}"""
        )
    )

    scale: Point3d = Point3d(**json.loads("""{'x': 1.0, 'y': 1.0, 'z': 1.0}"""))

    translate: Point3d = Point3d(**json.loads("""{'x': 0.0, 'y': 0.0, 'z': 0.0}"""))

    model_config = ConfigDict(protected_namespaces=())
