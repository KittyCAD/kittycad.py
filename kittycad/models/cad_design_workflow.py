from enum import Enum


class CadDesignWorkflow(str, Enum):
    """Strict design-workflow enum for onboarding/CRM form submissions."""  # noqa: E501

    """# Sketch-first workflow."""  # noqa: E501

    SKETCHING = "sketching"

    """# Code-first workflow."""  # noqa: E501

    CODING = "coding"

    """# AI-first workflow."""  # noqa: E501

    AI = "ai"

    """# Hybrid workflow spanning multiple approaches."""  # noqa: E501

    HYBRID_APPROACH = "hybrid_approach"

    def __str__(self) -> str:
        return str(self.value)
