from enum import Enum


class CreatedAtSortMode(str, Enum):
    CREATED_AT_ASCENDING = 'created-at-ascending'
    CREATED_AT_DESCENDING = 'created-at-descending'

    def __str__(self) -> str:
        return str(self.value)
