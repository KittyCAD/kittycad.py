import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.currency import Currency



class InvoiceLineItem(BaseModel):
    """An invoice line item."""
    
    
    amount: Optional[float] = None
    
    
    
    currency: Optional[Currency] = None
    
    
    
    description: Optional[str] = None
    
    
    
    id: Optional[str] = None
    
    
    
    invoice_item: Optional[str] = None
    
    
    
    metadata: Optional[Dict[str, str]] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )