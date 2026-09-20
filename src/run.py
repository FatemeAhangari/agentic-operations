import json
from pathlib import Path

from orchestrator import run_case


ROOT = Path(__file__).parents[1]
cases = json.loads((ROOT / "data" / "synthetic_cases.json").read_text())

for case in cases:
    print(json.dumps(run_case(case), ensure_ascii=False))
