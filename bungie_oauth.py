import base64
import shelve
import datetime
import requests

from dataclasses import dataclass
from typing import Dict


@dataclass
class BungieOauthToken:
    access_token: str
    access_expires_at: datetime.datetime
    refresh_token: str
    refresh_expires_at: datetime.datetime


class BungieOauth:
    api_root = "https://www.bungie.net/Platform"
    token_uri = f"{api_root}/app/oauth/token/"

    def __init__(self, api_key, client_id, client_secret):
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        auth = base64.b64encode(f"{client_id}:{client_secret}".encode("ascii"))
        self.api_headers = {
            "X-API-Key": api_key,
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {auth.decode('ascii')}",
        }

        self.token_file = f"{client_id}-oauth_tokens.pyshelf"

    def get_token(self, membership_id) -> BungieOauthToken:
        with shelve.open(self.token_file) as db:
            if membership_id not in db:
                raise Exception(f"{membership_id} not found, re-register user")
            token: BungieOauthToken = db[membership_id]
        if token.access_expires_at < datetime.datetime.utcnow():
            return self.renew_token(membership_id)
        with shelve.open(self.token_file) as db:
            return db[membership_id]

    def renew_token(self, membership_id) -> BungieOauthToken:
        with shelve.open(self.token_file) as db:
            if membership_id not in db:
                raise Exception(f"{membership_id} not found, re-register user")
            token: BungieOauthToken = db[membership_id]
        if token.refresh_expires_at < datetime.datetime.utcnow():
            raise Exception(f"{membership_id} has passed the refresh time")

        data = {
            "grant_type": "refresh_token",
            "refresh_token": token.refresh_token,
        }
        return self.set_token(data, "renewing token")

    def add_user(self, oauth_code) -> BungieOauthToken:
        data = {
            "grant_type": "authorization_code",
            "code": oauth_code,
        }
        return self.set_token(data, "adding new user")

    def set_token(self, data: Dict[str, str], action: str) -> BungieOauthToken:
        r = requests.post(
            self.token_uri,
            headers=self.api_headers,
            data=data,
        )

        if not r.ok:
            print(f"Failed to get token when {action}")
            r.raise_for_status()

        json_dict = r.json()
        token = self.json_dict_to_token(json_dict)

        with shelve.open(self.token_file) as db:
            db[json_dict["membership_id"]] = token

        return token

    def get_oauth_headers(self, membership_id: str) -> Dict[str, str]:
        token = self.get_token(membership_id)

        return {
            "X-API-Key": self.api_key,
            "Authorization": f"Bearer {token.access_token}",
        }

    @staticmethod
    def json_dict_to_token(t: Dict[str, str]) -> BungieOauthToken:
        return BungieOauthToken(
            t["access_token"],
            datetime.datetime.utcnow() + datetime.timedelta(seconds=t["expires_in"]),
            t["refresh_token"],
            datetime.datetime.utcnow()
            + datetime.timedelta(seconds=t["refresh_expires_in"]),
        )
