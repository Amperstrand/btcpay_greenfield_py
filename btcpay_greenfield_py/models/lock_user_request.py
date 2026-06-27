from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LockUserRequest")


@_attrs_define
class LockUserRequest:
    """
    Attributes:
        locked (bool | Unset): Whether to lock or unlock the user
    """

    locked: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        locked = self.locked

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if locked is not UNSET:
            field_dict["locked"] = locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locked = d.pop("locked", UNSET)

        lock_user_request = cls(
            locked=locked,
        )

        return lock_user_request
