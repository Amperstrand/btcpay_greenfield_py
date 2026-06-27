from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationHealthData")


@_attrs_define
class ApplicationHealthData:
    """
    Attributes:
        synchronized (bool | Unset): True if the instance is fully synchronized, according to NBXplorer
    """

    synchronized: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        synchronized = self.synchronized

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if synchronized is not UNSET:
            field_dict["synchronized"] = synchronized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        synchronized = d.pop("synchronized", UNSET)

        application_health_data = cls(
            synchronized=synchronized,
        )

        return application_health_data
