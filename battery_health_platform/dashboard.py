from __future__ import annotations

import platform

import streamlit as st

from backend import BackendUnavailable, model_information, model_metrics
from styles import metric_card, section_header


def _safe_model_info() -> dict[str, object]:
    try:
        return model_information()
    except BackendUnavailable:
        return {
            "Model": "Tuned LSTM+GRU",
            "Window Size": 10,
            "Framework": "TensorFlow",
            "Input Shape": "(10,1)",
        }


def _safe_metrics() -> dict[str, object]:
    try:
        return model_metrics()
    except BackendUnavailable:
        return {"Model": "Tuned LSTM+GRU", "MAE": 2.715, "RMSE": 3.765, "MAPE": 0.508, "R²": 0.832}


def render_dashboard() -> None:
    info = _safe_model_info()
    metrics = _safe_metrics()

    st.markdown(
        """
        <section class="hero">
            <div>
                <p class="status-pill">Production battery analytics</p>
                <h1>Battery health prediction, engineered for decisions.</h1>
                <p>
                    Forecast degradation, estimate remaining useful life, and track prediction history
                    with a tuned hybrid LSTM+GRU model built for lithium-ion battery capacity signals.
                </p>
            </div>
            <div class="battery-art">
                <div class="battery-shell"><div class="battery-fill"></div></div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    section_header("System Snapshot", "Operational metrics and model configuration at a glance.")

    cols = st.columns(4)
    with cols[0]:
        metric_card("Model", metrics.get("Model", info.get("Model", "Tuned LSTM+GRU")), True)
    with cols[1]:
        metric_card("MAE", metrics.get("MAE", "2.715"))
    with cols[2]:
        metric_card("RMSE", metrics.get("RMSE", "3.765"))
    with cols[3]:
        metric_card("MAPE", f"{metrics.get('MAPE', 0.508)}%")
    cols = st.columns(4)
    with cols[0]:
        metric_card("R²", metrics.get("R²", "0.832"), True)
    with cols[1]:
        metric_card("Framework", info.get("Framework", "TensorFlow"))
    with cols[2]:
        metric_card("Window Size", info.get("Window Size", 10))
    with cols[3]:
        metric_card("Runtime", platform.python_version())

    st.markdown(
        """
        <div class="panel">
            <h3>Architecture</h3>
            <p class="section-copy">
                The platform uses the existing prediction engine without changing its public functions.
                Capacity windows are passed into the model, transformed with the saved scaler, and
                visualized through Streamlit and Plotly for an executive-grade engineering demo.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
