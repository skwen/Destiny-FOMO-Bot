#!/usr/bin/env python3
import os
import requests
import configparser

if __name__ == "__main__":
    # Read secrets/variables from a file mount
    CONFIG_PATH = os.getenv('CONFIG_PATH')
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    discord = config["discord"]

    BOT_TOKEN = discord['bot_token']
    BOT_ID = discord['bot_id']
    GUILD_ID = discord['guild_id']
    url = f"https://discord.com/api/v8/applications/{BOT_ID}/guilds/{GUILD_ID}/commands"

    cmdJson = {
        "name": "fomo",
        "description": "Temp",
        "options": [
            {
                "name": "register",
                "description": "Register the user",
                "type": 3,
                "required": False,
            },
        ]
    }

    headers = {
        "Authorization": f"Bot {BOT_TOKEN}"
    }

    r = requests.post(url, headers=headers, json=cmdJson)
    print(f'{r}')