import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Regional Analytics",
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

st.title("🌍 Regional Energy Intelligence")

st.markdown("""
Enterprise regional analytics platform for
commercial electricity monitoring, regional
comparison, and operational intelligence.
""")

st.markdown("---")

# =====================================
# KPI SECTION
# =====================================

total_circles = df['circle'].nunique()

total_divisions = df['division'].nunique()

total_areas = df['area'].nunique()

avg_units = df['units'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏢 Total Circles",
        total_circles
    )

with col2:
    st.metric(
        "📍 Total Divisions",
        total_divisions
    )

with col3:
    st.metric(
        "🌐 Total Areas",
        total_areas
    )

with col4:
    st.metric(
        "⚡ Avg Units",
        f"{avg_units:,.2f}"
    )

st.markdown("---")

# =====================================
# CIRCLE-WISE CONSUMPTION
# =====================================

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

    color='units',

    title='Circle-wise Electricity Consumption',

    template='plotly_dark'
)

st.plotly_chart(fig1, width='stretch')

# =====================================
# DIVISION-WISE LOAD
# =====================================

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

    color='load',

    title='Top Divisions by Load',

    template='plotly_dark'
)

st.plotly_chart(fig2, width='stretch')

# =====================================
# REGIONAL EFFICIENCY
# =====================================

regional_efficiency = (

    df.groupby('circle')['load_efficiency']
    .mean()
    .reset_index()

)

fig3 = px.pie(

    regional_efficiency,

    names='circle',
    values='load_efficiency',

    title='Regional Load Efficiency',

    template='plotly_dark'
)

st.plotly_chart(fig3, width='stretch')

# =====================================
# SERVICE UTILIZATION
# =====================================

service_utilization = (

    df.groupby('area')[
        'service_utilization_ratio'
    ]
    .mean()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()

)

fig4 = px.treemap(

    service_utilization,

    path=['area'],

    values='service_utilization_ratio',

    color='service_utilization_ratio',

    title='Service Utilization Intelligence',

    template='plotly_dark'
)

st.plotly_chart(fig4, width='stretch')

# =====================================
# REGIONAL DATA TABLE
# =====================================

st.markdown("---")

st.subheader("📊 Regional Enterprise Intelligence")

regional_table = (

    df.groupby(
        ['circle', 'division']
    )
    .agg({

        'units': 'sum',

        'load': 'sum',

        'load_efficiency': 'mean',

        'service_utilization_ratio': 'mean'

    })
    .reset_index()

)

st.dataframe(
    regional_table.head(50),
    width='stretch'
)

# =====================================
# EXECUTIVE INSIGHTS
# =====================================

st.markdown("---")

st.subheader("🧠 Executive Regional Insights")

st.info("""
Regional intelligence analysis indicates:

• High-load enterprise regions require monitoring  
• Service utilization varies significantly across divisions  
• Regional efficiency optimization opportunities detected  
• Commercial energy patterns show operational imbalance  
• AI forecasting can improve regional planning efficiency  
""")

# =====================================
# SYSTEM STATUS
# =====================================

st.success(
    "Regional intelligence platform operational."
)