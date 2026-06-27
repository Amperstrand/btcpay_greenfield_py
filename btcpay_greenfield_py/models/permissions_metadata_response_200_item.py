from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionsMetadataResponse200Item")


@_attrs_define
class PermissionsMetadataResponse200Item:
    """
    Attributes:
        name (str | Unset): The permission id
        included (list[str] | Unset): Permissions included in this array are also granted by this permission
    """

    name: str | Unset = UNSET
    included: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        included: list[str] | Unset = UNSET
        if not isinstance(self.included, Unset):
            included = self.included

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        included = cast(list[str], d.pop("included", UNSET))

        permissions_metadata_response_200_item = cls(
            name=name,
            included=included,
        )

        permissions_metadata_response_200_item.additional_properties = d
        return permissions_metadata_response_200_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
