# ==========================================
# EXECUTIVE OVERVIEW DASHBOARD
# ==========================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Executive Overview",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/final_enterprise_energy_intelligence.csv"
)

# ==========================================
# HEADER
# ==========================================

st.title("📊 Executive Energy Overview")

st.markdown("""
Enterprise-level commercial energy intelligence dashboard
for monitoring operational efficiency and energy consumption.
""")

# ==========================================
# KPI CALCULATIONS
# ==========================================

total_units = df['units'].sum()

total_load = df['load'].sum()

total_services = df['totservices'].sum()

high_risk = (
    df['risk_category'] == 'HIGH RISK'
).sum()

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Units",
        f"{total_units:,.0f}"
    )

with col2:
    st.metric(
        "Total Load",
        f"{total_load:,.0f}"
    )

with col3:
    st.metric(
        "Total Services",
        f"{total_services:,.0f}"
    )

with col4:
    st.metric(
        "High Risk Regions",
        f"{high_risk}"
    )

st.markdown("---")

# ==========================================
# TOP AREAS CHART
# ==========================================

top_areas = (
    df.groupby('area')['units']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    top_areas,
    x='area',
    y='units',
    title="Top 10 Commercial Areas by Consumption",
    text_auto=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# RISK DISTRIBUTION
# ==========================================

risk_counts = (
    df['risk_category']
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    'Risk Category',
    'Count'
]

fig2 = px.pie(
    risk_counts,
    names='Risk Category',
    values='Count',
    title="Enterprise Risk Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# CIRCLE ANALYSIS
# ==========================================

circle_consumption = (
    df.groupby('circle')['units']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig3 = px.bar(
    circle_consumption,
    x='circle',
    y='units',
    title="Circle-wise Energy Consumption"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.markdown("---")

st.subheader("Executive Insights")

st.info(f"""
• Total commercial energy consumption reached {total_units:,.0f} units.

• {high_risk} high-risk operational regions were detected.

• Regional consumption patterns indicate concentration
  in top commercial zones.

• AI-driven optimization opportunities identified for
  enterprise efficiency improvement.
""")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "TGSPDCL AI Energy Intelligence Platform"
)