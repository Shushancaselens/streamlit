import streamlit as st
import pandas as pd
from datetime import datetime, date

# Page config
st.set_page_config(
    page_title="MV MESSILA Demurrage Dispute",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .metric-container {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
    }
    .stMetric > label {
        font-size: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("⚖️ MV MESSILA DEMURRAGE DISPUTE")
st.markdown("**Transasya v. Noksel Çelik Boru Sanayi A.Ş.** | Arbitrator: John Schofield | Award: Mar 19, 2023 | Due: Mar 19, 2025")

# Key metrics row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("💰 Award Amount", "$37,317.71", "+$3K fees")
with col2:
    st.metric("📅 Days to Payment", "180", "Until Mar 19, 2025")
with col3:
    st.metric("📈 Interest Rate", "5%", "Annual")
with col4:
    st.metric("⚖️ Case Status", "Awarded", "Payment arranged")

st.divider()

# Main layout
left_col, center_col, right_col = st.columns([2, 3, 2])

# LEFT COLUMN
with left_col:
    # Case Summary
    with st.container():
        st.subheader("📋 CASE SUMMARY")
        st.markdown("""
        Turkish steel supplier Noksel chartered MV MESSILA to deliver pipes to remote French Pacific island (Futuna) for dock project. After engine breakdown, 4-month repairs, and regulatory rejection at destination, cargo discharged in Fiji triggering $37K+ demurrage.
        """)
        
        st.info("**Claimant:** Transasya (Vessel Owners)")
        st.error("**Respondent:** Noksel (Turkish Supplier)")  
        st.warning("**Core Issue:** Who pays for vessel failure?")
        st.success("**Award Status:** Issued, payment arranged")

    # Key Documents
    with st.expander("📄 KEY DOCUMENTS", expanded=True):
        st.markdown("##### 🔴 CRITICAL - MUST READ")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Arbitration Award - John Schofield**")
            st.caption("Mar 19, 2023 • 23 pages • $37,317.71 awarded to Transasya")
        with col2:
            st.error("FINAL AWARD")
            
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Charter Party Agreement**")
            st.caption("Nov 12, 2020 • Transasya/Noksel agreement")
        with col2:
            st.info("CONTRACT")
        
        st.markdown("##### 🟠 KEY EVIDENCE")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Futuna Port Rejection Notice**")
            st.caption("Nov 10, 2021 • Official rejection letter")
        with col2:
            st.error("SMOKING GUN")
            
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Engine Repair Records**")
            st.caption("May-Oct 2021 • 4-month repair period")
        with col2:
            st.warning("TECHNICAL")

    # Critical Timeline
    with st.expander("🕐 CRITICAL TIMELINE", expanded=True):
        timeline_data = [
            {"Date": "Feb 4, 2020", "Event": "Noksel Çelik Boru Sanayi A.Ş. signs supply contract for Futuna dock project", "Type": "Contract"},
            {"Date": "Nov 12, 2020", "Event": "Transasya charters MV MESSILA for steel pipe transportation", "Type": "Charter"},
            {"Date": "Dec 1-3, 2020", "Event": "Noksel cargo loaded onto MV MESSILA at Turkish ports", "Type": "Loading"},
            {"Date": "May 25, 2021", "Event": "MV MESSILA ENGINE BREAKDOWN at sea", "Type": "Critical"},
            {"Date": "Jun-Oct 2021", "Event": "MV MESSILA undergoes 4-MONTH REPAIRS", "Type": "Critical"},
            {"Date": "Nov 10, 2021", "Event": "Futuna Port Authority REJECTS MV MESSILA entry due to length restrictions", "Type": "Critical"},
            {"Date": "Nov 23, 2021", "Event": "MV MESSILA diverts to Fiji - DEMURRAGE STARTS", "Type": "Critical"},
            {"Date": "Mar 19, 2023", "Event": "John Schofield issues award favoring Transasya under LMAA arbitration", "Type": "Award"}
        ]
        
        for item in timeline_data:
            if item["Type"] == "Critical":
                st.error(f"**{item['Date']}:** {item['Event']}")
            elif item["Type"] == "Award":
                st.success(f"**{item['Date']}:** {item['Event']}")
            else:
                st.info(f"**{item['Date']}:** {item['Event']}")

    # Key Entities
    with st.expander("👥 KEY ENTITIES", expanded=False):
        st.markdown("**KEY PARTIES**")
        st.info("**Noksel Çelik Boru Sanayi A.Ş.** (Respondent/Charterer) - Turkish steel manufacturer. Chartered vessel for Futuna delivery. Arguing force majeure defense.")
        st.success("**Transasya** (Claimant/Vessel Owner) - Vessel owners seeking $37,317.71 demurrage. Arguing due diligence failure.")
        
        st.markdown("**LEGAL OFFICIALS**")
        st.info("**John Schofield** (Arbitrator) - Maritime arbitrator. Issued final award Mar 19, 2023 favoring Transasya.")
        
        st.markdown("**VESSELS**")
        st.warning("**MV MESSILA** (Cargo Vessel) - Cargo vessel with history of name changes. Engine breakdown led to 4-month repairs. Rejected at Futuna for length compliance.")
        
        st.markdown("**KEY LOCATIONS**")
        st.info("**Futuna Island** (Intended Destination) - French Pacific territory. Strict vessel length restrictions led to rejection.")
        st.success("**Fiji** (Alternative Port) - Where cargo was ultimately discharged. Demurrage costs commenced here.")

    # Legal Issues
    with st.expander("⚖️ KEY LEGAL ISSUES", expanded=False):
        legal_issues = [
            {"Issue": "Contract Performance", "Description": "Did Noksel breach by failing to deliver to Futuna?", "Strength": "Strong for Claimant"},
            {"Issue": "Vessel Suitability", "Description": "Was vessel unsuitable for intended voyage?", "Strength": "Strong for Claimant"},
            {"Issue": "Due Diligence", "Description": "Should length requirements have been verified?", "Strength": "Strong for Claimant"},
            {"Issue": "Force Majeure", "Description": "Do engine/COVID problems excuse performance?", "Strength": "Noksel's best defense"}
        ]
        
        for issue in legal_issues:
            if "Claimant" in issue["Strength"]:
                st.success(f"**{issue['Issue']}:** {issue['Description']} - *{issue['Strength']}*")
            else:
                st.warning(f"**{issue['Issue']}:** {issue['Description']} - *{issue['Strength']}*")

# CENTER COLUMN
with center_col:
    st.subheader("🤝 STRONGEST COMPETING NARRATIVES")
    
    tab1, tab2 = st.tabs(["🟢 CLAIMANT'S STORY", "🔴 RESPONDENT'S DEFENSE"])
    
    with tab1:
        st.success("### CLAIMANT'S WINNING STORY")
        st.markdown("**'Noksel's Preventable Due Diligence Failure'**")
        
        st.markdown("**Opening:** This case is about basic professional negligence - Noksel failed to verify elementary vessel specifications before chartering.")
        
        with st.expander("Key Facts Supporting Story"):
            st.markdown("""
            • Futuna length limits: publicly available in maritime regulations
            • MV MESSILA specs: known and discoverable pre-charter  
            • Industry stand
