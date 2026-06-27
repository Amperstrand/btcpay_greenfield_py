from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustodiansGetStoreCustodianAccountDepositAddressResponse200")


@_attrs_define
class CustodiansGetStoreCustodianAccountDepositAddressResponse200:
    """A bitcoin address belonging to the custodian

    Attributes:
        deposit_address (str | Unset): The address to deposit your funds.
    """

    deposit_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deposit_address = self.deposit_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deposit_address is not UNSET:
            field_dict["depositAddress"] = deposit_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deposit_address = d.pop("depositAddress", UNSET)

        custodians_get_store_custodian_account_deposit_address_response_200 = cls(
            deposit_address=deposit_address,
        )

        custodians_get_store_custodian_account_deposit_address_response_200.additional_properties = d
        return custodians_get_store_custodian_account_deposit_address_response_200

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
