from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.invoices_refund_body_refund_variant import InvoicesRefundBodyRefundVariant
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicesRefundBody")


@_attrs_define
class InvoicesRefundBody:
    """
    Attributes:
        name (None | str | Unset): Name of the pull payment (Default: 'Refund' followed by the invoice id)
        description (str | Unset): Description of the pull payment
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        refund_variant (InvoicesRefundBodyRefundVariant | Unset): * `RateThen`: Refund the crypto currency price, at the
            rate the invoice got paid.
            * `CurrentRate`: Refund the crypto currency price, at the current rate.
            *`Fiat`: Refund the invoice currency, at the rate when the refund will be sent.
            *`OverpaidAmount`: Refund the crypto currency amount that was overpaid.
            *`Custom`: Specify the amount, currency, and rate of the refund. (see `customAmount` and `customCurrency`)
        subtract_percentage (str | Unset): Optional percentage by which to reduce the refund, e.g. as processing charge
            or to compensate for the mining fee. Example: 2.1.
        custom_amount (str | Unset): The amount to refund if the `refundVariant` is `Custom`. Example: 5.00.
        custom_currency (str | Unset): The currency to refund if the `refundVariant` is `Custom` Example: USD.
    """

    name: None | str | Unset = UNSET
    description: str | Unset = UNSET
    payment_method: str | Unset = UNSET
    refund_variant: InvoicesRefundBodyRefundVariant | Unset = UNSET
    subtract_percentage: str | Unset = UNSET
    custom_amount: str | Unset = UNSET
    custom_currency: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description = self.description

        payment_method = self.payment_method

        refund_variant: str | Unset = UNSET
        if not isinstance(self.refund_variant, Unset):
            refund_variant = self.refund_variant.value

        subtract_percentage = self.subtract_percentage

        custom_amount = self.custom_amount

        custom_currency = self.custom_currency

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if refund_variant is not UNSET:
            field_dict["refundVariant"] = refund_variant
        if subtract_percentage is not UNSET:
            field_dict["subtractPercentage"] = subtract_percentage
        if custom_amount is not UNSET:
            field_dict["customAmount"] = custom_amount
        if custom_currency is not UNSET:
            field_dict["customCurrency"] = custom_currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        description = d.pop("description", UNSET)

        payment_method = d.pop("paymentMethod", UNSET)

        _refund_variant = d.pop("refundVariant", UNSET)
        refund_variant: InvoicesRefundBodyRefundVariant | Unset
        if isinstance(_refund_variant, Unset):
            refund_variant = UNSET
        else:
            refund_variant = InvoicesRefundBodyRefundVariant(_refund_variant)

        subtract_percentage = d.pop("subtractPercentage", UNSET)

        custom_amount = d.pop("customAmount", UNSET)

        custom_currency = d.pop("customCurrency", UNSET)

        invoices_refund_body = cls(
            name=name,
            description=description,
            payment_method=payment_method,
            refund_variant=refund_variant,
            subtract_percentage=subtract_percentage,
            custom_amount=custom_amount,
            custom_currency=custom_currency,
        )

        return invoices_refund_body
