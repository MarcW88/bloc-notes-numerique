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
    asset_mode = spec.get("asset_mode", "functional_diagram")
    spec["asset_mode"] = asset_mode
    spec["page_url"] = f"/guides/{slug}/"

    asset_dir = ROOT / "assets" / "guides" / slug
    asset_dir.mkdir(parents=True, exist_ok=True)

    if asset_mode == "no_visual":
        spec["id"] = f"{slug}-no-visual"
        spec.pop("output", None)
        spec.pop("type", None)
        # Remove obsolete generated SVGs for pages that no longer need a visual.
        for old_asset in asset_dir.glob("*.svg"):
            old_asset.unlink()
            print("removed", old_asset.relative_to(ROOT))
    elif asset_mode == "functional_diagram":
        if not spec.get("type"):
            raise SystemExit(f"{slug}: functional_diagram missing type")
        spec["id"] = f"{slug}-{spec['type'].replace('_', '-')}"
        spec["output"] = f"assets/guides/{slug}/{spec['id']}.svg"
        spec.setdefault("canvas", {"width": 1200, "height": 700})
        # Keep only the currently selected generated SVG.
        for old_asset in asset_dir.glob("*.svg"):
            if old_asset.name != Path(spec["output"]).name:
                old_asset.unlink()
                print("removed", old_asset.relative_to(ROOT))
    elif asset_mode == "editorial_image":
        spec["id"] = spec.get("id", f"{slug}-editorial-image")
        if not spec.get("output"):
            raise SystemExit(f"{slug}: editorial_image needs an output path once generated")
    else:
        raise SystemExit(f"{slug}: unsupported asset_mode {asset_mode}")

    path = OUT / f"{slug}.json"
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("manifest", path.relative_to(ROOT))
