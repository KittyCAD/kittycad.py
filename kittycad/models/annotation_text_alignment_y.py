from enum import Enum


class AnnotationTextAlignmentY(str, Enum):
	""" Vertical Text aligment """ # noqa: E501
	BOTTOM = 'bottom'
	CENTER = 'center'
	TOP = 'top'

	def __str__(self) -> str:
		return str(self.value)
