import datetime
from typing import Dict, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

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
from .base64data import Base64Data


class file_conversion(BaseModel):
    """A file conversion."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_format: FileExportFormat

    output_format_options: Optional[OutputFormat] = None

    outputs: Optional[Dict[str, Base64Data]] = None

    src_format: FileImportFormat

    src_format_options: Optional[InputFormat] = None

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["file_conversion"] = "file_conversion"

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())


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

    type: Literal["file_center_of_mass"] = "file_center_of_mass"

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())


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

    type: Literal["file_mass"] = "file_mass"

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())


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

    type: Literal["file_volume"] = "file_volume"

    updated_at: datetime.datetime

    user_id: Uuid

    volume: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())


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

    type: Literal["file_density"] = "file_density"

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())


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

    type: Literal["file_surface_area"] = "file_surface_area"

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())


class text_to_cad(BaseModel):
    """Text to CAD."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[AiFeedback] = None

    id: Uuid

    model_version: str

    output_format: FileExportFormat

    outputs: Optional[Dict[str, Base64Data]] = None

    prompt: str

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["text_to_cad"] = "text_to_cad"

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())


AsyncApiCallOutput = RootModel[
    Annotated[
        Union[
            file_conversion,
            file_center_of_mass,
            file_mass,
            file_volume,
            file_density,
            file_surface_area,
            text_to_cad,
        ],
        Field(discriminator="type"),
    ]
]
