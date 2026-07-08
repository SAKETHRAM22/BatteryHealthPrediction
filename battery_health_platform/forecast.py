from __future__ import annotations

import streamlit as st

from backend import BackendUnavailable, forecast_capacity, forecast_plot
from prediction import DEFAULT_CAPACITIES
from styles import section_header


def render_forecast() -> None:
    section_header(
        "Forecast",
        "Explore future capacity decay using the backend forecast_capacity() and forecast_plot() functions.",
    )

    stored_history = st.session_state.get("last_capacities", DEFAULT_CAPACITIES)
    default_text = ", ".join(f"{value:.1f}" for value in stored_history)

    history_text = st.text_area("Historical capacity values", value=default_text, height=110)
    steps = st.slider("Forecast cycles", min_value=1, max_value=100, value=20, step=1)

    if st.button("Generate Forecast", use_container_width=True):
        try:
            history = [float(item.strip()) for item in history_text.split(",") if item.strip()]
            if len(history) < 10:
                st.error("Provide at least 10 capacity readings. The model uses the last 10 values as its window.")
                return
            model_window = history[-10:]
            forecast = forecast_capacity(model_window, steps=steps)
            fig = forecast_plot(model_window, forecast)
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"color": "#f7f9fc"},
            )
            st.plotly_chart(fig, use_container_width=True, config={"displaylogo": False, "toImageButtonOptions": {"format": "png"}})
            st.session_state["last_capacities"] = model_window
            st.session_state["last_forecast"] = forecast
        except (BackendUnavailable, FileNotFoundError, ValueError, TypeError) as exc:
            st.error(str(exc))

    if "last_forecast" in st.session_state:
        st.caption("Latest forecast is stored in session and reused across pages.")
