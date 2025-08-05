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

# Simple case title
st.title("MV MESSILA Demurrage Dispute")

# MAIN DASHBOARD TABS
tab1, tab2, tab3, tab4 = st.tabs(["📊 **CASE OVERVIEW**", "🤝 **COMPETING NARRATIVES**", "🎯 **CASE STRATEGY**", "📋 **DETAILED INTEL**"])

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

    # ✅ EXECUTIVE DECISION MATRIX - Include on Case Overview tab
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

with tab2:
    # 🎯 CORE QUESTION - NOW AT THE TOP for better context
    st.info("#### 🎯 TRIBUNAL DECISION POINT: Did Noksel's due diligence failure outweigh force majeure circumstances?")
    st.markdown("---")
    
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

with tab3:
    # REDESIGNED CASE STRATEGY - More practical and actionable
    st.markdown("#### 🎯 IMMEDIATE STRATEGIC DECISIONS")
    
    # Top priority decisions first
    priority_col1, priority_col2 = st.columns(2)
    
    with priority_col1:
        st.error("#### ⚡ URGENT - NEXT 7 DAYS")
        st.markdown("""
        **🥇 Priority 1: Commission LMAA Mediation**
        • Contact: LMAA appointment team
        • Timeline: Initiate within 48 hours
        • Cost: ~$5,000 setup
        • Success rate: 65% for maritime disputes
        
        **🥈 Priority 2: Asset Intelligence**
        • Noksel corporate structure investigation  
        • Turkish bank account identification
        • Asset protection risk assessment
        • Cost: $3,000 investigation budget
        
        **🥉 Priority 3: Settlement Framework**
        • Target: 65% recovery ($25K)
        • Minimum: 50% recovery ($19K)
        • Payment terms: 30-60 days max
        • Security: Turkish parent guarantee
        """)
        
    with priority_col2:
        st.warning("#### 📅 SHORT TERM - NEXT 30 DAYS")
        st.markdown("""
        **💼 Settlement Negotiation Strategy:**
        • Open at 85% ($32K) - expect counter at 40%
        • Leverage: Award in hand, Turkish enforcement risk
        • Concessions: Extended payment terms only
        • Walk-away: Below 50% recovery
        
        **📊 Evidence Preparation (if settlement fails):**
        • Maritime surveyor report on vessel condition
        • Regulatory expert on Futuna port requirements  
        • Industry expert on due diligence standards
        • Budget: $15K expert witness costs
        
        **⚖️ Enforcement Prep (backup plan):**
        • Turkish counsel identification
        • Enforcement cost analysis: $20-30K
        • Asset seizure options
        • Timeline: 6-12 months
        """)

    st.markdown("---")
    
    # Key strategic insights
    strategy_insights_col1, strategy_insights_col2, strategy_insights_col3 = st.columns(3)
    
    with strategy_insights_col1:
        st.markdown("#### 🔍 CASE STRENGTH ANALYSIS")
        
        # Visual case strength meter
        st.success("**OVERALL STRENGTH: STRONG (80%)**")
        
        st.markdown("**✅ WINNING ARGUMENTS:**")
        st.success("• Award already issued (100% strength)")
        st.success("• Due diligence failure clear (85% strength)")  
        st.success("• Industry standard breached (80% strength)")
        
        st.markdown("**⚠️ VULNERABILITIES:**")
        st.warning("• Force majeure claims (moderate risk)")
        st.warning("• COVID timing issues (low-medium risk)")
        
        st.markdown("**🎯 TRIBUNAL DECISION LOGIC:**")
        st.info("Arbitrator found due diligence failure outweighed force majeure - this is our strongest precedent foundation.")
        
    with strategy_insights_col2:
        st.markdown("#### 💰 FINANCIAL STRATEGY")
        
        # Financial decision matrix
        financial_scenarios = {
            "Scenario": ["Best Case", "Target", "Minimum", "Worst Case"],
            "Recovery": ["$40K (100%)", "$27K (65%)", "$19K (50%)", "$9K (25%)"],
            "Probability": ["15%", "45%", "30%", "10%"],
            "Strategy": ["Quick settle", "Negotiate", "Last offer", "Enforce"]
        }
        
        df_financial = pd.DataFrame(financial_scenarios)
        st.dataframe(df_financial, hide_index=True)
        
        st.success("**RECOMMENDED TARGET: $27K (65%)**")
        st.markdown("• Balances recovery vs. time/cost")
        st.markdown("• Realistic given Turkish enforcement challenges")
        st.markdown("• Preserves business relationship")
        
        st.error("**WALK-AWAY POINT: $19K (50%)**")
        st.markdown("• Below this, enforcement becomes better option")
        st.markdown("• Factor in $15K legal costs + time")
        
    with strategy_insights_col3:
        st.markdown("#### ⏰ TIME-CRITICAL WINDOWS")
        
        # Urgency timeline
        st.error("**🚨 PEAK WINDOW: Days 0-15**")
        st.markdown("• Noksel payment pressure highest")
        st.markdown("• Asset protection risk lowest") 
        st.markdown("• Recovery probability: 85%")
        
        st.warning("**⚠️ DECLINING WINDOW: Days 15-45**")
        st.markdown("• Settlement urgency peaks")
        st.markdown("• Enforcement prep needed")
        st.markdown("• Recovery probability: 70%")
        
        st.info("**📉 ENFORCEMENT ZONE: Days 45+**")
        st.markdown("• Settlement probability drops")
        st.markdown("• Asset hiding risk increases")
        st.markdown("• Recovery probability: 55%")
        
        st.success("**🎯 ACTION: SETTLE WITHIN 15 DAYS**")

    st.markdown("---")
    
    # Tactical playbook
    st.markdown("#### 📋 TACTICAL PLAYBOOK")
    
    tactical_col1, tactical_col2 = st.columns(2)
    
    with tactical_col1:
        st.markdown("**🎲 NEGOTIATION TACTICS**")
        
        st.success("**LEVERAGE POINTS:**")
        st.markdown("""
        • **Award in hand** - "We have binding arbitration decision"
        • **Turkish enforcement risk** - "Costly for you if we proceed" 
        • **Business relationship** - "Let's resolve this professionally"
        • **Time pressure** - "Settlement window closing rapidly"
        """)
        
        st.error("**POTENTIAL COUNTERS:**")
        st.markdown("""
        • **COVID force majeure** → Response: "Arbitrator already ruled"
        • **Engine problems** → Response: "Vessel rejected for length anyway"
        • **Regulatory timing** → Response: "Due diligence still required"
        • **Financial hardship** → Response: "Payment plan available"
        """)
        
    with tactical_col2:
        st.markdown("**⚖️ LITIGATION FALLBACK**")
        
        st.warning("**IF SETTLEMENT FAILS:**")
        st.markdown("""
        **Phase 1: Turkish Enforcement (6 months)**
        • Local counsel: Mehmet & Associates
        • Cost: $20-30K + court fees
        • Success rate: 60-70% in Turkish courts
        • Asset seizure: Bank accounts, receivables
        
        **Phase 2: International Enforcement**  
        • New York Convention (arbitration awards)
        • UK/EU enforcement if assets located
        • Cost: Additional $15-25K per jurisdiction
        
        **Risk Assessment:**
        • Total enforcement cost: $35-55K
        • Timeline: 12-18 months  
        • Recovery after costs: $15-25K net
        • **Conclusion: Settlement clearly preferred**
        """)

    # ✅ EXECUTIVE DECISION MATRIX - Include on Strategic Analysis tab
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

# Footer
st.caption(f"Legal Dashboard • Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} • Case: MV MESSILA Demurrage Dispute")
