from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_data import LabelData


T = TypeVar("T", bound="OnChainWalletUTXOData")


@_attrs_define
class OnChainWalletUTXOData:
    """
    Attributes:
        comment (str | Unset): A comment linked to this utxo
        amount (str | Unset): the value of this utxo
        link (str | Unset): a link to the configured blockchain explorer to view the utxo
        outpoint (str | Unset): outpoint of this utxo
        timestamp (float | Unset): A unix timestamp in seconds Example: 1592312018.
        key_path (str | Unset): the derivation path in relation to the HD account
        address (str | Unset): The wallet address of this utxo
        confirmations (float | Unset): The number of confirmations of this utxo
        labels (list[LabelData] | Unset): Labels linked to this transaction
    """

    comment: str | Unset = UNSET
    amount: str | Unset = UNSET
    link: str | Unset = UNSET
    outpoint: str | Unset = UNSET
    timestamp: float | Unset = UNSET
    key_path: str | Unset = UNSET
    address: str | Unset = UNSET
    confirmations: float | Unset = UNSET
    labels: list[LabelData] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        amount = self.amount

        link = self.link

        outpoint = self.outpoint

        timestamp = self.timestamp

        key_path = self.key_path

        address = self.address

        confirmations = self.confirmations

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if amount is not UNSET:
            field_dict["amount"] = amount
        if link is not UNSET:
            field_dict["link"] = link
        if outpoint is not UNSET:
            field_dict["outpoint"] = outpoint
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if key_path is not UNSET:
            field_dict["keyPath"] = key_path
        if address is not UNSET:
            field_dict["address"] = address
        if confirmations is not UNSET:
            field_dict["confirmations"] = confirmations
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_data import LabelData

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        amount = d.pop("amount", UNSET)

        link = d.pop("link", UNSET)

        outpoint = d.pop("outpoint", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        key_path = d.pop("keyPath", UNSET)

        address = d.pop("address", UNSET)

        confirmations = d.pop("confirmations", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[LabelData] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LabelData.from_dict(labels_item_data)

                labels.append(labels_item)

        on_chain_wallet_utxo_data = cls(
            comment=comment,
            amount=amount,
            link=link,
            outpoint=outpoint,
            timestamp=timestamp,
            key_path=key_path,
            address=address,
            confirmations=confirmations,
            labels=labels,
        )

        return on_chain_wallet_utxo_data
