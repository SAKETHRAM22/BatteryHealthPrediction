from __future__ import annotations

import streamlit as st

from about import render_about
from dashboard import render_dashboard
from forecast import render_forecast
from history import render_history
from performance import render_performance
from prediction import render_prediction
from styles import inject_global_styles


st.set_page_config(
    page_title="Battery Health Intelligence",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_global_styles()

PAGES = {
    "🏠 Dashboard": render_dashboard,
    "🔋 Battery Prediction": render_prediction,
    "📈 Forecast": render_forecast,
    "📊 Model Performance": render_performance,
    "📂 Prediction History": render_history,
    "ℹ About": render_about,
}

with st.sidebar:
    st.markdown("### Battery Intelligence")
    st.markdown("<span class='tiny'>Deep learning health prediction platform</span>", unsafe_allow_html=True)
    selected_page = st.radio("Navigation", list(PAGES.keys()), label_visibility="collapsed")
    st.divider()
    st.markdown("<span class='status-pill'>System Online</span>", unsafe_allow_html=True)
    st.markdown("<p class='tiny'>Tuned LSTM+GRU prediction engine</p>", unsafe_allow_html=True)

PAGES[selected_page]()
