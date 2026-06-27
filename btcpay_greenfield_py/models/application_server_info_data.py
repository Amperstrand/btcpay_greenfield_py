from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_server_info_sync_status_data import ApplicationServerInfoSyncStatusData


T = TypeVar("T", bound="ApplicationServerInfoData")


@_attrs_define
class ApplicationServerInfoData:
    """
    Attributes:
        version (str | Unset): BTCPay Server version
        onion (str | Unset): The Tor hostname
        supported_payment_methods (list[str] | Unset): The payment methods this server supports
        fully_synched (bool | Unset): True if the instance is fully synchronized, according to NBXplorer
        sync_status (list[ApplicationServerInfoSyncStatusData] | Unset):
    """

    version: str | Unset = UNSET
    onion: str | Unset = UNSET
    supported_payment_methods: list[str] | Unset = UNSET
    fully_synched: bool | Unset = UNSET
    sync_status: list[ApplicationServerInfoSyncStatusData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        onion = self.onion

        supported_payment_methods: list[str] | Unset = UNSET
        if not isinstance(self.supported_payment_methods, Unset):
            supported_payment_methods = self.supported_payment_methods

        fully_synched = self.fully_synched

        sync_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sync_status, Unset):
            sync_status = []
            for sync_status_item_data in self.sync_status:
                sync_status_item = sync_status_item_data.to_dict()
                sync_status.append(sync_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if onion is not UNSET:
            field_dict["onion"] = onion
        if supported_payment_methods is not UNSET:
            field_dict["supportedPaymentMethods"] = supported_payment_methods
        if fully_synched is not UNSET:
            field_dict["fullySynched"] = fully_synched
        if sync_status is not UNSET:
            field_dict["syncStatus"] = sync_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_server_info_sync_status_data import ApplicationServerInfoSyncStatusData

        d = dict(src_dict)
        version = d.pop("version", UNSET)

        onion = d.pop("onion", UNSET)

        supported_payment_methods = cast(list[str], d.pop("supportedPaymentMethods", UNSET))

        fully_synched = d.pop("fullySynched", UNSET)

        _sync_status = d.pop("syncStatus", UNSET)
        sync_status: list[ApplicationServerInfoSyncStatusData] | Unset = UNSET
        if _sync_status is not UNSET:
            sync_status = []
            for sync_status_item_data in _sync_status:
                sync_status_item = ApplicationServerInfoSyncStatusData.from_dict(sync_status_item_data)

                sync_status.append(sync_status_item)

        application_server_info_data = cls(
            version=version,
            onion=onion,
            supported_payment_methods=supported_payment_methods,
            fully_synched=fully_synched,
            sync_status=sync_status,
        )

        application_server_info_data.additional_properties = d
        return application_server_info_data

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
