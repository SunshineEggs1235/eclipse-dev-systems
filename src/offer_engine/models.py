from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class OfferType(str, Enum):
    COSMETIC = "cosmetic"
    NARRATIVE = "narrative"
    QOL = "quality_of_life"


@dataclass(frozen=True)
class Offer:
    id: str
    name: str
    offer_type: OfferType
    description: str


@dataclass
class PlayerProfile:
    player_id: str
    age: int
    playstyle: str  # e.g. "exploration", "stealth", "combat"
    preferred_modes: List[str] = field(default_factory=list)
    sessions_played: int = 0
