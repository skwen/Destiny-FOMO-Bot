import requests
from typing import Dict
from bungie_oauth import BungieOauth
from item_info import Item


class BungieApi:
    api_url_base = "https://www.bungie.net/Platform/"

    def __init__(self, config: Dict[str, str]):
        self.api_key = config["api_key"]
        self.client_id = config["client_id"]
        self.client_secret = config["client_secret"]

        self.api_key_header = {"X-API-Key": self.api_key}
        self.oauth = BungieOauth(self.api_key, self.client_id, self.client_secret)

    def search_account(self, name: str):
        search_uri = f"{self.api_url_base}Destiny2/SearchDestinyPlayer/3/{name}/"
        response = requests.get(search_uri, headers=self.api_key_header)

        if not response.ok:
            print("Account Search Error")
            print(response.content)
            return None
        response_object = response.json()
        return response_object["Response"][0]["membershipId"]

    def get_profile(self, membership_id):
        components = "100"
        uri = f"{self.api_url_base}Destiny2/3/Profile/{membership_id}/?components={components}"
        response = requests.get(
            uri, headers=self.oauth.get_oauth_headers(membership_id)
        )
        if not response.ok:
            print("Profile Error:")
            print(response.content)
            return None
        response_object = response.json()
        return response_object["Response"]["profile"]["data"]["characterIds"][0]

    def get_collections(self, membership_id):
        components = "800"
        uri = f"{self.api_url_base}Destiny2/3/Profile/{membership_id}/?components={components}"
        response = requests.get(
            uri, headers=self.oauth.get_oauth_headers(membership_id)
        )
        if not response.ok:
            print("Collections error:")
            print(response.content)
            return None

        response_object = response.json()
        return response_object["Response"]["profileCollectibles"]["data"][
            "collectibles"
        ]

    def get_vendor(self, membership_id, character_id, vendor_hash):
        components = "402"
        uri = f"{self.api_url_base}Destiny2/3/Profile/{membership_id}/Character/{character_id}/Vendors/{vendor_hash}/?components={components}"
        response = requests.get(
            uri, headers=self.oauth.get_oauth_headers(membership_id)
        )
        if not response.ok:
            print("Vendor error:")
            print(response.content)
            return None

        return response.json()

    def get_item_definition(self, hashidentifier):
        definition_uri = f"{self.api_url_base}Destiny2/Manifest/DestinyInventoryItemDefinition/{hashidentifier}/"
        response = requests.get(definition_uri, headers=self.api_key_header)
        if not response.ok:
            print("Item Definition Error:")
            print(response.content)
            return None

        return response.json()

    def item_search(self, search_term):
        search_uri = f"{self.api_url_base}Destiny2/Armory/Search/DestinyInventoryItemDefinition/{search_term}/"
        response = requests.get(search_uri, headers=self.api_key_header)
        if not response.ok:
            print("Item Definition Error:")
            print(response.content)
            return None

        response_object = response.json()
        if len(response_object["Response"]["results"]["results"]) == 0:
            return None
        else:
            return Item(
                response_object["Response"]["results"]["results"][0]["hash"],
                response_object["Response"]["results"]["results"][0][
                    "displayProperties"
                ]["name"],
            )
