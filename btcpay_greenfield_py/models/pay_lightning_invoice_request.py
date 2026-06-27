from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayLightningInvoiceRequest")


@_attrs_define
class PayLightningInvoiceRequest:
    """
    Attributes:
        bolt11 (str | Unset): The BOLT11 of the invoice to pay
        amount (None | str | Unset): Optional explicit payment amount in millisatoshi (if specified, it overrides the
            BOLT11 amount)
        max_fee_percent (None | str | Unset): The fee limit expressed as a percentage of the payment amount Example:
            6.15.
        max_fee_flat (None | str | Unset): The fee limit expressed as a fixed amount in satoshi Example: 21.
        send_timeout (float | None | Unset): The number of seconds after which the payment times out Default: 30.0.
            Example: 30.
    """

    bolt11: str | Unset = UNSET
    amount: None | str | Unset = UNSET
    max_fee_percent: None | str | Unset = UNSET
    max_fee_flat: None | str | Unset = UNSET
    send_timeout: float | None | Unset = 30.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bolt11 = self.bolt11

        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        max_fee_percent: None | str | Unset
        if isinstance(self.max_fee_percent, Unset):
            max_fee_percent = UNSET
        else:
            max_fee_percent = self.max_fee_percent

        max_fee_flat: None | str | Unset
        if isinstance(self.max_fee_flat, Unset):
            max_fee_flat = UNSET
        else:
            max_fee_flat = self.max_fee_flat

        send_timeout: float | None | Unset
        if isinstance(self.send_timeout, Unset):
            send_timeout = UNSET
        else:
            send_timeout = self.send_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bolt11 is not UNSET:
            field_dict["BOLT11"] = bolt11
        if amount is not UNSET:
            field_dict["amount"] = amount
        if max_fee_percent is not UNSET:
            field_dict["maxFeePercent"] = max_fee_percent
        if max_fee_flat is not UNSET:
            field_dict["maxFeeFlat"] = max_fee_flat
        if send_timeout is not UNSET:
            field_dict["sendTimeout"] = send_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bolt11 = d.pop("BOLT11", UNSET)

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_max_fee_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_fee_percent = _parse_max_fee_percent(d.pop("maxFeePercent", UNSET))

        def _parse_max_fee_flat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_fee_flat = _parse_max_fee_flat(d.pop("maxFeeFlat", UNSET))

        def _parse_send_timeout(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        send_timeout = _parse_send_timeout(d.pop("sendTimeout", UNSET))

        pay_lightning_invoice_request = cls(
            bolt11=bolt11,
            amount=amount,
            max_fee_percent=max_fee_percent,
            max_fee_flat=max_fee_flat,
            send_timeout=send_timeout,
        )

        pay_lightning_invoice_request.additional_properties = d
        return pay_lightning_invoice_request

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
