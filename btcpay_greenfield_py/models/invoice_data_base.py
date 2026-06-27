from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_options import CheckoutOptions
    from ..models.invoice_metadata import InvoiceMetadata
    from ..models.receipt_options import ReceiptOptions


T = TypeVar("T", bound="InvoiceDataBase")


@_attrs_define
class InvoiceDataBase:
    """
    Attributes:
        metadata (InvoiceMetadata | Unset): Additional information around the invoice that can be supplied. The
            mentioned properties are all optional and you can introduce any json format you wish. See [our
            documentation](https://docs.btcpayserver.org/Development/InvoiceMetadata/) for more information. Example:
            {'orderId': 'pos-app_346KRC5BjXXXo8cRFKwTBmdR6ZJ4', 'orderUrl':
            'https://localhost:14142/apps/346KRC5BjXXXo8cRFKwTBmdR6ZJ4/pos', 'itemDesc': 'Tea shop', 'posData': {'tip':
            0.48, 'cart': [{'id': 'pu erh', 'count': 1, 'image': '~/img/pos-sample/pu-erh.jpg', 'price': {'type': 2,
            'value': 2, 'formatted': '$2.00'}, 'title': 'Pu Erh', 'inventory': None}, {'id': 'rooibos', 'count': 1, 'image':
            '~/img/pos-sample/rooibos.jpg', 'price': {'type': 2, 'value': 1.2, 'formatted': '$1.20'}, 'title': 'Rooibos',
            'inventory': None}], 'total': 3.68, 'subTotal': 3.2, 'customAmount': 0, 'discountAmount': 0,
            'discountPercentage': 0}, 'receiptData': {'Tip': '$0.48', 'Cart': {'Pu Erh': '$2.00 x 1 = $2.00', 'Rooibos':
            '$1.20 x 1 = $1.20'}}}.
        checkout (CheckoutOptions | None | Unset): Additional settings to customize the checkout flow
        receipt (None | ReceiptOptions | Unset): Additional settings to customize the public receipt
    """

    metadata: InvoiceMetadata | Unset = UNSET
    checkout: CheckoutOptions | None | Unset = UNSET
    receipt: None | ReceiptOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkout_options import CheckoutOptions
        from ..models.receipt_options import ReceiptOptions

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        checkout: dict[str, Any] | None | Unset
        if isinstance(self.checkout, Unset):
            checkout = UNSET
        elif isinstance(self.checkout, CheckoutOptions):
            checkout = self.checkout.to_dict()
        else:
            checkout = self.checkout

        receipt: dict[str, Any] | None | Unset
        if isinstance(self.receipt, Unset):
            receipt = UNSET
        elif isinstance(self.receipt, ReceiptOptions):
            receipt = self.receipt.to_dict()
        else:
            receipt = self.receipt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if checkout is not UNSET:
            field_dict["checkout"] = checkout
        if receipt is not UNSET:
            field_dict["receipt"] = receipt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkout_options import CheckoutOptions
        from ..models.invoice_metadata import InvoiceMetadata
        from ..models.receipt_options import ReceiptOptions

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: InvoiceMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = InvoiceMetadata.from_dict(_metadata)

        def _parse_checkout(data: object) -> CheckoutOptions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                checkout_type_1 = CheckoutOptions.from_dict(data)

                return checkout_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CheckoutOptions | None | Unset, data)

        checkout = _parse_checkout(d.pop("checkout", UNSET))

        def _parse_receipt(data: object) -> None | ReceiptOptions | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                receipt_type_1 = ReceiptOptions.from_dict(data)

                return receipt_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReceiptOptions | Unset, data)

        receipt = _parse_receipt(d.pop("receipt", UNSET))

        invoice_data_base = cls(
            metadata=metadata,
            checkout=checkout,
            receipt=receipt,
        )

        invoice_data_base.additional_properties = d
        return invoice_data_base

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
