from .base import KittyCadBaseModel


class FactoryCustomerJobFile(KittyCadBaseModel):
    """Minimized submitted-file metadata, without Project identifiers or storage locations."""

    download_url: str

    file_name: str
