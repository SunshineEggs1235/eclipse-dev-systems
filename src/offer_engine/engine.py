def evaluate_offer(offer: dict) -> dict:
    """
    Evaluate an offer against simple policy rules.
    """

    rules = {
        "min_level": 10,
        "allowed_factions": ["Templar", "Sentinel"],
    }

    score = 0

    if offer.get("player_level", 0) >= rules["min_level"]:
        score += 1

    if offer.get("faction") in rules["allowed_factions"]:
        score += 1

    if offer.get("reputation", 0) >= 80:
        score += 1

    approved = score >= 2

    return {
        "approved": approved,
        "score": score,
        "rules": rules,
        "offer": offer,
    }
