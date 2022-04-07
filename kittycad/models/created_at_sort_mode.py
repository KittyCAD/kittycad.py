from enum import Enum

class CreatedAtSortMode(str, Enum):
	CREATED-AT-ASCENDING = 'created-at-ascending'
	CREATED-AT-DESCENDING = 'created-at-descending'

	def __str__(self) -> str:
		return str(self.value)
