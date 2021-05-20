item_search = """
```
{0}
{2}
{3} RPM
{4} Damage
{5} Ammo
```

"""

item_image_uri = "https://www.bungie.net{0}"

def make_light_gg_link(item):
    name = item.name.replace(" ", "-")
    return "https://www.light.gg/db/items/{0}/{1}/".format(item.hash, name)