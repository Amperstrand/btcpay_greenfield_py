from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnChainPaymentMethodPreviewResultAddressItem")


@_attrs_define
class OnChainPaymentMethodPreviewResultAddressItem:
    """
    Attributes:
        key_path (str | Unset): The key path relative to the account key path.
        address (str | Unset): The address generated at the key path
    """

    key_path: str | Unset = UNSET
    address: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key_path = self.key_path

        address = self.address

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key_path is not UNSET:
            field_dict["keyPath"] = key_path
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_path = d.pop("keyPath", UNSET)

        address = d.pop("address", UNSET)

        on_chain_payment_method_preview_result_address_item = cls(
            key_path=key_path,
            address=address,
        )

        return on_chain_payment_method_preview_result_address_item
