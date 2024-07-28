import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.modeling_app_individual_subscription_tier import (
    ModelingAppIndividualSubscriptionTier,
)
from .base64data import Base64Data


class ZooProductSubscriptionsUserRequest(BaseModel):
    """A struct of Zoo product subscriptions a user can request."""

    modeling_app: Optional[ModelingAppIndividualSubscriptionTier] = None

    model_config = ConfigDict(protected_namespaces=())
