#!/usr/bin/env python3
import discord
import mods_check

class FomoBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if (message.content.startswith('!mods')):
            oauth_headers = {'X-API-Key': 'API KEY HERE', 'Authorization': 'Bearer Auth Token Here'}
            membership_id = mods_check.search_account('Hegna')
            mods_list = mods_check.banshee_has_new_mod(oauth_headers, membership_id)
            await message.channel.send('Banshee has the following mods you do not own: {0}'.format(mods_list))
        elif(message.content.startswith('!mention')):
            await message.channel.send('{0} here is your mention'.format(message.author.mention))

client = FomoBotClient()
client.run('Discord bot token here')