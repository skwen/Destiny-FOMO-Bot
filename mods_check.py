#!/usr/bin/env python3

import api
import json
import requests

def search_account(name):
    search_uri = '{0}Destiny2/SearchDestinyPlayer/3/{1}/'.format(api.api_url_base, name)
    response = requests.get(search_uri, headers=api.headers)

    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        return response_object['Response'][0]['membershipId']
    else:
        return None

def get_oauth_token():
    token_uri = 'https://www.bungie.net/platform/app/oauth/token/'
    response = requests.post(token_uri,headers=api.headers, json={'grant_type': 'authorization_code', 'code': api.oauth_code})
    print(response.status_code)
    print(response.text)

def get_profile(membership_id):
    profile_uri = '{0}Destiny2/3/Profile/{1}/?components={2}'.format(api.api_url_base, membership_id, '100')
    response = requests.get(profile_uri, headers=api.headers)
    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        return response_object['Response']['profile']['data']['characterIds'][0]
    else:
        return None

def get_vendors(membership_id, character_id):
    vendors_uri = '{0}Destiny2/3/Profile/{1}/Character/{2}/Vendors/?components={3}'.format(api.api_url_base, membership_id, character_id, '400,402')
    response = requests.get(vendors_uri, headers=api.headers, )
    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        print(response_object)
        # return response_object['Response']['profile']['data']['characterIds'][0]
    else:
        print(response.content)
        return None
    return None

# membership_id = search_account('Hegna')
# first_character_id = get_profile(membership_id)
# get_vendors(membership_id, first_character_id)
get_oauth_token()