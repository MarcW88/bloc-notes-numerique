#!/usr/bin/env python3
import json
from pathlib import Path
from guide_visual_catalog import VISUALS
from guide_visual_overrides import NON_TABULAR_OVERRIDES

ROOT = Path(__file__).resolve().parent
OUT = ROOT / ".content" / "visuals"
OUT.mkdir(parents=True, exist_ok=True)

visuals = dict(VISUALS)
visuals.update(NON_TABULAR_OVERRIDES)

for slug, data in visuals.items():
    spec = dict(data)
    spec["id"] = f"{slug}-{spec['type'].replace('_', '-')}"
    spec["page_url"] = f"/guides/{slug}/"
    spec["output"] = f"assets/guides/{slug}/{spec['id']}.svg"
    spec.setdefault("canvas", {"width": 1200, "height": 700})
    path = OUT / f"{slug}.json"
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("manifest", path.relative_to(ROOT))
