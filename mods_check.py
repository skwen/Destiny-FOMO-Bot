#!/usr/bin/env python3

from item_info import Item
from DestinyEnums import D2Vendors


def banshee_has_new_mod(bungie_api, membership_id):
    # get character info
    first_character_id = bungie_api.get_profile(membership_id)
    # get items vendor is selling for that character
    banshee_vendor_info = bungie_api.get_vendor(
        membership_id, first_character_id, D2Vendors.Banshee.value
    )
    item_sales = banshee_vendor_info["Response"]["sales"]["data"]
    item_list = []
    for x in item_sales.values():
        item_hash = x["itemHash"]
        item_response = bungie_api.get_item_definition(item_hash)
        if "collectibleHash" in item_response["Response"].keys():
            item = Item(
                item_response["Response"]["collectibleHash"],
                item_response["Response"]["displayProperties"]["name"],
            )
            item_list.append(item)

    # look up item info
    collections_info = bungie_api.get_collections(membership_id)

    missing_mods = []
    for x in item_list:
        str_x = x.hash
        if str_x in collections_info.keys():
            if collections_info[str_x]["state"] & 0x1 == 1:
                missing_mods.append(x.name)
    return missing_mods
