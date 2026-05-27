import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Optimization Engine",
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

st.title("⚙ AI Optimization Engine")

st.markdown("""
AI-powered optimization intelligence system
for improving enterprise electricity efficiency
and reducing operational risk.
""")

st.markdown("---")

# =====================================
# KPI SECTION
# =====================================

high_risk_count = (
    df[df['risk_category'] == 'HIGH RISK']
    .shape[0]
)

low_efficiency = (
    df[df['load_efficiency'] < 50]
    .shape[0]
)

avg_utilization = (
    df['service_utilization_ratio']
    .mean()
)

avg_efficiency = (
    df['load_efficiency']
    .mean()
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚠ High Risk Regions",
        f"{high_risk_count:,}"
    )

with col2:
    st.metric(
        "📉 Low Efficiency Records",
        f"{low_efficiency:,}"
    )

with col3:
    st.metric(
        "🔋 Avg Utilization",
        f"{avg_utilization:.2f}"
    )

with col4:
    st.metric(
        "⚡ Avg Efficiency",
        f"{avg_efficiency:.2f}"
    )

st.markdown("---")

# =====================================
# LOW EFFICIENCY AREAS
# =====================================

low_efficiency_areas = (

    df.groupby('area')['load_efficiency']
    .mean()
    .sort_values()
    .head(10)
    .reset_index()

)

fig1 = px.bar(

    low_efficiency_areas,

    x='area',
    y='load_efficiency',

    color='load_efficiency',

    title='Low Efficiency Commercial Areas',

    template='plotly_dark'
)

st.plotly_chart(fig1, width='stretch')

# =====================================
# HIGH LOAD AREAS
# =====================================

high_load_areas = (

    df.groupby('area')['load']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()

)

fig2 = px.bar(

    high_load_areas,

    x='area',
    y='load',

    color='load',

    title='High Load Enterprise Regions',

    template='plotly_dark'
)

st.plotly_chart(fig2, width='stretch')

# =====================================
# OPTIMIZATION RECOMMENDATIONS
# =====================================

st.markdown("---")

st.subheader("🧠 AI Optimization Recommendations")

recommendations = pd.DataFrame({

    'Priority': [
        'HIGH',
        'HIGH',
        'MEDIUM',
        'MEDIUM',
        'LOW'
    ],

    'Recommendation': [

        'Investigate high anomaly commercial zones',

        'Reduce excessive operational load',

        'Improve service utilization ratio',

        'Monitor regional efficiency patterns',

        'Optimize enterprise energy distribution'
    ],

    'Expected Impact': [

        'Risk Reduction',

        'Operational Stability',

        'Better Efficiency',

        'Performance Monitoring',

        'Energy Optimization'
    ]

})

st.dataframe(
    recommendations,
    width='stretch'
)

# =====================================
# RISK VS EFFICIENCY
# =====================================

fig3 = px.scatter(

    df,

    x='load_efficiency',

    y='anomaly_score',

    color='risk_category',

    title='Risk vs Efficiency Intelligence',

    template='plotly_dark',

    hover_data=[
        'circle',
        'division',
        'area'
    ]
)

st.plotly_chart(fig3, width='stretch')

# =====================================
# EXECUTIVE ACTION CENTER
# =====================================

st.markdown("---")

st.subheader("🚀 Executive Action Center")

st.warning("""
Recommended enterprise actions:

• Prioritize HIGH RISK regions  
• Monitor inefficient commercial areas  
• Reduce abnormal operational loads  
• Improve utilization efficiency  
• Increase predictive monitoring frequency  
""")

# =====================================
# SYSTEM STATUS
# =====================================

st.success(
    "Optimization intelligence engine operational."
)