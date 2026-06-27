from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_data_base_authorized_events import WebhookDataBaseAuthorizedEvents


T = TypeVar("T", bound="WebhookDataBase")


@_attrs_define
class WebhookDataBase:
    """
    Attributes:
        enabled (bool | Unset): Whether this webhook is enabled or not Default: True.
        automatic_redelivery (bool | Unset): If true, BTCPay Server will retry to redeliver any failed delivery after 10
            seconds, 1 minutes and up to 6 times after 10 minutes. Default: True.
        url (str | Unset): The endpoint where BTCPay Server will make the POST request with the webhook body
        authorized_events (WebhookDataBaseAuthorizedEvents | Unset): Which event should be received by this endpoint
    """

    enabled: bool | Unset = True
    automatic_redelivery: bool | Unset = True
    url: str | Unset = UNSET
    authorized_events: WebhookDataBaseAuthorizedEvents | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        automatic_redelivery = self.automatic_redelivery

        url = self.url

        authorized_events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorized_events, Unset):
            authorized_events = self.authorized_events.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if automatic_redelivery is not UNSET:
            field_dict["automaticRedelivery"] = automatic_redelivery
        if url is not UNSET:
            field_dict["url"] = url
        if authorized_events is not UNSET:
            field_dict["authorizedEvents"] = authorized_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_data_base_authorized_events import WebhookDataBaseAuthorizedEvents

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        automatic_redelivery = d.pop("automaticRedelivery", UNSET)

        url = d.pop("url", UNSET)

        _authorized_events = d.pop("authorizedEvents", UNSET)
        authorized_events: WebhookDataBaseAuthorizedEvents | Unset
        if isinstance(_authorized_events, Unset):
            authorized_events = UNSET
        else:
            authorized_events = WebhookDataBaseAuthorizedEvents.from_dict(_authorized_events)

        webhook_data_base = cls(
            enabled=enabled,
            automatic_redelivery=automatic_redelivery,
            url=url,
            authorized_events=authorized_events,
        )

        return webhook_data_base
