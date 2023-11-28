from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

PI = TypeVar("PI", bound="AiPromptResultsPage")


@attr.s(auto_attribs=True)
class AiPromptResultsPage:
    """A single page of results"""  # noqa: E501

    from ..models.ai_prompt import AiPrompt

    items: Union[Unset, List[AiPrompt]] = UNSET
    next_page: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ai_prompt import AiPrompt

        items: Union[Unset, List[AiPrompt]] = UNSET
        if not isinstance(self.items, Unset):
            items = self.items
        next_page = self.next_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if next_page is not UNSET:
            field_dict["next_page"] = next_page

        return field_dict

    @classmethod
    def from_dict(cls: Type[PI], src_dict: Dict[str, Any]) -> PI:
        d = src_dict.copy()
        from ..models.ai_prompt import AiPrompt

        items = cast(List[AiPrompt], d.pop("items", UNSET))

        next_page = d.pop("next_page", UNSET)

        ai_prompt_results_page = cls(
            items=items,
            next_page=next_page,
        )

        ai_prompt_results_page.additional_properties = d
        return ai_prompt_results_page

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
