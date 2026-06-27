from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_additional_status import InvoiceAdditionalStatus
from ..models.invoice_status import InvoiceStatus
from ..models.invoice_type import InvoiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_options import CheckoutOptions
    from ..models.invoice_metadata import InvoiceMetadata
    from ..models.receipt_options import ReceiptOptions


T = TypeVar("T", bound="InvoiceData")


@_attrs_define
class InvoiceData:
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
        id (str | Unset): The identifier of the invoice
        store_id (str | Unset): The store identifier that the invoice belongs to
        amount (str | Unset): The amount of the invoice. Note that the amount will be zero for a top-up invoice that is
            paid after invoice expiry. Example: 5.00.
        currency (str | Unset): The currency of the invoice Example: USD.
        type_ (InvoiceType | Unset): The type of the invoice
        checkout_link (str | Unset): The link to the checkout page, where you can redirect the customer
        created_time (float | Unset): A unix timestamp in seconds Example: 1592312018.
        expiration_time (float | Unset): A unix timestamp in seconds Example: 1592312018.
        monitoring_expiration (float | Unset): A unix timestamp in seconds Example: 1592312018.
        status (InvoiceStatus | Unset): The status of the invoice
        additional_status (InvoiceAdditionalStatus | Unset): An additional status that describes why an invoice is in
            its current status.
        available_statuses_for_manual_marking (list[InvoiceStatus] | Unset): The statuses the invoice can be manually
            marked as
        archived (bool | Unset): true if the invoice is archived
    """

    metadata: InvoiceMetadata | Unset = UNSET
    checkout: CheckoutOptions | None | Unset = UNSET
    receipt: None | ReceiptOptions | Unset = UNSET
    id: str | Unset = UNSET
    store_id: str | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    type_: InvoiceType | Unset = UNSET
    checkout_link: str | Unset = UNSET
    created_time: float | Unset = UNSET
    expiration_time: float | Unset = UNSET
    monitoring_expiration: float | Unset = UNSET
    status: InvoiceStatus | Unset = UNSET
    additional_status: InvoiceAdditionalStatus | Unset = UNSET
    available_statuses_for_manual_marking: list[InvoiceStatus] | Unset = UNSET
    archived: bool | Unset = UNSET
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

        id = self.id

        store_id = self.store_id

        amount = self.amount

        currency = self.currency

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        checkout_link = self.checkout_link

        created_time = self.created_time

        expiration_time = self.expiration_time

        monitoring_expiration = self.monitoring_expiration

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        additional_status: str | Unset = UNSET
        if not isinstance(self.additional_status, Unset):
            additional_status = self.additional_status.value

        available_statuses_for_manual_marking: list[str] | Unset = UNSET
        if not isinstance(self.available_statuses_for_manual_marking, Unset):
            available_statuses_for_manual_marking = []
            for available_statuses_for_manual_marking_item_data in self.available_statuses_for_manual_marking:
                available_statuses_for_manual_marking_item = available_statuses_for_manual_marking_item_data.value
                available_statuses_for_manual_marking.append(available_statuses_for_manual_marking_item)

        archived = self.archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if checkout is not UNSET:
            field_dict["checkout"] = checkout
        if receipt is not UNSET:
            field_dict["receipt"] = receipt
        if id is not UNSET:
            field_dict["id"] = id
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if type_ is not UNSET:
            field_dict["type"] = type_
        if checkout_link is not UNSET:
            field_dict["checkoutLink"] = checkout_link
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if monitoring_expiration is not UNSET:
            field_dict["monitoringExpiration"] = monitoring_expiration
        if status is not UNSET:
            field_dict["status"] = status
        if additional_status is not UNSET:
            field_dict["additionalStatus"] = additional_status
        if available_statuses_for_manual_marking is not UNSET:
            field_dict["availableStatusesForManualMarking"] = available_statuses_for_manual_marking
        if archived is not UNSET:
            field_dict["archived"] = archived

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

        id = d.pop("id", UNSET)

        store_id = d.pop("storeId", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: InvoiceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InvoiceType(_type_)

        checkout_link = d.pop("checkoutLink", UNSET)

        created_time = d.pop("createdTime", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        monitoring_expiration = d.pop("monitoringExpiration", UNSET)

        _status = d.pop("status", UNSET)
        status: InvoiceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceStatus(_status)

        _additional_status = d.pop("additionalStatus", UNSET)
        additional_status: InvoiceAdditionalStatus | Unset
        if isinstance(_additional_status, Unset):
            additional_status = UNSET
        else:
            additional_status = InvoiceAdditionalStatus(_additional_status)

        _available_statuses_for_manual_marking = d.pop("availableStatusesForManualMarking", UNSET)
        available_statuses_for_manual_marking: list[InvoiceStatus] | Unset = UNSET
        if _available_statuses_for_manual_marking is not UNSET:
            available_statuses_for_manual_marking = []
            for available_statuses_for_manual_marking_item_data in _available_statuses_for_manual_marking:
                available_statuses_for_manual_marking_item = InvoiceStatus(
                    available_statuses_for_manual_marking_item_data
                )

                available_statuses_for_manual_marking.append(available_statuses_for_manual_marking_item)

        archived = d.pop("archived", UNSET)

        invoice_data = cls(
            metadata=metadata,
            checkout=checkout,
            receipt=receipt,
            id=id,
            store_id=store_id,
            amount=amount,
            currency=currency,
            type_=type_,
            checkout_link=checkout_link,
            created_time=created_time,
            expiration_time=expiration_time,
            monitoring_expiration=monitoring_expiration,
            status=status,
            additional_status=additional_status,
            available_statuses_for_manual_marking=available_statuses_for_manual_marking,
            archived=archived,
        )

        invoice_data.additional_properties = d
        return invoice_data

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
