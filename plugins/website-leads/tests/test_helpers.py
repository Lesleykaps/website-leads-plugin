import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).parents[1]
def run(*args): subprocess.run([sys.executable,*args],check=True,capture_output=True,text=True)
def test_dedupe_and_validation():
 with tempfile.TemporaryDirectory() as d:
  d=Path(d); candidates=ROOT/'examples'/'candidates.json'; accepted=d/'accepted.json'; duplicates=d/'duplicates.json'; quality=d/'quality.json'
  run(str(ROOT/'scripts'/'dedupe.py'),'--candidates',str(candidates),'--accepted',str(accepted),'--duplicates',str(duplicates))
  assert len(json.loads(accepted.read_text()))==1
  run(str(ROOT/'scripts'/'validate_leads.py'),'--qualified',str(accepted),'--output',str(quality))
  assert json.loads(quality.read_text())['passed'] is True
if __name__=='__main__': test_dedupe_and_validation(); print('helpers: PASS')

