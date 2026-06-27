from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationServerInfoNodeStatusDataType0")


@_attrs_define
class ApplicationServerInfoNodeStatusDataType0:
    """Detailed sync status of the internal full node

    Attributes:
        headers (int | Unset): The height of the chain of header of the internal full node
        blocks (int | Unset): The height of the latest validated block of the internal full node
        verification_progress (float | Unset): The current synchronization progress
    """

    headers: int | Unset = UNSET
    blocks: int | Unset = UNSET
    verification_progress: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers = self.headers

        blocks = self.blocks

        verification_progress = self.verification_progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if verification_progress is not UNSET:
            field_dict["verificationProgress"] = verification_progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        headers = d.pop("headers", UNSET)

        blocks = d.pop("blocks", UNSET)

        verification_progress = d.pop("verificationProgress", UNSET)

        application_server_info_node_status_data_type_0 = cls(
            headers=headers,
            blocks=blocks,
            verification_progress=verification_progress,
        )

        application_server_info_node_status_data_type_0.additional_properties = d
        return application_server_info_node_status_data_type_0

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
