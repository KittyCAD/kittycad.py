import datetime
from typing import Optional

from pydantic import BaseModel

from ..models.uuid import Uuid


class User(BaseModel):
    """A user."""

    company: Optional[str] = None

    created_at: datetime.datetime

    discord: Optional[str] = None

    email: Optional[str] = None

    email_verified: Optional[datetime.datetime] = None

    first_name: Optional[str] = None

    github: Optional[str] = None

    id: Uuid

    image: str

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    updated_at: datetime.datetime
