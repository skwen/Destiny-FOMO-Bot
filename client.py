#!/usr/bin/env python3
import discord
import re
import mods_check
import api
import auth_tokens
import DestinyEnums
import reply_strings


class FomoBotClient(discord.Client):
    def __init__(self, pattern):
        self.pattern = pattern
        super().__init__()

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        if message.content.startswith("!mods"):
            oauth_headers = {
                "X-API-Key": "API KEY HERE",
                "Authorization": "Bearer Auth Token Here",
            }
            membership_id = mods_check.search_account("Hegna")
            mods_list = mods_check.banshee_has_new_mod(oauth_headers, membership_id)
            await message.channel.send(
                "Banshee has the following mods you do not own: {0}".format(mods_list)
            )
        elif message.content.startswith("!mention"):
            await message.channel.send(
                "{0} here is your mention".format(message.author.mention)
            )
        elif pattern.search(message.content):
            item_found = mods_check.item_search(
                pattern.search(message.content).group(1)
            )
            # TODO(swen): Likely better to just return the string to reply with to the client, so that this class just handles discord interfacing
            item_definition = mods_check.get_item_definition(item_found.hash)
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


pattern = re.compile(r"\[\[(.*)\]\]")
client = FomoBotClient(pattern)
client.run(auth_tokens.discord_bot_token)
