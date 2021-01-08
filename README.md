# Destiny-FOMO-Bot

## Development use:
1. Create an application at https://www.bungie.net/en/Application to get an API key and client ID.
2. Set the redirect URL to https://127.0.0.1/
3. Create auth_tokens.py and populate it with your values of "api_key" and "client_id"
4. Go to https://www.bungie.net/en/OAuth/Authorize?client_id={your_client_id}&response_type=code and log-in properly
5. Copy the code from your redirected URL at https://127.0.0.1/?code={code}
6. Run test_script.py and supply the oauth code from step 5

## Future Work (In roughly prioritized order)
1. Add discord integration to tell people in discord when there are mods they're missing
2. Add a web page and proper oauth handling
3. Figure out oauth refresh tokens so that authentication doesn't only last 1 hour