from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEvent")


@_attrs_define
class WebhookEvent:
    """
    Attributes:
        delivery_id (str | Unset): The delivery id of the webhook
        webhook_id (str | Unset): The id of the webhook
        original_delivery_id (str | Unset): If this delivery is a redelivery, the is the delivery id of the original
            delivery.
        is_redelivery (bool | Unset): True if this delivery is a redelivery
        type_ (str | Unset): The type of this event, current available are `InvoiceCreated`, `InvoiceReceivedPayment`,
            `InvoiceProcessing`, `InvoiceExpired`, `InvoiceSettled`, `InvoiceInvalid`, and `InvoicePaymentSettled`.
        timestamp (float | Unset): A unix timestamp in seconds Example: 1592312018.
    """

    delivery_id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    original_delivery_id: str | Unset = UNSET
    is_redelivery: bool | Unset = UNSET
    type_: str | Unset = UNSET
    timestamp: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        delivery_id = self.delivery_id

        webhook_id = self.webhook_id

        original_delivery_id = self.original_delivery_id

        is_redelivery = self.is_redelivery

        type_ = self.type_

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivery_id = d.pop("deliveryId", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        original_delivery_id = d.pop("originalDeliveryId", UNSET)

        is_redelivery = d.pop("isRedelivery", UNSET)

        type_ = d.pop("type", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        webhook_event = cls(
            delivery_id=delivery_id,
            webhook_id=webhook_id,
            original_delivery_id=original_delivery_id,
            is_redelivery=is_redelivery,
            type_=type_,
            timestamp=timestamp,
        )

        return webhook_event
