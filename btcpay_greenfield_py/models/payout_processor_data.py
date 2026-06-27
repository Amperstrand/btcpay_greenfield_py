from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayoutProcessorData")


@_attrs_define
class PayoutProcessorData:
    """
    Attributes:
        name (str | Unset): unique identifier of the payout processor
        friendly_name (str | Unset): Human name of the payout processor
        payment_methods (list[str] | None | Unset): Supported, payment methods by this processor
    """

    name: str | Unset = UNSET
    friendly_name: str | Unset = UNSET
    payment_methods: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        friendly_name = self.friendly_name

        payment_methods: list[str] | None | Unset
        if isinstance(self.payment_methods, Unset):
            payment_methods = UNSET
        elif isinstance(self.payment_methods, list):
            payment_methods = self.payment_methods

        else:
            payment_methods = self.payment_methods

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        def _parse_payment_methods(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_methods_type_0 = cast(list[str], data)

                return payment_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        payment_methods = _parse_payment_methods(d.pop("paymentMethods", UNSET))

        payout_processor_data = cls(
            name=name,
            friendly_name=friendly_name,
            payment_methods=payment_methods,
        )

        return payout_processor_data
