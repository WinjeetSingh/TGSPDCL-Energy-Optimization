
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="GridPulse-AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# GLOBAL THEME
# =========================================================

st.markdown("""
<style>

#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

header {
    background: transparent;
}

.stApp{
    background:
        radial-gradient(circle at top left, rgba(0,212,255,0.08), transparent 30%),
        radial-gradient(circle at top right, rgba(139,92,246,0.12), transparent 30%),
        linear-gradient(135deg,#020617,#071028,#0F172A);

    color:white;
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background: rgba(15,23,42,0.96);
    border-right:1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* HERO */

.hero-box{
    background:
        linear-gradient(
            135deg,
            rgba(15,23,42,0.95),
            rgba(30,41,59,0.92)
        );

    padding:40px;

    border-radius:28px;

    border:1px solid rgba(255,255,255,0.08);

    margin-bottom:25px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35);
}

.hero-title{
    font-size:56px;
    font-weight:800;
    color:white;
}

.hero-sub{
    font-size:18px;
    color:#CBD5E1;
    margin-top:10px;
    line-height:1.8;
}

/* KPI */

.kpi-card{
    background: rgba(15,23,42,0.88);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:24px;

    padding:30px;

    margin-bottom:20px;

    transition:0.3s ease;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.25);
}

.kpi-card:hover{
    transform:translateY(-5px);

    border:1px solid rgba(56,189,248,0.40);

    box-shadow:
        0 15px 40px rgba(0,212,255,0.18);
}

.kpi-title{
    color:#CBD5E1;
    font-size:18px;
    margin-bottom:18px;
}

.kpi-value{
    font-size:52px;
    font-weight:800;
    margin-bottom:10px;
}

.kpi-delta{
    color:#94A3B8;
    font-size:16px;
}

/* SECTION */

.section-card{
    background: rgba(15,23,42,0.88);

    border-radius:24px;

    padding:28px;

    border:1px solid rgba(255,255,255,0.06);

    margin-top:20px;
}

/* ALERT */

.alert-box{
    background:
        linear-gradient(
            135deg,
            rgba(127,29,29,0.92),
            rgba(69,10,10,0.92)
        );

    border-left:5px solid #EF4444;

    padding:24px;

    border-radius:18px;

    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚡ GridPulse-AI")

st.sidebar.markdown("""
Enterprise Energy Intelligence Platform
""")

st.sidebar.success("AI Engine Active")
st.sidebar.info("Forecasting Pipeline Online")
st.sidebar.warning("1 High Risk Zone Detected")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 🧠 AI Modules

- Predictive Forecasting
- Risk Intelligence
- Load Optimization
- Carbon Analytics
- Smart Grid Insights
""")

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero-box">

<div class="hero-title">
⚡ GridPulse-AI
</div>

<div class="hero-sub">
Enterprise Energy Forecasting, Autonomous Risk Intelligence,
Carbon Analytics & Smart Grid Optimization Platform.
Designed with advanced AI-driven telemetry visualization,
executive-level forecasting intelligence and modern operational analytics.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.kpi-card{
    background: linear-gradient(145deg,#0F172A,#111827);
    border:1px solid rgba(56,189,248,0.2);
    border-radius:22px;
    padding:30px;
    min-height:220px;
    box-shadow:0 0 30px rgba(0,0,0,0.35);
    transition:0.3s;
}

.kpi-card:hover{
    transform:translateY(-5px);
    border:1px solid #38BDF8;
}

.kpi-title{
    color:#CBD5E1;
    font-size:20px;
    font-weight:600;
    margin-bottom:25px;
}

.kpi-value{
    font-size:54px;
    font-weight:800;
    margin-bottom:12px;
}

.kpi-delta{
    color:#94A3B8;
    font-size:18px;
}

.blue{
    color:#38BDF8;
}

.green{
    color:#22C55E;
}

.orange{
    color:#F59E0B;
}

.red{
    color:#EF4444;
}

</style>
""", unsafe_allow_html=True)
# ================= KPI SECTION =================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">Total Energy Demand</div>
        <div class="kpi-value blue">1.34M</div>
        <div class="kpi-delta">▲ 4.8% Growth</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">Grid Efficiency</div>
        <div class="kpi-value green">94.2%</div>
        <div class="kpi-delta">Optimal Performance</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">Carbon Reduction</div>
        <div class="kpi-value orange">-18%</div>
        <div class="kpi-delta">Sustainable Trend</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">Risk Detection</div>
        <div class="kpi-value red">ACTIVE</div>
        <div class="kpi-delta">1 Critical Zone</div>
    </div>
    """, unsafe_allow_html=True)
# =========================================================
# ALERT SECTION
# =========================================================

st.markdown("""
<div class="alert-box">

<h2 style="color:white;">
🚨 Autonomous Risk Intelligence Alert
</h2>

<p style="color:#FECACA; line-height:1.8; font-size:17px;">
Critical anomaly detected in Hyderabad South Circle.
The AI engine identified abnormal load deviation patterns
outside expected operational thresholds.

<br><br>

Recommended Action:
Throttle non-essential commercial load between
14:00 – 18:00 peak window.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# AI INTELLIGENCE SECTION
# =========================================================

st.markdown("""
<div class="section-card">

<h2 style="
color:white;
font-size:2rem;
font-weight:700;
margin-bottom:20px;
">
🧠 AI Intelligence
</h2>

<p style="
color:#CBD5E1;
font-size:1.05rem;
line-height:1.8;
">
GridPulse-AI continuously analyzes grid telemetry,
demand spikes, carbon performance, anomaly zones and
enterprise operational risk using advanced AI-driven
intelligence systems.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# CHART DATA
# =========================================================

dates = pd.date_range(
    start="2026-01-01",
    periods=30
)

demand = np.random.randint(
    800000,
    1400000,
    30
)

df = pd.DataFrame({
    "Date": dates,
    "Demand": demand
})

# =========================================================
# FORECAST CHART
# =========================================================

st.markdown("""
<div class="section-card">
<h2 style="color:white;">
📈 Predictive Demand Forecast
</h2>
</div>
""", unsafe_allow_html=True)

fig = px.area(
    df,
    x="Date",
    y="Demand",
    template="plotly_dark"
)

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(
    fig,
    use_container_width=True
)
