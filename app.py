import streamlit as st
import pandas as pd
import plotly.express as px
import time 

# 1. Page Configuration
st.set_page_config(
    page_title="RISKLY | AI Audit & Risk Management",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Global CSS
st.markdown("""
    <style>
    /* IMPORT MODERN FONT (Plus Jakarta Sans) */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* APPLY FONT GLOBALLY */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Dark Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Navbar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0rem;
        border-bottom: 1px solid #333;
        margin-bottom: 3rem;
    }
    .logo {
        font-size: 26px;
        font-weight: 800; /* Extra bold for logo */
        color: #4DB6AC; 
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .nav-links {
        display: flex; gap: 30px; color: #A0A0A0; font-weight: 500; font-size: 14px;
    }

    /* BUTTON STYLING */
    div.stButton > button:first-child {
        background-color: #FF4B4B !important;
        color: white !important;
        border: none !important;
        padding: 15px 40px !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        margin-top: 10px !important; 
    }
    div.stButton > button:hover {
        background-color: #FF1F1F !important;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.5);
    }
    
    /* File Uploader Dark Mode Fix */
    [data-testid="stFileUploader"] {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
    }
    
    /* Metric Cards Styling */
    [data-testid="stMetricValue"] {
        font-size: 26px !important;
        color: white;
        font-weight: 700;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    </style>
    
    <div class="navbar">
        <div class="logo">RISKLY.</div>
        <div class="nav-links">
            <span>PLATFORM</span>
            <span>SOLUTIONS</span>
            <span>RESOURCES</span>
            <span>PRICING</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Hero Section
col1, col2 = st.columns([3, 1]) 

with col1:
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    
    # TITLE: Using 'Plus Jakarta Sans' via Global CSS
    st.markdown("""
    <h1 style='
        font-size: 54px; 
        font-weight: 800; 
        color: white; 
        line-height: 1.2; 
        margin-bottom: 20px;
        white-space: nowrap; 
    '>
    Control & Risk Intelligence
    </h1>
    """, unsafe_allow_html=True)
    
    # SUBTITLE
    st.markdown("""
    <p style='
        font-size: 20px; 
        color: #B0B0B0; 
        margin-bottom: 40px; 
        line-height: 1.5;
        max-width: 800px; 
    '>
    Connect, analyze, and transform audit data into actionable insights with Riskly’s AI risk intelligence platform.
    </p>
    """, unsafe_allow_html=True)
    
    # BUTTON
    st.button("Get Started Now")

with col2:
    st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1632&q=80", use_container_width=True)

# 4. Interactive Dashboard Section
st.markdown("---")
st.markdown("### Interactive Risk Simulator")

dash_col1, dash_col2 = st.columns([1, 2])

with dash_col1:
    st.markdown("#### 1. Upload Financial Data")
    st.caption("Upload your ledger (CSV/XLSX) to trigger AI analysis.")
    
    # File Uploader
    uploaded_file = st.file_uploader("Upload Audit Trail", type=['csv', 'xlsx'])

    if uploaded_file is None:
        st.info("👆 Upload a file to see the risk analysis.")

with dash_col2:
    # LOGIC: Check if file is uploaded
    if uploaded_file is not None:
        # 1. Spinner
        with st.spinner('🤖 AI is scanning for anomalies...'):
            time.sleep(2) 
        
        # 2. Simulated Results
        simulated_data = pd.DataFrame({
            'Risk_Category': ['Fraud', 'Compliance', 'Operational', 'Liquidity', 'Market'],
            'Risk_Score': [92, 45, 20, 35, 88], 
            'Status': ['Critical', 'Stable', 'Safe', 'Stable', 'Critical']
        })
        
        avg_score = 76.4
        critical_flags = 2
        status = "ACTION REQUIRED"
        
        # 3. Display the Metrics
        m1, m2, m3 = st.columns(3)
        m1.metric("Avg Risk Score", f"{avg_score}", delta="+12.5")
        m2.metric("Critical Anomalies", f"{critical_flags}", delta="Immediate Action", delta_color="inverse")
        m3.metric("Audit Status", status, "Flagged")

        # 4. Display the Chart
        st.markdown("#### Real-time Risk Assessment")
        fig = px.bar(
            simulated_data, 
            x='Risk_Category', 
            y='Risk_Score', 
            color='Status', 
            color_discrete_map={'Critical':'#FF4B4B', 'Stable':'#00E676', 'Safe':'#2979FF'}, 
            template="plotly_dark"
        )
        
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#FAFAFA", family="Plus Jakarta Sans"), # Apply font to chart
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        # EMPTY STATE
        m1, m2, m3 = st.columns(3)
        m1.metric("Avg Risk Score", "--", delta=None)
        m2.metric("Critical Anomalies", "--", delta=None)
        m3.metric("Audit Status", "Waiting for Data...", delta=None)
        
        # Placeholder Box
        st.markdown("""
        <div style='
            border: 2px dashed #333; 
            border-radius: 10px; 
            height: 300px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            color: #555;'>
            <i>Chart will appear here after upload</i>
        </div>
        """, unsafe_allow_html=True)