import datetime
from typing import Dict, List, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.file_import_format import FileImportFormat
from ..models.input_format3d import InputFormat3d
from ..models.ml_feedback import MlFeedback
from ..models.output_format3d import OutputFormat3d
from ..models.point3d import Point3d
from ..models.source_range_prompt import SourceRangePrompt
from ..models.text_to_cad_model import TextToCadModel
from ..models.unit_area import UnitArea
from ..models.unit_density import UnitDensity
from ..models.unit_length import UnitLength
from ..models.unit_mass import UnitMass
from ..models.unit_volume import UnitVolume
from ..models.uuid import Uuid
from .base import KittyCadBaseModel
from .base64data import Base64Data


class OptionFileConversion(KittyCadBaseModel):
    """A file conversion."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_format: FileExportFormat

    output_format_options: Optional[OutputFormat3d] = None

    outputs: Optional[Dict[str, Base64Data]] = None

    src_format: FileImportFormat

    src_format_options: Optional[InputFormat3d] = None

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["file_conversion"] = "file_conversion"

    updated_at: datetime.datetime

    user_id: Uuid


class OptionFileCenterOfMass(KittyCadBaseModel):
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


class OptionFileMass(KittyCadBaseModel):
    """A file mass."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    mass: Optional[float] = None

    material_density: float = 0.0

    material_density_unit: UnitDensity

    output_unit: UnitMass

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["file_mass"] = "file_mass"

    updated_at: datetime.datetime

    user_id: Uuid


class OptionFileVolume(KittyCadBaseModel):
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


class OptionFileDensity(KittyCadBaseModel):
    """A file density."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    density: Optional[float] = None

    error: Optional[str] = None

    id: Uuid

    material_mass: float = 0.0

    material_mass_unit: UnitMass

    output_unit: UnitDensity

    src_format: FileImportFormat

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["file_density"] = "file_density"

    updated_at: datetime.datetime

    user_id: Uuid


class OptionFileSurfaceArea(KittyCadBaseModel):
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


class OptionTextToCad(KittyCadBaseModel):
    """Text to CAD."""

    code: Optional[str] = None

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Uuid

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    kcl_version: Optional[str] = None

    model: TextToCadModel

    model_version: str

    output_format: FileExportFormat

    outputs: Optional[Dict[str, Base64Data]] = None

    prompt: str

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["text_to_cad"] = "text_to_cad"

    updated_at: datetime.datetime

    user_id: Uuid


class OptionTextToCadIteration(KittyCadBaseModel):
    """Text to CAD iteration."""

    code: str

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Uuid

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    model: TextToCadModel

    model_version: str

    original_source_code: str

    prompt: Optional[str] = None

    source_ranges: List[SourceRangePrompt]

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["text_to_cad_iteration"] = "text_to_cad_iteration"

    updated_at: datetime.datetime

    user_id: Uuid


class OptionTextToCadMultiFileIteration(KittyCadBaseModel):
    """Text to CAD multi-file iteration."""

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Uuid

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    kcl_version: Optional[str] = None

    model: TextToCadModel

    model_version: str

    outputs: Optional[Dict[str, str]] = None

    project_name: Optional[str] = None

    prompt: Optional[str] = None

    source_ranges: List[SourceRangePrompt]

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: Literal["text_to_cad_multi_file_iteration"] = (
        "text_to_cad_multi_file_iteration"
    )

    updated_at: datetime.datetime

    user_id: Uuid


AsyncApiCallOutput = RootModel[
    Annotated[
        Union[
            OptionFileConversion,
            OptionFileCenterOfMass,
            OptionFileMass,
            OptionFileVolume,
            OptionFileDensity,
            OptionFileSurfaceArea,
            OptionTextToCad,
            OptionTextToCadIteration,
            OptionTextToCadMultiFileIteration,
        ],
        Field(discriminator="type"),
    ]
]
