import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.axis_direction_pair import AxisDirectionPair
from .base64data import Base64Data


class System(BaseModel):
    """Co-ordinate system definition.

    The `up` axis must be orthogonal to the `forward` axis.

    See [cglearn.eu] for background reading.

    [cglearn.eu](https://cglearn.eu/pub/computer-graphics/introduction-to-geometry#material-coordinate-systems-1)
    """

    forward: AxisDirectionPair

    up: AxisDirectionPair

    model_config = ConfigDict(protected_namespaces=())
