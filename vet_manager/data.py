import json
from pathlib import Path
from typing import Any, Dict, List

DATA_FILE = Path(__file__).parent / "data.json"

def load_data() -> Dict[str, List[Dict[str, Any]]]:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"owners": [], "pets": [], "appointments": []}

def save_data(data: Dict[str, List[Dict[str, Any]]]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
