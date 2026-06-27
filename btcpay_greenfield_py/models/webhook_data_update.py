from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_data_base_authorized_events import WebhookDataBaseAuthorizedEvents


T = TypeVar("T", bound="WebhookDataUpdate")


@_attrs_define
class WebhookDataUpdate:
    """
    Attributes:
        enabled (bool | Unset): Whether this webhook is enabled or not Default: True.
        automatic_redelivery (bool | Unset): If true, BTCPay Server will retry to redeliver any failed delivery after 10
            seconds, 1 minutes and up to 6 times after 10 minutes. Default: True.
        url (str | Unset): The endpoint where BTCPay Server will make the POST request with the webhook body
        authorized_events (WebhookDataBaseAuthorizedEvents | Unset): Which event should be received by this endpoint
        secret (None | str | Unset): Must be used by the callback receiver to ensure the delivery comes from BTCPay
            Server. BTCPay Server includes the `BTCPay-Sig` HTTP header, whose format is `sha256=HMAC256(UTF8(webhook's
            secret), body)`. The pattern to authenticate the webhook is similar to [how to secure webhooks in
            Github](https://docs.github.com/webhooks/securing/). If left out, null, or empty, the secret will not be
            changed.
    """

    enabled: bool | Unset = True
    automatic_redelivery: bool | Unset = True
    url: str | Unset = UNSET
    authorized_events: WebhookDataBaseAuthorizedEvents | Unset = UNSET
    secret: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        automatic_redelivery = self.automatic_redelivery

        url = self.url

        authorized_events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorized_events, Unset):
            authorized_events = self.authorized_events.to_dict()

        secret: None | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        else:
            secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if automatic_redelivery is not UNSET:
            field_dict["automaticRedelivery"] = automatic_redelivery
        if url is not UNSET:
            field_dict["url"] = url
        if authorized_events is not UNSET:
            field_dict["authorizedEvents"] = authorized_events
        if secret is not UNSET:
            field_dict["secret"] = secret

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

        def _parse_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret = _parse_secret(d.pop("secret", UNSET))

        webhook_data_update = cls(
            enabled=enabled,
            automatic_redelivery=automatic_redelivery,
            url=url,
            authorized_events=authorized_events,
            secret=secret,
        )

        webhook_data_update.additional_properties = d
        return webhook_data_update

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
