from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuoteResultData")


@_attrs_define
class QuoteResultData:
    """
    Example:
        {'fromAsset': 'USD', 'toAsset': 'BTC', 'bid': '30000.12', 'ask': '30002.24'}

    Attributes:
        from_asset (str | Unset): The asset to trade.
        to_asset (str | Unset): The asset you want.
        bid (str | Unset): The bid price.
        ask (str | Unset): The ask price
    """

    from_asset: str | Unset = UNSET
    to_asset: str | Unset = UNSET
    bid: str | Unset = UNSET
    ask: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_asset = self.from_asset

        to_asset = self.to_asset

        bid = self.bid

        ask = self.ask

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_asset is not UNSET:
            field_dict["fromAsset"] = from_asset
        if to_asset is not UNSET:
            field_dict["toAsset"] = to_asset
        if bid is not UNSET:
            field_dict["bid"] = bid
        if ask is not UNSET:
            field_dict["ask"] = ask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_asset = d.pop("fromAsset", UNSET)

        to_asset = d.pop("toAsset", UNSET)

        bid = d.pop("bid", UNSET)

        ask = d.pop("ask", UNSET)

        quote_result_data = cls(
            from_asset=from_asset,
            to_asset=to_asset,
            bid=bid,
            ask=ask,
        )

        quote_result_data.additional_properties = d
        return quote_result_data

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
