from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_entry_data import LedgerEntryData


T = TypeVar("T", bound="TradeResultData")


@_attrs_define
class TradeResultData:
    """
    Example:
        {'fromAsset': 'USD', 'toAsset': 'BTC', 'ledgerEntries': [{'asset': 'BTC', 'qty': '1.23456', 'type': 'Trade'},
            {'asset': 'USD', 'qty': '-61728', 'type': 'Trade'}, {'asset': 'BTC', 'qty': '-0.00123456', 'type': 'Fee'},
            {'asset': 'KFEE', 'qty': '-123.456', 'type': 'Fee'}], 'tradeId': 'XXXX-XXXX-XXXX-XXXX', 'accountId':
            'xxxxxxxxxxxxxx', 'custodianCode': 'kraken'}

    Attributes:
        from_asset (str | Unset): The asset to trade.
        to_asset (str | Unset): The asset you want.
        ledger_entries (list[LedgerEntryData] | Unset): The asset entries that were changed during the trade. This is an
            array of at least 2 items with the asset sold and the asset gained. It may also include ledger entries for the
            costs of the trade and possibly exchange tokens used.
        trade_id (None | str | Unset): The unique ID of the trade used by the exchange. This ID can be used to get the
            details of this trade at a later time.
        account_id (str | Unset): The unique ID of the custodian account used.
        custodian_code (str | Unset): The code of the custodian used.
    """

    from_asset: str | Unset = UNSET
    to_asset: str | Unset = UNSET
    ledger_entries: list[LedgerEntryData] | Unset = UNSET
    trade_id: None | str | Unset = UNSET
    account_id: str | Unset = UNSET
    custodian_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_asset = self.from_asset

        to_asset = self.to_asset

        ledger_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ledger_entries, Unset):
            ledger_entries = []
            for ledger_entries_item_data in self.ledger_entries:
                ledger_entries_item = ledger_entries_item_data.to_dict()
                ledger_entries.append(ledger_entries_item)

        trade_id: None | str | Unset
        if isinstance(self.trade_id, Unset):
            trade_id = UNSET
        else:
            trade_id = self.trade_id

        account_id = self.account_id

        custodian_code = self.custodian_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_asset is not UNSET:
            field_dict["fromAsset"] = from_asset
        if to_asset is not UNSET:
            field_dict["toAsset"] = to_asset
        if ledger_entries is not UNSET:
            field_dict["ledgerEntries"] = ledger_entries
        if trade_id is not UNSET:
            field_dict["tradeId"] = trade_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if custodian_code is not UNSET:
            field_dict["custodianCode"] = custodian_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_entry_data import LedgerEntryData

        d = dict(src_dict)
        from_asset = d.pop("fromAsset", UNSET)

        to_asset = d.pop("toAsset", UNSET)

        _ledger_entries = d.pop("ledgerEntries", UNSET)
        ledger_entries: list[LedgerEntryData] | Unset = UNSET
        if _ledger_entries is not UNSET:
            ledger_entries = []
            for ledger_entries_item_data in _ledger_entries:
                ledger_entries_item = LedgerEntryData.from_dict(ledger_entries_item_data)

                ledger_entries.append(ledger_entries_item)

        def _parse_trade_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_id = _parse_trade_id(d.pop("tradeId", UNSET))

        account_id = d.pop("accountId", UNSET)

        custodian_code = d.pop("custodianCode", UNSET)

        trade_result_data = cls(
            from_asset=from_asset,
            to_asset=to_asset,
            ledger_entries=ledger_entries,
            trade_id=trade_id,
            account_id=account_id,
            custodian_code=custodian_code,
        )

        trade_result_data.additional_properties = d
        return trade_result_data

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
