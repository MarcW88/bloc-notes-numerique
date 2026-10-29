#!/usr/bin/env python3
"""Import a real product photo from a verified image URL into assets/products/.

Usage:
  python scripts/import_product_image.py boox-note-air5-c https://example.com/photo.jpg
Requires Pillow and an internet-connected environment.
Does not modify the registry unless the download, decoding and conversion succeed.
"""
import argparse
import io
import json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".content/products/registry.json"
parser = argparse.ArgumentParser()
parser.add_argument("product_id")
parser.add_argument("image_url")
parser.add_argument("--source-page", required=True)
args = parser.parse_args()
if urlparse(args.image_url).scheme != "https":
    parser.error("HTTPS image URL required")
data = json.loads(REGISTRY.read_text(encoding="utf-8"))
if args.product_id not in data["products"]:
    parser.error("Unknown product ID")
request = Request(args.image_url, headers={"User-Agent": "Mozilla/5.0 (compatible; ProductPhotoImporter/1.0)"})
with urlopen(request, timeout=25) as response:
    raw = response.read(12 * 1024 * 1024 + 1)
    if len(raw) > 12 * 1024 * 1024:
        parser.error("Image exceeds 12 MB")
with Image.open(io.BytesIO(raw)) as original:
    if original.width < 300 or original.height < 300:
        parser.error("Source image is too small")
    image = ImageOps.exif_transpose(original).convert("RGB")
    image.thumbnail((900, 900), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (900, 900), "white")
    canvas.paste(image, ((900 - image.width)//2, (900 - image.height)//2))
    destination = ROOT / "assets/products" / (args.product_id + ".webp")
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, "WEBP", quality=84, method=6)
product = data["products"][args.product_id]
product["image"] = {"url": "/assets/products/" + args.product_id + ".webp",
                    "source_type": "manufacturer_or_retailer",
                    "rights_checked": False,
                    "source_page": args.source_page}
REGISTRY.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Imported {product['name']} -> {destination.relative_to(ROOT)}")
