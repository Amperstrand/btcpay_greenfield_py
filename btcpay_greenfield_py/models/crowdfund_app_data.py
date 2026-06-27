from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crowdfund_app_data_perks import CrowdfundAppDataPerks


T = TypeVar("T", bound="CrowdfundAppData")


@_attrs_define
class CrowdfundAppData:
    """
    Attributes:
        id (str | Unset): Id of the app Example: 3ki4jsAkN4u9rv1PUzj1odX4Nx7s.
        name (str | Unset): Name given to the app when it was created Example: my test app.
        store_id (str | Unset): Id of the store to which the app belongs Example:
            9CiNzKoANXxmk5ayZngSXrHTiVvvgCrwrpFQd4m2K776.
        created (int | Unset): UNIX timestamp for when the app was created Example: 1651554744.
        app_type (str | Unset): Type of the app which was created Example: PointOfSale.
        archived (bool | None | Unset): If true, the app does not appear in the apps list by default. Default: False.
        title (str | Unset): Display title of the app Example: My crowdfund app.
        description (str | Unset): App description Example: My crowdfund description.
        enabled (bool | Unset): Whether the app is enabled to be viewed by everyone Example: True.
        enforce_target_amount (bool | Unset): Whether contributions over the set target amount are allowed
        start_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        end_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        target_currency (str | Unset): Target currency for the crowdfund Example: BTC.
        target_amount (float | Unset): Target amount for the crowdfund Example: 420.69.
        custom_css_link (str | Unset): Link to a custom CSS stylesheet to be used in the app
        main_image_url (str | Unset): URL for image used as a cover image for the app
        embedded_css (str | Unset): Custom CSS embedded into the app
        perks (CrowdfundAppDataPerks | Unset): JSON of perks available in the app Example: [{'description': None, 'id':
            'test perk', 'image': None, 'price': {'type': 2, 'formatted': '$100.00', 'value': 100}, 'title': 'test perk',
            'buyButtonText': None, 'inventory': None, 'paymentMethods': None, 'disabled': False}, {'description': 'this is
            an amazing perk', 'id': 'test test', 'image':
            'https://mainnet.demo.btcpayserver.org/img/errorpages/404_nicolas.jpg', 'price': {'type': 1, 'formatted':
            '$69.42', 'value': 69.42}, 'title': 'test test', 'buyButtonText': None, 'inventory': 5, 'paymentMethods': None,
            'disabled': False}, {'description': None, 'id': 'f$t45hj764325', 'image': None, 'price': {'type': 0,
            'formatted': None, 'value': None}, 'title': 'amazing perk', 'buyButtonText': 'button text', 'inventory': None,
            'paymentMethods': None, 'disabled': True}].
        notification_url (str | Unset): Callback notification url to POST to once when invoice is paid for and once when
            there are enough blockchain confirmations
        tagline (str | Unset): Tagline for the app displayed to user Example: I can't believe it's not butter.
        disqus_enabled (bool | Unset): Whether Disqus is enabled for the app
        disqus_shortname (str | Unset): Disqus shortname to used for the app
        sounds_enabled (bool | Unset): Whether sounds on new contributions are enabled
        animations_enabled (bool | Unset): Whether background animations on new contributions are enabled Example: True.
        reset_every_amount (float | Unset): Contribution goal reset frequency amount Example: 1.
        reset_every (str | Unset): Contribution goal reset frequency Example: Day.
        display_perks_value (bool | Unset): Whether perk values are displayed
        sort_perks_by_popularity (bool | Unset): Whether perks are sorted by popularity Default: True.
        sounds (list[str] | Unset): Array of custom sounds which can be used on new contributions Example:
            ['https://github.com/ClaudiuHKS/AdvancedQuakeSounds/raw/master/sound/AQS/doublekill.wav'].
        animation_colors (list[str] | Unset): Array of custom HEX colors which can be used for background animations on
            new contributions Example: ['#FF0000', '#00FF00', '#0000FF'].
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    store_id: str | Unset = UNSET
    created: int | Unset = UNSET
    app_type: str | Unset = UNSET
    archived: bool | None | Unset = False
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    enforce_target_amount: bool | Unset = UNSET
    start_date: float | Unset = UNSET
    end_date: float | Unset = UNSET
    target_currency: str | Unset = UNSET
    target_amount: float | Unset = UNSET
    custom_css_link: str | Unset = UNSET
    main_image_url: str | Unset = UNSET
    embedded_css: str | Unset = UNSET
    perks: CrowdfundAppDataPerks | Unset = UNSET
    notification_url: str | Unset = UNSET
    tagline: str | Unset = UNSET
    disqus_enabled: bool | Unset = UNSET
    disqus_shortname: str | Unset = UNSET
    sounds_enabled: bool | Unset = UNSET
    animations_enabled: bool | Unset = UNSET
    reset_every_amount: float | Unset = UNSET
    reset_every: str | Unset = UNSET
    display_perks_value: bool | Unset = UNSET
    sort_perks_by_popularity: bool | Unset = True
    sounds: list[str] | Unset = UNSET
    animation_colors: list[str] | Unset = UNSET
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

        title = self.title

        description = self.description

        enabled = self.enabled

        enforce_target_amount = self.enforce_target_amount

        start_date = self.start_date

        end_date = self.end_date

        target_currency = self.target_currency

        target_amount = self.target_amount

        custom_css_link = self.custom_css_link

        main_image_url = self.main_image_url

        embedded_css = self.embedded_css

        perks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.perks, Unset):
            perks = self.perks.to_dict()

        notification_url = self.notification_url

        tagline = self.tagline

        disqus_enabled = self.disqus_enabled

        disqus_shortname = self.disqus_shortname

        sounds_enabled = self.sounds_enabled

        animations_enabled = self.animations_enabled

        reset_every_amount = self.reset_every_amount

        reset_every = self.reset_every

        display_perks_value = self.display_perks_value

        sort_perks_by_popularity = self.sort_perks_by_popularity

        sounds: list[str] | Unset = UNSET
        if not isinstance(self.sounds, Unset):
            sounds = self.sounds

        animation_colors: list[str] | Unset = UNSET
        if not isinstance(self.animation_colors, Unset):
            animation_colors = self.animation_colors

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
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enforce_target_amount is not UNSET:
            field_dict["enforceTargetAmount"] = enforce_target_amount
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if target_currency is not UNSET:
            field_dict["targetCurrency"] = target_currency
        if target_amount is not UNSET:
            field_dict["targetAmount"] = target_amount
        if custom_css_link is not UNSET:
            field_dict["customCSSLink"] = custom_css_link
        if main_image_url is not UNSET:
            field_dict["mainImageUrl"] = main_image_url
        if embedded_css is not UNSET:
            field_dict["embeddedCSS"] = embedded_css
        if perks is not UNSET:
            field_dict["perks"] = perks
        if notification_url is not UNSET:
            field_dict["notificationUrl"] = notification_url
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if disqus_enabled is not UNSET:
            field_dict["disqusEnabled"] = disqus_enabled
        if disqus_shortname is not UNSET:
            field_dict["disqusShortname"] = disqus_shortname
        if sounds_enabled is not UNSET:
            field_dict["soundsEnabled"] = sounds_enabled
        if animations_enabled is not UNSET:
            field_dict["animationsEnabled"] = animations_enabled
        if reset_every_amount is not UNSET:
            field_dict["resetEveryAmount"] = reset_every_amount
        if reset_every is not UNSET:
            field_dict["resetEvery"] = reset_every
        if display_perks_value is not UNSET:
            field_dict["displayPerksValue"] = display_perks_value
        if sort_perks_by_popularity is not UNSET:
            field_dict["sortPerksByPopularity"] = sort_perks_by_popularity
        if sounds is not UNSET:
            field_dict["sounds"] = sounds
        if animation_colors is not UNSET:
            field_dict["animationColors"] = animation_colors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crowdfund_app_data_perks import CrowdfundAppDataPerks

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

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        enforce_target_amount = d.pop("enforceTargetAmount", UNSET)

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        target_currency = d.pop("targetCurrency", UNSET)

        target_amount = d.pop("targetAmount", UNSET)

        custom_css_link = d.pop("customCSSLink", UNSET)

        main_image_url = d.pop("mainImageUrl", UNSET)

        embedded_css = d.pop("embeddedCSS", UNSET)

        _perks = d.pop("perks", UNSET)
        perks: CrowdfundAppDataPerks | Unset
        if isinstance(_perks, Unset):
            perks = UNSET
        else:
            perks = CrowdfundAppDataPerks.from_dict(_perks)

        notification_url = d.pop("notificationUrl", UNSET)

        tagline = d.pop("tagline", UNSET)

        disqus_enabled = d.pop("disqusEnabled", UNSET)

        disqus_shortname = d.pop("disqusShortname", UNSET)

        sounds_enabled = d.pop("soundsEnabled", UNSET)

        animations_enabled = d.pop("animationsEnabled", UNSET)

        reset_every_amount = d.pop("resetEveryAmount", UNSET)

        reset_every = d.pop("resetEvery", UNSET)

        display_perks_value = d.pop("displayPerksValue", UNSET)

        sort_perks_by_popularity = d.pop("sortPerksByPopularity", UNSET)

        sounds = cast(list[str], d.pop("sounds", UNSET))

        animation_colors = cast(list[str], d.pop("animationColors", UNSET))

        crowdfund_app_data = cls(
            id=id,
            name=name,
            store_id=store_id,
            created=created,
            app_type=app_type,
            archived=archived,
            title=title,
            description=description,
            enabled=enabled,
            enforce_target_amount=enforce_target_amount,
            start_date=start_date,
            end_date=end_date,
            target_currency=target_currency,
            target_amount=target_amount,
            custom_css_link=custom_css_link,
            main_image_url=main_image_url,
            embedded_css=embedded_css,
            perks=perks,
            notification_url=notification_url,
            tagline=tagline,
            disqus_enabled=disqus_enabled,
            disqus_shortname=disqus_shortname,
            sounds_enabled=sounds_enabled,
            animations_enabled=animations_enabled,
            reset_every_amount=reset_every_amount,
            reset_every=reset_every,
            display_perks_value=display_perks_value,
            sort_perks_by_popularity=sort_perks_by_popularity,
            sounds=sounds,
            animation_colors=animation_colors,
        )

        crowdfund_app_data.additional_properties = d
        return crowdfund_app_data

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
