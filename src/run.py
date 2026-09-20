import json
from pathlib import Path

from agent import process


ROOT = Path(__file__).parents[1]
cases = json.loads((ROOT / "data" / "synthetic_cases.json").read_text())

for case in cases:
    print(json.dumps(process(case), ensure_ascii=False))
