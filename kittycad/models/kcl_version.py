from enum import Enum


class KclVersion(str, Enum):
    """Which KCL versions does Zoo support?"""  # noqa: E501

    """# Original KCL released in 2025"""  # noqa: E501

    VAL_1_0 = "1.0"

    """# KCL v2 is the same as KCL v1, except that it supports the `region` function."""  # noqa: E501

    VAL_2_0 = "2.0"

    """# KCL v3 preview -- used while developing version 3."""  # noqa: E501

    VAL_3_0_PREVIEW = "3.0-preview"

    """# KCL v3 releases 2026"""  # noqa: E501

    VAL_3_0 = "3.0"

    """# KCL v4 preview -- used while developing and testing version 4."""  # noqa: E501

    VAL_4_0_PREVIEW = "4.0-preview"

    def __str__(self) -> str:
        return str(self.value)
