import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from theme import apply_theme

st.set_page_config(layout="wide")

apply_theme()

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Anomaly Detection",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "data/final_enterprise_energy_intelligence.csv"
)

# =====================================
# TITLE
# =====================================

st.title("🚨 AI Anomaly Detection System")

st.markdown("""
Isolation Forest-powered enterprise anomaly
intelligence system for detecting suspicious
commercial electricity behavior.
""")

st.markdown("---")

# =====================================
# KPI SECTION
# =====================================

total_anomalies = (
    df[df['anomaly'] == -1]
    .shape[0]
)

high_risk = (
    df[df['risk_category'] == 'HIGH RISK']
    .shape[0]
)

avg_anomaly_score = (
    df['anomaly_score']
    .mean()
)

total_records = df.shape[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🚨 Total Anomalies",
        f"{total_anomalies:,}"
    )

with col2:
    st.metric(
        "⚠ High Risk Regions",
        f"{high_risk:,}"
    )

with col3:
    st.metric(
        "📉 Avg Risk Score",
        f"{avg_anomaly_score:.4f}"
    )

with col4:
    st.metric(
        "📁 Total Records",
        f"{total_records:,}"
    )

st.markdown("---")

# =====================================
# ANOMALY SCATTER PLOT
# =====================================

fig1 = px.scatter(
    df,
    x='load',
    y='units',
    color='risk_category',
    title='Load vs Units Anomaly Intelligence',
    template='plotly_dark',
    hover_data=[
        'circle',
        'division',
        'area'
    ]
)

st.plotly_chart(fig1, width='stretch')

# =====================================
# TOP HIGH RISK AREAS
# =====================================

top_risk_areas = (
    df[df['risk_category'] == 'HIGH RISK']
    .groupby('area')
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

top_risk_areas.columns = [
    'Area',
    'Anomaly Count'
]

fig2 = px.bar(
    top_risk_areas,
    x='Area',
    y='Anomaly Count',
    color='Anomaly Count',
    title='Top High Risk Commercial Areas',
    template='plotly_dark'
)

st.plotly_chart(fig2, width='stretch')

# =====================================
# RISK DISTRIBUTION
# =====================================

risk_distribution = (
    df['risk_category']
    .value_counts()
    .reset_index()
)

risk_distribution.columns = [
    'Risk Category',
    'Count'
]

fig3 = px.pie(
    risk_distribution,
    names='Risk Category',
    values='Count',
    title='Enterprise Risk Distribution',
    template='plotly_dark'
)

st.plotly_chart(fig3, width='stretch')

# =====================================
# ANOMALY TABLE
# =====================================

st.markdown("---")

st.subheader("⚠ Suspicious Enterprise Records")

anomalies = df[df['anomaly'] == -1]

st.dataframe(

    anomalies[
        [
            'circle',
            'division',
            'area',
            'units',
            'load',
            'risk_category',
            'anomaly_score'
        ]
    ].head(50),

    width='stretch'
)

# =====================================
# RISK HEATMAP
# =====================================

st.markdown("---")

heatmap_data = (
    df.groupby('circle')['anomaly_score']
    .mean()
    .reset_index()
)

fig4 = px.treemap(
    heatmap_data,
    path=['circle'],
    values='anomaly_score',
    color='anomaly_score',
    title='Regional Risk Heatmap',
    template='plotly_dark'
)

st.plotly_chart(fig4, width='stretch')

# =====================================
# ALERT SECTION
# =====================================

st.markdown("---")

st.error("""
⚠ Enterprise monitoring system detected
high-risk commercial electricity patterns
requiring operational investigation.
""")

# =====================================
# FOOTER
# =====================================

st.success(
    "AI anomaly intelligence engine operational."
)