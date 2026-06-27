from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDeliveryData")


@_attrs_define
class WebhookDeliveryData:
    """
    Attributes:
        id (str | Unset): The id of the delivery
        timestamp (float | Unset): A unix timestamp in seconds Example: 1592312018.
        http_code (float | None | Unset): HTTP code received by the remote service, if any.
        error_message (str | Unset): User friendly error message, if any.
        status (str | Unset): Whether the delivery failed or not (possible values are: `Failed`, `HttpError`,
            `HttpSuccess`)
    """

    id: str | Unset = UNSET
    timestamp: float | Unset = UNSET
    http_code: float | None | Unset = UNSET
    error_message: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        timestamp = self.timestamp

        http_code: float | None | Unset
        if isinstance(self.http_code, Unset):
            http_code = UNSET
        else:
            http_code = self.http_code

        error_message = self.error_message

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if http_code is not UNSET:
            field_dict["httpCode"] = http_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        def _parse_http_code(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        http_code = _parse_http_code(d.pop("httpCode", UNSET))

        error_message = d.pop("errorMessage", UNSET)

        status = d.pop("status", UNSET)

        webhook_delivery_data = cls(
            id=id,
            timestamp=timestamp,
            http_code=http_code,
            error_message=error_message,
            status=status,
        )

        webhook_delivery_data.additional_properties = d
        return webhook_delivery_data

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
