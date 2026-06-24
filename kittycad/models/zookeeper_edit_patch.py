from typing import List, Optional

from ..models.zookeeper_edit_patch_file import ZookeeperEditPatchFile
from .base import KittyCadBaseModel


class ZookeeperEditPatch(KittyCadBaseModel):
    """Local replay data for a single successful Zookeeper project edit."""

    changed_files: Optional[List[ZookeeperEditPatchFile]] = None

    run_id: str
