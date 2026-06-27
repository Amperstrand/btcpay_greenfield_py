from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_payment_method_data_data_type_2 import GenericPaymentMethodDataDataType2
    from ..models.lightning_network_payment_method_base_data import LightningNetworkPaymentMethodBaseData
    from ..models.on_chain_payment_method_base_data import OnChainPaymentMethodBaseData


T = TypeVar("T", bound="GenericPaymentMethodData")


@_attrs_define
class GenericPaymentMethodData:
    """
    Attributes:
        enabled (bool | Unset): Whether the payment method is enabled
        crypto_code (str | Unset): The currency code of the payment method
        data (GenericPaymentMethodDataDataType2 | LightningNetworkPaymentMethodBaseData | OnChainPaymentMethodBaseData |
            Unset): Associated dynamic data based on payment method type.
    """

    enabled: bool | Unset = UNSET
    crypto_code: str | Unset = UNSET
    data: (
        GenericPaymentMethodDataDataType2 | LightningNetworkPaymentMethodBaseData | OnChainPaymentMethodBaseData | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.lightning_network_payment_method_base_data import LightningNetworkPaymentMethodBaseData
        from ..models.on_chain_payment_method_base_data import OnChainPaymentMethodBaseData

        enabled = self.enabled

        crypto_code = self.crypto_code

        data: dict[str, Any] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, OnChainPaymentMethodBaseData):
            data = self.data.to_dict()
        elif isinstance(self.data, LightningNetworkPaymentMethodBaseData):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if crypto_code is not UNSET:
            field_dict["cryptoCode"] = crypto_code
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_payment_method_data_data_type_2 import GenericPaymentMethodDataDataType2
        from ..models.lightning_network_payment_method_base_data import LightningNetworkPaymentMethodBaseData
        from ..models.on_chain_payment_method_base_data import OnChainPaymentMethodBaseData

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        crypto_code = d.pop("cryptoCode", UNSET)

        def _parse_data(
            data: object,
        ) -> (
            GenericPaymentMethodDataDataType2
            | LightningNetworkPaymentMethodBaseData
            | OnChainPaymentMethodBaseData
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = OnChainPaymentMethodBaseData.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = LightningNetworkPaymentMethodBaseData.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_2 = GenericPaymentMethodDataDataType2.from_dict(data)

            return data_type_2

        data = _parse_data(d.pop("data", UNSET))

        generic_payment_method_data = cls(
            enabled=enabled,
            crypto_code=crypto_code,
            data=data,
        )

        return generic_payment_method_data
