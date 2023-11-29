
from pydantic import BaseModel

from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId


class ModelingCmdReq(BaseModel):
    """A graphics command submitted to the KittyCAD engine via the Modeling API."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId
