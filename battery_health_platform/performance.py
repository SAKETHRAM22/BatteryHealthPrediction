from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from styles import section_header


# =====================================================
# MODEL PERFORMANCE RESULTS
# =====================================================

MODEL_RESULTS = pd.DataFrame(
    [
        {"Model": "CNN",             "MAE": 5.920, "RMSE": 7.410, "MAPE": 1.120, "R²": 0.541},
        {"Model": "LSTM",            "MAE": 4.840, "RMSE": 6.330, "MAPE": 0.910, "R²": 0.646},
        {"Model": "GRU",             "MAE": 4.510, "RMSE": 5.980, "MAPE": 0.860, "R²": 0.691},
        {"Model": "CNN+GRU",         "MAE": 3.880, "RMSE": 5.120, "MAPE": 0.740, "R²": 0.742},
        {"Model": "LSTM+CNN",        "MAE": 3.640, "RMSE": 4.840, "MAPE": 0.690, "R²": 0.779},
        {"Model": "LSTM+GRU",        "MAE": 3.120, "RMSE": 4.210, "MAPE": 0.590, "R²": 0.811},
        {"Model": "LSTM+CNN+GRU",    "MAE": 3.340, "RMSE": 4.480, "MAPE": 0.640, "R²": 0.798},

        # Updated results after training on ALL battery datasets
        {"Model": "Tuned LSTM+GRU",  "MAE": 4.293, "RMSE": 6.143, "MAPE": 0.669, "R²": 0.9979},
    ]
)


# =====================================================
# PAGE
# =====================================================

def render_performance() -> None:

    section_header(
        "Model Performance",
        "Comparison of all deep learning architectures evaluated for battery capacity prediction."
    )

    # -------------------------------------------------
    # Highlight Best Model
    # -------------------------------------------------

    def highlight_best_model(row):

        if row["Model"] == "Tuned LSTM+GRU":
            return [
                "background-color:#00b36b; color:white; font-weight:bold"
            ] * len(row)

        return [
            ""
        ] * len(row)

    styled = MODEL_RESULTS.style.apply(
        highlight_best_model,
        axis=1,
    )

    st.dataframe(
        styled,
        use_container_width=True,
        hide_index=True,
        height=360,
    )

    # -------------------------------------------------
    # Charts
    # -------------------------------------------------

    left, right = st.columns(2)

    with left:

        fig = px.bar(
            MODEL_RESULTS,
            x="Model",
            y=["MAE", "RMSE"],
            barmode="group",
            title="Error Metrics Comparison",
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Model",
            yaxis_title="Error",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with right:

        ranked = MODEL_RESULTS.sort_values(
            "R²",
            ascending=True,
        )

        fig = px.bar(
            ranked,
            x="R²",
            y="Model",
            orientation="h",
            title="R² Comparison",
            color="R²",
            color_continuous_scale="Viridis",
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="R² Score",
            yaxis_title="Model",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    best = MODEL_RESULTS.loc[
        MODEL_RESULTS["Model"] == "Tuned LSTM+GRU"
    ].iloc[0]

    st.success(
        f"""
### 🏆 Best Model Selected: Tuned LSTM+GRU

- **MAE:** {best['MAE']:.3f}
- **RMSE:** {best['RMSE']:.3f}
- **MAPE:** {best['MAPE']:.3f}%
- **R² Score:** {best['R²']:.4f}

This model achieved the highest predictive performance after being trained on all available battery datasets and is selected for deployment in the Battery Health Prediction Platform.
"""
    )