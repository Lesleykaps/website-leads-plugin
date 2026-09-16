#!/usr/bin/env python3
"""Portable, conservative deduplication for Website Leads JSON arrays/JSONL."""
import argparse, json, re, unicodedata
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlparse

def clean(v): return re.sub(r"\s+", " ", unicodedata.normalize("NFKD", str(v or "")).encode("ascii", "ignore").decode().lower()).strip()
def name(v): return " ".join(x for x in re.findall(r"[a-z0-9]+", clean(v)) if x not in {"ltd","limited","inc","llc","co","company","group","holdings"})
def domain(v):
    h=urlparse(str(v if "://" in str(v) else "https://"+str(v or ""))).hostname or ""
    return h.lower().removeprefix("www.")
def email(v):
    x=clean(v); return x if re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+",x) else ""
def phone(v):
    s=str(v or "")
    if re.search(r"\d{4,}\s*[-–]\s*\d{1,3}\s*$",s) or re.search(r"\b(or|to)\b|[/;]",s,re.I): return ""
    d=re.sub(r"\D","",s); return d if 7<=len(d)<=15 else ""
def keys(x): return {k:v for k,v in {"domain":domain(x.get("website_url")),"email":email(x.get("public_email")),"phone":phone(x.get("public_phone")),"name_place":name(x.get("business_name"))+"|"+clean(x.get("city"))+"|"+clean(x.get("country"))}.items() if v and v != "||"}
def load(p):
    raw=Path(p).read_text(encoding="utf-8").strip()
    return json.loads(raw) if raw.startswith("[") else [json.loads(x) for x in raw.splitlines() if x.strip()]
def main():
 p=argparse.ArgumentParser(); p.add_argument("--candidates",required=True);p.add_argument("--registry");p.add_argument("--accepted",required=True);p.add_argument("--duplicates",required=True);a=p.parse_args()
 history=load(a.registry) if a.registry and Path(a.registry).exists() else []; accepted=[]; duplicates=[]; seen=[]
 for c in load(a.candidates):
  ck=keys(c); match=None
  for old in history+seen:
   ok=keys(old); shared=[k for k in ("domain","email","phone","name_place") if ck.get(k) and ck.get(k)==ok.get(k)]
   if shared: match=("exact:"+shared[0],old);break
   if ck.get("name_place") and ck.get("name_place")==ok.get("name_place") and SequenceMatcher(None, name(c.get("business_name")),name(old.get("business_name"))).ratio()>=.92: match=("fuzzy_name_location",old);break
  if match: duplicates.append({"candidate":c,"reason":match[0],"matched_lead_id":match[1].get("lead_id")})
  else: accepted.append(c);seen.append(c)
 Path(a.accepted).write_text(json.dumps(accepted,indent=2),encoding="utf-8");Path(a.duplicates).write_text(json.dumps(duplicates,indent=2),encoding="utf-8")
if __name__=="__main__": main()

