from enum import Enum

class DestinyAmmunitionType(Enum):
    NoType = 0
    Primary = 1
    Special = 2
    Heavy = 3
    Unknown = 4

class DamageType(Enum):
    NoType = 0
    Kinetic = 1
    Arc = 2
    Solar = 3
    Void = 4
    Raid = 5
    Stasis = 6