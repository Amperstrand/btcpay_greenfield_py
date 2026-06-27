from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicePaymentMethodDataModelAdditionalDataType0")


@_attrs_define
class InvoicePaymentMethodDataModelAdditionalDataType0:
    """LNURL Pay information

    Attributes:
        provided_comment (None | str | Unset): The provided comment to a LNUrl payment with comments enabled Example:
            Thank you!.
        consumed_lightning_address (None | str | Unset): The consumed lightning address of a LN Address payment Example:
            customer@example.com.
    """

    provided_comment: None | str | Unset = UNSET
    consumed_lightning_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provided_comment: None | str | Unset
        if isinstance(self.provided_comment, Unset):
            provided_comment = UNSET
        else:
            provided_comment = self.provided_comment

        consumed_lightning_address: None | str | Unset
        if isinstance(self.consumed_lightning_address, Unset):
            consumed_lightning_address = UNSET
        else:
            consumed_lightning_address = self.consumed_lightning_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provided_comment is not UNSET:
            field_dict["providedComment"] = provided_comment
        if consumed_lightning_address is not UNSET:
            field_dict["consumedLightningAddress"] = consumed_lightning_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_provided_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provided_comment = _parse_provided_comment(d.pop("providedComment", UNSET))

        def _parse_consumed_lightning_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consumed_lightning_address = _parse_consumed_lightning_address(d.pop("consumedLightningAddress", UNSET))

        invoice_payment_method_data_model_additional_data_type_0 = cls(
            provided_comment=provided_comment,
            consumed_lightning_address=consumed_lightning_address,
        )

        invoice_payment_method_data_model_additional_data_type_0.additional_properties = d
        return invoice_payment_method_data_model_additional_data_type_0

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
