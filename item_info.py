from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Item:
    hash: str
    name: str
