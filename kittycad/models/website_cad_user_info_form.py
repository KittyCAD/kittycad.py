from typing import Optional

from ..models.cad_design_workflow import CadDesignWorkflow
from ..models.cad_discovery_source import CadDiscoverySource
from ..models.cad_experience_level import CadExperienceLevel
from ..models.cad_industry import CadIndustry
from ..models.cad_user_type import CadUserType
from ..models.company_size import CompanySize
from .base import KittyCadBaseModel


class WebsiteCadUserInfoForm(KittyCadBaseModel):
    """Request body for authenticated website CAD user info form submissions."""

    cad_experience_level: Optional[CadExperienceLevel] = None

    cad_industry: Optional[CadIndustry] = None

    cad_user_type: Optional[CadUserType] = None

    company_size: Optional[CompanySize] = None

    design_workflow: Optional[CadDesignWorkflow] = None

    has_used_zoo_design_studio_or_api_before: Optional[bool] = None

    how_did_you_find_us: Optional[CadDiscoverySource] = None

    how_did_you_find_us_other: Optional[str] = None

    location_city: Optional[str] = None

    location_country: Optional[str] = None

    location_state: Optional[str] = None

    number_of_cad_users: Optional[str] = None

    what_are_you_building: Optional[str] = None
