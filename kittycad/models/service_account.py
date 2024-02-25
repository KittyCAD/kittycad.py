import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.uuid import Uuid


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

    token: Uuid

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
