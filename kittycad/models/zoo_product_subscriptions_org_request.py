import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.modeling_app_organization_subscription_tier import (
    ModelingAppOrganizationSubscriptionTier,
)
from .base64data import Base64Data


class ZooProductSubscriptionsOrgRequest(BaseModel):
    """A struct of Zoo product subscriptions an organization can request."""

    modeling_app: Optional[ModelingAppOrganizationSubscriptionTier] = None

    model_config = ConfigDict(protected_namespaces=())
