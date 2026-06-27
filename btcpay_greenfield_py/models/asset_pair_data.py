from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetPairData")


@_attrs_define
class AssetPairData:
    """An asset pair we can trade.

    Example:
        {'assetBought': 'BTC', 'assetSold': 'USD', 'minimumTradeQty': 0.0001}

    Attributes:
        pair (str | Unset): The name of the asset pair.
        minimum_trade_qty (float | Unset): The smallest amount we can buy or sell.
    """

    pair: str | Unset = UNSET
    minimum_trade_qty: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pair = self.pair

        minimum_trade_qty = self.minimum_trade_qty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pair is not UNSET:
            field_dict["pair"] = pair
        if minimum_trade_qty is not UNSET:
            field_dict["minimumTradeQty"] = minimum_trade_qty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pair = d.pop("pair", UNSET)

        minimum_trade_qty = d.pop("minimumTradeQty", UNSET)

        asset_pair_data = cls(
            pair=pair,
            minimum_trade_qty=minimum_trade_qty,
        )

        asset_pair_data.additional_properties = d
        return asset_pair_data

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
