#!/usr/bin/env python3
import configparser
import re

from bungie_api import BungieApi
import discord
import mods_check
import DestinyEnums
import reply_strings


class FomoBotClient(discord.Client):
    def __init__(self, pattern, bungie_api_config):
        self.pattern = pattern
        self.api = BungieApi(bungie_api_config)
        super().__init__()

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        if message.content.startswith("!mods"):
            username = message.split(" ", maxsplit=1)[-1]
            membership_ids = self.api.search_accounts(username)
            print(f"Found {len(membership_ids)} users matching {username}")
            known_members = self.api.filter_unknown_memberships(membership_ids)
            if len(known_members) == 0:
                await message.channel.send(
                    f"No one by the {username} is authorized with me :("
                )
            # Pop someone off the set of known users (in most cases, it'll be length 1)
            membership_id = known_members.pop()
            mods_list = mods_check.banshee_has_new_mod(self.api, membership_id)
            await message.channel.send(
                f"Banshee has the following mods {membership_id} does not own: {mods_list}"
            )
        elif message.content.startswith("!mention"):
            await message.channel.send(
                "{0} here is your mention".format(message.author.mention)
            )
        elif pattern.search(message.content):
            item_found = self.api.item_search(pattern.search(message.content).group(1))
            # TODO(swen): Likely better to just return the string to reply with to the client, so that this class just handles discord interfacing
            item_definition = self.api.get_item_definition(item_found.hash)
            item_name = item_definition["Response"]["displayProperties"]["name"]
            item_icon = item_definition["Response"]["displayProperties"]["icon"]
            item_type = item_definition["Response"]["itemTypeAndTierDisplayName"]
            rpm = item_definition["Response"]["stats"]["stats"]["4284893193"]["value"]
            damage_type = DestinyEnums.DamageType(
                item_definition["Response"]["defaultDamageType"]
            ).name
            ammo_type = DestinyEnums.DestinyAmmunitionType(
                item_definition["Response"]["equippingBlock"]["ammoType"]
            ).name
            embed = discord.Embed(title=item_name, description=item_type)
            embed.set_image(url=reply_strings.item_image_uri.format(item_icon))
            embed.add_field(name="RPM", value=rpm)
            embed.add_field(name="Damage Type", value=damage_type)
            embed.add_field(name="Ammo Type", value=ammo_type)
            embed.add_field(
                name="light.gg", value=reply_strings.make_light_gg_link(item_found)
            )
            await message.channel.send(embed=embed)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")

    pattern = re.compile(r"\[\[(.*)\]\]")
    client = FomoBotClient(pattern, bungie_api_config=config["bungie"])
    client.run(config["discord"]["bot_token"])
