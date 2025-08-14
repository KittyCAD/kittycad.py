from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.side_face import SideFace


class Extrudedfaceinfo(BaseModel):
    """IDs for the extruded faces."""

    bottom: Optional[str] = None

    sides: List[SideFace]

    top: str

    model_config = ConfigDict(protected_namespaces=())
