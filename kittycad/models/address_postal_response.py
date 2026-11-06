from .base import KittyCadBaseModel


class AddressPostalResponse(KittyCadBaseModel):
    """Postal fields as stored, including incomplete historical billing addresses."""

    city: str

    country: str

    state: str

    street1: str

    street2: str

    zip: str
