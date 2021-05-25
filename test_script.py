#!/usr/bin/env python3
import mods_check
import api

# user_oauth_code = input('Please enter your OAuth Code:')
# oauth_headers = api.get_headers(user_oauth_code)
# membership_id = mods_check.search_account('Hegna')
# print('Banshee is selling the following mods you do not currently have: ')
# print(mods_check.banshee_has_new_mod(oauth_headers, membership_id))

mods_check.item_search("Sacred Provenance")
