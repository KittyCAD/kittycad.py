from enum import Enum


class CadIndustry(str, Enum):
    """Strict CAD industry enum for onboarding/CRM form submissions."""  # noqa: E501

    """# Mechanical engineering."""  # noqa: E501

    MECHANICAL_ENGINEERING = "mechanical_engineering"

    """# Manufacturing."""  # noqa: E501

    MANUFACTURING = "manufacturing"

    """# Automotive."""  # noqa: E501

    AUTOMOTIVE = "automotive"

    """# Aerospace."""  # noqa: E501

    AEROSPACE = "aerospace"

    """# Civil engineering."""  # noqa: E501

    CIVIL_ENGINEERING = "civil_engineering"

    """# Electrical engineering."""  # noqa: E501

    ELECTRICAL_ENGINEERING = "electrical_engineering"

    """# Construction."""  # noqa: E501

    CONSTRUCTION = "construction"

    """# Product design."""  # noqa: E501

    PRODUCT_DESIGN = "product_design"

    """# Architecture."""  # noqa: E501

    ARCHITECTURE = "architecture"

    """# Other industry."""  # noqa: E501

    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
