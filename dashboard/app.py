import sys
from pathlib import Path
import json

import pandas as pd
import streamlit as st

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "src"))

from orchestrator import run_case
from metrics import operational_metrics

st.set_page_config(
    page_title="Agentic Operations",
    page_icon="⚙️",
    layout="wide",
)

st.title("Agentic Operations")
st.caption("Synthetic operations-control dashboard — portfolio prototype")

cases = json.loads((ROOT / "data" / "synthetic_cases.json").read_text())
results = [run_case(case) for case in cases]

metrics = operational_metrics(results)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Cases", len(results))
c2.metric("Automation rate", f"{metrics['automation_rate']:.0%}")
c3.metric("Escalation rate", f"{metrics['escalation_rate']:.0%}")
c4.metric("High-risk automation", f"{metrics['high_risk_automation_rate']:.0%}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Case decisions")
    df = pd.DataFrame([
        {
            "Case": r["case_id"],
            "Intent": r["intent"],
            "Risk": r["risk"],
            "Confidence": f"{r['confidence']:.0%}",
            "Action": r["action"],
            "Human review": "Yes" if r["requires_human"] else "No",
        }
        for r in results
    ])
    st.dataframe(df, hide_index=True, use_container_width=True)

with right:
    st.subheader("Risk distribution")
    risk_counts = (
        pd.DataFrame(results)["risk"]
        .value_counts()
        .rename_axis("risk")
        .to_frame("cases")
    )
    st.bar_chart(risk_counts)

st.subheader("Decision trace")

selected = st.selectbox(
    "Inspect case",
    [r["case_id"] for r in results],
)

case_result = next(r for r in results if r["case_id"] == selected)

st.json(case_result)

st.info(
    "Synthetic data only. Metrics demonstrate the control-plane concept "
    "and are not real operational performance."
)
