from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleData")


@_attrs_define
class RoleData:
    """
    Attributes:
        id (str | Unset): The role's Id (Same as role if the role is created at server level, if the role is created at
            the store level the format is `STOREID::ROLE`) Example: Owner.
        role (str | Unset): The role's name Example: Owner.
        permissions (list[str] | Unset): The permissions attached to this role Example:
            ['btcpay.store.canmodifystoresettings', 'btcpay.store.cantradecustodianaccount',
            'btcpay.store.canwithdrawfromcustodianaccount', 'btcpay.store.candeposittocustodianaccount'].
        is_server_role (bool | Unset): Whether this role is at the scope of the store or scope of the server Example:
            True.
    """

    id: str | Unset = UNSET
    role: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    is_server_role: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        role = self.role

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        is_server_role = self.is_server_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if role is not UNSET:
            field_dict["role"] = role
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if is_server_role is not UNSET:
            field_dict["isServerRole"] = is_server_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        role = d.pop("role", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        is_server_role = d.pop("isServerRole", UNSET)

        role_data = cls(
            id=id,
            role=role,
            permissions=permissions,
            is_server_role=is_server_role,
        )

        role_data.additional_properties = d
        return role_data

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
