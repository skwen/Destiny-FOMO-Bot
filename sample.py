#!/usr/bin/env python3
import configparser

from bungie_api import BungieApi
import mods_check


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    api = BungieApi(config["bungie"])

    print("Sample item search:")
    print(api.item_search("Sacred Provenance"))

    print(
        f"Go to https://www.bungie.net/en/OAuth/Authorize?client_id={config['bungie']['client_id']}&response_type=code to get your oauth code"
    )
    oauth_code = input("Auth code: ")
    if len(oauth_code.strip()) == 0:
        print("No code entered, assuming you've authed already")
    else:
        api.add_oauth_user(oauth_code)

    username = input("Enter your username: ")
    memberships = api.search_accounts(username)
    print(f"Found {len(memberships)} users matching {username}")
    for membership_id in api.filter_unknown_memberships(memberships):
        print("Banshee is selling the following mods you do not currently have:")
        print(mods_check.banshee_has_new_mod(api, membership_id))
