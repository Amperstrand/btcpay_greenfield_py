from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnChainPaymentMethodDataPreview")


@_attrs_define
class OnChainPaymentMethodDataPreview:
    """
    Attributes:
        derivation_scheme (str | Unset): The derivation scheme Example: xpub....
        label (str | Unset): A label that will be shown in the UI
        account_key_path (str | Unset): The wallet fingerprint followed by the keypath to derive the account key used
            for signing operation or creating PSBTs Example: abcd82a1/84'/0'/0'.
        crypto_code (str | Unset): Crypto code of the payment method
    """

    derivation_scheme: str | Unset = UNSET
    label: str | Unset = UNSET
    account_key_path: str | Unset = UNSET
    crypto_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        derivation_scheme = self.derivation_scheme

        label = self.label

        account_key_path = self.account_key_path

        crypto_code = self.crypto_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if derivation_scheme is not UNSET:
            field_dict["derivationScheme"] = derivation_scheme
        if label is not UNSET:
            field_dict["label"] = label
        if account_key_path is not UNSET:
            field_dict["accountKeyPath"] = account_key_path
        if crypto_code is not UNSET:
            field_dict["cryptoCode"] = crypto_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        derivation_scheme = d.pop("derivationScheme", UNSET)

        label = d.pop("label", UNSET)

        account_key_path = d.pop("accountKeyPath", UNSET)

        crypto_code = d.pop("cryptoCode", UNSET)

        on_chain_payment_method_data_preview = cls(
            derivation_scheme=derivation_scheme,
            label=label,
            account_key_path=account_key_path,
            crypto_code=crypto_code,
        )

        on_chain_payment_method_data_preview.additional_properties = d
        return on_chain_payment_method_data_preview

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
