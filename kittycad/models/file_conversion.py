import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_call_status import ApiCallStatus
from ..models.base64data import Base64Data
from ..models.file_export_format import FileExportFormat
from ..models.file_import_format import FileImportFormat
from ..models.input_format import InputFormat
from ..models.output_format import OutputFormat
from ..models.uuid import Uuid
from ..types import UNSET, Unset

LK = TypeVar("LK", bound="FileConversion")

@attr.s(auto_attribs=True)
class FileConversion:
	""" A file conversion. """ # noqa: E501
	completed_at: Union[Unset, datetime.datetime] = UNSET
	created_at: Union[Unset, datetime.datetime] = UNSET
	error: Union[Unset, str] = UNSET
	id: Union[Unset, str] = UNSET
	output_format: Union[Unset, FileExportFormat] = UNSET
	output_format_options: Union[Unset, OutputFormat] = UNSET
	outputs: Union[Unset, Dict[str, Base64Data]] = UNSET
	src_format: Union[Unset, FileImportFormat] = UNSET
	src_format_options: Union[Unset, InputFormat] = UNSET
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
		if not isinstance(self.output_format, Unset):
			output_format = self.output_format
		if not isinstance(self.output_format_options, Unset):
			output_format_options = self.output_format_options
		outputs: Union[Unset, Dict[str, str]] = UNSET
		if not isinstance(self.outputs, Unset):
			new_dict: Dict[str, str] = {}
			for key, value in self.outputs.items():
				new_dict[key] = value.get_encoded()
			outputs = new_dict
		if not isinstance(self.src_format, Unset):
			src_format = self.src_format
		if not isinstance(self.src_format_options, Unset):
			src_format_options = self.src_format_options
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
		if output_format is not UNSET:
			field_dict['output_format'] = output_format
		if output_format_options is not UNSET:
			field_dict['output_format_options'] = output_format_options
		if outputs is not UNSET:
			field_dict['outputs'] = outputs
		if src_format is not UNSET:
			field_dict['src_format'] = src_format
		if src_format_options is not UNSET:
			field_dict['src_format_options'] = src_format_options
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
	def from_dict(cls: Type[LK], src_dict: Dict[str, Any]) -> LK:
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

		_output_format = d.pop("output_format", UNSET)
		output_format: Union[Unset, FileExportFormat]
		if isinstance(_output_format, Unset):
			output_format = UNSET
		else:
			output_format = _output_format # type: ignore[arg-type]

		_output_format_options = d.pop("output_format_options", UNSET)
		output_format_options: Union[Unset, OutputFormat]
		if isinstance(_output_format_options, Unset):
			output_format_options = UNSET
		else:
			output_format_options = _output_format_options # type: ignore[arg-type]

		_outputs = d.pop("outputs", UNSET)
		if isinstance(_outputs, Unset):
			outputs = UNSET
		else:
			new_map: Dict[str, Base64Data] = {}
			for k, v in _outputs.items():
				new_map[k] = Base64Data(bytes(v, 'utf-8'))
			outputs = new_map # type: ignore

		_src_format = d.pop("src_format", UNSET)
		src_format: Union[Unset, FileImportFormat]
		if isinstance(_src_format, Unset):
			src_format = UNSET
		else:
			src_format = _src_format # type: ignore[arg-type]

		_src_format_options = d.pop("src_format_options", UNSET)
		src_format_options: Union[Unset, InputFormat]
		if isinstance(_src_format_options, Unset):
			src_format_options = UNSET
		else:
			src_format_options = _src_format_options # type: ignore[arg-type]

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


		file_conversion = cls(
			completed_at= completed_at,
			created_at= created_at,
			error= error,
			id= id,
			output_format= output_format,
			output_format_options= output_format_options,
			outputs= outputs,
			src_format= src_format,
			src_format_options= src_format_options,
			started_at= started_at,
			status= status,
			updated_at= updated_at,
			user_id= user_id,
		)

		file_conversion.additional_properties = d
		return file_conversion

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
