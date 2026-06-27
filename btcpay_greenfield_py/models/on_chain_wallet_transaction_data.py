from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.transaction_status import TransactionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_data import LabelData


T = TypeVar("T", bound="OnChainWalletTransactionData")


@_attrs_define
class OnChainWalletTransactionData:
    """
    Attributes:
        transaction_hash (None | str | Unset): The transaction id
        comment (str | Unset): A comment linked to the transaction
        amount (str | Unset): The amount the wallet balance changed with this transaction
        block_hash (None | str | Unset): The hash of the block that confirmed this transaction. Null if still
            unconfirmed.
        block_height (None | str | Unset): The height of the block that confirmed this transaction. Null if still
            unconfirmed.
        confirmations (None | str | Unset): The number of confirmations for this transaction
        timestamp (float | Unset): A unix timestamp in seconds Example: 1592312018.
        status (TransactionStatus | Unset):
        labels (list[LabelData] | Unset): Labels linked to this transaction
    """

    transaction_hash: None | str | Unset = UNSET
    comment: str | Unset = UNSET
    amount: str | Unset = UNSET
    block_hash: None | str | Unset = UNSET
    block_height: None | str | Unset = UNSET
    confirmations: None | str | Unset = UNSET
    timestamp: float | Unset = UNSET
    status: TransactionStatus | Unset = UNSET
    labels: list[LabelData] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        transaction_hash: None | str | Unset
        if isinstance(self.transaction_hash, Unset):
            transaction_hash = UNSET
        else:
            transaction_hash = self.transaction_hash

        comment = self.comment

        amount = self.amount

        block_hash: None | str | Unset
        if isinstance(self.block_hash, Unset):
            block_hash = UNSET
        else:
            block_hash = self.block_hash

        block_height: None | str | Unset
        if isinstance(self.block_height, Unset):
            block_height = UNSET
        else:
            block_height = self.block_height

        confirmations: None | str | Unset
        if isinstance(self.confirmations, Unset):
            confirmations = UNSET
        else:
            confirmations = self.confirmations

        timestamp = self.timestamp

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if transaction_hash is not UNSET:
            field_dict["transactionHash"] = transaction_hash
        if comment is not UNSET:
            field_dict["comment"] = comment
        if amount is not UNSET:
            field_dict["amount"] = amount
        if block_hash is not UNSET:
            field_dict["blockHash"] = block_hash
        if block_height is not UNSET:
            field_dict["blockHeight"] = block_height
        if confirmations is not UNSET:
            field_dict["confirmations"] = confirmations
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_data import LabelData

        d = dict(src_dict)

        def _parse_transaction_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transaction_hash = _parse_transaction_hash(d.pop("transactionHash", UNSET))

        comment = d.pop("comment", UNSET)

        amount = d.pop("amount", UNSET)

        def _parse_block_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_hash = _parse_block_hash(d.pop("blockHash", UNSET))

        def _parse_block_height(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_height = _parse_block_height(d.pop("blockHeight", UNSET))

        def _parse_confirmations(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmations = _parse_confirmations(d.pop("confirmations", UNSET))

        timestamp = d.pop("timestamp", UNSET)

        _status = d.pop("status", UNSET)
        status: TransactionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TransactionStatus(_status)

        _labels = d.pop("labels", UNSET)
        labels: list[LabelData] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LabelData.from_dict(labels_item_data)

                labels.append(labels_item)

        on_chain_wallet_transaction_data = cls(
            transaction_hash=transaction_hash,
            comment=comment,
            amount=amount,
            block_hash=block_hash,
            block_height=block_height,
            confirmations=confirmations,
            timestamp=timestamp,
            status=status,
            labels=labels,
        )

        return on_chain_wallet_transaction_data
