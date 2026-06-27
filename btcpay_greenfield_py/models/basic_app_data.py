from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicAppData")


@_attrs_define
class BasicAppData:
    """
    Attributes:
        id (str | Unset): Id of the app Example: 3ki4jsAkN4u9rv1PUzj1odX4Nx7s.
        name (str | Unset): Name given to the app when it was created Example: my test app.
        store_id (str | Unset): Id of the store to which the app belongs Example:
            9CiNzKoANXxmk5ayZngSXrHTiVvvgCrwrpFQd4m2K776.
        created (int | Unset): UNIX timestamp for when the app was created Example: 1651554744.
        app_type (str | Unset): Type of the app which was created Example: PointOfSale.
        archived (bool | None | Unset): If true, the app does not appear in the apps list by default. Default: False.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    store_id: str | Unset = UNSET
    created: int | Unset = UNSET
    app_type: str | Unset = UNSET
    archived: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        store_id = self.store_id

        created = self.created

        app_type = self.app_type

        archived: bool | None | Unset
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if created is not UNSET:
            field_dict["created"] = created
        if app_type is not UNSET:
            field_dict["appType"] = app_type
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        store_id = d.pop("storeId", UNSET)

        created = d.pop("created", UNSET)

        app_type = d.pop("appType", UNSET)

        def _parse_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        archived = _parse_archived(d.pop("archived", UNSET))

        basic_app_data = cls(
            id=id,
            name=name,
            store_id=store_id,
            created=created,
            app_type=app_type,
            archived=archived,
        )

        basic_app_data.additional_properties = d
        return basic_app_data

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
