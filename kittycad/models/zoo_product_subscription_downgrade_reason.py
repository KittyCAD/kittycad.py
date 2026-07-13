from enum import Enum


class ZooProductSubscriptionDowngradeReason(str, Enum):
    """Customer-selected reason for downgrading an individual subscription."""  # noqa: E501

    """# The subscription price is too expensive for the customer."""  # noqa: E501

    COST_TOO_HIGH = "cost_too_high"

    """# The customer encountered product errors or bugs."""  # noqa: E501

    ERRORS_OR_BUGS = "errors_or_bugs"

    """# The product is missing features the customer needs."""  # noqa: E501

    MISSING_FEATURES = "missing_features"

    """# The customer prefers another AI product."""  # noqa: E501

    ANOTHER_AI_PRODUCT_BETTER = "another_ai_product_better"

    """# The customer is unhappy with Zookeeper output quality."""  # noqa: E501

    ZOOKEEPER_RESULTS_LOW_QUALITY = "zookeeper_results_low_quality"

    """# The customer runs out of reasoning time too quickly."""  # noqa: E501

    REASONING_TIME_RUNS_OUT = "reasoning_time_runs_out"

    """# The product feels too slow for the customer."""  # noqa: E501

    PRODUCT_TOO_SLOW = "product_too_slow"

    """# The customer selected another reason."""  # noqa: E501

    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
