#!/usr/bin/env python3
from pathlib import Path
import json
from comparison_pages import COMPARISON_PAGES
from comparison_products import COMPARISON_PRODUCTS
ROOT=Path(__file__).resolve().parent
D=ROOT/'.content'/'comparisons'; D.mkdir(parents=True, exist_ok=True)
for slug,p in COMPARISON_PAGES.items():
    payload={
      'slug':slug,'url':f'/comparatifs/{slug}/','researched_at':'2026-09-08','status':'DRAFT_READY',
      'intent':{'query':p['query'],'type':p['type'],'user_job':p['job']},
      'criteria':[{'id':c,'label':c,'weight':w} for c,w in p['weights'].items()],
      'product_universe':[], 'scores':{}, 'ranking':[],
      'affiliate_commission_used_in_ranking':False,
      'methodology_note':'Desk-research scoring. Scores are editorial inferences from verified product capabilities, not hands-on measurements.'
    }
    for pid in p['products']:
        pr=COMPARISON_PRODUCTS[pid]
        payload['product_universe'].append({'id':pid,'name':pr['name'],'status':'ELIGIBLE','source':pr['source'],'price_snapshot':pr['price']})
        payload['scores'][pid]={c:{'score':pr['scores'][c],'evidence_class':'VERIFIED','justification':f"Official capabilities reviewed for {pr['name']}; numeric score is an editorial normalization for {c}."} for c in p['weights']}
    for rank,(pid,score) in enumerate(p['ranking'],1): payload['ranking'].append({'rank':rank,'product_id':pid,'score':score})
    (D/f'{slug}.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    print('metadata',slug)
