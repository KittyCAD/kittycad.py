from pydantic import BaseModel, ConfigDict

from ..models.solid_info import SolidInfo


class Solid3dGetInfo(BaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces)"""

    info: SolidInfo

    model_config = ConfigDict(protected_namespaces=())
