# Destiny-FOMO-Bot

## Development use (Mod Checking locally):
1. Create an application at https://www.bungie.net/en/Application to get an API key and client ID.
2. Set the redirect URL to https://127.0.0.1/
3. Create auth_tokens.py and populate it with your values of "api_key", "client_id", and "client_secret" (use the example for help)
4. Go to https://www.bungie.net/en/OAuth/Authorize?client_id={your_client_id}&response_type=code and log-in properly
5. Copy the code from your redirected URL at https://127.0.0.1/?code={code}
6. uncomment test_script.py's main code block
7. Run test_script.py and supply the oauth code from step 5

## Development use (Discord Bot)
1. Create an application at https://www.bungie.net/en/Application to get an API key and client ID.
2. Set the redirect URL to https://127.0.0.1/
3. Create auth_tokens.py and populate it with your values of "api_key", "client_id", and "client_secret" (use the example for help)
4. Create a discord bot at https://discord.com/developers/applications
5. Add the bot's token to auth_tokens.py (use the example for help)
6. Get a user authorization token if you want mod checking functionality (necessary for vendor checking and comparing inventory as far as I know)
7. Run client.py

## Future Work (In roughly prioritized order)
Honestly, not positive right now, but for mod checking, the following needs to be done:
1. Switch vendor to Ada-1
2. Add a web page and proper oauth handling
3. Figure out oauth refresh tokens so that authentication doesn't only last 1 hour

For Item info, the following would be beneficial:
1. Adding ability to see weapon slot
2. Adding perks information
