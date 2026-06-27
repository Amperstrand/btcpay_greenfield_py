from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_pair_data import AssetPairData


T = TypeVar("T", bound="CustodianData")


@_attrs_define
class CustodianData:
    """
    Example:
        {'code': 'kraken', 'name': 'Kraken', 'tradableAssetPairs': {'BTC/USD': {'assetBought': 'BTC', 'assetSold':
            'USD', 'minimumTradeQty': 0.001}, 'BTC/EUR': {'assetBought': 'BTC', 'assetSold': 'EUR', 'minimumTradeQty':
            0.001}, 'LTC/USD': {'assetBought': 'LTC', 'assetSold': 'USD', 'minimumTradeQty': 0.05}, 'LTC/EUR':
            {'assetBought': 'LTC', 'assetSold': 'EUR', 'minimumTradeQty': 0.05}}, 'withdrawablePaymentMethods': ['BTC-
            OnChain', 'LTC-OnChain'], 'depositablePaymentMethods': ['BTC-OnChain', 'LTC-OnChain']}

    Attributes:
        code (str | Unset): The unique code of the custodian.
        label (str | Unset): The name of the custodian.
        depositable_payment_methods (list[str] | Unset): A list of payment methods (crypto code + network) you can
            deposit to the custodian.
        withdrawable_payment_methods (list[str] | Unset): A list of payment methods (crypto code + network) you can
            withdraw from the custodian.
        tradable_asset_pairs (list[AssetPairData] | None | Unset): A list of tradable asset pair objects, or NULL if the
            custodian cannot trades/convert assets.
    """

    code: str | Unset = UNSET
    label: str | Unset = UNSET
    depositable_payment_methods: list[str] | Unset = UNSET
    withdrawable_payment_methods: list[str] | Unset = UNSET
    tradable_asset_pairs: list[AssetPairData] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        label = self.label

        depositable_payment_methods: list[str] | Unset = UNSET
        if not isinstance(self.depositable_payment_methods, Unset):
            depositable_payment_methods = self.depositable_payment_methods

        withdrawable_payment_methods: list[str] | Unset = UNSET
        if not isinstance(self.withdrawable_payment_methods, Unset):
            withdrawable_payment_methods = self.withdrawable_payment_methods

        tradable_asset_pairs: list[dict[str, Any]] | None | Unset
        if isinstance(self.tradable_asset_pairs, Unset):
            tradable_asset_pairs = UNSET
        elif isinstance(self.tradable_asset_pairs, list):
            tradable_asset_pairs = []
            for tradable_asset_pairs_type_0_item_data in self.tradable_asset_pairs:
                tradable_asset_pairs_type_0_item = tradable_asset_pairs_type_0_item_data.to_dict()
                tradable_asset_pairs.append(tradable_asset_pairs_type_0_item)

        else:
            tradable_asset_pairs = self.tradable_asset_pairs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if label is not UNSET:
            field_dict["label"] = label
        if depositable_payment_methods is not UNSET:
            field_dict["depositablePaymentMethods"] = depositable_payment_methods
        if withdrawable_payment_methods is not UNSET:
            field_dict["withdrawablePaymentMethods"] = withdrawable_payment_methods
        if tradable_asset_pairs is not UNSET:
            field_dict["tradableAssetPairs"] = tradable_asset_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_pair_data import AssetPairData

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        label = d.pop("label", UNSET)

        depositable_payment_methods = cast(list[str], d.pop("depositablePaymentMethods", UNSET))

        withdrawable_payment_methods = cast(list[str], d.pop("withdrawablePaymentMethods", UNSET))

        def _parse_tradable_asset_pairs(data: object) -> list[AssetPairData] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tradable_asset_pairs_type_0 = []
                _tradable_asset_pairs_type_0 = data
                for tradable_asset_pairs_type_0_item_data in _tradable_asset_pairs_type_0:
                    tradable_asset_pairs_type_0_item = AssetPairData.from_dict(tradable_asset_pairs_type_0_item_data)

                    tradable_asset_pairs_type_0.append(tradable_asset_pairs_type_0_item)

                return tradable_asset_pairs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetPairData] | None | Unset, data)

        tradable_asset_pairs = _parse_tradable_asset_pairs(d.pop("tradableAssetPairs", UNSET))

        custodian_data = cls(
            code=code,
            label=label,
            depositable_payment_methods=depositable_payment_methods,
            withdrawable_payment_methods=withdrawable_payment_methods,
            tradable_asset_pairs=tradable_asset_pairs,
        )

        custodian_data.additional_properties = d
        return custodian_data

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
