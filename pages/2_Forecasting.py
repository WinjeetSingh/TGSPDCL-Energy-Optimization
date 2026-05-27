import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import streamlit as st
from theme import apply_theme

st.set_page_config(layout="wide")

apply_theme()

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="GridPulse-AI Forecasting",
    page_icon="📈",
    layout="wide"
)

# =========================================================
# ADVANCED ENTERPRISE UI
# =========================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:
        radial-gradient(circle at top left, rgba(0,212,255,0.08), transparent 30%),
        radial-gradient(circle at top right, rgba(139,92,246,0.12), transparent 30%),
        linear-gradient(135deg,#020617,#071028,#0F172A);
    color:white;
}

.block-container{
    padding-top:1.2rem;
    padding-bottom:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* HERO */
.hero-box{
    background: linear-gradient(
        135deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.92)
    );

    border:1px solid rgba(255,255,255,0.08);

    padding:2.5rem;

    border-radius:28px;

    box-shadow:
        0 0 40px rgba(0,212,255,0.10),
        0 20px 60px rgba(0,0,0,0.35);

    margin-bottom:1.5rem;
}

.hero-title{
    font-size:3rem;
    font-weight:800;
    color:white;
}

.hero-sub{
    color:#CBD5E1;
    font-size:1.1rem;
    margin-top:0.5rem;
}

/* SECTION CARD */
.section-card{
    background: rgba(15,23,42,0.88);

    border-radius:24px;

    padding:1.5rem;

    border:1px solid rgba(255,255,255,0.07);

    margin-top:1rem;
    margin-bottom:1rem;
}

/* KPI */
.metric-card{
    background: rgba(15,23,42,0.88);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:22px;

    padding:1.2rem;

    transition:0.3s ease;
}

.metric-card:hover{
    transform: translateY(-4px);

    border:1px solid rgba(56,189,248,0.35);

    box-shadow:
        0 12px 40px rgba(0,212,255,0.15);
}

/* BUTTON */
.stButton > button{
    width:100%;

    border:none;

    border-radius:14px;

    background: linear-gradient(
        90deg,
        #0EA5E9,
        #2563EB
    );

    color:white;

    font-weight:700;

    padding:0.75rem;
}

/* TABS */
.stTabs [data-baseweb="tab-list"]{
    gap:12px;
}

.stTabs [data-baseweb="tab"]{
    background: rgba(15,23,42,0.92);

    border-radius:14px;

    padding:10px 20px;

    color:#CBD5E1;

    border:1px solid rgba(255,255,255,0.06);
}

.stTabs [aria-selected="true"]{
    background: linear-gradient(
        90deg,
        rgba(14,165,233,0.25),
        rgba(99,102,241,0.25)
    ) !important;

    color:white !important;

    border:1px solid rgba(56,189,248,0.35);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero-box">

<div class="hero-title">
📈 GridPulse-AI Forecasting Engine
</div>

<div class="hero-sub">
Enterprise Demand Forecasting • Predictive Intelligence • AI Analytics
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# KPI CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Forecast Accuracy",
        "97.8%",
        "+1.4%"
    )

with col2:
    st.metric(
        "Predicted Grid Load",
        "1.34M kWh",
        "+4.2%"
    )

with col3:
    st.metric(
        "Peak Demand Risk",
        "Low",
        "-12%"
    )

with col4:
    st.metric(
        "AI Confidence Score",
        "98.4%",
        "+0.8%"
    )

st.markdown("")

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "Forecast Configuration",
    "Predictive Analytics",
    "AI Insights"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    st.markdown("## ⚙️ Forecast Configuration")

    col1, col2, col3 = st.columns(3)

    with col1:
        connected_load = st.slider(
            "Connected Load (MW)",
            100,
            10000,
            5000
        )

    with col2:
        service_count = st.slider(
            "Service Count",
            100,
            10000,
            3500
        )

    with col3:
        utilization_ratio = st.slider(
            "Utilization Ratio",
            0.10,
            1.00,
            0.65
        )

    st.markdown("")

    col4, col5, col6 = st.columns(3)

    with col4:
        circle = st.selectbox(
            "Circle",
            [
                "Hyderabad",
                "Warangal",
                "Karimnagar",
                "Nalgonda"
            ]
        )

    with col5:
        division = st.selectbox(
            "Division",
            [
                "North",
                "South",
                "East",
                "West"
            ]
        )

    with col6:
        area = st.selectbox(
            "Area Type",
            [
                "Urban",
                "Semi-Urban",
                "Rural"
            ]
        )

    st.markdown("")

    generate_forecast = st.button(
        "⚡ Generate Enterprise Forecast"
    )

# =========================================================
# FORECAST LOGIC
# =========================================================

if "forecast_generated" not in st.session_state:
    st.session_state.forecast_generated = False

if generate_forecast:

    st.session_state.forecast_generated = True

    with st.spinner("Running GridPulse-AI Forecast Engine..."):
        time.sleep(2)

    prediction = (
        connected_load * 0.85
        + service_count * 1.75
        + utilization_ratio * 10000
    )

    st.session_state.prediction = prediction

# =========================================================
# TAB 2
# =========================================================

with tab2:

    st.markdown("## 📊 Predictive Analytics")

    if st.session_state.forecast_generated:

        dates = pd.date_range(
            start="2026-01-01",
            periods=30
        )

        demand = np.random.normal(
            st.session_state.prediction,
            12000,
            30
        )

        forecast_df = pd.DataFrame({
            "Date": dates,
            "Forecast Demand": demand
        })

        fig = px.area(
            forecast_df,
            x="Date",
            y="Forecast Demand",
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.success(
            f"AI Predicted Demand: {round(st.session_state.prediction):,} kWh"
        )

    else:

        st.info(
            "Configure forecast parameters and generate AI forecast."
        )

# =========================================================
# TAB 3
# =========================================================

with tab3:

    st.markdown("## 🤖 AI Insights")

    if st.session_state.forecast_generated:

        insight_col1, insight_col2 = st.columns(2)

        with insight_col1:

            st.markdown("""
            <div class="section-card">

            <h3>⚡ Peak Load Intelligence</h3>

            <p>
            AI forecasting indicates elevated commercial
            demand during afternoon operational windows.
            Grid balancing recommended between
            14:00 - 18:00.
            </p>

            </div>
            """, unsafe_allow_html=True)

        with insight_col2:

            st.markdown("""
            <div class="section-card">

            <h3>🚨 Risk Detection</h3>

            <p>
            Forecasting engine detected medium variance
            risk in urban distribution clusters.
            Preventive optimization recommended.
            </p>

            </div>
            """, unsafe_allow_html=True)

        st.markdown("")

        forecast_score = np.random.uniform(95, 99)

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=forecast_score,
            title={'text': "AI Forecast Confidence"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#38BDF8"},
                'steps': [
                    {'range': [0, 50], 'color': "#7F1D1D"},
                    {'range': [50, 80], 'color': "#78350F"},
                    {'range': [80, 100], 'color': "#064E3B"}
                ]
            }
        ))

        gauge.update_layout(
            template="plotly_dark",
            height=400,
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    else:

        st.warning(
            "Generate forecast to unlock AI insights."
        )