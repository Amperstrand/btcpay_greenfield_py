from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LNURLPayPaymentMethodData")


@_attrs_define
class LNURLPayPaymentMethodData:
    """
    Attributes:
        use_bech_32_scheme (bool | Unset): Whether to use [LUD-01](https://github.com/fiatjaf/lnurl-
            rfc/blob/luds/01.md)'s bech32 format or to use [LUD-17](https://github.com/fiatjaf/lnurl-rfc/blob/luds/17.md)
            url formatting.
        lud_12_enabled (bool | Unset): Allow comments to be passed on via lnurl.
        enabled (bool | Unset): Whether the payment method is enabled. Note that this can only enabled when a Lightning
            Network payment method is available and enabled
        crypto_code (str | Unset): Crypto code of the payment method
    """

    use_bech_32_scheme: bool | Unset = UNSET
    lud_12_enabled: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    crypto_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_bech_32_scheme = self.use_bech_32_scheme

        lud_12_enabled = self.lud_12_enabled

        enabled = self.enabled

        crypto_code = self.crypto_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_bech_32_scheme is not UNSET:
            field_dict["useBech32Scheme"] = use_bech_32_scheme
        if lud_12_enabled is not UNSET:
            field_dict["lud12Enabled"] = lud_12_enabled
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if crypto_code is not UNSET:
            field_dict["cryptoCode"] = crypto_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_bech_32_scheme = d.pop("useBech32Scheme", UNSET)

        lud_12_enabled = d.pop("lud12Enabled", UNSET)

        enabled = d.pop("enabled", UNSET)

        crypto_code = d.pop("cryptoCode", UNSET)

        lnurl_pay_payment_method_data = cls(
            use_bech_32_scheme=use_bech_32_scheme,
            lud_12_enabled=lud_12_enabled,
            enabled=enabled,
            crypto_code=crypto_code,
        )

        lnurl_pay_payment_method_data.additional_properties = d
        return lnurl_pay_payment_method_data

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
