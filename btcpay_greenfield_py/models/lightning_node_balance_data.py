from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offchain_balance_data import OffchainBalanceData
    from ..models.onchain_balance_data import OnchainBalanceData


T = TypeVar("T", bound="LightningNodeBalanceData")


@_attrs_define
class LightningNodeBalanceData:
    """
    Attributes:
        onchain (None | OnchainBalanceData | Unset): On-chain balance of the Lightning node
        offchain (None | OffchainBalanceData | Unset): Off-chain balance of the Lightning node
    """

    onchain: None | OnchainBalanceData | Unset = UNSET
    offchain: None | OffchainBalanceData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.offchain_balance_data import OffchainBalanceData
        from ..models.onchain_balance_data import OnchainBalanceData

        onchain: dict[str, Any] | None | Unset
        if isinstance(self.onchain, Unset):
            onchain = UNSET
        elif isinstance(self.onchain, OnchainBalanceData):
            onchain = self.onchain.to_dict()
        else:
            onchain = self.onchain

        offchain: dict[str, Any] | None | Unset
        if isinstance(self.offchain, Unset):
            offchain = UNSET
        elif isinstance(self.offchain, OffchainBalanceData):
            offchain = self.offchain.to_dict()
        else:
            offchain = self.offchain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if onchain is not UNSET:
            field_dict["onchain"] = onchain
        if offchain is not UNSET:
            field_dict["offchain"] = offchain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offchain_balance_data import OffchainBalanceData
        from ..models.onchain_balance_data import OnchainBalanceData

        d = dict(src_dict)

        def _parse_onchain(data: object) -> None | OnchainBalanceData | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                onchain_type_1 = OnchainBalanceData.from_dict(data)

                return onchain_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OnchainBalanceData | Unset, data)

        onchain = _parse_onchain(d.pop("onchain", UNSET))

        def _parse_offchain(data: object) -> None | OffchainBalanceData | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                offchain_type_1 = OffchainBalanceData.from_dict(data)

                return offchain_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OffchainBalanceData | Unset, data)

        offchain = _parse_offchain(d.pop("offchain", UNSET))

        lightning_node_balance_data = cls(
            onchain=onchain,
            offchain=offchain,
        )

        lightning_node_balance_data.additional_properties = d
        return lightning_node_balance_data

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
