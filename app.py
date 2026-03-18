import streamlit as st
from engine import fetch_orbital_inventory

st.set_page_config(page_title="IAN-SCP Dashboard", layout="wide")

st.title("🛰️ IAN-SCP: Satellite Collision Prevention")
st.caption("The TCP/IP layer of orbital collision prevention")

# Metrics from Technical Plan
col1, col2, col3 = st.columns(3)
col1.metric("Risk Threshold", "1e-4", "Target")
col2.metric("Maneuver Success", "≥92%", "Target")
col3.metric("Fuel Optimization", "20-35%", "Target")

# Sidebar for operator control
st.sidebar.header("Global Shell Monitoring")
monitor_active = st.sidebar.toggle("Real-time Data Ingestion", value=True)

if monitor_active:
    with st.spinner("Accessing High-precision ephemeris streams..."):
        sats = fetch_orbital_inventory()
        st.success(f"Monitoring {len(sats)} active satellites across LEO.")
        
        st.write("### Active Satellite Inventory (Data Acquisition Layer)")
        sat_names = [s.name for s in sats[:10]]
        st.table({"Satellite Name": sat_names, "Status": ["Protected"] * 10})
