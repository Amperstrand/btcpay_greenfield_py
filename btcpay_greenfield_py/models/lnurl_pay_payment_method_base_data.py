from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LNURLPayPaymentMethodBaseData")


@_attrs_define
class LNURLPayPaymentMethodBaseData:
    """
    Attributes:
        use_bech_32_scheme (bool | Unset): Whether to use [LUD-01](https://github.com/fiatjaf/lnurl-
            rfc/blob/luds/01.md)'s bech32 format or to use [LUD-17](https://github.com/fiatjaf/lnurl-rfc/blob/luds/17.md)
            url formatting.
        lud_12_enabled (bool | Unset): Allow comments to be passed on via lnurl.
    """

    use_bech_32_scheme: bool | Unset = UNSET
    lud_12_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        use_bech_32_scheme = self.use_bech_32_scheme

        lud_12_enabled = self.lud_12_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if use_bech_32_scheme is not UNSET:
            field_dict["useBech32Scheme"] = use_bech_32_scheme
        if lud_12_enabled is not UNSET:
            field_dict["lud12Enabled"] = lud_12_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_bech_32_scheme = d.pop("useBech32Scheme", UNSET)

        lud_12_enabled = d.pop("lud12Enabled", UNSET)

        lnurl_pay_payment_method_base_data = cls(
            use_bech_32_scheme=use_bech_32_scheme,
            lud_12_enabled=lud_12_enabled,
        )

        return lnurl_pay_payment_method_base_data
