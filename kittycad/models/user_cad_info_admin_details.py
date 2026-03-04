from typing import Optional

from ..models.cad_discovery_source import CadDiscoverySource
from ..models.cad_industry import CadIndustry
from ..models.cad_user_type import CadUserType
from ..models.company_size import CompanySize
from .base import KittyCadBaseModel


class UserCadInfoAdminDetails(KittyCadBaseModel):
    """CAD user info details for admin surfaces."""

    cad_industry: Optional[CadIndustry] = None

    cad_user_type: Optional[CadUserType] = None

    company_size: Optional[CompanySize] = None

    how_did_you_find_us: Optional[CadDiscoverySource] = None

    how_did_you_find_us_other: Optional[str] = None

    number_of_cad_users: Optional[str] = None
