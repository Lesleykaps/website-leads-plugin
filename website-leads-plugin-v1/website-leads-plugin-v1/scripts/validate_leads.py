#!/usr/bin/env python3
"""Fail-closed pre-export checks; outputs a portable quality report."""
import argparse,json,re
from pathlib import Path
EMAIL=re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
REQ=("business_name","country","website_status","verified_problem_summary","verification_confidence","primary_source_url","evidence_url","contact_source_url","business_specific_fact")
SCORES=("score_website_problem_severity","score_evidence_strength","score_business_activity","score_contactability","score_enquiry_need","score_commercial_fit")
def main():
 p=argparse.ArgumentParser();p.add_argument("--qualified",required=True);p.add_argument("--output",required=True);a=p.parse_args();rows=json.loads(Path(a.qualified).read_text());errors=[]
 for i,x in enumerate(rows):
  missing=[k for k in REQ if not str(x.get(k," ")).strip()]
  if not (str(x.get("public_email","")).strip() or str(x.get("public_phone","")).strip()): missing.append("public_email_or_phone")
  total=0
  for k in SCORES:
   try: v=float(x.get(k)); total+=v
   except: missing.append(k);continue
   if v<0: missing.append(k+"_negative")
  if total>100: missing.append("score_total_over_100")
  if str(x.get("public_email","")).strip() and not EMAIL.fullmatch(str(x["public_email"]).strip()): missing.append("invalid_public_email")
  if x.get("website_status")!="No Website" and not (x.get("desktop_screenshot") and x.get("mobile_screenshot")): missing.append("existing_site_screenshots")
  if missing: errors.append({"index":i,"business_name":x.get("business_name"),"errors":missing})
 Path(a.output).write_text(json.dumps({"passed":not errors,"qualified_checked":len(rows),"errors":errors},indent=2),encoding="utf-8")
if __name__=="__main__": main()
