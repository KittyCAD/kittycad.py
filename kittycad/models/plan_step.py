from .base import KittyCadBaseModel


class PlanStep(KittyCadBaseModel):
    """A step in the design plan."""

    edit_instructions: str

    filepath_to_edit: str
