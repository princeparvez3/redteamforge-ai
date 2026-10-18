"""JSONL data loader for RedTeamForge AI."""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ATTACKS_FILE = BASE_DIR / "data" / "raw" / "attacks.jsonl"
ATTACK_RESULTS_FILE = BASE_DIR / "data" / "raw" / "attack_results.jsonl"
CLASSIFIED_FILE = BASE_DIR / "data" / "analyzed" / "classified_results.jsonl"
BIAS_FILE = BASE_DIR / "data" / "analyzed" / "bias_results.jsonl"
AUDIT_FILE = BASE_DIR / "data" / "reports" / "safety_audit.jsonl"


def load_jsonl(file_path):
    """Load a JSONL file into a list of dictionaries."""
    path = Path(file_path)
    if not path.exists():
        return []
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON in {path.name}, line {line_number}: {exc}"
                ) from exc
    return records


def append_jsonl(file_path, record):
    """Append a single record to a JSONL file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")