import streamlit as st
import pandas as pd
import numpy as np
from inference.Predict_freight import predict_freight_cost
from inference.Predict_invoice_flag import predict_invoice_flag

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom Styling (ADVANCED UI)
# --------------------------------------------------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    h1, h2, h3 {
        font-weight: 700;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 16px;
        font-weight: 600;
    }

    .metric-card {
        background-color: #111827;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
    }

    .section-card {
        padding: 25px;
        border-radius: 15px;
        background: #0f172a;
        border: 1px solid #1e293b;
        margin-bottom: 20px;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header Section
# --------------------------------------------------
st.markdown("""
# 📦 Vendor Invoice Intelligence Portal
### AI-Powered Freight Prediction & Invoice Risk Intelligence
""")

st.markdown("""
<div class="section-card">
<b> What this system does:</b>
<ul>
<li>📊 Forecast freight costs with ML precision</li>
<li>🛡 Detect abnormal / risky invoices</li>
<li>⚡ Reduce manual approval workload</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Advanced Sidebar UI
# --------------------------------------------------
with st.sidebar:

    # Logo / Title Section
    st.markdown("""
    <div style="text-align:center; padding-bottom: 10px;">
        <h2 style="margin-bottom:0;">📦 VENDOR AI</h2>
        <p style="font-size:13px; color:gray;">Intelligence Portal</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Navigation Section
    st.markdown("### 🧭 Navigation")

    selected_model = st.radio(
        "",
        [
            "🚚 Freight Cost Prediction",
            "🚩 Invoice Risk Flagging"
        ]
    )

    st.markdown("---")

    # Model Info Card (Dynamic)
    if selected_model == "🚚 Freight Cost Prediction":
        st.markdown("""
        <div style="
            background: #0f172a;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #1e293b;
        ">
        <b>🚚 Freight Model</b><br><br>
        Predicts logistics cost using:
        <ul>
        <li>Quantity</li>
        <li>Invoice Value</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="
            background: #0f172a;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #1e293b;
        ">
        <b>🚩 Risk Detection Model</b><br><br>
        Flags invoices based on:
        <ul>
        <li>Cost anomalies</li>
        <li>Freight irregularities</li>
        <li>Quantity mismatch</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Business Impact Section
    st.markdown("### 📈 Impact")

    st.markdown("""
    <div style="font-size:14px;">
    📊 Better forecasting<br>
    🛡 Fraud detection<br>
    ⚡ Faster approvals<br>
    💰 Cost optimization
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Footer
    st.markdown("""
    <div style="text-align:center; font-size:12px; color:gray;">
    Built with ❤️ using ML
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Freight Cost Prediction UI
# --------------------------------------------------
if selected_model == "🚚 Freight Cost Prediction":

    st.markdown("## 🚚 Freight Cost Prediction")

    st.markdown("""
    <div class="section-card">
    Predict freight cost using invoice quantity and value.
    Helps in budgeting and vendor negotiation.
    </div>
    """, unsafe_allow_html=True)

    with st.form("freight_form"):
        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "📦 Quantity",
                min_value=1,
                value=1200
            )

        with col2:
            dollars = st.number_input(
                "💰 Invoice Dollars",
                min_value=1.0,
                value=18500.0
            )

        submit_freight = st.form_submit_button("🔮 Predict Freight Cost")

    if submit_freight:
        input_data = {
            "Quantity": [quantity],
            "Dollars": [dollars]
        }

        prediction = predict_freight_cost(input_data)['Predicted_Freight']

        st.success("Prediction completed successfully!")

        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="📊 Estimated Freight Cost",
            value=f"${prediction[0]:,.2f}"
        )
        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# Invoice Flag Prediction UI
# --------------------------------------------------
else:
    st.markdown("## 🚩 Invoice Risk Flagging")

    st.markdown("""
    <div class="section-card">
    Identify invoices that require manual approval based on cost,
    freight anomalies, and unusual patterns.
    </div>
    """, unsafe_allow_html=True)

    with st.form("invoice_flag_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            invoice_quantity = st.number_input(
                "📦 Invoice Quantity",
                min_value=1,
                value=50
            )
            freight = st.number_input(
                "🚚 Freight Cost",
                min_value=0.0,
                value=1.73
            )

        with col2:
            invoice_dollars = st.number_input(
                "💰 Invoice Dollars",
                min_value=1.0,
                value=352.95
            )
            total_item_quantity = st.number_input(
                "📊 Total Item Quantity",
                min_value=1,
                value=162
            )

        with col3:
            total_item_dollars = st.number_input(
                "💵 Total Item Dollars",
                min_value=1.0,
                value=2476.0
            )

        submit_flag = st.form_submit_button("🧠 Evaluate Invoice Risk")

    if submit_flag:
        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        flag_prediction = predict_invoice_flag(input_data)['Predicted_risk_flag']
        is_flagged = bool(flag_prediction[0])

        if is_flagged:
            st.error("🚨 Invoice requires **MANUAL APPROVAL**")
        else:
            st.success("✅ Invoice is SAFE for Auto-Approval")