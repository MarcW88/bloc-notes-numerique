#!/usr/bin/env python3
from pathlib import Path
import re,json,sys
ROOT=Path(__file__).resolve().parent
fail=[]
for fp in sorted((ROOT/'.content'/'comparisons').glob('*.json')):
    d=json.loads(fp.read_text())
    if sum(c['weight'] for c in d['criteria'])!=100: fail.append(f'{fp.name}: weights')
    if d.get('affiliate_commission_used_in_ranking') is not False: fail.append(f'{fp.name}: affiliate commission')
    page=ROOT/'comparatifs'/fp.stem/'index.html'; h=page.read_text()
    art=re.search(r'<article class="content-main">(.*?)</article>',h,re.S)
    if not art: fail.append(f'{fp.stem}: article') ; continue
    body=art.group(1)
    if '<!-- Contenu à rédiger -->' in body: fail.append(f'{fp.stem}: placeholder')
    if len(re.findall(r'<h2\b',body))<8: fail.append(f'{fp.stem}: shallow headings')
    if len(re.findall(r'href="/',body))<5: fail.append(f'{fp.stem}: internal links')
    if 'Sources officielles consultées' not in body: fail.append(f'{fp.stem}: sources')
    if 'name="robots" content="noindex,follow"' not in h: fail.append(f'{fp.stem}: noindex')
if fail:
    print('\n'.join('FAIL '+x for x in fail)); sys.exit(1)
print('PASS: all comparison pages meet structural methodology floor')
