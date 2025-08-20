from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from .base import KittyCadBaseModel


class ModelingCmdReq(KittyCadBaseModel):
    """A graphics command submitted to the KittyCAD engine via the Modeling API."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId
