from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_entry_data import LedgerEntryData


T = TypeVar("T", bound="WithdrawalResultData")


@_attrs_define
class WithdrawalResultData:
    """
    Example:
        {'asset': 'BTC', 'paymentMethod': 'BTC-OnChain', 'ledgerEntries': [{'asset': 'BTC', 'qty': '-0.123456', 'type':
            'Withdrawal'}, {'asset': 'BTC', 'qty': '-0.005', 'type': 'Fee'}], 'withdrawalId': 'XXXX-XXXX-XXXX-XXXX',
            'accountId': 'xxxxxxxxxxxxxxx', 'custodianCode': 'kraken', 'status': 'Complete', 'transactionId':
            'xxxxxxxxxxxxxxx', 'targetAddress': 'bc1qxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}

    Attributes:
        asset (str | Unset): The asset that is being withdrawn.
        payment_method (str | Unset): The payment method that is used (crypto code + network).
        ledger_entries (list[LedgerEntryData] | Unset): The asset entries that were changed during the withdrawal. The
            first item is always the withdrawal itself. It could also includes ledger entries for the costs and may include
            credits or exchange tokens to give a discount.
        withdrawal_id (None | str | Unset): The unique ID of the withdrawal used by the exchange.
        account_id (str | Unset): The unique ID of the custodian account used.
        custodian_code (str | Unset): The code of the custodian used.
        status (str | Unset): The status of the withdrawal: 'Queued', 'Complete', 'Failed' or 'Unknown'.
        transaction_id (None | str | Unset): The transaction ID on the blockchain once the withdrawal has been executed.
        target_address (None | str | Unset): The address where the funds were sent to once the withdrawal has been
            executed.
    """

    asset: str | Unset = UNSET
    payment_method: str | Unset = UNSET
    ledger_entries: list[LedgerEntryData] | Unset = UNSET
    withdrawal_id: None | str | Unset = UNSET
    account_id: str | Unset = UNSET
    custodian_code: str | Unset = UNSET
    status: str | Unset = UNSET
    transaction_id: None | str | Unset = UNSET
    target_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset

        payment_method = self.payment_method

        ledger_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ledger_entries, Unset):
            ledger_entries = []
            for ledger_entries_item_data in self.ledger_entries:
                ledger_entries_item = ledger_entries_item_data.to_dict()
                ledger_entries.append(ledger_entries_item)

        withdrawal_id: None | str | Unset
        if isinstance(self.withdrawal_id, Unset):
            withdrawal_id = UNSET
        else:
            withdrawal_id = self.withdrawal_id

        account_id = self.account_id

        custodian_code = self.custodian_code

        status = self.status

        transaction_id: None | str | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        else:
            transaction_id = self.transaction_id

        target_address: None | str | Unset
        if isinstance(self.target_address, Unset):
            target_address = UNSET
        else:
            target_address = self.target_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset is not UNSET:
            field_dict["asset"] = asset
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if ledger_entries is not UNSET:
            field_dict["ledgerEntries"] = ledger_entries
        if withdrawal_id is not UNSET:
            field_dict["withdrawalId"] = withdrawal_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if custodian_code is not UNSET:
            field_dict["custodianCode"] = custodian_code
        if status is not UNSET:
            field_dict["status"] = status
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if target_address is not UNSET:
            field_dict["targetAddress"] = target_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_entry_data import LedgerEntryData

        d = dict(src_dict)
        asset = d.pop("asset", UNSET)

        payment_method = d.pop("paymentMethod", UNSET)

        _ledger_entries = d.pop("ledgerEntries", UNSET)
        ledger_entries: list[LedgerEntryData] | Unset = UNSET
        if _ledger_entries is not UNSET:
            ledger_entries = []
            for ledger_entries_item_data in _ledger_entries:
                ledger_entries_item = LedgerEntryData.from_dict(ledger_entries_item_data)

                ledger_entries.append(ledger_entries_item)

        def _parse_withdrawal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        withdrawal_id = _parse_withdrawal_id(d.pop("withdrawalId", UNSET))

        account_id = d.pop("accountId", UNSET)

        custodian_code = d.pop("custodianCode", UNSET)

        status = d.pop("status", UNSET)

        def _parse_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transaction_id = _parse_transaction_id(d.pop("transactionId", UNSET))

        def _parse_target_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_address = _parse_target_address(d.pop("targetAddress", UNSET))

        withdrawal_result_data = cls(
            asset=asset,
            payment_method=payment_method,
            ledger_entries=ledger_entries,
            withdrawal_id=withdrawal_id,
            account_id=account_id,
            custodian_code=custodian_code,
            status=status,
            transaction_id=transaction_id,
            target_address=target_address,
        )

        withdrawal_result_data.additional_properties = d
        return withdrawal_result_data

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
