from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePayoutRequest")


@_attrs_define
class CreatePayoutRequest:
    """
    Attributes:
        destination (str | Unset): The destination of the payout (can be an address or a BIP21 url) Example:
            1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2.
        amount (str | Unset): The amount of the payout in the currency of the pull payment (eg. USD). Example: 10399.18.
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
    """

    destination: str | Unset = UNSET
    amount: str | Unset = UNSET
    payment_method: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        amount = self.amount

        payment_method = self.payment_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination = d.pop("destination", UNSET)

        amount = d.pop("amount", UNSET)

        payment_method = d.pop("paymentMethod", UNSET)

        create_payout_request = cls(
            destination=destination,
            amount=amount,
            payment_method=payment_method,
        )

        create_payout_request.additional_properties = d
        return create_payout_request

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
