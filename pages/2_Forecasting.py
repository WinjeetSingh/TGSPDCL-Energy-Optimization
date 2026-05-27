import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
from sklearn.preprocessing import LabelEncoder

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Forecasting",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "data/final_energy_dataset.csv"
)

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load(
    "models/lightgbm_energy_model.pkl"
)

# =====================================
# TITLE
# =====================================

st.title("📈 AI Energy Forecasting Engine")

st.markdown("""
LightGBM-powered commercial energy forecasting
system for predicting enterprise electricity consumption.
""")

st.markdown("---")

# =====================================
# SIDEBAR INPUTS
# =====================================

st.sidebar.header("⚙ Forecast Inputs")

circle = st.sidebar.selectbox(
    "Select Circle",
    df['circle'].unique()
)

division = st.sidebar.selectbox(
    "Select Division",
    df['division'].unique()
)

subdivision = st.sidebar.selectbox(
    "Select Subdivision",
    df['subdivision'].unique()
)

section = st.sidebar.selectbox(
    "Select Section",
    df['section'].unique()
)

area = st.sidebar.selectbox(
    "Select Area",
    df['area'].unique()
)

totservices = st.sidebar.number_input(
    "Total Services",
    min_value=1,
    value=100
)

billdservices = st.sidebar.number_input(
    "Billed Services",
    min_value=1,
    value=90
)

load = st.sidebar.number_input(
    "Load",
    min_value=1.0,
    value=5000.0
)

# =====================================
# FEATURE ENGINEERING
# =====================================

units_per_service = load / totservices

service_utilization_ratio = (
    billdservices / totservices
)

avg_load_per_service = (
    load / totservices
)

load_efficiency = (
    load / billdservices
)

# =====================================
# ENCODING
# =====================================

categorical_columns = [
    'circle',
    'division',
    'subdivision',
    'section',
    'area'
]

for col in categorical_columns:
    
    le = LabelEncoder()
    
    df[col] = le.fit_transform(
        df[col].astype(str)
    )

# Store encoders
encoders = {}

for col in categorical_columns:
    
    encoder = LabelEncoder()
    
    encoder.fit(
        pd.read_csv(
            "data/final_energy_dataset.csv"
        )[col].astype(str)
    )
    
    encoders[col] = encoder

# Encode inputs
circle_encoded = encoders['circle'].transform([circle])[0]

division_encoded = encoders['division'].transform([division])[0]

subdivision_encoded = encoders['subdivision'].transform([subdivision])[0]

section_encoded = encoders['section'].transform([section])[0]

area_encoded = encoders['area'].transform([area])[0]

# =====================================
# CREATE INPUT DATAFRAME
# =====================================

input_df = pd.DataFrame({

    'circle': [circle_encoded],

    'division': [division_encoded],

    'subdivision': [subdivision_encoded],

    'section': [section_encoded],

    'area': [area_encoded],

    'totservices': [totservices],

    'billdservices': [billdservices],

    'load': [load],

    'units_per_service': [units_per_service],

    'service_utilization_ratio': [
        service_utilization_ratio
    ],

    'avg_load_per_service': [
        avg_load_per_service
    ],

    'load_efficiency': [
        load_efficiency
    ]

})

# =====================================
# PREDICTION
# =====================================

prediction = model.predict(input_df)[0]

# =====================================
# PREDICTION CARD
# =====================================

st.subheader("⚡ Forecasted Energy Consumption")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Predicted Units",
        f"{prediction:,.2f}"
    )

with col2:
    st.metric(
        "Load",
        f"{load:,.2f}"
    )

with col3:
    st.metric(
        "Service Utilization",
        f"{service_utilization_ratio:.2f}"
    )

st.markdown("---")

# =====================================
# FORECAST VISUALIZATION
# =====================================

forecast_df = pd.DataFrame({
    'Metric': [
        'Predicted Units',
        'Load',
        'Total Services'
    ],
    'Value': [
        prediction,
        load,
        totservices
    ]
})

fig1 = px.bar(
    forecast_df,
    x='Metric',
    y='Value',
    color='Metric',
    title='Forecast Intelligence',
    template='plotly_dark'
)

st.plotly_chart(fig1, width='stretch')

# =====================================
# LOAD VS FORECAST
# =====================================

fig2 = px.scatter(
    df,
    x='load',
    y='units',
    title='Historical Load vs Units',
    template='plotly_dark'
)

fig2.add_trace(
    go.Scatter(
        x=[load],
        y=[prediction],
        mode='markers',
        marker=dict(
            size=15
        ),
        name='Current Prediction'
    )
)

st.plotly_chart(fig2, width='stretch')

# =====================================
# MODEL INSIGHTS
# =====================================

st.markdown("---")

st.subheader("🧠 AI Model Insights")

st.info("""
The LightGBM forecasting engine analyzes:

• enterprise energy consumption  
• operational efficiency  
• service utilization  
• regional energy patterns  
• commercial load behavior  
""")

# =====================================
# FOOTER
# =====================================

st.success(
    "AI Forecasting Engine operational."
)