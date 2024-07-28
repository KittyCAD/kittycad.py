import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.string_uuid import StringUuid
from ..models.uuid import Uuid
from .base64data import Base64Data


class ServiceAccount(BaseModel):
    """A service account.

    These are used to authenticate orgs with Bearer authentication.

    This works just like an API token, but it is tied to an organization versus an individual user.
    """

    created_at: datetime.datetime

    id: Uuid

    is_valid: bool

    label: Optional[str] = None

    org_id: Uuid

    token: StringUuid

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
