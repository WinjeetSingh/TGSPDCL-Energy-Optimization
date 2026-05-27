# ==========================================
# ANOMALY DETECTION DASHBOARD
# ==========================================

import streamlit as st
import pandas as pd

import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Anomaly Detection",
    page_icon="🚨",
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

st.title("🚨 Enterprise Anomaly Detection")

st.markdown("""
Isolation Forest powered anomaly detection system
for identifying abnormal commercial energy behavior.
""")

# ==========================================
# KPI METRICS
# ==========================================

total_records = len(df)

anomaly_count = (
    df['anomaly'] == -1
).sum()

normal_count = (
    df['anomaly'] == 1
).sum()

high_risk = (
    df['risk_category'] == 'HIGH RISK'
).sum()

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Records",
        f"{total_records:,}"
    )

with col2:
    st.metric(
        "Anomalies Detected",
        f"{anomaly_count:,}"
    )

with col3:
    st.metric(
        "Normal Operations",
        f"{normal_count:,}"
    )

with col4:
    st.metric(
        "High Risk Regions",
        f"{high_risk:,}"
    )

st.markdown("---")

# ==========================================
# ANOMALY VISUALIZATION
# ==========================================

fig1 = px.scatter(
    df,
    x='load',
    y='units',
    color='risk_category',
    title="Energy Consumption Anomaly Detection",
    opacity=0.7
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# RISK DISTRIBUTION
# ==========================================

risk_distribution = (
    df['risk_category']
    .value_counts()
    .reset_index()
)

risk_distribution.columns = [
    'Risk Category',
    'Count'
]

fig2 = px.pie(
    risk_distribution,
    names='Risk Category',
    values='Count',
    title="Operational Risk Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# TOP HIGH-RISK AREAS
# ==========================================

high_risk_areas = (
    df[df['risk_category'] == 'HIGH RISK']
    .groupby('area')
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

high_risk_areas.columns = [
    'Area',
    'Anomaly Count'
]

fig3 = px.bar(
    high_risk_areas,
    x='Area',
    y='Anomaly Count',
    title="Top High-Risk Commercial Areas",
    text_auto=True
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# INTERACTIVE FILTER
# ==========================================

st.markdown("---")

st.subheader("Regional Risk Intelligence")

selected_circle = st.selectbox(
    "Select Circle",
    df['circle'].unique()
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
            'risk_category',
            'anomaly_score'
        ]
    ].head(50)
)

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.markdown("---")

st.subheader("Operational Intelligence Insights")

st.warning(f"""
• {anomaly_count:,} operational anomalies detected.

• High-risk regions indicate abnormal
  enterprise electricity behavior.

• Commercial load spikes suggest
  optimization opportunities.

• AI monitoring system successfully
  identified enterprise operational outliers.
""")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Enterprise Risk Intelligence System"
)