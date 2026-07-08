from __future__ import annotations

import streamlit as st
import plotly.graph_objects as go

from backend import (
    BackendUnavailable,
    battery_gauge,
    battery_status,
    calculate_soh,
    estimate_remaining_cycles,
    forecast_capacity,
    predict_capacity,
    save_prediction,
)

from styles import metric_card, section_header


DEFAULT_CAPACITIES = [
    527.0, 526.0, 526.0, 525.0, 525.0,
    524.0, 524.0, 523.0, 523.0, 522.0
]

RATED_CAPACITY = 530.0


def _capacity_inputs() -> list[float]:
    cols = st.columns(5)
    values = []

    for index in range(10):
        with cols[index % 5]:
            values.append(
                st.number_input(
                    f"Cycle {index + 1}",
                    min_value=0.001,
                    value=DEFAULT_CAPACITIES[index],
                    step=0.1,
                    format="%.3f",
                )
            )

    return values


def render_prediction() -> None:

    section_header(
        "Battery Prediction",
        "Enter the previous 10 capacity readings to predict the next battery capacity using the tuned LSTM+GRU model.",
    )

    with st.container(border=False):

        st.markdown("<div class='panel'>", unsafe_allow_html=True)

        capacities = _capacity_inputs()

        horizon = st.select_slider(
            "Forecast horizon",
            options=[1, 5, 10, 20, 50],
            value=10,
        )

        run_prediction = st.button(
            "Predict Battery Health",
            use_container_width=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)

    if not run_prediction:
        return

    try:

        with st.spinner("Running tuned LSTM+GRU prediction..."):

            predicted = predict_capacity(capacities)

            forecast = forecast_capacity(
                capacities,
                steps=int(horizon),
            )

            soh = calculate_soh(predicted)

            status = battery_status(soh)

            rul = estimate_remaining_cycles(
                capacities,
                rated_capacity=RATED_CAPACITY,
            )

            save_prediction(
                predicted,
                soh,
                rul,
                int(horizon),
            )

            st.session_state["last_capacities"] = capacities
            st.session_state["last_forecast"] = forecast

    except (
        BackendUnavailable,
        FileNotFoundError,
        ValueError,
        TypeError,
    ) as exc:

        st.error(str(exc))
        return

    # =====================================================
    # RESULTS
    # =====================================================

    section_header("Prediction Results")

    cols = st.columns(4)

    with cols[0]:
        metric_card(
            "Predicted Capacity (mAh)",
            f"{predicted:.3f}",
            True,
        )

    with cols[1]:
        metric_card(
            "Battery SOH",
            f"{soh:.2f}%",
        )

    with cols[2]:
        metric_card(
            "Battery Status",
            status,
        )

    with cols[3]:

        rul_text = (
            ">500 cycles"
            if rul is None
            else f"{rul} cycles"
        )

        metric_card(
            "Remaining Useful Life",
            rul_text,
        )

    # =====================================================
    # GAUGE + BATTERY
    # =====================================================

    gauge_col, battery_col = st.columns([1.1, 0.9])

    with gauge_col:

        st.plotly_chart(
            battery_gauge(soh),
            use_container_width=True,
        )

    with battery_col:

        fill = max(0, min(100, soh))

        color = (
            "#00e676"
            if fill >= 90
            else "#ffc107"
            if fill >= 80
            else "#ff9800"
            if fill >= 70
            else "#ff5252"
        )

        st.markdown(
            f"""
            <div class="panel" style="height:350px;display:grid;place-items:center;">
                <div style="width:min(88%,380px);
                            height:118px;
                            border:3px solid rgba(255,255,255,.7);
                            border-radius:22px;
                            padding:10px;
                            position:relative;">

                    <div style="
                        height:100%;
                        width:{fill}%;
                        border-radius:14px;
                        background:{color};
                        box-shadow:0 0 30px {color}55;
                        transition:width .6s ease;">
                    </div>

                </div>

                <div class="metric-value">
                    {fill:.1f}%
                </div>

                <div class="tiny">
                    Animated battery state of health
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================================
    # FORECAST GRAPH
    # =====================================================

    section_header("Capacity Forecast")

    history = capacities
    future = forecast

    fig = go.Figure()

    # Historical Capacity

    fig.add_trace(
        go.Scatter(
            x=list(range(1, len(history) + 1)),
            y=history,
            mode="lines+markers",
            name="Historical Capacity",
            line=dict(
                color="#00bfff",
                width=3,
            ),
        )
    )

    # Forecast Capacity

    fig.add_trace(
        go.Scatter(
            x=list(
                range(
                    len(history),
                    len(history) + len(future) + 1,
                )
            ),
            y=[history[-1]] + future,
            mode="lines+markers",
            name="Forecast",
            line=dict(
                color="#00e676",
                width=3,
                dash="dash",
            ),
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        title="Battery Capacity Forecast",
        xaxis_title="Cycle Number",
        yaxis_title="Capacity (mAh)",
        legend=dict(
            orientation="h",
            y=1.05,
            x=0,
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )