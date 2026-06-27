from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_crowdfund_app_request_reset_every import CreateCrowdfundAppRequestResetEvery
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCrowdfundAppRequest")


@_attrs_define
class CreateCrowdfundAppRequest:
    """
    Attributes:
        app_name (str | Unset): The name of the app (shown in admin UI) Example: Kukkstarter.
        title (None | str | Unset): The title of the app (shown to the user) Example: My crowdfund app.
        description (None | str | Unset): The description of the app (shown to the user) Example: My app description.
        enabled (bool | None | Unset): Determines if the app is enabled to be viewed by everyone Default: True.
        enforce_target_amount (bool | None | Unset): Will not allow contributions over the set target amount Default:
            False.
        start_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        end_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        target_currency (None | str | Unset): Target currency for the crowdfund. Defaults to the currency used by the
            store if not specified Example: BTC.
        target_amount (float | None | Unset): Target amount for the crowdfund Example: 420.
        custom_css_link (None | str | Unset): Link to a custom CSS stylesheet to be used in the app
        main_image_url (None | str | Unset): URL for image to be used as a cover image for the app
        embedded_css (None | str | Unset): Custom CSS to embed into the app
        perks_template (None | str | Unset): YAML template of perks available in the app Example: test_perk:
              price: 100
              title: test perk
              price_type: "fixed"
              disabled: false.
        notification_url (None | str | Unset): Callback notification url to POST to once when invoice is paid for and
            once when there are enough blockchain confirmations
        tagline (None | str | Unset): Tagline for the app (shown to the user) Example: I can't believe it's not butter.
        disqus_shortname (None | str | Unset): Disqus shortname to used for the app. Enables Disqus functionality if
            set.
        sounds_enabled (bool | None | Unset): Enables sounds on new contributions if set to true Default: False.
        animations_enabled (bool | None | Unset): Enables background animations on new contributions if set to true
            Default: False.
        reset_every_amount (float | None | Unset): Contribution goal reset frequency amount. Must be used in conjunction
            with resetEvery and startDate. Default: 1.0.
        reset_every (CreateCrowdfundAppRequestResetEvery | Unset): Contribution goal reset frequency. Must be used in
            conjunction with resetEveryAmount and startDate. Default: CreateCrowdfundAppRequestResetEvery.NEVER.
        display_perks_value (bool | None | Unset): Displays values of perks if set to true Default: False.
        sort_perks_by_popularity (bool | None | Unset): Sorts perks by popularity if set to true Default: False.
        sounds (list[str] | None | Unset): Array of custom sounds to use on new contributions Example:
            ['https://github.com/ClaudiuHKS/AdvancedQuakeSounds/raw/master/sound/AQS/doublekill.wav'].
        animation_colors (list[str] | None | Unset): Array of custom HEX colors to use for background animations on new
            contributions Example: ['#FF0000', '#00FF00', '#0000FF'].
    """

    app_name: str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | None | Unset = True
    enforce_target_amount: bool | None | Unset = False
    start_date: float | Unset = UNSET
    end_date: float | Unset = UNSET
    target_currency: None | str | Unset = UNSET
    target_amount: float | None | Unset = UNSET
    custom_css_link: None | str | Unset = UNSET
    main_image_url: None | str | Unset = UNSET
    embedded_css: None | str | Unset = UNSET
    perks_template: None | str | Unset = UNSET
    notification_url: None | str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    disqus_shortname: None | str | Unset = UNSET
    sounds_enabled: bool | None | Unset = False
    animations_enabled: bool | None | Unset = False
    reset_every_amount: float | None | Unset = 1.0
    reset_every: CreateCrowdfundAppRequestResetEvery | Unset = CreateCrowdfundAppRequestResetEvery.NEVER
    display_perks_value: bool | None | Unset = False
    sort_perks_by_popularity: bool | None | Unset = False
    sounds: list[str] | None | Unset = UNSET
    animation_colors: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        enforce_target_amount: bool | None | Unset
        if isinstance(self.enforce_target_amount, Unset):
            enforce_target_amount = UNSET
        else:
            enforce_target_amount = self.enforce_target_amount

        start_date = self.start_date

        end_date = self.end_date

        target_currency: None | str | Unset
        if isinstance(self.target_currency, Unset):
            target_currency = UNSET
        else:
            target_currency = self.target_currency

        target_amount: float | None | Unset
        if isinstance(self.target_amount, Unset):
            target_amount = UNSET
        else:
            target_amount = self.target_amount

        custom_css_link: None | str | Unset
        if isinstance(self.custom_css_link, Unset):
            custom_css_link = UNSET
        else:
            custom_css_link = self.custom_css_link

        main_image_url: None | str | Unset
        if isinstance(self.main_image_url, Unset):
            main_image_url = UNSET
        else:
            main_image_url = self.main_image_url

        embedded_css: None | str | Unset
        if isinstance(self.embedded_css, Unset):
            embedded_css = UNSET
        else:
            embedded_css = self.embedded_css

        perks_template: None | str | Unset
        if isinstance(self.perks_template, Unset):
            perks_template = UNSET
        else:
            perks_template = self.perks_template

        notification_url: None | str | Unset
        if isinstance(self.notification_url, Unset):
            notification_url = UNSET
        else:
            notification_url = self.notification_url

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        disqus_shortname: None | str | Unset
        if isinstance(self.disqus_shortname, Unset):
            disqus_shortname = UNSET
        else:
            disqus_shortname = self.disqus_shortname

        sounds_enabled: bool | None | Unset
        if isinstance(self.sounds_enabled, Unset):
            sounds_enabled = UNSET
        else:
            sounds_enabled = self.sounds_enabled

        animations_enabled: bool | None | Unset
        if isinstance(self.animations_enabled, Unset):
            animations_enabled = UNSET
        else:
            animations_enabled = self.animations_enabled

        reset_every_amount: float | None | Unset
        if isinstance(self.reset_every_amount, Unset):
            reset_every_amount = UNSET
        else:
            reset_every_amount = self.reset_every_amount

        reset_every: str | Unset = UNSET
        if not isinstance(self.reset_every, Unset):
            reset_every = self.reset_every.value

        display_perks_value: bool | None | Unset
        if isinstance(self.display_perks_value, Unset):
            display_perks_value = UNSET
        else:
            display_perks_value = self.display_perks_value

        sort_perks_by_popularity: bool | None | Unset
        if isinstance(self.sort_perks_by_popularity, Unset):
            sort_perks_by_popularity = UNSET
        else:
            sort_perks_by_popularity = self.sort_perks_by_popularity

        sounds: list[str] | None | Unset
        if isinstance(self.sounds, Unset):
            sounds = UNSET
        elif isinstance(self.sounds, list):
            sounds = self.sounds

        else:
            sounds = self.sounds

        animation_colors: list[str] | None | Unset
        if isinstance(self.animation_colors, Unset):
            animation_colors = UNSET
        elif isinstance(self.animation_colors, list):
            animation_colors = self.animation_colors

        else:
            animation_colors = self.animation_colors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
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
        if perks_template is not UNSET:
            field_dict["perksTemplate"] = perks_template
        if notification_url is not UNSET:
            field_dict["notificationUrl"] = notification_url
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
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
        d = dict(src_dict)
        app_name = d.pop("appName", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_enforce_target_amount(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enforce_target_amount = _parse_enforce_target_amount(d.pop("enforceTargetAmount", UNSET))

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        def _parse_target_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_currency = _parse_target_currency(d.pop("targetCurrency", UNSET))

        def _parse_target_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target_amount = _parse_target_amount(d.pop("targetAmount", UNSET))

        def _parse_custom_css_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_css_link = _parse_custom_css_link(d.pop("customCSSLink", UNSET))

        def _parse_main_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        main_image_url = _parse_main_image_url(d.pop("mainImageUrl", UNSET))

        def _parse_embedded_css(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedded_css = _parse_embedded_css(d.pop("embeddedCSS", UNSET))

        def _parse_perks_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        perks_template = _parse_perks_template(d.pop("perksTemplate", UNSET))

        def _parse_notification_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_url = _parse_notification_url(d.pop("notificationUrl", UNSET))

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))

        def _parse_disqus_shortname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disqus_shortname = _parse_disqus_shortname(d.pop("disqusShortname", UNSET))

        def _parse_sounds_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sounds_enabled = _parse_sounds_enabled(d.pop("soundsEnabled", UNSET))

        def _parse_animations_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        animations_enabled = _parse_animations_enabled(d.pop("animationsEnabled", UNSET))

        def _parse_reset_every_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reset_every_amount = _parse_reset_every_amount(d.pop("resetEveryAmount", UNSET))

        _reset_every = d.pop("resetEvery", UNSET)
        reset_every: CreateCrowdfundAppRequestResetEvery | Unset
        if isinstance(_reset_every, Unset):
            reset_every = UNSET
        else:
            reset_every = CreateCrowdfundAppRequestResetEvery(_reset_every)

        def _parse_display_perks_value(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        display_perks_value = _parse_display_perks_value(d.pop("displayPerksValue", UNSET))

        def _parse_sort_perks_by_popularity(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sort_perks_by_popularity = _parse_sort_perks_by_popularity(d.pop("sortPerksByPopularity", UNSET))

        def _parse_sounds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sounds_type_0 = cast(list[str], data)

                return sounds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        sounds = _parse_sounds(d.pop("sounds", UNSET))

        def _parse_animation_colors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                animation_colors_type_0 = cast(list[str], data)

                return animation_colors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        animation_colors = _parse_animation_colors(d.pop("animationColors", UNSET))

        create_crowdfund_app_request = cls(
            app_name=app_name,
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
            perks_template=perks_template,
            notification_url=notification_url,
            tagline=tagline,
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

        create_crowdfund_app_request.additional_properties = d
        return create_crowdfund_app_request

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
