from __future__ import annotations

from dataclasses import dataclass
from typing import List

from models import Offer, OfferType, PlayerProfile


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reasons: List[str]


class PolicyGuard:
    """
    Enforces Eclipse Templars' player-first monetization rules.

    The goal: prevent predatory monetization at the code level.
    """

    # Hard bans (placeholder: if you add other forbidden types later, put them here)
    BANNED_OFFER_TYPES = set()

    # Safety defaults
    MINIMUM_PLAYER_AGE = 13
    MAX_SESSIONS_BEFORE_REPEAT = 3

    def evaluate(self, player: PlayerProfile, offer: Offer) -> PolicyDecision:
        reasons: List[str] = []

        # --- Age safety ---
        if player.age < self.MINIMUM_PLAYER_AGE:
            reasons.append("Player is under minimum age for any monetized offers.")
            return PolicyDecision(allowed=False, reasons=reasons)

        # --- Offer type bans ---
        if offer.offer_type in self.BANNED_OFFER_TYPES:
            reasons.append(f"Offer type '{offer.offer_type.value}' is prohibited by policy.")
            return PolicyDecision(allowed=False, reasons=reasons)

        # --- Anti pay-to-win (structural safeguard) ---
        allowed_types = {OfferType.COSMETIC, OfferType.NARRATIVE, OfferType.QOL}
        if offer.offer_type not in allowed_types:
            reasons.append("Offer type is not permitted (non-cosmetic, non-narrative, non-QOL).")
            return PolicyDecision(allowed=False, reasons=reasons)

        # --- Anti-FOMO / cooldown enforcement ---
        if player.sessions_played < self.MAX_SESSIONS_BEFORE_REPEAT:
            reasons.append("Offer deferred to avoid FOMO or early-session pressure.")
            return PolicyDecision(allowed=False, reasons=reasons)

        reasons.append("Offer complies with all player-first monetization rules.")
        return PolicyDecision(allowed=True, reasons=reasons)
