from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.curve_get_control_points import CurveGetControlPoints
from ...models.curve_get_type import CurveGetType
from ...models.empty import Empty
from ...models.entity_get_all_child_uuids import EntityGetAllChildUuids
from ...models.entity_get_child_uuid import EntityGetChildUuid
from ...models.entity_get_num_children import EntityGetNumChildren
from ...models.entity_get_parent_id import EntityGetParentId
from ...models.error import Error
from ...models.export import Export
from ...models.get_entity_type import GetEntityType
from ...models.highlight_set_entity import HighlightSetEntity
from ...models.modeling_cmd_req import ModelingCmdReq
from ...models.mouse_click import MouseClick
from ...models.path_get_info import PathGetInfo
from ...models.select_get import SelectGet
from ...models.select_with_point import SelectWithPoint
from ...models.solid3d_get_all_edge_faces import Solid3dGetAllEdgeFaces
from ...models.solid3d_get_all_opposite_edges import Solid3dGetAllOppositeEdges
from ...models.solid3d_get_next_adjacent_edge import Solid3dGetNextAdjacentEdge
from ...models.solid3d_get_opposite_edge import Solid3dGetOppositeEdge
from ...models.solid3d_get_prev_adjacent_edge import Solid3dGetPrevAdjacentEdge
from ...models.take_snapshot import TakeSnapshot
from ...types import Response


