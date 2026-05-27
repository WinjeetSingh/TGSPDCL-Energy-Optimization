import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Forecasting Engine",
    layout="wide"
)

# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv(
    "data/final_enterprise_energy_intelligence.csv"
)

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load(
    "models/lightgbm_energy_model.pkl"
)

# =========================================
# PAGE TITLE
# =========================================

st.title("📈 AI Energy Forecasting Engine")

st.markdown("""
LightGBM-powered commercial energy forecasting system
for predicting enterprise electricity consumption.
""")

# =========================================
# SELECT FEATURES
# =========================================

selected_features = [
    'circle',
    'division',
    'subdivision',
    'section',
    'area',
    'totservices',
    'billdservices',
    'load',
    'units_per_service',
    'service_utilization_ratio',
    'avg_load_per_service',
    'load_efficiency'
]

# =========================================
# CREATE FEATURE DATAFRAME
# =========================================

X = df[selected_features].copy()

# =========================================
# ENCODE CATEGORICAL COLUMNS
# =========================================

categorical_columns = [
    'circle',
    'division',
    'subdivision',
    'section',
    'area'
]

for col in categorical_columns:
    X[col] = X[col].astype('category').cat.codes

# =========================================
# PREDICTIONS
# =========================================

predictions = model.predict(X)

df['predicted_units'] = predictions

# =========================================
# KPI SECTION
# =========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Predicted Units",
        f"{df['predicted_units'].mean():,.2f}"
    )

with col2:
    st.metric(
        "Maximum Predicted Units",
        f"{df['predicted_units'].max():,.2f}"
    )

with col3:
    st.metric(
        "Minimum Predicted Units",
        f"{df['predicted_units'].min():,.2f}"
    )

# =========================================
# ACTUAL VS PREDICTED
# =========================================

st.subheader("Actual vs Predicted Consumption")

fig = px.scatter(
    df,
    x='units',
    y='predicted_units',
    title='Actual vs Predicted Electricity Consumption',
    labels={
        'units': 'Actual Units',
        'predicted_units': 'Predicted Units'
    }
)

st.plotly_chart(fig, width='stretch')

# =========================================
# TOP PREDICTED AREAS
# =========================================

st.subheader("Top Areas by Predicted Consumption")

top_predicted = (
    df.groupby('area')['predicted_units']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    top_predicted,
    x='area',
    y='predicted_units',
    title='Top 10 Areas by Predicted Energy Consumption'
)

st.plotly_chart(fig2, width='stretch')

# =========================================
# FORECAST TABLE
# =========================================

st.subheader("Forecast Data Table")

forecast_table = df[
    [
        'circle',
        'division',
        'area',
        'units',
        'predicted_units'
    ]
].head(50)

st.dataframe(
    forecast_table,
    width='stretch'
)

# =========================================
# SUCCESS MESSAGE
# =========================================

st.success("Forecasting system initialized successfully.")