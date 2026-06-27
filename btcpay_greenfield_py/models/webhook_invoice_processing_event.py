from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_invoice_event_metadata import WebhookInvoiceEventMetadata


T = TypeVar("T", bound="WebhookInvoiceProcessingEvent")


@_attrs_define
class WebhookInvoiceProcessingEvent:
    """Callback sent if the `type` is `InvoiceProcessing`

    Attributes:
        delivery_id (str | Unset): The delivery id of the webhook
        webhook_id (str | Unset): The id of the webhook
        original_delivery_id (str | Unset): If this delivery is a redelivery, the is the delivery id of the original
            delivery.
        is_redelivery (bool | Unset): True if this delivery is a redelivery
        type_ (str | Unset): The type of this event, current available are `InvoiceCreated`, `InvoiceReceivedPayment`,
            `InvoiceProcessing`, `InvoiceExpired`, `InvoiceSettled`, `InvoiceInvalid`, and `InvoicePaymentSettled`.
        timestamp (float | Unset): A unix timestamp in seconds Example: 1592312018.
        store_id (str | Unset): The store id of the invoice's event
        invoice_id (str | Unset): The invoice id of the invoice's event
        metadata (WebhookInvoiceEventMetadata | Unset): User-supplied metadata added to the invoice at the time of its
            creation
        over_paid (bool | Unset): Whether this invoice has received more money than expected
    """

    delivery_id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    original_delivery_id: str | Unset = UNSET
    is_redelivery: bool | Unset = UNSET
    type_: str | Unset = UNSET
    timestamp: float | Unset = UNSET
    store_id: str | Unset = UNSET
    invoice_id: str | Unset = UNSET
    metadata: WebhookInvoiceEventMetadata | Unset = UNSET
    over_paid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_id = self.delivery_id

        webhook_id = self.webhook_id

        original_delivery_id = self.original_delivery_id

        is_redelivery = self.is_redelivery

        type_ = self.type_

        timestamp = self.timestamp

        store_id = self.store_id

        invoice_id = self.invoice_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        over_paid = self.over_paid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_id is not UNSET:
            field_dict["deliveryId"] = delivery_id
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if original_delivery_id is not UNSET:
            field_dict["originalDeliveryId"] = original_delivery_id
        if is_redelivery is not UNSET:
            field_dict["isRedelivery"] = is_redelivery
        if type_ is not UNSET:
            field_dict["type"] = type_
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if over_paid is not UNSET:
            field_dict["overPaid"] = over_paid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_invoice_event_metadata import WebhookInvoiceEventMetadata

        d = dict(src_dict)
        delivery_id = d.pop("deliveryId", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        original_delivery_id = d.pop("originalDeliveryId", UNSET)

        is_redelivery = d.pop("isRedelivery", UNSET)

        type_ = d.pop("type", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        store_id = d.pop("storeId", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: WebhookInvoiceEventMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = WebhookInvoiceEventMetadata.from_dict(_metadata)

        over_paid = d.pop("overPaid", UNSET)

        webhook_invoice_processing_event = cls(
            delivery_id=delivery_id,
            webhook_id=webhook_id,
            original_delivery_id=original_delivery_id,
            is_redelivery=is_redelivery,
            type_=type_,
            timestamp=timestamp,
            store_id=store_id,
            invoice_id=invoice_id,
            metadata=metadata,
            over_paid=over_paid,
        )

        webhook_invoice_processing_event.additional_properties = d
        return webhook_invoice_processing_event

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
