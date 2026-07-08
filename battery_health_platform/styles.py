import streamlit as st


def inject_global_styles() -> None:
    st.html(
        """
        <style>
        @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap");

        :root {
            --bg: #0f1117;
            --panel: #1a1d29;
            --panel-2: #151823;
            --line: rgba(255,255,255,.10);
            --text: #f7f9fc;
            --muted: #9aa4b2;
            --green: #00e676;
            --blue: #00b0ff;
            --warning: #ffc107;
            --danger: #ff5252;
        }

        html, body, [class*="css"] {
            font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 12% 8%, rgba(0,176,255,.14), transparent 28%),
                radial-gradient(circle at 88% 18%, rgba(0,230,118,.10), transparent 24%),
                linear-gradient(180deg, #0f1117 0%, #11131b 100%);
            color: var(--text);
        }

        section[data-testid="stSidebar"] {
            background: rgba(15,17,23,.88);
            border-right: 1px solid var(--line);
            backdrop-filter: blur(18px);
        }

        section[data-testid="stSidebar"] * {
            color: var(--text);
        }

        .block-container {
            max-width: 1280px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        h1, h2, h3 {
            letter-spacing: 0;
        }

        h1 {
            font-size: clamp(2.2rem, 5vw, 4.9rem);
            line-height: .95;
            font-weight: 800;
        }

        h2 {
            font-size: 1.55rem;
            font-weight: 750;
        }

        .hero {
            min-height: 430px;
            display: grid;
            grid-template-columns: minmax(0, 1.25fr) minmax(320px, .75fr);
            gap: 2rem;
            align-items: center;
            padding: 2.4rem;
            border: 1px solid var(--line);
            border-radius: 24px;
            background:
                linear-gradient(135deg, rgba(26,29,41,.92), rgba(21,24,35,.72)),
                linear-gradient(90deg, rgba(0,176,255,.10), rgba(0,230,118,.10));
            box-shadow: 0 24px 80px rgba(0,0,0,.32);
            overflow: hidden;
        }

        .hero p, .section-copy {
            color: var(--muted);
            font-size: 1.02rem;
            line-height: 1.7;
            max-width: 760px;
        }

        .battery-art {
            position: relative;
            min-height: 260px;
            border: 1px solid rgba(255,255,255,.12);
            border-radius: 24px;
            background: linear-gradient(145deg, rgba(255,255,255,.08), rgba(255,255,255,.02));
            box-shadow: inset 0 1px 0 rgba(255,255,255,.12), 0 24px 70px rgba(0,0,0,.28);
            display: grid;
            place-items: center;
        }

        .battery-shell {
            width: min(80%, 360px);
            height: 128px;
            border: 3px solid rgba(255,255,255,.76);
            border-radius: 22px;
            padding: 11px;
            position: relative;
        }

        .battery-shell:after {
            content: "";
            position: absolute;
            right: -24px;
            top: 37px;
            width: 16px;
            height: 48px;
            border-radius: 0 8px 8px 0;
            background: rgba(255,255,255,.72);
        }

        .battery-fill {
            height: 100%;
            width: 83%;
            border-radius: 14px;
            background: linear-gradient(90deg, var(--green), var(--blue));
            box-shadow: 0 0 28px rgba(0,230,118,.38);
            animation: pulseFill 2.4s ease-in-out infinite;
        }

        @keyframes pulseFill {
            0%, 100% { transform: scaleX(.97); transform-origin: left; opacity: .88; }
            50% { transform: scaleX(1); opacity: 1; }
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 1rem;
            margin: 1.2rem 0 1.8rem;
        }

        .card, .metric-card, .result-card {
            border: 1px solid var(--line);
            border-radius: 20px;
            background: linear-gradient(180deg, rgba(26,29,41,.94), rgba(21,24,35,.86));
            box-shadow: 0 18px 55px rgba(0,0,0,.22);
        }

        .metric-card, .result-card {
            padding: 1.15rem;
            transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;
        }

        .metric-card:hover, .result-card:hover {
            transform: translateY(-3px);
            border-color: rgba(0,176,255,.38);
            box-shadow: 0 22px 70px rgba(0,0,0,.30);
        }

        .metric-label {
            color: var(--muted);
            font-size: .82rem;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: .06em;
        }

        .metric-value {
            color: var(--text);
            font-size: 1.55rem;
            font-weight: 800;
            margin-top: .45rem;
        }

        .accent {
            color: var(--green);
        }

        .panel {
            padding: 1.25rem;
            border: 1px solid var(--line);
            border-radius: 22px;
            background: rgba(26,29,41,.74);
            box-shadow: 0 18px 55px rgba(0,0,0,.18);
        }

        div[data-testid="stButton"] button,
        div[data-testid="stDownloadButton"] button {
            border-radius: 999px;
            min-height: 2.85rem;
            border: 1px solid rgba(0,230,118,.35);
            color: #07110c;
            background: linear-gradient(135deg, #00e676, #00b0ff);
            font-weight: 800;
            box-shadow: 0 14px 34px rgba(0,230,118,.18);
            transition: transform .18s ease, filter .18s ease, box-shadow .18s ease;
        }

        div[data-testid="stButton"] button:hover,
        div[data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 0 18px 42px rgba(0,176,255,.24);
        }

        div[data-baseweb="input"] input,
        textarea,
        div[data-baseweb="select"] > div {
            border-radius: 14px;
            border-color: rgba(255,255,255,.12);
            background-color: rgba(255,255,255,.04);
        }

        [data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 18px;
            overflow: hidden;
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: .45rem;
            padding: .5rem .75rem;
            border-radius: 999px;
            background: rgba(0,230,118,.12);
            border: 1px solid rgba(0,230,118,.28);
            color: #dfffee;
            font-weight: 700;
        }

        .tiny {
            color: var(--muted);
            font-size: .86rem;
        }

        @media (max-width: 980px) {
            .hero {
                grid-template-columns: 1fr;
            }
            .metric-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 640px) {
            .hero {
                padding: 1.2rem;
            }
            .metric-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """
    )


def metric_card(label: str, value: object, accent: bool = False) -> None:
    value_class = "metric-value accent" if accent else "metric-value"
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="{value_class}">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, body: str | None = None) -> None:
    st.markdown(f"## {title}")
    if body:
        st.markdown(f"<p class='section-copy'>{body}</p>", unsafe_allow_html=True)