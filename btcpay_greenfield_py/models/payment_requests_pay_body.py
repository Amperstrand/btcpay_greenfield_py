from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentRequestsPayBody")


@_attrs_define
class PaymentRequestsPayBody:
    """
    Attributes:
        amount (None | str | Unset): The amount of the invoice. If `null` or `unspecified`, it will be set to the
            payment request's due amount. Note that the payment's request `allowCustomPaymentAmounts` must be `true`, or a
            422 error will be sent back.' Example: 0.1.
        allow_pending_invoice_reuse (bool | None | Unset): If `true`, this endpoint will not necessarily create a new
            invoice, and instead attempt to give back a pending one for this payment request. Default: False.
    """

    amount: None | str | Unset = UNSET
    allow_pending_invoice_reuse: bool | None | Unset = False

    def to_dict(self) -> dict[str, Any]:
        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        allow_pending_invoice_reuse: bool | None | Unset
        if isinstance(self.allow_pending_invoice_reuse, Unset):
            allow_pending_invoice_reuse = UNSET
        else:
            allow_pending_invoice_reuse = self.allow_pending_invoice_reuse

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if allow_pending_invoice_reuse is not UNSET:
            field_dict["allowPendingInvoiceReuse"] = allow_pending_invoice_reuse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_allow_pending_invoice_reuse(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_pending_invoice_reuse = _parse_allow_pending_invoice_reuse(d.pop("allowPendingInvoiceReuse", UNSET))

        payment_requests_pay_body = cls(
            amount=amount,
            allow_pending_invoice_reuse=allow_pending_invoice_reuse,
        )

        return payment_requests_pay_body
