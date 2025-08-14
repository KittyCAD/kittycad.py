from typing import List

from pydantic import BaseModel, ConfigDict


class Solid3dgetalledgefaces(BaseModel):
    """The response from the `Solid3dGetAllEdgeFaces` command."""

    faces: List[str]

    model_config = ConfigDict(protected_namespaces=())
