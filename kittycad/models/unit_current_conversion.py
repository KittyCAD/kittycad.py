import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_call_status import ApiCallStatus
from ..models.unit_current import UnitCurrent
from ..models.uuid import Uuid
from ..types import UNSET, Unset

OP = TypeVar("OP", bound="UnitCurrentConversion")

@attr.s(auto_attribs=True)
class UnitCurrentConversion:
	""" Result of converting between units. """ # noqa: E501
	completed_at: Union[Unset, datetime.datetime] = UNSET
	created_at: Union[Unset, datetime.datetime] = UNSET
	error: Union[Unset, str] = UNSET
	id: Union[Unset, str] = UNSET
	input:  Union[Unset, float] = UNSET
	input_unit: Union[Unset, UnitCurrent] = UNSET
	output:  Union[Unset, float] = UNSET
	output_unit: Union[Unset, UnitCurrent] = UNSET
	started_at: Union[Unset, datetime.datetime] = UNSET
	status: Union[Unset, ApiCallStatus] = UNSET
	updated_at: Union[Unset, datetime.datetime] = UNSET
	user_id: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		completed_at: Union[Unset, str] = UNSET
		if not isinstance(self.completed_at, Unset):
			completed_at = self.completed_at.isoformat()
		created_at: Union[Unset, str] = UNSET
		if not isinstance(self.created_at, Unset):
			created_at = self.created_at.isoformat()
		error = self.error
		id = self.id
		input = self.input
		if not isinstance(self.input_unit, Unset):
			input_unit = self.input_unit
		output = self.output
		if not isinstance(self.output_unit, Unset):
			output_unit = self.output_unit
		started_at: Union[Unset, str] = UNSET
		if not isinstance(self.started_at, Unset):
			started_at = self.started_at.isoformat()
		if not isinstance(self.status, Unset):
			status = self.status
		updated_at: Union[Unset, str] = UNSET
		if not isinstance(self.updated_at, Unset):
			updated_at = self.updated_at.isoformat()
		user_id = self.user_id

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if completed_at is not UNSET:
			field_dict['completed_at'] = completed_at
		if created_at is not UNSET:
			field_dict['created_at'] = created_at
		if error is not UNSET:
			field_dict['error'] = error
		if id is not UNSET:
			field_dict['id'] = id
		if input is not UNSET:
			field_dict['input'] = input
		if input_unit is not UNSET:
			field_dict['input_unit'] = input_unit
		if output is not UNSET:
			field_dict['output'] = output
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if started_at is not UNSET:
			field_dict['started_at'] = started_at
		if status is not UNSET:
			field_dict['status'] = status
		if updated_at is not UNSET:
			field_dict['updated_at'] = updated_at
		if user_id is not UNSET:
			field_dict['user_id'] = user_id

		return field_dict

	@classmethod
	def from_dict(cls: Type[OP], src_dict: Dict[str, Any]) -> OP:
		d = src_dict.copy()
		_completed_at = d.pop("completed_at", UNSET)
		completed_at: Union[Unset, datetime.datetime]
		if isinstance(_completed_at, Unset):
			completed_at = UNSET
		else:
			completed_at = isoparse(_completed_at)

		_created_at = d.pop("created_at", UNSET)
		created_at: Union[Unset, datetime.datetime]
		if isinstance(_created_at, Unset):
			created_at = UNSET
		else:
			created_at = isoparse(_created_at)

		error = d.pop("error", UNSET)

		_id = d.pop("id", UNSET)
		id: Union[Unset, Uuid]
		if isinstance(_id, Unset):
			id = UNSET
		else:
			id = _id # type: ignore[arg-type]

		input = d.pop("input", UNSET)

		_input_unit = d.pop("input_unit", UNSET)
		input_unit: Union[Unset, UnitCurrent]
		if isinstance(_input_unit, Unset):
			input_unit = UNSET
		else:
			input_unit = _input_unit # type: ignore[arg-type]

		output = d.pop("output", UNSET)

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitCurrent]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		_started_at = d.pop("started_at", UNSET)
		started_at: Union[Unset, datetime.datetime]
		if isinstance(_started_at, Unset):
			started_at = UNSET
		else:
			started_at = isoparse(_started_at)

		_status = d.pop("status", UNSET)
		status: Union[Unset, ApiCallStatus]
		if isinstance(_status, Unset):
			status = UNSET
		else:
			status = _status # type: ignore[arg-type]

		_updated_at = d.pop("updated_at", UNSET)
		updated_at: Union[Unset, datetime.datetime]
		if isinstance(_updated_at, Unset):
			updated_at = UNSET
		else:
			updated_at = isoparse(_updated_at)

		user_id = d.pop("user_id", UNSET)


		unit_current_conversion = cls(
			completed_at= completed_at,
			created_at= created_at,
			error= error,
			id= id,
			input= input,
			input_unit= input_unit,
			output= output,
			output_unit= output_unit,
			started_at= started_at,
			status= status,
			updated_at= updated_at,
			user_id= user_id,
		)

		unit_current_conversion.additional_properties = d
		return unit_current_conversion

	@property
	def additional_keys(self) -> List[str]:
		return list(self.additional_properties.keys())

	def __getitem__(self, key: str) -> Any:
		return self.additional_properties[key]

	def __setitem__(self, key: str, value: Any) -> None:
		self.additional_properties[key] = value

	def __delitem__(self, key: str) -> None:
		del self.additional_properties[key]

	def __contains__(self, key: str) -> bool:
		return key in self.additional_properties
