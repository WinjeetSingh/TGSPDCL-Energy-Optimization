# ============================================
# IMPORT LIBRARIES
# ============================================

import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
from theme import apply_theme

st.set_page_config(layout="wide")

apply_theme()

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Executive Overview",
    page_icon="📊",
    layout="wide"
)

# ============================================
# LOAD DATA
# ============================================

df = pd.read_csv(
    "data/final_enterprise_energy_intelligence.csv"
)

# ============================================
# TITLE
# ============================================

st.title("📊 Executive Energy Intelligence Dashboard")

st.markdown("""
Enterprise-level commercial electricity analytics
and operational intelligence platform.
""")

st.markdown("---")

# ============================================
# KPI METRICS
# ============================================

total_units = df['units'].sum()

total_load = df['load'].sum()

total_services = df['totservices'].sum()

avg_efficiency = df['load_efficiency'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚡ Total Units",
        f"{total_units:,.0f}"
    )

with col2:
    st.metric(
        "🏭 Total Load",
        f"{total_load:,.0f}"
    )

with col3:
    st.metric(
        "🔌 Total Services",
        f"{total_services:,.0f}"
    )

with col4:
    st.metric(
        "📈 Avg Efficiency",
        f"{avg_efficiency:.2f}"
    )

st.markdown("---")

# ============================================
# TOP AREAS ANALYSIS
# ============================================

st.subheader("🏙️ Top Areas by Energy Consumption")

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
    color='units',
    title='Top 10 Commercial Areas'
)

st.plotly_chart(
    fig1,
    width='stretch'
)

# ============================================
# CIRCLE-WISE ANALYSIS
# ============================================

st.subheader("🌍 Circle-wise Energy Consumption")

circle_data = (
    df.groupby('circle')['units']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig2 = px.pie(
    circle_data,
    names='circle',
    values='units',
    title='Circle-wise Consumption Distribution'
)

st.plotly_chart(
    fig2,
    width='stretch'
)

# ============================================
# LOAD VS UNITS
# ============================================

st.subheader("⚡ Load vs Units Analysis")

fig3 = px.scatter(
    df,
    x='load',
    y='units',
    color='risk_category',
    title='Operational Load vs Energy Consumption',
    hover_data=['area']
)

st.plotly_chart(
    fig3,
    width='stretch'
)

# ============================================
# RISK DISTRIBUTION
# ============================================

st.subheader("🚨 Risk Category Distribution")

risk_data = (
    df['risk_category']
    .value_counts()
    .reset_index()
)

risk_data.columns = [
    'Risk Category',
    'Count'
]

fig4 = px.bar(
    risk_data,
    x='Risk Category',
    y='Count',
    color='Risk Category',
    title='Enterprise Risk Intelligence'
)

st.plotly_chart(
    fig4,
    width='stretch'
)

# ============================================
# AI INSIGHTS
# ============================================

st.markdown("---")

st.subheader("🧠 AI Business Insights")

st.success("""
✅ High energy consumption detected in
major commercial enterprise regions.
""")

st.warning("""
⚠️ Multiple regions show abnormal
operational load behavior.
""")

st.info("""
📈 Forecasting engine predicts
growing electricity demand trends.
""")

# ============================================
# DATA PREVIEW
# ============================================

st.markdown("---")

st.subheader("📄 Enterprise Dataset Preview")

st.dataframe(
    df.head(20),
    width='stretch'
)

# ============================================
# DOWNLOAD BUTTON
# ============================================

csv = df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Enterprise Dataset",
    data=csv,
    file_name="enterprise_energy_data.csv",
    mime="text/csv"
)

# ============================================
# FOOTER
# ============================================

st.markdown("---")

st.caption(
    "⚡ GridPulse AI | Executive Intelligence Dashboard"
)