from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SLUGS = [
    "methode-de-test",
    "comment-nous-comparons",
    "a-propos",
    "contact",
    "transparence-affiliation",
    "mentions-legales",
]

for slug in SLUGS:
    path = ROOT / ".content" / "trust" / f"{slug}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("editorial_rules", {})["preserve_noindex"] = False
    if "qa" in data and "noindex_preserved" in data["qa"]:
        data["qa"]["noindex_preserved"] = False
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated", path)
