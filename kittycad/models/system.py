
from pydantic import BaseModel, ConfigDict

from ..models.axis_direction_pair import AxisDirectionPair


class System(BaseModel):
    """Co-ordinate system definition.

    The `up` axis must be orthogonal to the `forward` axis.

    See [cglearn.eu] for background reading.

    [cglearn.eu](https://cglearn.eu/pub/computer-graphics/introduction-to-geometry#material-coordinate-systems-1)
    """

    forward: AxisDirectionPair

    up: AxisDirectionPair

    model_config = ConfigDict(protected_namespaces=())
