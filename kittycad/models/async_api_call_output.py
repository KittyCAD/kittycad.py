import datetime
from typing import Any, Dict, Optional, Type, TypeVar, Union

import attr
from pydantic import Base64Bytes, BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from ..models.ai_feedback import AiFeedback
from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.file_import_format import FileImportFormat
from ..models.input_format import InputFormat
from ..models.output_format import OutputFormat
from ..models.point3d import Point3d
from ..models.unit_area import UnitArea
from ..models.unit_density import UnitDensity
from ..models.unit_length import UnitLength
from ..models.unit_mass import UnitMass
from ..models.unit_volume import UnitVolume
from ..models.uuid import Uuid


class file_conversion(BaseModel):
    """A file conversion."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_format: FileExportFormat

    output_format_options: Optional[OutputFormat] = None

    outputs: Optional[Dict[str, Base64Bytes]] = None

    src_format: FileImportFormat

    src_format_options: Optional[InputFormat] = None

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: str = "file_conversion"

    updated_at: datetime.datetime

    user_id: Uuid


class file_center_of_mass(BaseModel):
    """File center of mass."""

    center_of_mass: Optional[Point3d] = None

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_unit: UnitLength

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: str = "file_center_of_mass"

    updated_at: datetime.datetime

    user_id: Uuid


class file_mass(BaseModel):
    """A file mass."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    mass: Optional[float] = None

    material_density: Optional[float] = None

    material_density_unit: UnitDensity

    output_unit: UnitMass

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: str = "file_mass"

    updated_at: datetime.datetime

    user_id: Uuid


class file_volume(BaseModel):
    """A file volume."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_unit: UnitVolume

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: str = "file_volume"

    updated_at: datetime.datetime

    user_id: Uuid

    volume: Optional[float] = None


class file_density(BaseModel):
    """A file density."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    density: Optional[float] = None

    error: Optional[str] = None

    id: Uuid

    material_mass: Optional[float] = None

    material_mass_unit: UnitMass

    output_unit: UnitDensity

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: str = "file_density"

    updated_at: datetime.datetime

    user_id: Uuid


class file_surface_area(BaseModel):
    """A file surface area."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_unit: UnitArea

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    surface_area: Optional[float] = None

    type: str = "file_surface_area"

    updated_at: datetime.datetime

    user_id: Uuid


class text_to_cad(BaseModel):
    """Text to CAD."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[AiFeedback] = None

    id: Uuid

    model_version: str

    output_format: FileExportFormat

    outputs: Optional[Dict[str, Base64Bytes]] = None

    prompt: str

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: str = "text_to_cad"

    updated_at: datetime.datetime

    user_id: Uuid


GY = TypeVar("GY", bound="AsyncApiCallOutput")


@attr.s(auto_attribs=True)
class AsyncApiCallOutput:

    """The output from the async API call."""

    type: Union[
        file_conversion,
        file_center_of_mass,
        file_mass,
        file_volume,
        file_density,
        file_surface_area,
        text_to_cad,
    ]

    def __init__(
        self,
        type: Union[
            file_conversion,
            file_center_of_mass,
            file_mass,
            file_volume,
            file_density,
            file_surface_area,
            text_to_cad,
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, file_conversion):
            SB: file_conversion = self.type
            return SB.model_dump()
        elif isinstance(self.type, file_center_of_mass):
            SA: file_center_of_mass = self.type
            return SA.model_dump()
        elif isinstance(self.type, file_mass):
            PI: file_mass = self.type
            return PI.model_dump()
        elif isinstance(self.type, file_volume):
            FB: file_volume = self.type
            return FB.model_dump()
        elif isinstance(self.type, file_density):
            KC: file_density = self.type
            return KC.model_dump()
        elif isinstance(self.type, file_surface_area):
            LB: file_surface_area = self.type
            return LB.model_dump()
        elif isinstance(self.type, text_to_cad):
            TL: text_to_cad = self.type
            return TL.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "file_conversion":
            NP: file_conversion = file_conversion(**d)
            return cls(type=NP)
        elif d.get("type") == "file_center_of_mass":
            GO: file_center_of_mass = file_center_of_mass(**d)
            return cls(type=GO)
        elif d.get("type") == "file_mass":
            UZ: file_mass = file_mass(**d)
            return cls(type=UZ)
        elif d.get("type") == "file_volume":
            QP: file_volume = file_volume(**d)
            return cls(type=QP)
        elif d.get("type") == "file_density":
            HX: file_density = file_density(**d)
            return cls(type=HX)
        elif d.get("type") == "file_surface_area":
            NE: file_surface_area = file_surface_area(**d)
            return cls(type=NE)
        elif d.get("type") == "text_to_cad":
            MN: text_to_cad = text_to_cad(**d)
            return cls(type=MN)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
                Union[
                    file_conversion,
                    file_center_of_mass,
                    file_mass,
                    file_volume,
                    file_density,
                    file_surface_area,
                    text_to_cad,
                ]
            ),
        )
