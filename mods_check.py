#!/usr/bin/env python3

from bungie_api import BungieApi
from typing import Iterable, Tuple, Any
from api_types import Membership
from item_info import Item
from DestinyEnums import D2Vendors, DestinyItemType


def banshee_has_new_mod(bungie_api: BungieApi, membership: Membership) -> Tuple[Iterable[str], Iterable[Item]]:
    # get character info
    first_character_id = bungie_api.get_profile(membership)
    # get items vendor is selling for that character
    item_list = []
    mod_vendors = [D2Vendors.Banshee, D2Vendors.Ada]
    for vendor in mod_vendors:
        vendor_info = bungie_api.get_vendor(
            membership, first_character_id, vendor.value
        )
        item_sales = vendor_info["Response"]["sales"]["data"]
        for x in item_sales.values():
            item_hash = x["itemHash"]
            item_response = bungie_api.get_item_definition(item_hash)
            if "collectibleHash" in item_response["Response"].keys() and "itemType" in item_response["Response"].keys() and item_response["Response"]["itemType"] == DestinyItemType.Mod.value:
                item = Item(
                    item_response["Response"]["collectibleHash"],
                    item_response["Response"]["displayProperties"]["name"],
                )
                item_list.append(item)

    # look up item info
    collections_info = bungie_api.get_collections(membership)

    missing_mods = []
    for x in item_list:
        str_x = x.hash
        if str_x in collections_info.keys():
            if collections_info[str_x]["state"] & 0x1 == 1:
                missing_mods.append(x.name)
    return missing_mods, item_list
