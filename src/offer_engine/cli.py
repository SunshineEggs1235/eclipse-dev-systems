from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import typer
from rich import print

# IMPORTANT:
# Your engine already returns a dict like:
# {'approved': False, 'score': 0, 'rules': {...}, 'offer': {...}}
from offer_engine.engine import evaluate_offer

app = typer.Typer(help="Offer Engine: evaluate offers using policy + rules.")


def print_json(obj: Any) -> None:
    """Pretty-print valid JSON (portfolio-grade output)."""
    print(json.dumps(obj, indent=2, sort_keys=True))


@app.command()
def eval(
    input_path: Path = typer.Argument(..., exists=True, readable=True, help="Path to JSON input"),
) -> None:
    """
    Evaluate an offer described by a JSON file and print the decision + rationale as JSON.
    """
    data: Dict[str, Any] = json.loads(input_path.read_text(encoding="utf-8"))
    result = evaluate_offer(data)
    print_json(result)


if __name__ == "__main__":
    app()
