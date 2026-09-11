from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://bloc-notes-numeriques.fr"

# 1) Homepage hero: make the image exactly fill the visual placeholder with no top/bottom gaps.
index = ROOT / "index.html"
html = index.read_text(encoding="utf-8")
html = html.replace('style="margin:28px 0 32px;"', 'style="margin:0;width:100%;height:100%;"', 1)
html = html.replace('style="width:100%;height:auto;border-radius:var(--radius-md);display:block;"', 'style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-md);display:block;"', 1)
index.write_text(html, encoding="utf-8")

style = ROOT / "style.css"
css = style.read_text(encoding="utf-8")
hero_override = '''\n\n/* Homepage hero image: fill the placeholder without letterboxing. */\n.hero-visual {\n  min-height: 0;\n  aspect-ratio: 32 / 21;\n}\n.hero-visual .editorial-media {\n  width: 100%;\n  height: 100%;\n  margin: 0 !important;\n}\n.hero-visual .editorial-media img {\n  width: 100% !important;\n  height: 100% !important;\n  object-fit: cover;\n}\n'''
if "Homepage hero image: fill the placeholder without letterboxing." not in css:
    css += hero_override
style.write_text(css, encoding="utf-8")

# 2) Open all public HTML pages to indexing.
changed = 0
for path in ROOT.rglob("*.html"):
    rel = path.relative_to(ROOT)
    if rel.parts and rel.parts[0].startswith("."):
        continue
    text = path.read_text(encoding="utf-8")
    new = re.sub(
        r'<meta\s+name="robots"\s+content="noindex(?:,\s*(?:follow|nofollow))?"\s*/?>',
        '<meta name="robots" content="index,follow">',
        text,
        flags=re.I,
    )
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1

# 3) Rebuild sitemap from every public index.html, including the homepage.
urls = []
for path in ROOT.rglob("index.html"):
    rel = path.relative_to(ROOT)
    if rel.parts and rel.parts[0].startswith("."):
        continue
    if rel == Path("index.html"):
        url = BASE + "/"
    else:
        url = BASE + "/" + "/".join(rel.parts[:-1]) + "/"
    urls.append(url)

urls = sorted(set(urls), key=lambda u: (u != BASE + "/", u))
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sitemap += [f'  <url><loc>{u}</loc></url>' for u in urls]
sitemap.append('</urlset>')
(ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")

print(f"Indexing enabled on {changed} previously noindex HTML pages")
print(f"Sitemap contains {len(urls)} public URLs")
