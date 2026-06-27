from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRateSourcesResponse200Item")


@_attrs_define
class GetRateSourcesResponse200Item:
    """
    Attributes:
        id (str | Unset): The id of the rate provider
        name (str | Unset): The name of the rate provider
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_rate_sources_response_200_item = cls(
            id=id,
            name=name,
        )

        return get_rate_sources_response_200_item
