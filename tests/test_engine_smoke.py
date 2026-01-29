from offer_engine.engine import evaluate_offer

def test_evaluate_offer_returns_expected_shape():
    out = evaluate_offer({"pay_rate": 22, "hours": 34, "commute_minutes": 20})

    assert isinstance(out, dict)
    assert "approved" in out
    assert "score" in out
    assert "rules" in out
    assert "offer" in out
