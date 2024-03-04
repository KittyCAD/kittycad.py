import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.payment_method_card_checks import PaymentMethodCardChecks



class CardDetails(BaseModel):
    """The card details of a payment method."""
    
    
    brand: Optional[str] = None
    
    
    
    checks: Optional[PaymentMethodCardChecks] = None
    
    
    
    country: Optional[str] = None
    
    
    
    exp_month: Optional[int] = None
    
    
    
    exp_year: Optional[int] = None
    
    
    
    fingerprint: Optional[str] = None
    
    
    
    funding: Optional[str] = None
    
    
    
    last4: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )