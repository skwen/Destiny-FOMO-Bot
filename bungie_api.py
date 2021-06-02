import requests
from DestinyEnums import DestinyComponentType
from typing import Dict, Set, Iterable
from bungie_oauth import BungieOauth
from item_info import Item
from api_types import Membership

class BungieApi:
    api_url_base = "https://www.bungie.net/Platform/"

    def __init__(self, config: Dict[str, str]):
        self.api_key = config["api_key"]
        self.client_id = config["client_id"]
        self.client_secret = config["client_secret"]

        self.api_key_header = {"X-API-Key": self.api_key}
        self.oauth = BungieOauth(self.api_key, self.client_id, self.client_secret)

    def add_oauth_user(self, oauth_code: str) -> None:
        self.oauth.add_user(oauth_code)

    def filter_unknown_memberships(self, memberships: Iterable[Membership]) -> Set[Membership]:
        return self.oauth.filter_d2_memberships(memberships)

    def search_accounts(self, name: str) -> Set[Membership]:
        # https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType
        # Searching all platforms with -1
        search_uri = f"{self.api_url_base}Destiny2/SearchDestinyPlayer/-1/{name}/"
        response = requests.get(search_uri, headers=self.api_key_header)

        if not response.ok:
            print("Account Search Error")
            print(response.content)
            return None
        response_object = response.json()
        return {Membership(r["displayName"], r["membershipId"], r["membershipType"]) for r in response_object["Response"]}

    def get_component(self, membership: Membership, component: DestinyComponentType):
        uri = f"{self.api_url_base}Destiny2/{membership.type}/Profile/{membership.id}/?components={component.value}"
        response = requests.get(
            uri, headers=self.oauth.get_oauth_headers(membership.id)
        )
        if not response.ok:
            print(f"{component.name} Error:")
            print(response.content)
            return None
        return response.json()

    def get_profile(self, membership: Membership):
        response_object = self.get_component(membership, DestinyComponentType.Profiles)
        return response_object["Response"]["profile"]["data"]["characterIds"][0]

    def get_collections(self, membership: Membership):
        response_object = self.get_component(membership, DestinyComponentType.Collectibles)
        return response_object["Response"]["profileCollectibles"]["data"][
            "collectibles"
        ]

    def get_vendor(self, membership: Membership, character_id: str, vendor_hash: str):
        uri = f"{self.api_url_base}Destiny2/{membership.type}/Profile/{membership.id}/Character/{character_id}/Vendors/{vendor_hash}/?components={DestinyComponentType.VendorSales.value}"
        response = requests.get(
            uri, headers=self.oauth.get_oauth_headers(membership.id)
        )
        if not response.ok:
            print("Vendor error:")
            print(response.content)
            return None

        return response.json()

    def get_item_definition(self, hashidentifier: str):
        definition_uri = f"{self.api_url_base}Destiny2/Manifest/DestinyInventoryItemDefinition/{hashidentifier}/"
        response = requests.get(definition_uri, headers=self.api_key_header)
        if not response.ok:
            print("Item Definition Error:")
            print(response.content)
            return None

        return response.json()

    def item_search(self, search_term: str):
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
