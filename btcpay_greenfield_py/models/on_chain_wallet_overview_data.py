from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnChainWalletOverviewData")


@_attrs_define
class OnChainWalletOverviewData:
    """
    Attributes:
        balance (str | Unset): The total current balance of the wallet
        unconfirmed_balance (str | Unset): The current unconfirmed balance of the wallet
        confirmed_balance (str | Unset): The current confirmed balance of the wallet
    """

    balance: str | Unset = UNSET
    unconfirmed_balance: str | Unset = UNSET
    confirmed_balance: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        unconfirmed_balance = self.unconfirmed_balance

        confirmed_balance = self.confirmed_balance

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if unconfirmed_balance is not UNSET:
            field_dict["unconfirmedBalance"] = unconfirmed_balance
        if confirmed_balance is not UNSET:
            field_dict["confirmedBalance"] = confirmed_balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        unconfirmed_balance = d.pop("unconfirmedBalance", UNSET)

        confirmed_balance = d.pop("confirmedBalance", UNSET)

        on_chain_wallet_overview_data = cls(
            balance=balance,
            unconfirmed_balance=unconfirmed_balance,
            confirmed_balance=confirmed_balance,
        )

        return on_chain_wallet_overview_data
