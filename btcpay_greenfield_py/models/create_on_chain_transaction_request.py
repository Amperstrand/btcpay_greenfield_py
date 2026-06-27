from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_on_chain_transaction_request_destination import CreateOnChainTransactionRequestDestination


T = TypeVar("T", bound="CreateOnChainTransactionRequest")


@_attrs_define
class CreateOnChainTransactionRequest:
    """
    Attributes:
        destinations (list[CreateOnChainTransactionRequestDestination] | Unset): What and where to send money
        feerate (float | Unset): Transaction fee.
        proceed_with_payjoin (bool | None | Unset): Whether to attempt to do a BIP78 payjoin if one of the destinations
            is a BIP21 with payjoin enabled Default: True.
        proceed_with_broadcast (bool | None | Unset): Whether to broadcast the transaction after creating it or to
            simply return the transaction in hex format. Default: True.
        no_change (bool | None | Unset): Whether to send all the spent coins to the destinations (THIS CAN COST YOU
            SIGNIFICANT AMOUNTS OF MONEY, LEAVE FALSE UNLESS YOU KNOW WHAT YOU ARE DOING). Default: False.
        rbf (bool | None | Unset): Whether to enable RBF for the transaction. Leave blank to have it random (beneficial
            to privacy)
        exclude_unconfirmed (bool | None | Unset): Whether to exclude unconfirmed UTXOs from the transaction. Default:
            False.
        selected_inputs (list[str] | None | Unset): Restrict the creation of the transactions from the outpoints
            provided ONLY (coin selection)
    """

    destinations: list[CreateOnChainTransactionRequestDestination] | Unset = UNSET
    feerate: float | Unset = UNSET
    proceed_with_payjoin: bool | None | Unset = True
    proceed_with_broadcast: bool | None | Unset = True
    no_change: bool | None | Unset = False
    rbf: bool | None | Unset = UNSET
    exclude_unconfirmed: bool | None | Unset = False
    selected_inputs: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        destinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = []
            for destinations_item_data in self.destinations:
                destinations_item = destinations_item_data.to_dict()
                destinations.append(destinations_item)

        feerate = self.feerate

        proceed_with_payjoin: bool | None | Unset
        if isinstance(self.proceed_with_payjoin, Unset):
            proceed_with_payjoin = UNSET
        else:
            proceed_with_payjoin = self.proceed_with_payjoin

        proceed_with_broadcast: bool | None | Unset
        if isinstance(self.proceed_with_broadcast, Unset):
            proceed_with_broadcast = UNSET
        else:
            proceed_with_broadcast = self.proceed_with_broadcast

        no_change: bool | None | Unset
        if isinstance(self.no_change, Unset):
            no_change = UNSET
        else:
            no_change = self.no_change

        rbf: bool | None | Unset
        if isinstance(self.rbf, Unset):
            rbf = UNSET
        else:
            rbf = self.rbf

        exclude_unconfirmed: bool | None | Unset
        if isinstance(self.exclude_unconfirmed, Unset):
            exclude_unconfirmed = UNSET
        else:
            exclude_unconfirmed = self.exclude_unconfirmed

        selected_inputs: list[str] | None | Unset
        if isinstance(self.selected_inputs, Unset):
            selected_inputs = UNSET
        elif isinstance(self.selected_inputs, list):
            selected_inputs = self.selected_inputs

        else:
            selected_inputs = self.selected_inputs

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if feerate is not UNSET:
            field_dict["feerate"] = feerate
        if proceed_with_payjoin is not UNSET:
            field_dict["proceedWithPayjoin"] = proceed_with_payjoin
        if proceed_with_broadcast is not UNSET:
            field_dict["proceedWithBroadcast"] = proceed_with_broadcast
        if no_change is not UNSET:
            field_dict["noChange"] = no_change
        if rbf is not UNSET:
            field_dict["rbf"] = rbf
        if exclude_unconfirmed is not UNSET:
            field_dict["excludeUnconfirmed"] = exclude_unconfirmed
        if selected_inputs is not UNSET:
            field_dict["selectedInputs"] = selected_inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_on_chain_transaction_request_destination import CreateOnChainTransactionRequestDestination

        d = dict(src_dict)
        _destinations = d.pop("destinations", UNSET)
        destinations: list[CreateOnChainTransactionRequestDestination] | Unset = UNSET
        if _destinations is not UNSET:
            destinations = []
            for destinations_item_data in _destinations:
                destinations_item = CreateOnChainTransactionRequestDestination.from_dict(destinations_item_data)

                destinations.append(destinations_item)

        feerate = d.pop("feerate", UNSET)

        def _parse_proceed_with_payjoin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        proceed_with_payjoin = _parse_proceed_with_payjoin(d.pop("proceedWithPayjoin", UNSET))

        def _parse_proceed_with_broadcast(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        proceed_with_broadcast = _parse_proceed_with_broadcast(d.pop("proceedWithBroadcast", UNSET))

        def _parse_no_change(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        no_change = _parse_no_change(d.pop("noChange", UNSET))

        def _parse_rbf(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        rbf = _parse_rbf(d.pop("rbf", UNSET))

        def _parse_exclude_unconfirmed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_unconfirmed = _parse_exclude_unconfirmed(d.pop("excludeUnconfirmed", UNSET))

        def _parse_selected_inputs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_inputs_type_0 = cast(list[str], data)

                return selected_inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        selected_inputs = _parse_selected_inputs(d.pop("selectedInputs", UNSET))

        create_on_chain_transaction_request = cls(
            destinations=destinations,
            feerate=feerate,
            proceed_with_payjoin=proceed_with_payjoin,
            proceed_with_broadcast=proceed_with_broadcast,
            no_change=no_change,
            rbf=rbf,
            exclude_unconfirmed=exclude_unconfirmed,
            selected_inputs=selected_inputs,
        )

        return create_on_chain_transaction_request
