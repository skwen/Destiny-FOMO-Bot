#!/usr/bin/env python3

import api
from item_info import Item
import json
import requests

def search_account(name):
    search_uri = '{0}Destiny2/SearchDestinyPlayer/3/{1}/'.format(api.api_url_base, name)
    response = requests.get(search_uri, headers=api.api_key_headers)

    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        return response_object['Response'][0]['membershipId']
    else:
        print('Account Search Error')
        print(response.content)
        return None

def get_profile(oauth_headers, membership_id):
    profile_uri = '{0}Destiny2/3/Profile/{1}/?components={2}'.format(api.api_url_base, membership_id, '100')
    response = requests.get(profile_uri, headers=oauth_headers)
    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        return response_object['Response']['profile']['data']['characterIds'][0]
    else:
        print('Profile Error:')
        print(response.content)
        return None

def get_collections(oauth_headers, membership_id):
    profile_uri = '{0}Destiny2/3/Profile/{1}/?components={2}'.format(api.api_url_base, membership_id, '800')
    response = requests.get(profile_uri, headers=oauth_headers)
    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        return response_object['Response']['profileCollectibles']['data']['collectibles']
    else:
        print('Collections error:')
        print(response.content)
        return None

def get_vendor(oauth_headers, membership_id, character_id, vendor_hash):
    vendors_uri = '{0}Destiny2/3/Profile/{1}/Character/{2}/Vendors/{3}/?components={4}'.format(api.api_url_base, membership_id, character_id, vendor_hash, '402')
    response = requests.get(vendors_uri, headers=oauth_headers)
    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        return response_object
    else:
        print('Vendor error:')
        print(response.content)
        return None

def get_item_definition(hashidentifier):
    definition_uri = '{0}Destiny2/Manifest/DestinyInventoryItemDefinition/{1}/'.format(api.api_url_base, hashidentifier)
    response = requests.get(definition_uri, headers=api.api_key_headers)
    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        print(response.content.decode('utf-8'))
        return response_object
    else:
        print('Item Definition Error:')
        print(response.content)
        return None
    return None

def item_search(search_term):
    search_uri = '{0}Destiny2/Armory/Search/DestinyInventoryItemDefinition/{1}/'.format(api.api_url_base, search_term)
    response = requests.get(search_uri, headers=api.api_key_headers)
    if response.status_code == 200:
            response_object = json.loads(response.content.decode('utf-8'))
            if len(response_object['Response']['results']['results']) == 0:
                return None
            else:
                return Item(response_object['Response']['results']['results'][0]['hash'], response_object['Response']['results']['results'][0]['displayProperties']['name'])
    else:
        print('Item Definition Error:')
        print(response.content)
        return None
    return None

def banshee_has_new_mod(oauth_headers, membership_id):
    # get character info
    first_character_id = get_profile(oauth_headers, membership_id)
    # get items vendor is selling for that character
    banshee_vendor_info = get_vendor(oauth_headers, membership_id, first_character_id, '672118013')
    item_sales = banshee_vendor_info['Response']['sales']['data']
    item_list = []
    for x in item_sales.values():
        item_hash = x['itemHash']
        item_response = get_item_definition(oauth_headers, item_hash)
        if 'collectibleHash' in  item_response['Response'].keys():
            item = Item(item_response['Response']['collectibleHash'], item_response['Response']['displayProperties']['name'])
            item_list.append(item)

    # look up item info
    collections_info = get_collections(oauth_headers, membership_id)
    # print(collections_info)

    missing_mods = []
    for x in item_list:
        str_x = x.hash
        if str_x in collections_info.keys():
            if collections_info[str_x]['state'] & 0x1 == 1:
                missing_mods.append(x.name)
    return missing_mods

# use to dump request info to a file to manually investigate if needed
# vendor_file = open("vendorFile{0}.json".format(vendor_hash), "w")
# vendor_file.write(json.dumps(response_object, indent=4, sort_keys=True))
# vendor_file.close()