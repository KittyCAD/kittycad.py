from typing import List

from pydantic import BaseModel, ConfigDict



class PathGetCurveUuidsForVertices(BaseModel):
    """The response from the `PathGetCurveUuidsForVertices` command."""

    curve_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
