from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WithdrawalRequestData")


@_attrs_define
class WithdrawalRequestData:
    """
    Example:
        {'paymentMethod': 'BTC-OnChain', 'qty': '0.123456'}

    Attributes:
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        qty (str | Unset):
    """

    payment_method: str | Unset = UNSET
    qty: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_method = self.payment_method

        qty: str | Unset
        if isinstance(self.qty, Unset):
            qty = UNSET
        else:
            qty = self.qty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if qty is not UNSET:
            field_dict["qty"] = qty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_method = d.pop("paymentMethod", UNSET)

        def _parse_qty(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        qty = _parse_qty(d.pop("qty", UNSET))

        withdrawal_request_data = cls(
            payment_method=payment_method,
            qty=qty,
        )

        withdrawal_request_data.additional_properties = d
        return withdrawal_request_data

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
