from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnChainWalletAddressData")


@_attrs_define
class OnChainWalletAddressData:
    """
    Attributes:
        address (str | Unset): The bitcoin address
        key_path (str | Unset): the derivation path in relation to the HD account
        payment_link (str | Unset): a bip21 payment link
    """

    address: str | Unset = UNSET
    key_path: str | Unset = UNSET
    payment_link: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        key_path = self.key_path

        payment_link = self.payment_link

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if key_path is not UNSET:
            field_dict["keyPath"] = key_path
        if payment_link is not UNSET:
            field_dict["paymentLink"] = payment_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        key_path = d.pop("keyPath", UNSET)

        payment_link = d.pop("paymentLink", UNSET)

        on_chain_wallet_address_data = cls(
            address=address,
            key_path=key_path,
            payment_link=payment_link,
        )

        return on_chain_wallet_address_data
