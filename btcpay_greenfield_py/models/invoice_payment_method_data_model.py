from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_payment_method_data_model_additional_data_type_0 import (
        InvoicePaymentMethodDataModelAdditionalDataType0,
    )
    from ..models.invoice_payment_method_data_model_additional_data_type_1 import (
        InvoicePaymentMethodDataModelAdditionalDataType1,
    )
    from ..models.payment import Payment


T = TypeVar("T", bound="InvoicePaymentMethodDataModel")


@_attrs_define
class InvoicePaymentMethodDataModel:
    """
    Attributes:
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        crypto_code (str | Unset): Crypto code of the payment method (e.g., "BTC" or "LTC") Example: BTC.
        destination (str | Unset): The destination the payment must be made to
        payment_link (None | str | Unset): A payment link that helps pay to the payment destination
        rate (str | Unset): The rate between this payment method's currency and the invoice currency Example: 64392.23.
        payment_method_paid (str | Unset): The amount paid by this payment method
        total_paid (str | Unset): The total amount paid by all payment methods to the invoice, converted to this payment
            method's currency
        due (str | Unset): The total amount left to be paid, converted to this payment method's currency (will be
            negative if overpaid)
        amount (str | Unset): The invoice amount, converted to this payment method's currency
        network_fee (str | Unset): The added merchant fee to pay for network costs of this payment method.
        payments (list[Payment] | Unset): Payments made with this payment method.
        activated (bool | Unset): If the payment method is activated (when lazy payments option is enabled
        additional_data (InvoicePaymentMethodDataModelAdditionalDataType0 |
            InvoicePaymentMethodDataModelAdditionalDataType1 | Unset): Additional data provided by the payment method.
    """

    payment_method: str | Unset = UNSET
    crypto_code: str | Unset = UNSET
    destination: str | Unset = UNSET
    payment_link: None | str | Unset = UNSET
    rate: str | Unset = UNSET
    payment_method_paid: str | Unset = UNSET
    total_paid: str | Unset = UNSET
    due: str | Unset = UNSET
    amount: str | Unset = UNSET
    network_fee: str | Unset = UNSET
    payments: list[Payment] | Unset = UNSET
    activated: bool | Unset = UNSET
    additional_data: (
        InvoicePaymentMethodDataModelAdditionalDataType0 | InvoicePaymentMethodDataModelAdditionalDataType1 | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_payment_method_data_model_additional_data_type_0 import (
            InvoicePaymentMethodDataModelAdditionalDataType0,
        )

        payment_method = self.payment_method

        crypto_code = self.crypto_code

        destination = self.destination

        payment_link: None | str | Unset
        if isinstance(self.payment_link, Unset):
            payment_link = UNSET
        else:
            payment_link = self.payment_link

        rate = self.rate

        payment_method_paid = self.payment_method_paid

        total_paid = self.total_paid

        due = self.due

        amount = self.amount

        network_fee = self.network_fee

        payments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)

        activated = self.activated

        additional_data: dict[str, Any] | Unset
        if isinstance(self.additional_data, Unset):
            additional_data = UNSET
        elif isinstance(self.additional_data, InvoicePaymentMethodDataModelAdditionalDataType0):
            additional_data = self.additional_data.to_dict()
        else:
            additional_data = self.additional_data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if crypto_code is not UNSET:
            field_dict["cryptoCode"] = crypto_code
        if destination is not UNSET:
            field_dict["destination"] = destination
        if payment_link is not UNSET:
            field_dict["paymentLink"] = payment_link
        if rate is not UNSET:
            field_dict["rate"] = rate
        if payment_method_paid is not UNSET:
            field_dict["paymentMethodPaid"] = payment_method_paid
        if total_paid is not UNSET:
            field_dict["totalPaid"] = total_paid
        if due is not UNSET:
            field_dict["due"] = due
        if amount is not UNSET:
            field_dict["amount"] = amount
        if network_fee is not UNSET:
            field_dict["networkFee"] = network_fee
        if payments is not UNSET:
            field_dict["payments"] = payments
        if activated is not UNSET:
            field_dict["activated"] = activated
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_payment_method_data_model_additional_data_type_0 import (
            InvoicePaymentMethodDataModelAdditionalDataType0,
        )
        from ..models.invoice_payment_method_data_model_additional_data_type_1 import (
            InvoicePaymentMethodDataModelAdditionalDataType1,
        )
        from ..models.payment import Payment

        d = dict(src_dict)
        payment_method = d.pop("paymentMethod", UNSET)

        crypto_code = d.pop("cryptoCode", UNSET)

        destination = d.pop("destination", UNSET)

        def _parse_payment_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_link = _parse_payment_link(d.pop("paymentLink", UNSET))

        rate = d.pop("rate", UNSET)

        payment_method_paid = d.pop("paymentMethodPaid", UNSET)

        total_paid = d.pop("totalPaid", UNSET)

        due = d.pop("due", UNSET)

        amount = d.pop("amount", UNSET)

        network_fee = d.pop("networkFee", UNSET)

        _payments = d.pop("payments", UNSET)
        payments: list[Payment] | Unset = UNSET
        if _payments is not UNSET:
            payments = []
            for payments_item_data in _payments:
                payments_item = Payment.from_dict(payments_item_data)

                payments.append(payments_item)

        activated = d.pop("activated", UNSET)

        def _parse_additional_data(
            data: object,
        ) -> (
            InvoicePaymentMethodDataModelAdditionalDataType0 | InvoicePaymentMethodDataModelAdditionalDataType1 | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_data_type_0 = InvoicePaymentMethodDataModelAdditionalDataType0.from_dict(data)

                return additional_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            additional_data_type_1 = InvoicePaymentMethodDataModelAdditionalDataType1.from_dict(data)

            return additional_data_type_1

        additional_data = _parse_additional_data(d.pop("additionalData", UNSET))

        invoice_payment_method_data_model = cls(
            payment_method=payment_method,
            crypto_code=crypto_code,
            destination=destination,
            payment_link=payment_link,
            rate=rate,
            payment_method_paid=payment_method_paid,
            total_paid=total_paid,
            due=due,
            amount=amount,
            network_fee=network_fee,
            payments=payments,
            activated=activated,
            additional_data=additional_data,
        )

        return invoice_payment_method_data_model
