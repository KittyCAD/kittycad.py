from typing import Optional

from pydantic import BaseModel



class Onboarding(BaseModel):
    """Onboarding details"""

    first_call_from_modeling_app_date: Optional[str] = None

    first_call_from_text_to_cad_date: Optional[str] = None

    first_call_from_their_machine_date: Optional[str] = None

    first_litterbox_execute_date: Optional[str] = None

    first_token_date: Optional[str] = None
