from __future__ import annotations

import streamlit as st

from backend import BackendUnavailable, clear_history, export_history, load_prediction_history
from styles import section_header


def render_history() -> None:
    section_header(
        "Prediction History",
        "Search, sort, download, and clear saved predictions from results/Prediction_History.csv.",
    )

    try:
        history = load_prediction_history()
    except BackendUnavailable as exc:
        st.error(str(exc))
        return

    if history.empty:
        st.info("No predictions have been saved yet.")
        return

    search = st.text_input("Search history", placeholder="Filter by timestamp, status, horizon, or metric value")
    filtered = history.copy()
    if search:
        mask = filtered.astype(str).apply(lambda column: column.str.contains(search, case=False, na=False)).any(axis=1)
        filtered = filtered[mask]

    st.dataframe(filtered, use_container_width=True, hide_index=True)

    col_download, col_clear = st.columns([1, 1])
    with col_download:
        try:
            csv_bytes = export_history()
        except BackendUnavailable:
            csv_bytes = filtered.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv_bytes, "Prediction_History.csv", "text/csv", use_container_width=True)

    with col_clear:
        confirm = st.checkbox("Confirm clear history")
        if st.button("Clear History", disabled=not confirm, use_container_width=True):
            clear_history()
            st.success("Prediction history cleared.")
            st.rerun()

    st.caption(f"Showing {len(filtered):,} of {len(history):,} saved predictions.")
