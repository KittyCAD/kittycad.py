from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.complementary_edges import ComplementaryEdges


class SolidInfo(BaseModel):
    """Solid info struct (useful for maintaining mappings between edges and faces and adjacent/opposite edges)."""

    bottom_cap_id: Optional[str] = None

    common_edges: Dict[str, List[str]]

    complementary_edges: Dict[str, ComplementaryEdges]

    top_cap_id: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
