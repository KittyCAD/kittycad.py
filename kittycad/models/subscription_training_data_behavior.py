from enum import Enum


class SubscriptionTrainingDataBehavior(str, Enum):
    """An enum representing a subscription training data behavior."""  # noqa: E501

    """# The data is always used for training and cannot be turned off. """  # noqa: E501
    ALWAYS = "always"
    """# The data is used for training by default, but can be turned off. """  # noqa: E501
    DEFAULT_ON = "default_on"
    """# The data is not used for training by default, but can be turned on. """  # noqa: E501
    DEFAULT_OFF = "default_off"

    def __str__(self) -> str:
        return str(self.value)
