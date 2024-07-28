import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.modeling_app_subscription_tier import ModelingAppSubscriptionTier
from .base64data import Base64Data


class ZooProductSubscriptions(BaseModel):
    """A struct of Zoo product subscriptions."""

    modeling_app: ModelingAppSubscriptionTier

    model_config = ConfigDict(protected_namespaces=())
