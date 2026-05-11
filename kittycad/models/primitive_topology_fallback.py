from .base import KittyCadBaseModel


class PrimitiveTopologyFallback(KittyCadBaseModel):
    """Optional fallback when primary UUIDs are missing from the client artifact graph (e.g. stale or engine-only ids). Identifies the same topology via a **parent** entity UUID and a **primitive index** on that parent.

    Semantics by selection kind (aligned with engine BREP topology):

    - **Face / Edge (3D)**: `parent_id` is the owning [`EntityType::Solid3D`] body UUID; `primitive_index` matches the index returned by **EntityGetPrimitiveIndex** for that face or edge (and matches **EntityGetParentId** → parent + **EntityGetPrimitiveIndex** → index). - **Vertex (3D)**: same `parent_id` (solid); `primitive_index` is the BREP vertex index on that solid. - **Solid2dEdge**: `parent_id` is the **Solid2D** profile UUID; `primitive_index` is the curve index within that profile. - **Segment**: `parent_id` is the **Path** UUID; `primitive_index` is the curve index within that path.

    Other [`EntityReference`] variants may omit this field or leave it unset when not applicable."""

    parent_id: str

    primitive_index: int
