from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)
HISTORY_FILE = RESULTS_DIR / "Prediction_History.csv"
RATED_CAPACITY = 530.0


def calculate_soh(capacity):
    soh = (capacity / RATED_CAPACITY) * 100
    return round(soh, 2)


def battery_status(soh):
    if soh >= 90:
        return "Excellent"
    if soh >= 80:
        return "Good"
    if soh >= 70:
        return "Moderate"
    if soh >= 60:
        return "Poor"
    return "Replace Immediately"


def rul_status(cycles):
    if cycles is None:
        return "Unable to Estimate"
    if cycles > 300:
        return "Very Long Life"
    if cycles > 150:
        return "Moderate Life"
    if cycles > 50:
        return "Near End of Life"
    return "Replace Soon"


def save_prediction(predicted_capacity, soh, rul, horizon):
    row = pd.DataFrame(
        {
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Predicted Capacity": [predicted_capacity],
            "SOH (%)": [soh],
            "Remaining Cycles": [rul],
            "Forecast Horizon": [horizon],
        }
    )

    if HISTORY_FILE.exists():
        history = pd.read_csv(HISTORY_FILE)
        history = pd.concat([history, row], ignore_index=True)
    else:
        history = row

    history.to_csv(HISTORY_FILE, index=False)


def load_prediction_history():
    if HISTORY_FILE.exists():
        return pd.read_csv(HISTORY_FILE)
    return pd.DataFrame()


def clear_history():
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()


def battery_gauge(soh):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=soh,
            number={"suffix": " %", "font": {"color": "#f7f9fc"}},
            title={"text": "Battery SOH", "font": {"color": "#f7f9fc"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#9aa4b2"},
                "bar": {"color": "#00e676"},
                "bgcolor": "rgba(255,255,255,.04)",
                "borderwidth": 1,
                "bordercolor": "rgba(255,255,255,.12)",
                "steps": [
                    {"range": [0, 60], "color": "#ff5252"},
                    {"range": [60, 80], "color": "#ff9800"},
                    {"range": [80, 90], "color": "#ffc107"},
                    {"range": [90, 100], "color": "#00e676"},
                ],
            },
        )
    )

    fig.update_layout(
        height=350,
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin={"l": 20, "r": 20, "t": 50, "b": 20},
    )
    return fig


def forecast_plot(history, forecast):
    x_history = list(range(1, len(history) + 1))
    x_forecast = list(range(len(history) + 1, len(history) + len(forecast) + 1))

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_history,
            y=history,
            mode="lines+markers",
            name="Historical Capacity",
            line={"color": "#00b0ff", "width": 3},
            marker={"size": 8},
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x_forecast,
            y=forecast,
            mode="lines+markers",
            name="Forecast Capacity",
            line={"color": "#00e676", "width": 3},
            marker={"size": 8},
        )
    )
    fig.update_layout(
        title="Battery Capacity Forecast",
        xaxis_title="Cycle",
        yaxis_title="Capacity",
        hovermode="x unified",
        template="plotly_dark",
        height=500,
    )
    return fig


def model_metrics():
    return {
        "Model": "Tuned LSTM+GRU",
        "MAE": 2.715,
        "RMSE": 3.765,
        "MAPE": 0.508,
        "R²": 0.832,
    }


def project_information():
    return {
        "Project": "Battery Health Prediction System",
        "Institution": "National Institute of Technology Silchar",
        "Technique": "Hybrid Deep Learning",
        "Best Model": "Tuned LSTM+GRU",
        "Framework": "TensorFlow + Streamlit",
        "Visualization": "Plotly",
    }


def export_history():
    history = load_prediction_history()
    return history.to_csv(index=False).encode("utf-8")
