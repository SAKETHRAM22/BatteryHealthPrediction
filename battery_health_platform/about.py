from __future__ import annotations

import streamlit as st

from backend import BackendUnavailable, project_information
from styles import metric_card, section_header


def _safe_project_info() -> dict[str, object]:
    try:
        return project_information()
    except BackendUnavailable:
        return {
            "Project": "Battery Health Prediction System",
            "Institution": "National Institute of Technology Silchar",
            "Technique": "Hybrid Deep Learning",
            "Best Model": "Tuned LSTM+GRU",
            "Framework": "TensorFlow + Streamlit",
            "Visualization": "Plotly",
        }


def render_about() -> None:
    info = _safe_project_info()
    section_header(
        "About",
        "A final-year engineering project built as a premium battery health prediction platform.",
    )

    cols = st.columns(3)
    keys = ["Project", "Institution", "Technique", "Best Model", "Framework", "Visualization"]
    for index, key in enumerate(keys):
        with cols[index % 3]:
            metric_card(key, info.get(key, "-"), accent=key == "Best Model")

    st.markdown(
        """
        <div class="panel">
            <h3>Project Objective</h3>
            <p class="section-copy">
                Predict next-cycle battery capacity, calculate state of health, forecast future degradation,
                estimate remaining useful life, and preserve prediction history for inspection.
            </p>
            <h3>Dataset Description</h3>
            <p class="section-copy">
                The model consumes rolling windows of ten capacity readings from battery cycle data.
                Capacity is scaled with the saved preprocessing object before inference.
            </p>
            <h3>Hyperparameter Tuning Summary</h3>
            <p class="section-copy">
                CNN, LSTM, GRU, and hybrid variants were evaluated. Tuned LSTM+GRU was selected
                because it produced the strongest balance of low error and high explanatory power.
            </p>
            <h3>Developer Information</h3>
            <p class="section-copy">
                National Institute of Technology Silchar<br>Developer: Saketh Ram<br>
                GitHub repository: <your-repository-url>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
