# ==========================================
# REGIONAL ANALYTICS DASHBOARD
# ==========================================

import streamlit as st
import pandas as pd

import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Regional Analytics",
    page_icon="🌍",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/final_enterprise_energy_intelligence.csv"
)

# ==========================================
# PAGE HEADER
# ==========================================

st.title("🌍 Regional Energy Analytics")

st.markdown("""
Regional enterprise intelligence dashboard
for analyzing commercial electricity consumption,
efficiency, and operational behavior.
""")

# ==========================================
# KPI CALCULATIONS
# ==========================================

total_circles = df['circle'].nunique()

total_divisions = df['division'].nunique()

total_areas = df['area'].nunique()

avg_efficiency = (
    df['load_efficiency']
    .mean()
)

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Circles",
        total_circles
    )

with col2:
    st.metric(
        "Total Divisions",
        total_divisions
    )

with col3:
    st.metric(
        "Commercial Areas",
        total_areas
    )

with col4:
    st.metric(
        "Avg Efficiency",
        f"{avg_efficiency:.2f}"
    )

st.markdown("---")

# ==========================================
# CIRCLE-WISE CONSUMPTION
# ==========================================

circle_consumption = (
    df.groupby('circle')['units']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig1 = px.bar(
    circle_consumption,
    x='circle',
    y='units',
    title="Circle-wise Electricity Consumption",
    text_auto=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# DIVISION-WISE LOAD
# ==========================================

division_load = (
    df.groupby('division')['load']
    .sum()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

fig2 = px.bar(
    division_load,
    x='division',
    y='load',
    title="Top Divisions by Operational Load",
    text_auto=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# REGIONAL EFFICIENCY
# ==========================================

circle_efficiency = (
    df.groupby('circle')['load_efficiency']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig3 = px.bar(
    circle_efficiency,
    x='circle',
    y='load_efficiency',
    title="Regional Load Efficiency Ranking",
    text_auto=True
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# RISK HEATMAP
# ==========================================

risk_summary = (
    df.groupby(['circle', 'risk_category'])
    .size()
    .reset_index(name='count')
)

fig4 = px.density_heatmap(
    risk_summary,
    x='circle',
    y='risk_category',
    z='count',
    title="Regional Risk Heatmap"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ==========================================
# INTERACTIVE FILTER
# ==========================================

st.markdown("---")

st.subheader("Regional Intelligence Explorer")

selected_circle = st.selectbox(
    "Select Circle",
    sorted(df['circle'].unique())
)

filtered_df = df[
    df['circle'] == selected_circle
]

st.dataframe(
    filtered_df[
        [
            'circle',
            'division',
            'area',
            'units',
            'load',
            'load_efficiency',
            'risk_category'
        ]
    ].head(100)
)

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.markdown("---")

st.subheader("Regional Intelligence Insights")

st.info(f"""
• {total_circles} operational circles analyzed.

• Regional consumption patterns indicate
  concentrated enterprise energy demand.

• Efficiency analysis highlights
  operational optimization opportunities.

• Geographic intelligence supports
  targeted commercial energy planning.
""")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Regional Enterprise Intelligence System"
)