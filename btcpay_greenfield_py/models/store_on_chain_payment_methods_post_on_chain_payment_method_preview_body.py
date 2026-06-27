from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreOnChainPaymentMethodsPOSTOnChainPaymentMethodPreviewBody")


@_attrs_define
class StoreOnChainPaymentMethodsPOSTOnChainPaymentMethodPreviewBody:
    """
    Attributes:
        derivation_scheme (str | Unset): The derivation scheme Example: xpub....
    """

    derivation_scheme: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        derivation_scheme = self.derivation_scheme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if derivation_scheme is not UNSET:
            field_dict["derivationScheme"] = derivation_scheme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        derivation_scheme = d.pop("derivationScheme", UNSET)

        store_on_chain_payment_methods_post_on_chain_payment_method_preview_body = cls(
            derivation_scheme=derivation_scheme,
        )

        store_on_chain_payment_methods_post_on_chain_payment_method_preview_body.additional_properties = d
        return store_on_chain_payment_methods_post_on_chain_payment_method_preview_body

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
