# See https://bungie-net.github.io/
from enum import Enum

# https://bungie-net.github.io/#/components/schemas/Destiny.DestinyAmmunitionType
class DestinyAmmunitionType(Enum):
    NoType = 0
    Primary = 1
    Special = 2
    Heavy = 3
    Unknown = 4


# https://bungie-net.github.io/#/components/schemas/Destiny.DamageType
class DamageType(Enum):
    NoType = 0
    Kinetic = 1
    Arc = 2
    Solar = 3
    Void = 4
    Raid = 5
    Stasis = 6

class D2Vendors(Enum):
    Banshee = 672118013

# https://bungie-net.github.io/#/components/schemas/BungieMembershipType
class BungieMembershipType(Enum):
    All = -1
    NoType = 0
    TigerXbox = 1
    TigerPsn = 2
    TigerSteam = 3
    TigerBlizzard = 4
    TigerStadia = 5
    TigerDemon = 10
    BungieNext = 254

# https://bungie-net.github.io/#/components/schemas/Destiny.DestinyComponentType
class DestinyComponentType(Enum):
    NoType = 0
    Profiles = 100
    VendorReceipts = 101
    ProfileInventories = 102
    ProfileCurrencies = 103
    ProfileProgression = 104
    PlatformSilver = 105
    Characters = 200
    CharacterInventories = 201
    CharacterProgressions = 202
    CharacterRenderData = 203
    CharacterActivities = 204
    CharacterEquipment = 205
    ItemInstances = 300
    ItemObjectives = 301
    ItemPerks = 302
    ItemRenderData = 303
    ItemStats = 304
    ItemSockets = 305
    ItemTalentGrids = 306
    ItemCommonData = 307
    ItemPlugStates = 308
    ItemPlugObjectives = 309
    ItemReusablePlugs = 310
    Vendors = 400
    VendorCategories = 401
    VendorSales = 402
    Kiosks = 500
    CurrencyLookups = 600
    PresentationNodes = 700
    Collectibles = 800
    Records = 900
    Transitory = 1000
    Metrics = 1100
    StringVariables = 1200