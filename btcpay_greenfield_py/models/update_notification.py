from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateNotification")


@_attrs_define
class UpdateNotification:
    """
    Attributes:
        seen (bool | None | Unset): Sets the notification as seen/unseen. If left null, sets it to the opposite value
    """

    seen: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        seen: bool | None | Unset
        if isinstance(self.seen, Unset):
            seen = UNSET
        else:
            seen = self.seen

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if seen is not UNSET:
            field_dict["seen"] = seen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_seen(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        seen = _parse_seen(d.pop("seen", UNSET))

        update_notification = cls(
            seen=seen,
        )

        return update_notification
