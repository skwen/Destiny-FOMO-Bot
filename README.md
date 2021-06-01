# Destiny-FOMO-Bot

## Development setup
### Local
1. Create a Python virtualenv (`python3.8 -m venv pyenv`)
2. Install dependencies (`pip install -r requirements.txt`)
### VSCode Remote Dev-Container
1. Install the **Remote - Containers** Extension (`ms-vscode-remote.remote-containers`). You may need to run Docker Desktop.
2. In the command palette, run **Remote-Containers: Open Folder in Container...** and select the main repository folder.

## Development use (Mod Checking locally):
1. Create an application at https://www.bungie.net/en/Application to get an API key, client ID, and client secret.
    * Choose "Confidential" for the OAuth Client Type
    * Choose "Private" for the Application Status
    * Check the following OAuth Scopes:
        * Read your Destiny 2 information (Vault, Inventory, and Vendors), as well as Destiny 1 Vault and Inventory data.
2. Set the redirect URL to https://127.0.0.1/
3. Modify config.ini and populate it with your values of "api_key", "client_id", and "client_secret"
4. Run sample.py and follow the instructions to supply the oauth code.
5. Enter the screen name of the account you are using to check the vendors.
6. The script will check the today's inventory of Banshee-44 for mods not in collections.

## Development use (Discord Bot)
1. Create an application at https://www.bungie.net/en/Application to get an API key and client ID.
2. Set the redirect URL to https://127.0.0.1/
3. Modify config.ini and populate it with your values of "api_key", "client_id", and "client_secret"
4. Create a discord bot at https://discord.com/developers/applications
5. Add the bot's token to config.ini
6. Get a user authorization token if you want mod checking functionality (necessary for vendor checking and comparing inventory as far as I know)
7. Run client.py

## Future Work (In roughly prioritized order)
Honestly, not positive right now, but for mod checking, the following needs to be done:
1. Check both Banshee-44 vendor and Ada-1 (and possibly seasonal vendors in the H.E.L.M.)
2. Add a web page and proper oauth handling so that the code does not need to be manually pasted
3. Figure out oauth refresh tokens so that authentication doesn't only last 1 hour
4. Containerize the process so that we don't need to modify files if deploying the process to a Cloud vendor

For Item info, the following would be beneficial:
1. Adding ability to see weapon slot
2. Adding perks information
