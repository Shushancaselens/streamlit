import streamlit as st
import pandas as pd
from datetime import datetime
import datetime as dt

# Page configuration
st.set_page_config(
    page_title="MV MESSILA Dispute Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for compact styling
st.markdown("""
<style>
    .metric-container {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .timeline-item {
        padding: 8px;
        margin: 4px 0;
        border-left: 3px solid #ff6b6b;
        background-color: #fff5f5;
        border-radius: 0 5px 5px 0;
    }
    .timeline-item.critical {
        border-left-color: #ff6b6b;
        background-color: #fff5f5;
    }
    .timeline-item.normal {
        border-left-color: #4ecdc4;
        background-color: #f0fdfc;
    }
    .narrative-box {
        border: 2px solid;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    .claimant-box {
        border-color: #10b981;
        background-color: #f0fdf4;
    }
    .respondent-box {
        border-color: #ef4444;
        background-color: #fef2f2;
    }
    .evidence-strong { background-color: #dcfce7; padding: 8px; border-radius: 4px; margin: 2px 0; }
    .evidence-medium { background-color: #fef3c7; padding: 8px; border-radius: 4px; margin: 2px 0; }
    .evidence-weak { background-color: #fee2e2; padding: 8px; border-radius: 4px; margin: 2px 0; }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("### ⚖️ MV MESSILA DEMURRAGE DISPUTE - LEGAL BRIEF")
st.markdown("**Transasya v. Noksel Çelik Boru Sanayi A.Ş.** | Arbitrator: John Schofield | Award: Mar 19, 2023 | Due: Mar 19, 2025")

# Top metrics row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Award Amount", "$37,317.71", "+$3K fees")
with col2:
    st.metric("Interest Rate", "5% annually", "Compounding")
with col3:
    st.metric("Days to Payment", "180", "From award date")
with col4:
    st.metric("Expected Recovery", "$28K", "65% target")

st.divider()

# Main content in columns
left_col, center_col, right_col = st.columns([2, 3, 2])

# LEFT COLUMN - Case Overview & Timeline
with left_col:
    # Case Summary
    with st.container():
        st.markdown("#### 📋 CASE SUMMARY")
        st.info("""
        Turkish steel supplier Noksel chartered MV MESSILA to deliver pipes to remote French Pacific island (Futuna) for dock project. 
        After engine breakdown, 4-month repairs, and regulatory rejection at destination, cargo discharged in Fiji triggering $37K+ demurrage.
        """)
        
        # Key facts in expandable section
        with st.expander("📊 Key Case Facts"):
            facts_df = pd.DataFrame({
                'Aspect': ['Claimant', 'Respondent', 'Core Issue', 'Award Status'],
                'Details': ['Transasya (Vessel Owners)', 'Noksel (Turkish Supplier)', 
                           'Who pays for vessel failure?', 'Issued, payment arranged']
            })
            st.dataframe(facts_df, hide_index=True, use_container_width=True)
    
    # Critical Timeline
    st.markdown("#### ⏰ CRITICAL TIMELINE")
    timeline_data = [
        ("Feb 4, 2020", "Supply contract signed", "normal", "📄"),
        ("Nov 12, 2020", "MV MESSILA chartered", "normal", "🚢"),
        ("Dec 1-3, 2020", "Cargo loaded Turkey", "normal", "📦"),
        ("May 25, 2021", "ENGINE BREAKDOWN", "critical", "⚠️"),
        ("Jun-Oct 2021", "4-MONTH REPAIRS", "critical", "🔧"),
        ("Nov 10, 2021", "REJECTED at Futuna", "critical", "❌"),
        ("Nov 23, 2021", "DEMURRAGE STARTS", "critical", "💰"),
        ("Mar 19, 2023", "Arbitration award", "normal", "⚖️")
    ]
    
    for date, event, impact, icon in timeline_data:
        if impact == "critical":
            st.markdown(f'<div class="timeline-item critical">{icon} <strong>{date}:</strong> {event}</div>', 
                       unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="timeline-item normal">{icon} <strong>{date}:</strong> {event}</div>', 
                       unsafe_allow_html=True)
    
    # Legal Issues
    st.markdown("#### ⚖️ KEY LEGAL ISSUES")
    legal_issues = [
        ("Contract Performance", "Did Noksel breach by failing to deliver to Futuna?", "Strong for Claimant"),
        ("Vessel Suitability", "Was vessel unsuitable for intended voyage?", "Strong for Claimant"),
        ("Due Diligence", "Should length requirements have been verified?", "Strong for Claimant"),
        ("Force Majeure", "Do engine/COVID problems excuse performance?", "Noksel's best defense")
    ]
    
    for issue, desc, strength in legal_issues:
        with st.expander(f"📌 {issue}"):
            st.write(f"**Question:** {desc}")
            if "Claimant" in strength:
                st.success(f"**Assessment:** {strength}")
            else:
                st.warning(f"**Assessment:** {strength}")

# CENTER COLUMN - Competing Narratives
with center_col:
    st.markdown("#### 👥 STRONGEST COMPETING NARRATIVES")
    
    # Create two columns for competing stories
    story_col1, story_col2 = st.columns(2)
    
    with story_col1:
        st.markdown('<div class="narrative-box claimant-box">', unsafe_allow_html=True)
        st.markdown("**🏆 CLAIMANT'S WINNING STORY**")
        st.markdown("*'Noksel's Preventable Due Diligence Failure'*")
        
        st.markdown("**Opening:**")
        st.write("This case is about basic professional negligence - Noksel failed to verify elementary vessel specifications before chartering.")
        
        st.markdown("**Key Supporting Facts:**")
        st.write("• Futuna length limits: publicly available in maritime regulations")
        st.write("• MV MESSILA specs: known and discoverable pre-charter")
        st.write("• Industry standard: charterer verifies destination compliance")
        st.write("• 11-month voyage wasted due to 5-minute regulation check")
        
        st.markdown("**Narrative Arc:**")
        st.write("We provided a vessel in good faith. Despite extraordinary 4-month engine repairs costing us significantly, we still attempted delivery. When rejected due to Noksel's oversight, we immediately found alternative port to mitigate damages.")
        
        st.markdown("**Powerful Arguments:**")
        st.write("• Engine problems irrelevant - vessel would have been rejected anyway")
        st.write("• Our mitigation efforts (Fiji discharge) show good faith")
        st.write("• Demurrage is natural consequence of charterer's failures")
        st.write("• Professional standard breached - any competent charterer would have checked")
        
        st.markdown("**Closing:**")
        st.write("Noksel wants to blame engine problems for their own professional negligence. The vessel was rejected for basic specifications they should have verified on day one.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with story_col2:
        st.markdown('<div class="narrative-box respondent-box">', unsafe_allow_html=True)
        st.markdown("**🛡️ RESPONDENT'S BEST DEFENSE**")
        st.markdown("*'Vessel Owner Misrepresentation & Force Majeure'*")
        
        st.markdown("**Opening:**")
        st.write("We were victims of vessel owner misrepresentation and extraordinary circumstances beyond any party's control.")
        
        st.markdown("**Key Supporting Facts:**")
        st.write("• Vessel history: Multiple name changes suggest concealment")
        st.write("• Build records: Contradictory construction data (Ukraine vs Netherlands)")
        st.write("• Engine condition: Award claims 'no problems' but 4-month repairs needed")
        st.write("• COVID-19: 2021 spare parts delivery restrictions were unforeseeable")
        
        st.markdown("**Narrative Arc:**")
        st.write("We relied on vessel owner representations about seaworthiness. The vessel's hidden problems caused the real delay. When we finally reached Futuna after overcoming these obstacles, sudden regulatory enforcement seemed suspiciously timed.")
        
        st.markdown("**Powerful Arguments:**")
        st.write("• Vessel owners knew of seaworthiness issues but concealed them")
        st.write("• Multiple vessel identity changes show pattern of liability avoidance")
        st.write("• Futuna regulation timing: Nov 9 amendment day before rejection")
        st.write("• Force majeure: Engine failure + COVID = unforeseeable events")
        
        st.markdown("**Closing:**")
        st.write("If the vessel had been seaworthy as represented, we would have reached Futuna months earlier, before any regulatory changes. This is vessel owner liability, not charterer negligence.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.info("**Tribunal Decision Point:** Did Noksel's due diligence failure outweigh force majeure circumstances?")
    
    # Causation Analysis
    st.markdown("#### 🔗 CAUSATION CHAIN ANALYSIS")
    st.markdown("**Proximate Cause Test:** What was the 'but for' cause of demurrage?")
    
    cause_col1, cause_col2 = st.columns(2)
    with cause_col1:
        st.success("**Claimant's Theory**\n\nLength non-compliance → Rejection → Demurrage\n\n*(Engine problems irrelevant)*")
    with cause_col2:
        st.error("**Respondent's Theory**\n\nEngine failure → Delay → Late arrival → Rejection\n\n*(Timing was everything)*")
    
    st.warning("**Key Issue:** Would vessel have been rejected even if arrived on time?")

# RIGHT COLUMN - Strategic Analysis
with right_col:
    # Evidence Strength Analysis
    st.markdown("#### 📊 EVIDENCE STRENGTH ANALYSIS")
    
    evidence_tabs = st.tabs(["Strong", "Medium", "Weak"])
    
    with evidence_tabs[0]:
        st.markdown('<div class="evidence-strong">• Arbitration award issued</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-strong">• Vessel rejection documented</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-strong">• Multiple vessel name changes</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-strong">• Contradictory build records</div>', unsafe_allow_html=True)
    
    with evidence_tabs[1]:
        st.markdown('<div class="evidence-medium">• Engine repair duration</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-medium">• COVID supply disruptions</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-medium">• Regulatory timing issues</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-medium">• Industry practice standards</div>', unsafe_allow_html=True)
    
    with evidence_tabs[2]:
        st.markdown('<div class="evidence-weak">• Vessel owner knowledge</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-weak">• Regulation discoverability</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-weak">• Force majeure scope</div>', unsafe_allow_html=True)
        st.markdown('<div class="evidence-weak">• Mitigation efforts adequacy</div>', unsafe_allow_html=True)
    
    # Time-Decay Risk Analysis
    st.markdown("#### ⏱️ TIME-DECAY RISK ANALYSIS")
    risk_data = pd.DataFrame({
        'Period': ['Days 0-30 (Peak)', 'Days 30-90', 'Days 90-150', 'Days 150-180'],
        'Recovery %': [85, 70, 55, 40],
        'Status': ['Payment deadline pressure', 'Settlement urgency peaks', 
                  'Enforcement preparation', 'Default triggers']
    })
    st.dataframe(risk_data, hide_index=True, use_container_width=True)
    st.success("**Optimal Window:** Days 15-45")
    
    # Recovery Scenarios
    st.markdown("#### 💰 RECOVERY SCENARIOS")
    scenario_data = pd.DataFrame({
        'Scenario': ['Best (90%)', 'Likely (60%)', 'Worst (20%)'],
        'Amount': ['$40K+', '$27K+', '$9K+'],
        'Probability': [0.1, 0.7, 0.2]
    })
    st.dataframe(scenario_data, hide_index=True, use_container_width=True)
    st.info("**Expected Recovery:** $28K")
    
    # Settlement vs Litigation
    st.markdown("#### ⚖️ SETTLEMENT vs LITIGATION")
    
    settlement_tab, litigation_tab = st.tabs(["Settlement", "Litigation"])
    
    with settlement_tab:
        st.success("**Settlement Drivers (70% probability)**")
        st.write("• Payment arrangement already in place")
        st.write("• Turkish enforcement uncertainty") 
        st.write("• Ongoing business relationships")
        st.write("• Cost of extended litigation")
    
    with litigation_tab:
        st.warning("**Litigation Drivers (Medium risk)**")
        st.write("• Strong precedent value")
        st.write("• Clear liability case")
        st.write("• Vessel credibility issues")
        st.write("• Recovery potential high")

# Bottom section - Executive Dashboard
st.divider()
st.markdown("#### 🎯 EXECUTIVE DASHBOARD")

dashboard_col1, dashboard_col2, dashboard_col3, dashboard_col4 = st.columns(4)

with dashboard_col1:
    st.success("**GO/NO-GO**\n\nSettlement: **GO**")

with dashboard_col2:
    st.info("**TIMING**\n\nWithin **15 days**")

with dashboard_col3:
    st.warning("**BUDGET**\n\n**$15K** costs")

with dashboard_col4:
    st.error("**TARGET**\n\n**65%** recovery")

st.success("**🎯 NEXT ACTION:** Commission LMAA mediation")

# Sidebar for additional controls
with st.sidebar:
    st.markdown("### 📋 Case Controls")
    
    # Date inputs
    award_date = st.date_input("Award Date", value=dt.date(2023, 3, 19))
    payment_due = st.date_input("Payment Due", value=dt.date(2025, 3, 19))
    
    # Calculation inputs
    award_amount = st.number_input("Award Amount ($)", value=37317.71, format="%.2f")
    interest_rate = st.slider("Interest Rate (%)", 0.0, 10.0, 5.0, 0.1)
    
    # Strategy settings
    st.markdown("### 🎯 Strategy Settings")
    settlement_target = st.slider("Settlement Target (%)", 50, 100, 65, 5)
    timeline_urgency = st.selectbox("Timeline Urgency", ["Low", "Medium", "High"], index=2)
    
    # Export options
    st.markdown("### 📥 Export Options")
    if st.button("Generate PDF Report"):
        st.success("PDF export functionality would be implemented here")
    
    if st.button("Export to Excel"):
        st.success("Excel export functionality would be implemented here")

# Footer
st.markdown("---")
st.caption("MV MESSILA Dispute Analysis Dashboard | Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
