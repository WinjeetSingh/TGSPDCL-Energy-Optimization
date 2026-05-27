import streamlit as st

def apply_theme():

    st.markdown("""
    <style>

    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header {visibility:hidden;}

    html, body, [class*="css"]{
        font-family:'Segoe UI',sans-serif;
        color:white;
    }

    .stApp{
        background:
            radial-gradient(circle at top left, rgba(0,212,255,0.10), transparent 30%),
            radial-gradient(circle at top right, rgba(139,92,246,0.12), transparent 30%),
            linear-gradient(
                135deg,
                #020617 0%,
                #071028 40%,
                #0F172A 100%
            );
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"]{
        background:
            linear-gradient(
                180deg,
                rgba(2,6,23,0.98),
                rgba(15,23,42,0.98)
            );

        border-right:1px solid rgba(255,255,255,0.08);
    }

    /* HERO CARD */

    .hero-card{
        background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.95),
                rgba(30,41,59,0.90)
            );

        border:1px solid rgba(255,255,255,0.08);

        border-radius:30px;

        padding:3rem;

        box-shadow:
            0 0 40px rgba(0,212,255,0.12),
            0 20px 60px rgba(0,0,0,0.35);

        margin-bottom:2rem;
    }

    /* KPI */

    .kpi-card{
        background:rgba(15,23,42,0.90);

        border:1px solid rgba(255,255,255,0.08);

        border-radius:24px;

        padding:30px;

        min-height:220px;

        transition:0.3s ease;

        box-shadow:
            0 10px 30px rgba(0,0,0,0.25);
    }

    .kpi-card:hover{
        transform:translateY(-6px);

        border:1px solid rgba(56,189,248,0.35);

        box-shadow:
            0 15px 40px rgba(0,212,255,0.15);
    }

    .kpi-title{
        color:#CBD5E1;
        font-size:1.1rem;
        font-weight:600;
        margin-bottom:20px;
    }

    .kpi-value{
        font-size:3rem;
        font-weight:800;
        margin-bottom:10px;
    }

    .kpi-delta{
        color:#94A3B8;
        font-size:1rem;
    }

    /* SECTION */

    .section-card{
        background:rgba(15,23,42,0.90);

        border-radius:28px;

        padding:2rem;

        border:1px solid rgba(255,255,255,0.06);

        margin-top:1rem;
        margin-bottom:1rem;
    }

    /* CHART */

    .chart-card{
        background:rgba(15,23,42,0.88);

        border-radius:24px;

        padding:1.5rem;

        border:1px solid rgba(255,255,255,0.06);

        margin-top:1rem;
    }

    /* SIDEBAR TEXT */

    .sidebar-title{
        color:white;
        font-size:1.5rem;
        font-weight:800;
        margin-bottom:0.5rem;
    }

    .sidebar-sub{
        color:#CBD5E1;
        font-size:0.95rem;
        line-height:1.7;
    }

    /* BUTTON */

    .stButton > button{
        width:100%;

        border:none;

        border-radius:14px;

        background:
            linear-gradient(
                90deg,
                #0EA5E9,
                #2563EB
            );

        color:white;

        font-weight:700;

        padding:0.8rem;
    }

    /* METRIC */

    [data-testid="metric-container"]{
        background:rgba(15,23,42,0.88);

        border:1px solid rgba(255,255,255,0.06);

        padding:1rem;

        border-radius:18px;
    }

    </style>
    """, unsafe_allow_html=True)