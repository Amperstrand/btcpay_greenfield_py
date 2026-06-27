from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnChainPaymentMethodBaseData")


@_attrs_define
class OnChainPaymentMethodBaseData:
    """
    Attributes:
        derivation_scheme (str | Unset): The derivation scheme Example: xpub....
        label (str | Unset): A label that will be shown in the UI
        account_key_path (str | Unset): The wallet fingerprint followed by the keypath to derive the account key used
            for signing operation or creating PSBTs Example: abcd82a1/84'/0'/0'.
    """

    derivation_scheme: str | Unset = UNSET
    label: str | Unset = UNSET
    account_key_path: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        derivation_scheme = self.derivation_scheme

        label = self.label

        account_key_path = self.account_key_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if derivation_scheme is not UNSET:
            field_dict["derivationScheme"] = derivation_scheme
        if label is not UNSET:
            field_dict["label"] = label
        if account_key_path is not UNSET:
            field_dict["accountKeyPath"] = account_key_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        derivation_scheme = d.pop("derivationScheme", UNSET)

        label = d.pop("label", UNSET)

        account_key_path = d.pop("accountKeyPath", UNSET)

        on_chain_payment_method_base_data = cls(
            derivation_scheme=derivation_scheme,
            label=label,
            account_key_path=account_key_path,
        )

        return on_chain_payment_method_base_data
