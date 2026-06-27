from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_balance_data import AssetBalanceData
    from ..models.custodian_account_data_config_type_0 import CustodianAccountDataConfigType0


T = TypeVar("T", bound="CustodianAccountData")


@_attrs_define
class CustodianAccountData:
    """
    Example:
        {'accountId': 'xxxxxxxxxxxxxxx', 'storeId': 'xxxxxxxxxxxxxx', 'custodianCode': 'kraken', 'name': 'My Kraken
            Account', 'assetBalances': [{'asset': 'BTC', 'qty': '1.23456'}, {'asset': 'USD', 'qty': '123456.78'}], 'config':
            {'WithdrawToAddressNamePerPaymentMethod': {'BTC-OnChain': 'My Ledger Nano'}, 'ApiKey': 'xxx', 'PrivateKey':
            'xxx'}}

    Attributes:
        id (str | Unset): The unique code of the customer's account with this custodian. The format depends on the
            custodian.
        store_id (str | Unset): The store ID.
        custodian_code (str | Unset): The code for the custodian.
        name (str | Unset): The name of the custodian account.
        asset_balances (list[AssetBalanceData] | None | Unset): A real-time loaded list of all assets (fiat and crypto)
            on this custodian and the quantity held in the account. Assets with qty 0 can be omitted.
        config (CustodianAccountDataConfigType0 | None | Unset): The configuration of this custodian account. Specific
            contents depend on the custodian and your access permissions.
    """

    id: str | Unset = UNSET
    store_id: str | Unset = UNSET
    custodian_code: str | Unset = UNSET
    name: str | Unset = UNSET
    asset_balances: list[AssetBalanceData] | None | Unset = UNSET
    config: CustodianAccountDataConfigType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custodian_account_data_config_type_0 import CustodianAccountDataConfigType0

        id = self.id

        store_id = self.store_id

        custodian_code = self.custodian_code

        name = self.name

        asset_balances: list[dict[str, Any]] | None | Unset
        if isinstance(self.asset_balances, Unset):
            asset_balances = UNSET
        elif isinstance(self.asset_balances, list):
            asset_balances = []
            for asset_balances_type_0_item_data in self.asset_balances:
                asset_balances_type_0_item = asset_balances_type_0_item_data.to_dict()
                asset_balances.append(asset_balances_type_0_item)

        else:
            asset_balances = self.asset_balances

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, CustodianAccountDataConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if custodian_code is not UNSET:
            field_dict["custodianCode"] = custodian_code
        if name is not UNSET:
            field_dict["name"] = name
        if asset_balances is not UNSET:
            field_dict["assetBalances"] = asset_balances
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_balance_data import AssetBalanceData
        from ..models.custodian_account_data_config_type_0 import CustodianAccountDataConfigType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        store_id = d.pop("storeId", UNSET)

        custodian_code = d.pop("custodianCode", UNSET)

        name = d.pop("name", UNSET)

        def _parse_asset_balances(data: object) -> list[AssetBalanceData] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_balances_type_0 = []
                _asset_balances_type_0 = data
                for asset_balances_type_0_item_data in _asset_balances_type_0:
                    asset_balances_type_0_item = AssetBalanceData.from_dict(asset_balances_type_0_item_data)

                    asset_balances_type_0.append(asset_balances_type_0_item)

                return asset_balances_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetBalanceData] | None | Unset, data)

        asset_balances = _parse_asset_balances(d.pop("assetBalances", UNSET))

        def _parse_config(data: object) -> CustodianAccountDataConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = CustodianAccountDataConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustodianAccountDataConfigType0 | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        custodian_account_data = cls(
            id=id,
            store_id=store_id,
            custodian_code=custodian_code,
            name=name,
            asset_balances=asset_balances,
            config=config,
        )

        return custodian_account_data
