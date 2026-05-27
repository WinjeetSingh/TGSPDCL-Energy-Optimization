import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Executive Overview",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "data/final_enterprise_energy_intelligence.csv"
)

# =====================================
# HEADER
# =====================================

st.title("📊 Executive Energy Intelligence Dashboard")

st.markdown("""
AI-powered enterprise monitoring system for
commercial electricity intelligence.
""")

st.markdown("---")

# =====================================
# KPI SECTION
# =====================================

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
        "🔌 Total Load",
        f"{total_load:,.0f}"
    )

with col3:
    st.metric(
        "🏢 Total Services",
        f"{total_services:,.0f}"
    )

with col4:
    st.metric(
        "📈 Avg Efficiency",
        f"{avg_efficiency:.2f}"
    )

st.markdown("---")

# =====================================
# TOP AREAS
# =====================================

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
    title='Top 10 Areas by Consumption',
    template='plotly_dark'
)

st.plotly_chart(fig1, width='stretch')

# =====================================
# CIRCLE CONSUMPTION
# =====================================

circle_data = (
    df.groupby('circle')['units']
    .sum()
    .reset_index()
)

fig2 = px.pie(
    circle_data,
    names='circle',
    values='units',
    title='Circle-wise Consumption Distribution',
    template='plotly_dark'
)

st.plotly_chart(fig2, width='stretch')

# =====================================
# LOAD VS UNITS
# =====================================

fig3 = px.scatter(
    df,
    x='load',
    y='units',
    color='risk_category',
    title='Load vs Units Consumption',
    template='plotly_dark'
)

st.plotly_chart(fig3, width='stretch')

# =====================================
# RISK DISTRIBUTION
# =====================================

risk_counts = (
    df['risk_category']
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    'Risk Category',
    'Count'
]

fig4 = px.bar(
    risk_counts,
    x='Risk Category',
    y='Count',
    color='Risk Category',
    title='Enterprise Risk Distribution',
    template='plotly_dark'
)

st.plotly_chart(fig4, width='stretch')

# =====================================
# DATA PREVIEW
# =====================================

st.markdown("---")

st.subheader("📁 Enterprise Intelligence Dataset")

st.dataframe(
    df.head(20),
    width='stretch'
)

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.success(
    "Executive monitoring system operational."
)