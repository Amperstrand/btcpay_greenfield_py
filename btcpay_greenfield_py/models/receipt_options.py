from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReceiptOptions")


@_attrs_define
class ReceiptOptions:
    """
    Attributes:
        enabled (bool | None | Unset): A public page will be accessible once the invoice is settled. If null or
            unspecified, it will fallback to the store's settings. (The default store settings is true)
        show_qr (bool | None | Unset): Show the QR code of the receipt in the public receipt page. If null or
            unspecified, it will fallback to the store's settings. (The default store setting is true)
        show_payments (bool | None | Unset): Show the payment list in the public receipt page. If null or unspecified,
            it will fallback to the store's settings. (The default store setting is true)
    """

    enabled: bool | None | Unset = UNSET
    show_qr: bool | None | Unset = UNSET
    show_payments: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        show_qr: bool | None | Unset
        if isinstance(self.show_qr, Unset):
            show_qr = UNSET
        else:
            show_qr = self.show_qr

        show_payments: bool | None | Unset
        if isinstance(self.show_payments, Unset):
            show_payments = UNSET
        else:
            show_payments = self.show_payments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if show_qr is not UNSET:
            field_dict["showQR"] = show_qr
        if show_payments is not UNSET:
            field_dict["showPayments"] = show_payments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_show_qr(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_qr = _parse_show_qr(d.pop("showQR", UNSET))

        def _parse_show_payments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_payments = _parse_show_payments(d.pop("showPayments", UNSET))

        receipt_options = cls(
            enabled=enabled,
            show_qr=show_qr,
            show_payments=show_payments,
        )

        return receipt_options
