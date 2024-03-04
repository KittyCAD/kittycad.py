import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.billing_info import BillingInfo


from ..models.card_details import CardDetails


from ..models.payment_method_type import PaymentMethodType



class PaymentMethod(BaseModel):
    """A payment method."""
    
    
    billing_info: BillingInfo
    
    
    
    card: Optional[CardDetails] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    id: Optional[str] = None
    
    
    
    metadata: Optional[Dict[str, str]] = None
    
    
    
    type: PaymentMethodType
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )