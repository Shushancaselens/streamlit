import streamlit as st
import pandas as pd
from datetime import datetime, date

# Page config
st.set_page_config(
    page_title="MV MESSILA Legal Dashboard",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dashboard-style layout with smaller headers
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e293b 0%, #475569 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #374151;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    /* Make headers smaller */
    h1 { font-size: 24px !important; }
    h2 { font-size: 20px !important; }
    h3 { font-size: 18px !important; }
    h4 { font-size: 16px !important; }
    h5 { font-size: 14px !important; }
    h6 { font-size: 12px !important; }
</style>
""", unsafe_allow_html=True)

# HEADER SECTION - Smaller title
st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h2 style="margin: 0; font-size: 22px;">⚖️ MV MESSILA DEMURRAGE DISPUTE</h2>
            <p style="margin: 0; opacity: 0.9; font-size: 14px;">Transasya v. Noksel Çelik Boru Sanayi A.Ş. | John Schofield | Award: Mar 19, 2023</p>
        </div>
        <div style="text-align: right;">
            <h3 style="margin: 0; color: #10b981; font-size: 20px;">$37,317.71</h3>
            <p style="margin: 0; font-size: 14px;">+ $3K fees • 180 days to payment</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# EXECUTIVE SUMMARY ROW - Always visible
exec_col1, exec_col2, exec_col3, exec_col4, exec_col5 = st.columns(5)

with exec_col1:
    st.metric("💰 Award Amount", "$37,317.71", "Awarded to Transasya")
with exec_col2:
    st.metric("📅 Payment Due", "180 days", "March 19, 2025")
with exec_col3:
    st.metric("🎯 Settlement Prob.", "70%", "Strong drivers")
with exec_col4:
    st.metric("⏱️ Optimal Window", "15-45 days", "Peak recovery")
with exec_col5:
    st.metric("🚀 Next Action", "LMAA Mediation", "Commission now")

st.markdown("---")

# MAIN DASHBOARD TABS
tab1, tab2, tab3, tab4 = st.tabs(["📊 **CASE OVERVIEW**", "🤝 **COMPETING NARRATIVES**", "📈 **STRATEGIC ANALYSIS**", "📋 **DETAILED INTEL**"])

with tab1:
    # CASE OVERVIEW - Three column layout for side-by-side viewing
    overview_left, overview_center, overview_right = st.columns([1, 1, 1])
    
    with overview_left:
        st.markdown("#### 📋 Case Summary")
        st.markdown("""
        **The Dispute:** Turkish steel supplier Noksel chartered MV MESSILA to deliver pipes to Futuna for dock project. After engine breakdown and 4-month repairs, vessel rejected at destination for length non-compliance. Cargo discharged in Fiji triggering $37K+ demurrage.
        
        **Core Issue:** Due diligence failure vs. force majeure
        """)
        
        # Key Parties - Compact format
        st.markdown("**🔵 CLAIMANT:** Transasya (Vessel Owners)")
        st.markdown("**🔴 RESPONDENT:** Noksel (Turkish Supplier)")
        st.markdown("**⚖️ ARBITRATOR:** John Schofield")
        st.markdown("**🚢 VESSEL:** MV MESSILA")
        
    with overview_center:
        st.markdown("#### 📄 Key Documents")
        
        # Critical docs - compact list
        st.markdown("**🔴 CRITICAL**")
        st.error("📄 **Arbitration Award** - John Schofield (Mar 19, 2023)")
        st.info("📄 **Charter Party Agreement** - Nov 12, 2020")
        
        st.markdown("**🟠 KEY EVIDENCE**") 
        st.warning("📄 **Port Rejection Notice** - Nov 10, 2021 (SMOKING GUN)")
        st.info("📄 **Engine Repair Records** - May-Oct 2021")
        
        st.markdown("#### ⚖️ Legal Strength")
        st.success("✅ Contract Performance - **Strong for Claimant**")
        st.success("✅ Vessel Suitability - **Strong for Claimant**") 
        st.success("✅ Due Diligence - **Strong for Claimant**")
        st.warning("⚠️ Force Majeure - **Noksel's best defense**")
        
    with overview_right:
        st.markdown("#### 🕐 Critical Timeline")
        
        # Compact timeline
        timeline_events = [
            ("Feb 4, 2020", "📄 Supply contract signed", "blue"),
            ("Nov 12, 2020", "🚢 MV MESSILA chartered", "blue"), 
            ("May 25, 2021", "⚠️ ENGINE BREAKDOWN", "red"),
            ("Jun-Oct 2021", "🔧 4-MONTH REPAIRS", "red"),
            ("Nov 10, 2021", "❌ REJECTED at Futuna", "red"),
            ("Nov 23, 2021", "💰 DEMURRAGE STARTS", "red"),
            ("Mar 19, 2023", "⚖️ Award issued", "green")
        ]
        
        for date, event, color in timeline_events:
            if color == "red":
                st.error(f"**{date}:** {event}")
            elif color == "green":
                st.success(f"**{date}:** {event}")
            else:
                st.info(f"**{date}:** {event}")

with tab2:
    # COMPETING NARRATIVES - Side by side comparison
    narrative_left, narrative_right = st.columns(2)
    
    with narrative_left:
        st.success("#### 🟢 CLAIMANT'S WINNING STORY")
        st.markdown("**'Noksel's Preventable Due Diligence Failure'**")
        
        st.markdown("""
        **Opening Argument:**
        "Basic professional negligence - Noksel failed to verify elementary vessel specifications."
        
        **Key Facts:**
        • Futuna length limits: publicly available
        • MV MESSILA specs: discoverable pre-charter
        • Industry standard: charterer verifies compliance
        • 11-month voyage wasted due to 5-minute check
        
        **Narrative Arc:**
        "We provided vessel in good faith, attempted delivery despite costly repairs, found alternative port when rejected due to Noksel's oversight."
        
        **Powerful Arguments:**
        • Engine problems irrelevant - rejection inevitable
        • Mitigation efforts show good faith
        • Demurrage natural consequence of charterer failures
        • Professional standard clearly breached
        
        **Closing:**
        "Noksel blames engine problems for their own negligence. Vessel rejected for basic specs they should have verified on day one."
        """)
    
    with narrative_right:
        st.error("#### 🔴 RESPONDENT'S BEST DEFENSE")
        st.markdown("**'Vessel Owner Misrepresentation & Force Majeure'**")
        
        st.markdown("""
        **Opening Argument:**
        "Victims of vessel owner misrepresentation and extraordinary circumstances beyond control."
        
        **Key Facts:**
        • Multiple vessel name changes suggest concealment
        • Contradictory build records (Ukraine vs Netherlands)
        • 4-month repairs despite 'no problems' claim
        • COVID-19 supply chain disruptions unforeseeable
        
        **Narrative Arc:**
        "Relied on vessel owner representations. Hidden problems caused delay. Reached Futuna after obstacles, sudden regulatory enforcement suspiciously timed."
        
        **Powerful Arguments:**
        • Vessel owners concealed seaworthiness issues
        • Name changes show liability avoidance pattern
        • Regulation timing: Nov 9 amendment, Nov 10 rejection
        • Force majeure: Engine failure + COVID
        
        **Closing:**
        "If vessel seaworthy as represented, would have arrived before regulatory changes. This is vessel owner liability, not charterer negligence."
        """)
    
    st.info("**🎯 TRIBUNAL DECISION POINT:** Did Noksel's due diligence failure outweigh force majeure circumstances?")

with tab3:
    # STRATEGIC ANALYSIS - Dashboard style layout
    strategy_left, strategy_center, strategy_right = st.columns(3)
    
    with strategy_left:
        st.markdown("#### 🔍 Causation Analysis")
        st.info("**Proximate Cause Test:** What was the 'but for' cause?")
        st.success("**Claimant:** Length non-compliance → Rejection → Demurrage")
        st.error("**Respondent:** Engine failure → Delay → Late arrival → Rejection")
        st.warning("**Key Issue:** Would vessel be rejected even if on time?")
        
        st.markdown("#### 👨‍🎓 Expert Witnesses")
        st.success("**CLAIMANT NEEDS:**\n• Maritime surveyor\n• Regulatory expert\n• Industry expert")
        st.error("**RESPONDENT NEEDS:**\n• Marine engineer\n• COVID expert\n• Regulatory expert")
        
    with strategy_center:
        st.markdown("#### 📊 Evidence Strength")
        
        strength_col1, strength_col2, strength_col3 = st.columns(3)
        with strength_col1:
            st.success("**STRONG**")
            st.markdown("• Award issued\n• Vessel rejection\n• Name changes\n• Build records")
        with strength_col2:
            st.warning("**MEDIUM**")
            st.markdown("• Engine repairs\n• COVID impact\n• Timing issues\n• Standards")
        with strength_col3:
            st.error("**WEAK**")
            st.markdown("• Owner knowledge\n• Discoverability\n• Force majeure\n• Mitigation")
            
        st.markdown("#### 💼 Settlement vs Litigation")
        st.success("**SETTLEMENT (70% Prob.)**\n• Payment arrangement exists\n• Turkish enforcement uncertain\n• Business relationships\n• Cost concerns")
        st.error("**LITIGATION (Med. Risk)**\n• Strong precedent value\n• Clear liability case\n• High recovery potential")
        
    with strategy_right:
        st.markdown("#### ⏱️ Time-Decay Risk")
        
        # Compact risk visualization
        risk_data = [
            ("Days 0-30", "85%", "Peak window", "success"),
            ("Days 30-90", "70%", "Urgency peaks", "warning"),
            ("Days 90-150", "55%", "Enforcement prep", "error"),
            ("Days 150-180", "40%", "Default triggers", "error")
        ]
        
        for period, prob, desc, status in risk_data:
            if status == "success":
                st.success(f"**{period}:** {prob} - {desc}")
            elif status == "warning":
                st.warning(f"**{period}:** {prob} - {desc}")
            else:
                st.error(f"**{period}:** {prob} - {desc}")
        
        st.info("**🎯 OPTIMAL:** Days 15-45")
        
        st.markdown("#### 💰 Recovery Scenarios")
        st.success("**Best (90%):** $40K+")
        st.warning("**Likely (60%):** $27K+")
        st.error("**Worst (20%):** $9K+")
        st.info("**Expected:** $28K")

with tab4:
    # DETAILED INTEL - For deeper dive
    intel_left, intel_right = st.columns(2)
    
    with intel_left:
        st.markdown("#### 👥 Key Entities")
        
        with st.expander("🏢 KEY PARTIES", expanded=True):
            st.info("**Noksel Çelik Boru Sanayi A.Ş.** (Respondent) - Turkish steel manufacturer arguing force majeure")
            st.success("**Transasya** (Claimant) - Vessel owners seeking $37,317.71 demurrage")
            
        with st.expander("⚖️ LEGAL OFFICIALS"):
            st.info("**John Schofield** (Arbitrator) - Issued final award Mar 19, 2023 favoring Transasya")
            
        with st.expander("🚢 VESSELS & LOCATIONS"):
            st.warning("**MV MESSILA** - Cargo vessel with name change history, engine breakdown, rejected for length")
            st.info("**Futuna Island** - Intended destination with strict length restrictions")
            st.success("**Fiji** - Alternative discharge port where demurrage commenced")
    
    with intel_right:
        st.markdown("#### 📈 Financial Analysis")
        
        # Financial breakdown
        financial_data = {
            "Component": ["Base Demurrage", "Arbitration Fees", "Interest (5%)", "Total Claim"],
            "Amount": ["$37,317.71", "$3,000.00", "Accruing", "$40,317.71+"]
        }
        
        df = pd.DataFrame(financial_data)
        st.dataframe(df, hide_index=True)
        
        st.markdown("#### 🎯 Action Items")
        st.error("**IMMEDIATE (Next 7 days):**\n• Commission LMAA mediation\n• Asset investigation\n• Settlement framework")
        st.warning("**SHORT TERM (7-30 days):**\n• Negotiate terms\n• Document enforcement prep\n• Monitor compliance")
        st.info("**MEDIUM TERM (30-90 days):**\n• Execute settlement\n• Enforcement if needed\n• Case closure")

# BOTTOM EXECUTIVE SUMMARY - Smaller headers
st.markdown("---")
st.markdown("#### 🎯 Executive Decision Matrix")

decision_col1, decision_col2, decision_col3, decision_col4 = st.columns(4)

with decision_col1:
    st.success("**✅ GO/NO-GO**\nSettlement: **GO**\nStrong case, willing counterparty")

with decision_col2:
    st.info("**⏱️ TIMING**\nTarget: **15 days**\nOptimal recovery window")

with decision_col3:
    st.warning("**💰 BUDGET**\nLegal costs: **$15K**\nTarget recovery: **65%**")

with decision_col4:
    st.error("**🚀 NEXT ACTION**\n**Commission LMAA mediation**\nPriority: Immediate")

# Footer
st.caption(f"Legal Dashboard • Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} • Case: MV MESSILA Demurrage Dispute")
