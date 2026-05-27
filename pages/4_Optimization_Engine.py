# ==========================================
# OPTIMIZATION ENGINE
# ==========================================

import streamlit as st
import pandas as pd

import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Optimization Engine",
    page_icon="⚙️",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/optimization_recommendations.csv"
)

# ==========================================
# PAGE HEADER
# ==========================================

st.title("⚙️ AI Optimization Engine")

st.markdown("""
AI-powered operational optimization system
for enterprise electricity intelligence and
business recommendation generation.
""")

# ==========================================
# KPI CALCULATIONS
# ==========================================

total_savings = (
    df['estimated_savings_units']
    .sum()
)

high_priority = (
    df['priority_level'] == 'HIGH PRIORITY'
).sum()

medium_priority = (
    df['priority_level'] == 'MEDIUM PRIORITY'
).sum()

low_priority = (
    df['priority_level'] == 'LOW PRIORITY'
).sum()

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Estimated Savings",
        f"{total_savings:,.0f}"
    )

with col2:
    st.metric(
        "High Priority",
        f"{high_priority:,}"
    )

with col3:
    st.metric(
        "Medium Priority",
        f"{medium_priority:,}"
    )

with col4:
    st.metric(
        "Low Priority",
        f"{low_priority:,}"
    )

st.markdown("---")

# ==========================================
# PRIORITY DISTRIBUTION
# ==========================================

priority_distribution = (
    df['priority_level']
    .value_counts()
    .reset_index()
)

priority_distribution.columns = [
    'Priority Level',
    'Count'
]

fig1 = px.pie(
    priority_distribution,
    names='Priority Level',
    values='Count',
    title="Operational Priority Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# HIGH PRIORITY AREAS
# ==========================================

high_priority_areas = (
    df[df['priority_level'] == 'HIGH PRIORITY']
    .groupby('area')
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

high_priority_areas.columns = [
    'Area',
    'Count'
]

fig2 = px.bar(
    high_priority_areas,
    x='Area',
    y='Count',
    title="Top High Priority Commercial Areas",
    text_auto=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# SAVINGS OPPORTUNITIES
# ==========================================

top_savings = (
    df.groupby('area')['estimated_savings_units']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    top_savings,
    x='area',
    y='estimated_savings_units',
    title="Top Estimated Energy Savings Areas",
    text_auto=True
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# AI RECOMMENDATION TABLE
# ==========================================

st.markdown("---")

st.subheader("AI Optimization Recommendations")

selected_priority = st.selectbox(
    "Select Priority Level",
    df['priority_level'].unique()
)

filtered_df = df[
    df['priority_level'] == selected_priority
]

st.dataframe(
    filtered_df[
        [
            'circle',
            'division',
            'area',
            'priority_level',
            'optimization_recommendation',
            'estimated_savings_units'
        ]
    ].head(50)
)

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.markdown("---")

st.subheader("Executive Optimization Insights")

st.success(f"""
• Estimated enterprise savings opportunity:
  {total_savings:,.0f} energy units.

• High-priority operational regions require
  immediate optimization attention.

• AI recommendation engine identified
  enterprise efficiency improvement opportunities.

• Regional intelligence suggests targeted
  operational load balancing strategies.
""")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "AI Optimization & Decision Intelligence System"
)