from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_custodian_account_request_config_type_0 import CreateCustodianAccountRequestConfigType0


T = TypeVar("T", bound="CreateCustodianAccountRequest")


@_attrs_define
class CreateCustodianAccountRequest:
    """
    Example:
        {'accountId': 'xxxxxxxxxxxxxxx', 'storeId': 'xxxxxxxxxxxxxx', 'custodianCode': 'kraken', 'name': 'My Kraken
            Account', 'config': {'WithdrawToAddressNamePerPaymentMethod': {'BTC-OnChain': 'My Ledger Nano'}, 'ApiKey':
            'xxx', 'PrivateKey': 'xxx'}}

    Attributes:
        id (str | Unset): The unique code of the customer's account with this custodian. The format depends on the
            custodian.
        store_id (str | Unset): The store ID.
        custodian_code (str | Unset): The code for the custodian.
        name (str | Unset): The name of the custodian account.
        config (CreateCustodianAccountRequestConfigType0 | None | Unset): The configuration of this custodian account.
            Specific contents depend on the custodian and your access permissions.
    """

    id: str | Unset = UNSET
    store_id: str | Unset = UNSET
    custodian_code: str | Unset = UNSET
    name: str | Unset = UNSET
    config: CreateCustodianAccountRequestConfigType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_custodian_account_request_config_type_0 import CreateCustodianAccountRequestConfigType0

        id = self.id

        store_id = self.store_id

        custodian_code = self.custodian_code

        name = self.name

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, CreateCustodianAccountRequestConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if custodian_code is not UNSET:
            field_dict["custodianCode"] = custodian_code
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_custodian_account_request_config_type_0 import CreateCustodianAccountRequestConfigType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        store_id = d.pop("storeId", UNSET)

        custodian_code = d.pop("custodianCode", UNSET)

        name = d.pop("name", UNSET)

        def _parse_config(data: object) -> CreateCustodianAccountRequestConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = CreateCustodianAccountRequestConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateCustodianAccountRequestConfigType0 | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        create_custodian_account_request = cls(
            id=id,
            store_id=store_id,
            custodian_code=custodian_code,
            name=name,
            config=config,
        )

        return create_custodian_account_request
