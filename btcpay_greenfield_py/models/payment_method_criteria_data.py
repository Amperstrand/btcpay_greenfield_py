from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethodCriteriaData")


@_attrs_define
class PaymentMethodCriteriaData:
    """
    Attributes:
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        currency_code (str | Unset): The currency Default: 'USD'. Example: USD.
        amount (str | Unset): The amount
        above (bool | Unset): If the criterion is for above or below the amount Default: False.
    """

    payment_method: str | Unset = UNSET
    currency_code: str | Unset = "USD"
    amount: str | Unset = UNSET
    above: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_method = self.payment_method

        currency_code = self.currency_code

        amount = self.amount

        above = self.above

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if amount is not UNSET:
            field_dict["amount"] = amount
        if above is not UNSET:
            field_dict["above"] = above

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_method = d.pop("paymentMethod", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        amount = d.pop("amount", UNSET)

        above = d.pop("above", UNSET)

        payment_method_criteria_data = cls(
            payment_method=payment_method,
            currency_code=currency_code,
            amount=amount,
            above=above,
        )

        payment_method_criteria_data.additional_properties = d
        return payment_method_criteria_data

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
