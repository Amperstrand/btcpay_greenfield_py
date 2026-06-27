from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeysCreateUserApiKeyBody")


@_attrs_define
class ApiKeysCreateUserApiKeyBody:
    """
    Attributes:
        label (None | str | Unset): The label of the new API Key
        permissions (list[str] | None | Unset): The permissions granted to this API Key (See API Key Authentication)
    """

    label: None | str | Unset = UNSET
    permissions: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        permissions: list[str] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = self.permissions

        else:
            permissions = self.permissions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = cast(list[str], data)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        api_keys_create_user_api_key_body = cls(
            label=label,
            permissions=permissions,
        )

        return api_keys_create_user_api_key_body
