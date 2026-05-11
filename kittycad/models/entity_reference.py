from typing import List, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.primitive_topology_fallback import PrimitiveTopologyFallback
from .base import KittyCadBaseModel


class OptionPlane(KittyCadBaseModel):
    """A uuid referencing a plane."""

    plane_id: str

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["plane"] = "plane"


class OptionFace(KittyCadBaseModel):
    """A uuid referencing a face."""

    face_id: str

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["face"] = "face"


class OptionEdge(KittyCadBaseModel):
    """A collection of ids that uniquely identify an edge."""

    end_faces: Optional[List[str]] = None

    index: Optional[int] = None

    side_faces: List[str]

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["edge"] = "edge"


class OptionVertex(KittyCadBaseModel):
    """A collection of ids that uniquely identify an vertex."""

    index: Optional[int] = None

    side_faces: List[str]

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["vertex"] = "vertex"


class OptionSolid2d(KittyCadBaseModel):
    """A uuid referencing a solid2d (profile)."""

    solid2d_id: str

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["solid2d"] = "solid2d"


class OptionSolid3d(KittyCadBaseModel):
    """A uuid referencing a solid3d (body)."""

    solid3d_id: str

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["solid3d"] = "solid3d"


class OptionSolid2dEdge(KittyCadBaseModel):
    """A uuid referencing an edge on a solid2d (profile) - used for raw sketch/profile edges. This is distinct from the face-based Edge reference which is used for BRep/swept body edges."""

    edge_id: str

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["solid2d_edge"] = "solid2d_edge"


class OptionSegment(KittyCadBaseModel):
    """A single segment (curve) within a path."""

    path_id: str

    segment_id: str

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["segment"] = "segment"


class OptionRegion(KittyCadBaseModel):
    """A closed sketch region/profile area."""

    region_id: str

    topology_fallback: Optional[PrimitiveTopologyFallback] = None

    type: Literal["region"] = "region"


EntityReference = RootModel[
    Annotated[
        Union[
            OptionPlane,
            OptionFace,
            OptionEdge,
            OptionVertex,
            OptionSolid2d,
            OptionSolid3d,
            OptionSolid2dEdge,
            OptionSegment,
            OptionRegion,
        ],
        Field(discriminator="type"),
    ]
]
