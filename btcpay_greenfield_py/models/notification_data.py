from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationData")


@_attrs_define
class NotificationData:
    """
    Attributes:
        id (str | Unset): The id of the notification
        identifier (str | Unset): The identifier of the notification
        type_ (str | Unset): The type of the notification
        body (str | Unset): The html body of the notifications
        link (None | str | Unset): The link of the notification
        created_time (float | Unset): A unix timestamp in seconds Example: 1592312018.
        seen (bool | Unset): If the notification has been seen by the user
    """

    id: str | Unset = UNSET
    identifier: str | Unset = UNSET
    type_: str | Unset = UNSET
    body: str | Unset = UNSET
    link: None | str | Unset = UNSET
    created_time: float | Unset = UNSET
    seen: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        identifier = self.identifier

        type_ = self.type_

        body = self.body

        link: None | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        created_time = self.created_time

        seen = self.seen

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if body is not UNSET:
            field_dict["body"] = body
        if link is not UNSET:
            field_dict["link"] = link
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if seen is not UNSET:
            field_dict["seen"] = seen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        type_ = d.pop("type", UNSET)

        body = d.pop("body", UNSET)

        def _parse_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link = _parse_link(d.pop("link", UNSET))

        created_time = d.pop("createdTime", UNSET)

        seen = d.pop("seen", UNSET)

        notification_data = cls(
            id=id,
            identifier=identifier,
            type_=type_,
            body=body,
            link=link,
            created_time=created_time,
            seen=seen,
        )

        return notification_data
