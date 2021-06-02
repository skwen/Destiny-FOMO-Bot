from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Membership:
    displayName: str
    id: str
    type: int
