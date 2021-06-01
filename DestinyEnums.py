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
    Ada = 350061650
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

# https://bungie-net.github.io/#/components/schemas/Destiny.DestinyItemType
class DestinyItemType(Enum):
    NoType = 0
    Currency = 1
    Armor = 2
    Weapon = 3
    Message = 7
    Engram = 8
    Consumable = 9
    ExchangeMaterial = 10
    MissionReward = 11
    QuestStep = 12
    QuestStepComplete = 13
    Emblem = 14
    Quest = 15
    Subclass = 16
    ClanBanner = 17
    Aura = 18
    Mod = 19
    Dummy = 20
    Ship = 21
    Vehicle = 22
    Emote = 23
    Ghost = 24
    Package = 25
    Bounty = 26
    Wrapper = 27
    SeasonalArtifact = 28
    Finisher = 29
