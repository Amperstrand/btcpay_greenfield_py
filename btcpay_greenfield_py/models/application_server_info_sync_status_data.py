from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_server_info_node_status_data_type_0 import ApplicationServerInfoNodeStatusDataType0


T = TypeVar("T", bound="ApplicationServerInfoSyncStatusData")


@_attrs_define
class ApplicationServerInfoSyncStatusData:
    """Detailed sync status

    Attributes:
        crypto_code (str | Unset): The CryptoCode of the crypto currency (eg. BTC) Example: BTC.
        node_information (ApplicationServerInfoNodeStatusDataType0 | None | Unset): Detailed sync status of the internal
            full node
        chain_height (int | Unset): The height of the chain of header of the internal indexer
        sync_height (float | None | Unset): The height of the latest indexed block of the internal indexer
        available (bool | Unset): True if the full node and the indexer are fully synchronized
    """

    crypto_code: str | Unset = UNSET
    node_information: ApplicationServerInfoNodeStatusDataType0 | None | Unset = UNSET
    chain_height: int | Unset = UNSET
    sync_height: float | None | Unset = UNSET
    available: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.application_server_info_node_status_data_type_0 import ApplicationServerInfoNodeStatusDataType0

        crypto_code = self.crypto_code

        node_information: dict[str, Any] | None | Unset
        if isinstance(self.node_information, Unset):
            node_information = UNSET
        elif isinstance(self.node_information, ApplicationServerInfoNodeStatusDataType0):
            node_information = self.node_information.to_dict()
        else:
            node_information = self.node_information

        chain_height = self.chain_height

        sync_height: float | None | Unset
        if isinstance(self.sync_height, Unset):
            sync_height = UNSET
        else:
            sync_height = self.sync_height

        available = self.available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_code is not UNSET:
            field_dict["cryptoCode"] = crypto_code
        if node_information is not UNSET:
            field_dict["nodeInformation"] = node_information
        if chain_height is not UNSET:
            field_dict["chainHeight"] = chain_height
        if sync_height is not UNSET:
            field_dict["syncHeight"] = sync_height
        if available is not UNSET:
            field_dict["available"] = available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_server_info_node_status_data_type_0 import ApplicationServerInfoNodeStatusDataType0

        d = dict(src_dict)
        crypto_code = d.pop("cryptoCode", UNSET)

        def _parse_node_information(data: object) -> ApplicationServerInfoNodeStatusDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_application_server_info_node_status_data_type_0 = (
                    ApplicationServerInfoNodeStatusDataType0.from_dict(data)
                )

                return componentsschemas_application_server_info_node_status_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplicationServerInfoNodeStatusDataType0 | None | Unset, data)

        node_information = _parse_node_information(d.pop("nodeInformation", UNSET))

        chain_height = d.pop("chainHeight", UNSET)

        def _parse_sync_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sync_height = _parse_sync_height(d.pop("syncHeight", UNSET))

        available = d.pop("available", UNSET)

        application_server_info_sync_status_data = cls(
            crypto_code=crypto_code,
            node_information=node_information,
            chain_height=chain_height,
            sync_height=sync_height,
            available=available,
        )

        application_server_info_sync_status_data.additional_properties = d
        return application_server_info_sync_status_data

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
