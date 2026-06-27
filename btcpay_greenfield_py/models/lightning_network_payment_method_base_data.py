from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LightningNetworkPaymentMethodBaseData")


@_attrs_define
class LightningNetworkPaymentMethodBaseData:
    """
    Attributes:
        connection_string (str | Unset): The lightning connection string. Set to 'Internal Node' to use the internal
            node. (See [this doc](https://github.com/btcpayserver/BTCPayServer.Lightning/blob/master/README.md#examples) for
            some example) Example: type=clightning;server=....
    """

    connection_string: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        connection_string = self.connection_string

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if connection_string is not UNSET:
            field_dict["connectionString"] = connection_string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_string = d.pop("connectionString", UNSET)

        lightning_network_payment_method_base_data = cls(
            connection_string=connection_string,
        )

        return lightning_network_payment_method_base_data
