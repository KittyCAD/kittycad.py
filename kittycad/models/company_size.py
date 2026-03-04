from enum import Enum


class CompanySize(str, Enum):
    """Strict company-size enum for onboarding/CRM form submissions."""  # noqa: E501

    """# 1-10 people."""  # noqa: E501

    ONE_TO_TEN = "one_to_ten"

    """# 11-50 people."""  # noqa: E501

    ELEVEN_TO_FIFTY = "eleven_to_fifty"

    """# 51-200 people."""  # noqa: E501

    FIFTY_ONE_TO_TWO_HUNDRED = "fifty_one_to_two_hundred"

    """# 201-500 people."""  # noqa: E501

    TWO_HUNDRED_ONE_TO_FIVE_HUNDRED = "two_hundred_one_to_five_hundred"

    """# 501-1000 people."""  # noqa: E501

    FIVE_HUNDRED_ONE_TO_ONE_THOUSAND = "five_hundred_one_to_one_thousand"

    """# 1000+ people."""  # noqa: E501

    ONE_THOUSAND_PLUS = "one_thousand_plus"

    """# Other company size."""  # noqa: E501

    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
