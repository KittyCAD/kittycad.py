from typing import Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.system import System
from ..models.unit_length import UnitLength
from .base import KittyCadBaseModel


class OptionAcis(KittyCadBaseModel):
    """ACIS part format."""

    coords: Optional[System] = {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["acis"] = "acis"


class OptionCatia(KittyCadBaseModel):
    """CATIA part format."""

    coords: Optional[System] = {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["catia"] = "catia"


class OptionCreo(KittyCadBaseModel):
    """PTC Creo part format."""

    coords: Optional[System] = {
        "forward": {"axis": "z", "direction": "positive"},
        "up": {"axis": "y", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["creo"] = "creo"


class OptionFbx(KittyCadBaseModel):
    """Autodesk Filmbox (FBX) format."""

    type: Literal["fbx"] = "fbx"


class OptionGltf(KittyCadBaseModel):
    """Binary glTF 2.0. We refer to this as glTF since that is how our customers refer to it, but this can also import binary glTF (glb)."""

    type: Literal["gltf"] = "gltf"


class OptionInventor(KittyCadBaseModel):
    """Autodesk Inventor part format."""

    coords: Optional[System] = {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["inventor"] = "inventor"


class OptionNx(KittyCadBaseModel):
    """Siemens NX part format."""

    coords: Optional[System] = {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["nx"] = "nx"


class OptionObj(KittyCadBaseModel):
    """Wavefront OBJ format."""

    coords: System

    type: Literal["obj"] = "obj"

    units: UnitLength


class OptionParasolid(KittyCadBaseModel):
    """Parasolid part format."""

    coords: Optional[System] = {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["parasolid"] = "parasolid"


class OptionPly(KittyCadBaseModel):
    """The PLY Polygon File Format."""

    coords: System

    type: Literal["ply"] = "ply"

    units: UnitLength


class OptionSldprt(KittyCadBaseModel):
    """SolidWorks part (SLDPRT) format."""

    coords: Optional[System] = {
        "forward": {"axis": "z", "direction": "positive"},
        "up": {"axis": "y", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["sldprt"] = "sldprt"


class OptionStep(KittyCadBaseModel):
    """ISO 10303-21 (STEP) format."""

    coords: Optional[System] = {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }  # type: ignore[assignment]

    split_closed_faces: Optional[bool] = False

    type: Literal["step"] = "step"


class OptionStl(KittyCadBaseModel):
    """*ST**ereo**L**ithography format."""

    coords: System

    type: Literal["stl"] = "stl"

    units: UnitLength


InputFormat3d = RootModel[
    Annotated[
        Union[
            OptionAcis,
            OptionCatia,
            OptionCreo,
            OptionFbx,
            OptionGltf,
            OptionInventor,
            OptionNx,
            OptionObj,
            OptionParasolid,
            OptionPly,
            OptionSldprt,
            OptionStep,
            OptionStl,
        ],
        Field(discriminator="type"),
    ]
]
