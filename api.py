import auth_tokens
import requests
import json

api_url_base = 'https://www.bungie.net/Platform/'

api_key_headers = {'X-API-Key': auth_tokens.api_key}

def get_headers(user_oauth_code):
    token_uri = 'https://www.bungie.net/platform/app/oauth/token/'
    response = requests.post(token_uri,headers=api_key_headers, data={'grant_type': 'authorization_code', 'code': user_oauth_code, 'client_id': auth_tokens.client_id})
    if response.status_code == 200:
        response_object = json.loads(response.content.decode('utf-8'))
        access_token = response_object['access_token']
        return {'X-API-Key': auth_tokens.api_key, 'Authorization': 'Bearer {0}'.format(access_token)}

# TODO: Figure out how to get refresh tokens to work. Don't seem to have enough info right now
# def get_refresh_token(oauth_, refresh_token):
#     refresh_uri = '{0}app/OAuth/token/'.format(api_url_base)
#     response = requests.post(refresh_uri, headers=api_key_headers, data={'grant_type': 'refresh_token', 'refresh_token': refresh_token})
#     return response