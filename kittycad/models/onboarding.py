import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict



class Onboarding(BaseModel):
    """Onboarding details"""

    first_call_from_modeling_app_date: Optional[datetime.datetime] = None

    first_call_from_text_to_cad_date: Optional[datetime.datetime] = None

    first_token_date: Optional[datetime.datetime] = None

    model_config = ConfigDict(protected_namespaces=())
