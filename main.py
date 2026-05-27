import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="TGSPDCL AI Energy Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #111827 0%,
        #0F172A 100%
    );
}

h1, h2, h3 {
    color: white;
}

.metric-card {
    background: linear-gradient(
        135deg,
        #1E293B,
        #0F172A
    );
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #334155;
    box-shadow: 0px 0px 15px rgba(0,255,255,0.08);
}

.module-card {
    background: linear-gradient(
        135deg,
        #111827,
        #1E293B
    );
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #334155;
    margin-bottom: 20px;
}

.highlight {
    color: #38BDF8;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("⚡ TGSPDCL AI Platform")

st.sidebar.markdown("---")

st.sidebar.success("System Active")

st.sidebar.markdown("""
### Modules

✅ Executive Overview  
✅ Forecasting Engine  
✅ Anomaly Detection  
✅ Optimization Engine  
✅ Regional Analytics  
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Enterprise AI Energy Intelligence System"
)

# =====================================
# HERO SECTION
# =====================================

st.markdown("""
# ⚡ TGSPDCL AI Energy Intelligence Platform
""")

st.markdown("""
### Enterprise Energy Forecasting & Optimization System
""")

st.markdown("""
AI-powered commercial energy intelligence system for:
- forecasting
- anomaly detection
- operational optimization
- regional analytics
""")

st.markdown("---")

# =====================================
# PLATFORM OVERVIEW
# =====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
    <h3>📈 AI Forecasting</h3>
    <p>LightGBM-based enterprise prediction engine.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
    <h3>🚨 Risk Detection</h3>
    <p>Isolation Forest anomaly intelligence system.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
    <h3>🌍 Regional Analytics</h3>
    <p>Commercial electricity consumption intelligence.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# =====================================
# PROJECT CAPABILITIES
# =====================================

st.markdown("""
## 🚀 Platform Capabilities
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">

    ### AI Intelligence Features

    ✔ Energy Consumption Forecasting  
    ✔ Commercial Load Prediction  
    ✔ Enterprise Efficiency Analytics  
    ✔ Regional Intelligence Monitoring  
    ✔ Consumption Trend Analysis  

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">

    ### Optimization Features

    ✔ High-Risk Area Detection  
    ✔ Operational Optimization  
    ✔ Resource Utilization Insights  
    ✔ Business KPI Monitoring  
    ✔ AI-powered Recommendations  

    </div>
    """, unsafe_allow_html=True)

# =====================================
# SYSTEM STATUS
# =====================================

st.markdown("---")

st.success("✅ System initialized successfully.")

st.caption(
    "TGSPDCL Enterprise Energy Optimization Platform | AIMD 2026 Capstone Project"
)