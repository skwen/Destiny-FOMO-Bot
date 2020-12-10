api_token = '08833c369fb7488b876951c83e24c427'
api_url_base = 'https://www.bungie.net/Platform/'

oauth_code = '97e9d1e8e8ae585cedfd376ce6ac9911' # temp oauth code for dev
client_id = '34928'
access_token = 'CPPaAhKGAgAgmnbGDs0wsDQGDg05Hi8woo4tXTNeeyCcgJOAD62nhODgAAAAZEhjJoUMBh5UBpuvQSwEcM3+ijUpzuzCI6peP032/zyfw+iq50CXceyCzEZXRN5Yq26pFvvk6KgcX6FHFPbIyfkpM9MGPauhJlFtgljRs3IBbhpD2O/dwX2eFAZcDUR8hL1bbJThEWRDaXltCsxKRure9qbHUH6bkw7o58KJIriemYRQaVpyLLrWAUogE1l7HY366n23/6+uQ0sKUJEB69JmL5aAqu3GBA7cwZo5sadEJYq0lqS5vaYX39tG19hJHYCw3dTSS4MwRC7a14AulfECykyPblQwuFZMO5+KAEI='

headers = {'X-API-Key': api_token, 'Authorization': 'Bearer {0}'.format(access_token)}
post_data = {'code': oauth_code}