def _get_kwargs(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/modeling/cmd".format(
        client.base_url,
    )  # noqa: E501

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "content": body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[
        Empty,
        Export,
        SelectWithPoint,
        HighlightSetEntity,
        EntityGetChildUuid,
        EntityGetNumChildren,
        EntityGetParentId,
        EntityGetAllChildUuids,
        SelectGet,
        GetEntityType,
        Solid3dGetAllEdgeFaces,
        Solid3dGetAllOppositeEdges,
        Solid3dGetOppositeEdge,
        Solid3dGetPrevAdjacentEdge,
        Solid3dGetNextAdjacentEdge,
        MouseClick,
        CurveGetType,
        CurveGetControlPoints,
        TakeSnapshot,
        PathGetInfo,
        Error,
    ]
]:
    if response.status_code == 200:
        data = response.json()
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_empty = Empty.from_dict(data)
            return option_empty
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_export = Export.from_dict(data)
            return option_export
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_select_with_point = SelectWithPoint.from_dict(data)
            return option_select_with_point
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_highlight_set_entity = HighlightSetEntity.from_dict(data)
            return option_highlight_set_entity
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_entity_get_child_uuid = EntityGetChildUuid.from_dict(data)
            return option_entity_get_child_uuid
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_entity_get_num_children = EntityGetNumChildren.from_dict(data)
            return option_entity_get_num_children
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_entity_get_parent_id = EntityGetParentId.from_dict(data)
            return option_entity_get_parent_id
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_entity_get_all_child_uuids = EntityGetAllChildUuids.from_dict(data)
            return option_entity_get_all_child_uuids
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_select_get = SelectGet.from_dict(data)
            return option_select_get
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_get_entity_type = GetEntityType.from_dict(data)
            return option_get_entity_type
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_solid3d_get_all_edge_faces = Solid3dGetAllEdgeFaces.from_dict(data)
            return option_solid3d_get_all_edge_faces
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_solid3d_get_all_opposite_edges = (
                Solid3dGetAllOppositeEdges.from_dict(data)
            )
            return option_solid3d_get_all_opposite_edges
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_solid3d_get_opposite_edge = Solid3dGetOppositeEdge.from_dict(data)
            return option_solid3d_get_opposite_edge
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_solid3d_get_prev_adjacent_edge = (
                Solid3dGetPrevAdjacentEdge.from_dict(data)
            )
            return option_solid3d_get_prev_adjacent_edge
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_solid3d_get_next_adjacent_edge = (
                Solid3dGetNextAdjacentEdge.from_dict(data)
            )
            return option_solid3d_get_next_adjacent_edge
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_mouse_click = MouseClick.from_dict(data)
            return option_mouse_click
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_curve_get_type = CurveGetType.from_dict(data)
            return option_curve_get_type
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_curve_get_control_points = CurveGetControlPoints.from_dict(data)
            return option_curve_get_control_points
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_take_snapshot = TakeSnapshot.from_dict(data)
            return option_take_snapshot
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            if not isinstance(data, dict):
                raise TypeError()
            option_path_get_info = PathGetInfo.from_dict(data)
            return option_path_get_info
        except ValueError:
            raise
        except TypeError:
            raise
    if response.status_code == 400:
        response_4XX = Error.from_dict(response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error.from_dict(response.json())
        return response_5XX
    return Error.from_dict(response.json())


def _build_response(
    *, response: httpx.Response
) -> Response[
    Optional[
        Union[
            Empty,
            Export,
            SelectWithPoint,
            HighlightSetEntity,
            EntityGetChildUuid,
            EntityGetNumChildren,
            EntityGetParentId,
            EntityGetAllChildUuids,
            SelectGet,
            GetEntityType,
            Solid3dGetAllEdgeFaces,
            Solid3dGetAllOppositeEdges,
            Solid3dGetOppositeEdge,
            Solid3dGetPrevAdjacentEdge,
            Solid3dGetNextAdjacentEdge,
            MouseClick,
            CurveGetType,
            CurveGetControlPoints,
            TakeSnapshot,
            PathGetInfo,
            Error,
        ]
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Response[
    Optional[
        Union[
            Empty,
            Export,
            SelectWithPoint,
            HighlightSetEntity,
            EntityGetChildUuid,
            EntityGetNumChildren,
            EntityGetParentId,
            EntityGetAllChildUuids,
            SelectGet,
            GetEntityType,
            Solid3dGetAllEdgeFaces,
            Solid3dGetAllOppositeEdges,
            Solid3dGetOppositeEdge,
            Solid3dGetPrevAdjacentEdge,
            Solid3dGetNextAdjacentEdge,
            MouseClick,
            CurveGetType,
            CurveGetControlPoints,
            TakeSnapshot,
            PathGetInfo,
            Error,
        ]
    ]
]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Optional[
    Union[
        Empty,
        Export,
        SelectWithPoint,
        HighlightSetEntity,
        EntityGetChildUuid,
        EntityGetNumChildren,
        EntityGetParentId,
        EntityGetAllChildUuids,
        SelectGet,
        GetEntityType,
        Solid3dGetAllEdgeFaces,
        Solid3dGetAllOppositeEdges,
        Solid3dGetOppositeEdge,
        Solid3dGetPrevAdjacentEdge,
        Solid3dGetNextAdjacentEdge,
        MouseClick,
        CurveGetType,
        CurveGetControlPoints,
        TakeSnapshot,
        PathGetInfo,
        Error,
    ]
]:
    """Response depends on which command was submitted, so unfortunately the OpenAPI schema can't generate the right response type."""  # noqa: E501

    return sync_detailed(
        body=body,
        client=client,
    ).parsed


async def asyncio_detailed(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Response[
    Optional[
        Union[
            Empty,
            Export,
            SelectWithPoint,
            HighlightSetEntity,
            EntityGetChildUuid,
            EntityGetNumChildren,
            EntityGetParentId,
            EntityGetAllChildUuids,
            SelectGet,
            GetEntityType,
            Solid3dGetAllEdgeFaces,
            Solid3dGetAllOppositeEdges,
            Solid3dGetOppositeEdge,
            Solid3dGetPrevAdjacentEdge,
            Solid3dGetNextAdjacentEdge,
            MouseClick,
            CurveGetType,
            CurveGetControlPoints,
            TakeSnapshot,
            PathGetInfo,
            Error,
        ]
    ]
]:
    kwargs = _get_kwargs(
        body=body,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    body: ModelingCmdReq,
    *,
    client: Client,
) -> Optional[
    Union[
        Empty,
        Export,
        SelectWithPoint,
        HighlightSetEntity,
        EntityGetChildUuid,
        EntityGetNumChildren,
        EntityGetParentId,
        EntityGetAllChildUuids,
        SelectGet,
        GetEntityType,
        Solid3dGetAllEdgeFaces,
        Solid3dGetAllOppositeEdges,
        Solid3dGetOppositeEdge,
        Solid3dGetPrevAdjacentEdge,
        Solid3dGetNextAdjacentEdge,
        MouseClick,
        CurveGetType,
        CurveGetControlPoints,
        TakeSnapshot,
        PathGetInfo,
        Error,
    ]
]:
    """Response depends on which command was submitted, so unfortunately the OpenAPI schema can't generate the right response type."""  # noqa: E501

    return (
        await asyncio_detailed(
            body=body,
            client=client,
        )
    ).parsed
