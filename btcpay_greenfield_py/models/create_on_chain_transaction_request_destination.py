from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOnChainTransactionRequestDestination")


@_attrs_define
class CreateOnChainTransactionRequestDestination:
    """
    Attributes:
        destination (str | Unset): A wallet address or a BIP21 payment link
        amount (None | str | Unset): The amount to send. If `destination` is a BIP21 link, the amount must be the same
            or null.
        subtract_from_amount (bool | Unset): Whether to subtract the transaction fee from the provided amount. This
            makes the receiver receive less, or in other words: he or she pays the transaction fee. Also useful if you want
            to clear out your wallet. Must be false if `destination` is a BIP21 link
    """

    destination: str | Unset = UNSET
    amount: None | str | Unset = UNSET
    subtract_from_amount: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        subtract_from_amount = self.subtract_from_amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if amount is not UNSET:
            field_dict["amount"] = amount
        if subtract_from_amount is not UNSET:
            field_dict["subtractFromAmount"] = subtract_from_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination = d.pop("destination", UNSET)

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        subtract_from_amount = d.pop("subtractFromAmount", UNSET)

        create_on_chain_transaction_request_destination = cls(
            destination=destination,
            amount=amount,
            subtract_from_amount=subtract_from_amount,
        )

        return create_on_chain_transaction_request_destination
