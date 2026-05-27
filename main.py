# ==========================================
# TGSPDCL AI ENERGY INTELLIGENCE PLATFORM
# ==========================================

import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="TGSPDCL AI Energy Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# MAIN HEADER
# ==========================================

st.title("⚡ TGSPDCL AI Energy Intelligence Platform")

st.markdown("""
### Enterprise Energy Forecasting & Optimization System
AI-powered commercial energy intelligence system for
forecasting, anomaly detection, and operational optimization.
""")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.success("Select a module from the sidebar.")

st.sidebar.markdown("---")

st.sidebar.info("""
Modules Included:

✅ Executive Overview  
✅ Forecasting Engine  
✅ Anomaly Detection  
✅ Optimization Engine  
✅ Regional Analytics
""")

# ==========================================
# HOME PAGE CONTENT
# ==========================================

st.header("Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "AI Forecasting",
        "LightGBM"
    )

with col2:
    st.metric(
        "Risk Detection",
        "Isolation Forest"
    )

with col3:
    st.metric(
        "Deployment",
        "Streamlit Cloud"
    )

st.markdown("---")

st.subheader("Project Capabilities")

st.write("""
This platform enables:

- Commercial energy forecasting
- Enterprise anomaly detection
- AI-driven optimization recommendations
- Regional electricity intelligence
- Operational risk analysis
""")

st.markdown("---")

st.success("System initialized successfully.")