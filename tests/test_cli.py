import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import argparse
import json
from vet_manager import cli


def test_add_owner(tmp_path, monkeypatch):
    temp_data = tmp_path / "data.json"
    monkeypatch.setattr(cli, "load_data", lambda: {"owners": [], "pets": [], "appointments": []})
    monkeypatch.setattr(cli, "save_data", lambda d: json.dump(d, open(temp_data, "w")))
    cli.add_owner(argparse.Namespace(name="Alice", contact="123", func=None))
    saved = json.load(open(temp_data))
    assert saved["owners"][0]["name"] == "Alice"
