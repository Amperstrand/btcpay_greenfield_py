from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyData")


@_attrs_define
class ApiKeyData:
    """
    Attributes:
        api_key (str | Unset): The API Key to use for API Key Authentication
        label (str | Unset): The label given by the user to this API Key
        permissions (list[str] | Unset): The permissions associated to this API Key (can be scoped to a specific store)
            Example: ['btcpay.server.canmanageusers',
            'btcpay.server.canmanageusers:2KxSpc9V5zDWfUbvgYiZuAfka4wUhGF96F75Ao8y4zHP'].
    """

    api_key: str | Unset = UNSET
    label: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        label = self.label

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if label is not UNSET:
            field_dict["label"] = label
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        label = d.pop("label", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        api_key_data = cls(
            api_key=api_key,
            label=label,
            permissions=permissions,
        )

        return api_key_data
