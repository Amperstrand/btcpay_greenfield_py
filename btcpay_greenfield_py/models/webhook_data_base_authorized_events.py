from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDataBaseAuthorizedEvents")


@_attrs_define
class WebhookDataBaseAuthorizedEvents:
    """Which event should be received by this endpoint

    Attributes:
        everything (bool | Unset): If true, the endpoint will receive all events related to the store. Default: True.
        specific_events (list[str] | Unset): If `everything` is false, the specific events that the endpoint is
            interested in. Current events are: `InvoiceCreated`, `InvoiceReceivedPayment`, `InvoiceProcessing`,
            `InvoiceExpired`, `InvoiceSettled`, `InvoiceInvalid`.
    """

    everything: bool | Unset = True
    specific_events: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        everything = self.everything

        specific_events: list[str] | Unset = UNSET
        if not isinstance(self.specific_events, Unset):
            specific_events = self.specific_events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if everything is not UNSET:
            field_dict["everything"] = everything
        if specific_events is not UNSET:
            field_dict["specificEvents"] = specific_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        everything = d.pop("everything", UNSET)

        specific_events = cast(list[str], d.pop("specificEvents", UNSET))

        webhook_data_base_authorized_events = cls(
            everything=everything,
            specific_events=specific_events,
        )

        webhook_data_base_authorized_events.additional_properties = d
        return webhook_data_base_authorized_events

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
