from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LightningNetworkPaymentMethodData")


@_attrs_define
class LightningNetworkPaymentMethodData:
    """
    Attributes:
        connection_string (str | Unset): The lightning connection string. Set to 'Internal Node' to use the internal
            node. (See [this doc](https://github.com/btcpayserver/BTCPayServer.Lightning/blob/master/README.md#examples) for
            some example) Example: type=clightning;server=....
        enabled (bool | Unset): Whether the payment method is enabled
        crypto_code (str | Unset): Crypto code of the payment method
        payment_method (str | Unset): The payment method
    """

    connection_string: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    crypto_code: str | Unset = UNSET
    payment_method: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_string = self.connection_string

        enabled = self.enabled

        crypto_code = self.crypto_code

        payment_method = self.payment_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_string is not UNSET:
            field_dict["connectionString"] = connection_string
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if crypto_code is not UNSET:
            field_dict["cryptoCode"] = crypto_code
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_string = d.pop("connectionString", UNSET)

        enabled = d.pop("enabled", UNSET)

        crypto_code = d.pop("cryptoCode", UNSET)

        payment_method = d.pop("paymentMethod", UNSET)

        lightning_network_payment_method_data = cls(
            connection_string=connection_string,
            enabled=enabled,
            crypto_code=crypto_code,
            payment_method=payment_method,
        )

        lightning_network_payment_method_data.additional_properties = d
        return lightning_network_payment_method_data

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
