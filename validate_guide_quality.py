#!/usr/bin/env python3
"""Qualitative structural gate for /guides/.

The price guide is the editorial reference: useful sections must be developed,
tables need interpretation, and pages need contextual internal links. The gate
checks observable structure only; it does not replace fact-checking or human style
review and it deliberately avoids forcing filler just to hit one global word count.
"""
from pathlib import Path
import re
import html as html_lib

ROOT = Path(__file__).resolve().parent
GUIDES = ROOT / "guides"

TAG_RE = re.compile(r"<[^>]+>", re.S)
H2_RE = re.compile(r'<h2\b[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="(/[^"]+)"', re.I)
SOURCE_LINK_RE = re.compile(r'<li>\s*<a\b[^>]*href="https?://', re.I)
P_RE = re.compile(r'<p\b[^>]*>(.*?)</p>', re.S | re.I)
TABLE_RE = re.compile(r'<table\b.*?</table>', re.S | re.I)

# Narrow tutorials and technical explainers can be shorter than the budget pillar,
# but no guide may collapse into a thin summary.
MIN_WORDS = {
    "imprimer-notes-numeriques": 800,
    "transfert-notes-vers-ordinateur": 850,
    "bloc-notes-numerique-google-drive": 800,
    "bloc-notes-numerique-onedrive": 800,
    "bloc-notes-numerique-dropbox": 800,
    "tablette-e-ink": 900,
    "encre-electronique-fonctionnement": 900,
    "latence-ecriture": 900,
    "ocr-manuscrit": 900,
    "autonomie-tablette-e-ink": 900,
    "formats-fichiers-compatibles": 900,
    "convertir-notes-manuscrites-en-texte": 900,
    "ecosysteme-ouvert-ou-ferme": 900,
}
DEFAULT_MIN_WORDS = 950
MIN_SECTION_WORDS = 80
MIN_CLOSING_WORDS = 60
CLOSING_IDS = {"decision", "suite", "test-decision"}
MIN_PROSE_AROUND_TABLE = 55
MIN_INTERNAL_LINKS = 4
MIN_UNIQUE_INTERNAL_LINKS = 3
MIN_SOURCE_LINKS = 3


def text(raw: str) -> str:
    raw = TAG_RE.sub(" ", raw)
    raw = html_lib.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()


def words(raw: str) -> int:
    return len(re.findall(r"\b[\wÀ-ÿ'-]+\b", text(raw)))


def article_html(page_html: str) -> str:
    m = re.search(r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>', page_html, re.S | re.I)
    return m.group(1) if m else ""


def sections(article: str):
    matches = list(H2_RE.finditer(article))
    out = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(article)
        out.append((m.group(1), text(m.group(2)), article[start:end]))
    return out


def inspect(page: Path):
    slug = page.parent.name
    page_html = page.read_text(encoding="utf-8")
    article = article_html(page_html)
    issues = []

    if not article:
        return ["article.content-main absent"]
    if '<!-- Contenu à rédiger -->' in article:
        return ["placeholder présent"]
    if 'name="robots" content="noindex,follow"' not in page_html:
        issues.append("noindex,follow absent")
    if article.count('<p class="article-answer"') != 1:
        issues.append("réponse initiale absente ou dupliquée")

    main_without_sources = re.split(r'<h2\b[^>]*id="sources"', article, maxsplit=1, flags=re.I)[0]
    wc = words(main_without_sources)
    min_wc = MIN_WORDS.get(slug, DEFAULT_MIN_WORDS)
    if wc < min_wc:
        issues.append(f"contenu utile trop court: {wc} mots < {min_wc}")

    sec = sections(article)
    substantive = [(sid, title, body) for sid, title, body in sec if sid != "sources"]
    if len(substantive) < 5:
        issues.append(f"seulement {len(substantive)} H2 substantiels")

    for sid, title, body in substantive:
        sw = words(body)
        section_floor = MIN_CLOSING_WORDS if sid in CLOSING_IDS else MIN_SECTION_WORDS
        if sw < section_floor:
            issues.append(f"section '{title}' trop légère: {sw} mots < {section_floor}")

        tables = TABLE_RE.findall(body)
        if tables:
            body_without_tables = TABLE_RE.sub(" ", body)
            prose_words = sum(words(p) for p in P_RE.findall(body_without_tables))
            if prose_words < MIN_PROSE_AROUND_TABLE:
                issues.append(f"tableau insuffisamment contextualisé dans '{title}': {prose_words} mots de prose")
            first_table = TABLE_RE.search(body)
            if first_table:
                before = body[:first_table.start()]
                after = body[first_table.end():]
                if not P_RE.search(before):
                    issues.append(f"tableau sans contexte avant dans '{title}'")
                if not P_RE.search(after):
                    issues.append(f"tableau sans interprétation après dans '{title}'")

    internal = [u for u in LINK_RE.findall(article) if not u.startswith('/transparence-affiliation/')]
    unique = sorted(set(internal))
    if len(internal) < MIN_INTERNAL_LINKS:
        issues.append(f"maillage interne trop faible: {len(internal)} liens < {MIN_INTERNAL_LINKS}")
    if len(unique) < MIN_UNIQUE_INTERNAL_LINKS:
        issues.append(f"maillage interne peu diversifié: {len(unique)} cibles uniques")

    sources = len(SOURCE_LINK_RE.findall(article))
    if sources < MIN_SOURCE_LINKS:
        issues.append(f"sources primaires insuffisantes: {sources} < {MIN_SOURCE_LINKS}")

    # The failure mode we are explicitly preventing: a heading followed by one thin
    # paragraph and nothing else. This stays strict even for conclusions.
    for sid, title, body in substantive:
        pcount = len(P_RE.findall(body))
        has_table = bool(TABLE_RE.search(body))
        has_list = bool(re.search(r'<(?:ul|ol)\b', body, re.I))
        if pcount == 1 and not has_table and not has_list and words(body) < 140:
            issues.append(f"section mono-paragraphe non développée: '{title}'")

    return issues


def main():
    pages = sorted(GUIDES.glob('*/index.html'))
    failures = {}
    for page in pages:
        issues = inspect(page)
        if issues:
            failures[page.parent.name] = issues
    if failures:
        for slug, issues in failures.items():
            print(f"FAIL {slug}")
            for issue in issues:
                print(f"  - {issue}")
        raise SystemExit(1)
    print(f"PASS: {len(pages)} guide pages meet the price-guide structural quality floor")


if __name__ == '__main__':
    main()
