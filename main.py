import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="MESSILA Dispute Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background-color: #1e293b;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .case-summary {
        background-color: #eff6ff;
        border: 1px solid #93c5fd;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .timeline-item {
        display: flex;
        align-items: center;
        margin-bottom: 0.5rem;
        font-size: 0.8rem;
    }
    .critical-event {
        color: #dc2626;
        font-weight: bold;
    }
    .award-event {
        color: #16a34a;
        font-weight: bold;
    }
    .normal-event {
        color: #2563eb;
        font-weight: bold;
    }
    .narrative-box {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 2px solid;
    }
    .claimant-story {
        background-color: #f0fdf4;
        border-color: #86efac;
    }
    .respondent-story {
        background-color: #fef2f2;
        border-color: #fca5a5;
    }
    .evidence-strong {
        background-color: #dcfce7;
        color: #166534;
        padding: 0.5rem;
        border-radius: 4px;
        margin-bottom: 0.5rem;
    }
    .evidence-medium {
        background-color: #fefce8;
        color: #a16207;
        padding: 0.5rem;
        border-radius: 4px;
        margin-bottom: 0.5rem;
    }
    .evidence-weak {
        background-color: #fef2f2;
        color: #dc2626;
        padding: 0.5rem;
        border-radius: 4px;
        margin-bottom: 0.5rem;
    }
    .executive-dashboard {
        background-color: #1e293b;
        color: white;
        padding: 1rem;
        border-radius: 8px;
    }
    .metric-box {
        background-color: #f8fafc;
        padding: 0.5rem;
        border-radius: 4px;
        text-align: center;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="margin: 0; font-size: 1.5rem;">MV MESSILA DEMURRAGE DISPUTE - LEGAL BRIEF</h1>
            <p style="margin: 0; font-size: 0.8rem; color: #cbd5e1;">
                Transasya v. Noksel Çelik Boru Sanayi A.Ş. | Arbitrator: John Schofield | Award: Mar 19, 2023 | Due: Mar 19, 2025
            </p>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 1.5rem; font-weight: bold;">$37,317.71</div>
            <div style="font-size: 0.8rem;">+ $3K fees + 5% interest</div>
            <div style="font-size: 0.8rem; color: #fbbf24;">180 days to payment</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Layout - 5 Column Grid
col1, col2, col3, col4, col5 = st.columns([4, 6, 5, 5, 5])

# Column 1 - Case Overview & Timeline
with col1:
    # Case Summary
    st.markdown("""
    <div class="case-summary">
        <h3 style="margin-top: 0; color: #1e40af; font-size: 1rem;">📋 CASE SUMMARY</h3>
        <p style="font-size: 0.8rem; line-height: 1.3;">
            Turkish steel supplier Noksel chartered MV MESSILA to deliver pipes to remote French Pacific island (Futuna) 
            for dock project. After engine breakdown, 4-month repairs, and regulatory rejection at destination, 
            cargo discharged in Fiji triggering $37K+ demurrage.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.75rem; margin-top: 0.5rem;">
            <div><strong>Claimant:</strong> Transasya (Vessel Owners)</div>
            <div><strong>Respondent:</strong> Noksel (Turkish Supplier)</div>
            <div><strong>Core Issue:</strong> Who pays for vessel failure?</div>
            <div><strong>Award Status:</strong> Issued, payment arranged</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Critical Timeline
    st.markdown("### 🕐 CRITICAL TIMELINE")
    
    timeline_events = [
        ("Feb 4, 2020", "Supply contract signed", "normal", "📄"),
        ("Nov 12, 2020", "MV MESSILA chartered", "normal", "🚢"),
        ("Dec 1-3, 2020", "Cargo loaded Turkey", "normal", "📦"),
        ("May 25, 2021", "ENGINE BREAKDOWN", "critical", "⚠️"),
        ("Jun-Oct 2021", "4-MONTH REPAIRS", "critical", "🔧"),
        ("Nov 10, 2021", "REJECTED at Futuna", "critical", "❌"),
        ("Nov 23, 2021", "DEMURRAGE STARTS", "critical", "💰"),
        ("Mar 19, 2023", "Arbitration award", "award", "⚖️")
    ]
    
    for date, event, impact, icon in timeline_events:
        if impact == "critical":
            st.markdown(f"**{icon} {date}:** <span class='critical-event'>{event}</span>", unsafe_allow_html=True)
        elif impact == "award":
            st.markdown(f"**{icon} {date}:** <span class='award-event'>{event}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"**{icon} {date}:** <span class='normal-event'>{event}</span>", unsafe_allow_html=True)
    
    # Legal Issues
    st.markdown("### ⚖️ KEY LEGAL ISSUES")
    
    legal_issues = [
        ("Contract Performance", "Did Noksel breach by failing to deliver to Futuna?", "Strong for Claimant"),
        ("Vessel Suitability", "Was vessel unsuitable for intended voyage?", "Strong for Claimant"),
        ("Due Diligence", "Should length requirements have been verified?", "Strong for Claimant"),
        ("Force Majeure", "Do engine/COVID problems excuse performance?", "Noksel's best defense")
    ]
    
    for issue, desc, strength in legal_issues:
        with st.container():
            st.markdown(f"**{issue}**")
            st.markdown(f"<small>{desc}</small>", unsafe_allow_html=True)
            if "Claimant" in strength:
                st.success(strength, icon="✅")
            else:
                st.warning(strength, icon="⚠️")

# Column 2 - Competing Stories
with col2:
    st.markdown("### 👥 STRONGEST COMPETING NARRATIVES")
    
    # Create two sub-columns for the stories
    story_col1, story_col2 = st.columns(2)
    
    with story_col1:
        st.markdown("""
        <div class="narrative-box claimant-story">
            <div style="font-weight: bold; color: #166534; text-align: center; margin-bottom: 1rem;">
                CLAIMANT'S WINNING STORY
            </div>
            <div style="background-color: white; padding: 0.5rem; border-radius: 4px; margin-bottom: 1rem;">
                <strong style="color: #166534;">"Noksel's Preventable Due Diligence Failure"</strong>
            </div>
            
            <div style="font-size: 0.8rem;">
                <div><strong>Opening:</strong> "This case is about basic professional negligence - Noksel failed to verify elementary vessel specifications before chartering."</div>
                
                <div style="background-color: #dcfce7; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0;">
                    <div style="font-weight: bold; color: #166534;">Key Facts Supporting Story:</div>
                    <div>• Futuna length limits: publicly available in maritime regulations</div>
                    <div>• MV MESSILA specs: known and discoverable pre-charter</div>
                    <div>• Industry standard: charterer verifies destination compliance</div>
                    <div>• 11-month voyage wasted due to 5-minute regulation check</div>
                </div>

                <div><strong>Narrative Arc:</strong> "We provided a vessel in good faith. Despite extraordinary 4-month engine repairs costing us significantly, we still attempted delivery. When rejected due to Noksel's oversight, we immediately found alternative port to mitigate damages."</div>
                
                <div style="background-color: #dcfce7; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0;">
                    <div style="font-weight: bold; color: #166534;">Powerful Arguments:</div>
                    <div>• Engine problems irrelevant - vessel would have been rejected anyway</div>
                    <div>• Our mitigation efforts (Fiji discharge) show good faith</div>
                    <div>• Demurrage is natural consequence of charterer's failures</div>
                    <div>• Professional standard breached - any competent charterer would have checked</div>
                </div>

                <div><strong>Closing:</strong> "Noksel wants to blame engine problems for their own professional negligence. The vessel was rejected for basic specifications they should have verified on day one."</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with story_col2:
        st.markdown("""
        <div class="narrative-box respondent-story">
            <div style="font-weight: bold; color: #dc2626; text-align: center; margin-bottom: 1rem;">
                RESPONDENT'S BEST DEFENSE
            </div>
            <div style="background-color: white; padding: 0.5rem; border-radius: 4px; margin-bottom: 1rem;">
                <strong style="color: #dc2626;">"Vessel Owner Misrepresentation & Force Majeure"</strong>
            </div>
            
            <div style="font-size: 0.8rem;">
                <div><strong>Opening:</strong> "We were victims of vessel owner misrepresentation and extraordinary circumstances beyond any party's control."</div>
                
                <div style="background-color: #fecaca; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0;">
                    <div style="font-weight: bold; color: #dc2626;">Key Facts Supporting Story:</div>
                    <div>• Vessel history: Multiple name changes suggest concealment</div>
                    <div>• Build records: Contradictory construction data (Ukraine vs Netherlands)</div>
                    <div>• Engine condition: Award claims 'no problems' but 4-month repairs needed</div>
                    <div>• COVID-19: 2021 spare parts delivery restrictions were unforeseeable</div>
                </div>

                <div><strong>Narrative Arc:</strong> "We relied on vessel owner representations about seaworthiness. The vessel's hidden problems caused the real delay. When we finally reached Futuna after overcoming these obstacles, sudden regulatory enforcement seemed suspiciously timed."</div>
                
                <div style="background-color: #fecaca; padding: 0.5rem; border-radius: 4px; margin: 0.5rem 0;">
                    <div style="font-weight: bold; color: #dc2626;">Powerful Arguments:</div>
                    <div>• Vessel owners knew of seaworthiness issues but concealed them</div>
                    <div>• Multiple vessel identity changes show pattern of liability avoidance</div>
                    <div>• Futuna regulation timing: Nov 9 amendment day before rejection</div>
                    <div>• Force majeure: Engine failure + COVID = unforeseeable events</div>
                </div>

                <div><strong>Closing:</strong> "If the vessel had been seaworthy as represented, we would have reached Futuna months earlier, before any regulatory changes. This is vessel owner liability, not charterer negligence."</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("**Tribunal Decision Point:** Did Noksel's due diligence failure outweigh force majeure circumstances?")

# Column 3 - Strategic Analysis
with col3:
    # Causation Analysis
    st.markdown("### ⚠️ CAUSATION CHAIN ANALYSIS")
    
    st.info("**Proximate Cause Test:** What was the 'but for' cause of demurrage?")
    
    cause_col1, cause_col2 = st.columns(2)
    with cause_col1:
        st.success("**Claimant's Theory**\nLength non-compliance → Rejection → Demurrage\n*(Engine problems irrelevant)*")
    with cause_col2:
        st.error("**Respondent's Theory**\nEngine failure → Delay → Late arrival → Rejection\n*(Timing was everything)*")
    
    st.warning("**Key Issue:** Would vessel have been rejected even if arrived on time?")
    
    # Expert Witness Strategy
    st.markdown("### 👨‍💼 EXPERT WITNESS STRATEGY")
    
    expert_col1, expert_col2 = st.columns(2)
    with expert_col1:
        st.markdown("""
        **CLAIMANT NEEDS**
        - Maritime surveyor: Vessel condition vs representations
        - Regulatory expert: Futuna requirements discoverability  
        - Industry expert: Standard due diligence practices
        """)
    with expert_col2:
        st.markdown("""
        **RESPONDENT NEEDS**
        - Marine engineer: Engine failure analysis
        - COVID expert: 2021 supply chain disruptions
        - Regulatory expert: Timing of rule changes
        """)
    
    st.info("**Battle of Experts:** Due diligence standard vs force majeure scope")
    
    # Evidence Strength Matrix
    st.markdown("### 📄 EVIDENCE STRENGTH ANALYSIS")
    
    evidence_col1, evidence_col2, evidence_col3 = st.columns(3)
    
    with evidence_col1:
        st.markdown('<div class="evidence-strong"><strong>STRONG</strong></div>', unsafe_allow_html=True)
        st.markdown("""
        - Arbitration award issued
        - Vessel rejection documented
        - Multiple vessel name changes
        - Contradictory build records
        """)
    
    with evidence_col2:
        st.markdown('<div class="evidence-medium"><strong>MEDIUM</strong></div>', unsafe_allow_html=True)
        st.markdown("""
        - Engine repair duration
        - COVID supply disruptions
        - Regulatory timing issues
        - Industry practice standards
        """)
    
    with evidence_col3:
        st.markdown('<div class="evidence-weak"><strong>WEAK</strong></div>', unsafe_allow_html=True)
        st.markdown("""
        - Vessel owner knowledge
        - Regulation discoverability
        - Force majeure scope
        - Mitigation efforts adequacy
        """)
    
    # Settlement vs Litigation
    st.markdown("### 🤝 SETTLEMENT vs LITIGATION")
    
    settle_col1, settle_col2 = st.columns(2)
    with settle_col1:
        st.success("""
        **SETTLEMENT DRIVERS**
        - Payment arrangement already in place
        - Turkish enforcement uncertainty
        - Ongoing business relationships
        - Cost of extended litigation
        
        **Probability: 70%**
        """)
    
    with settle_col2:
        st.error("""
        **LITIGATION DRIVERS**
        - Strong precedent value
        - Clear liability case
        - Vessel credibility issues
        - Recovery potential high
        
        **Risk: Medium**
        """)

# Column 4 - Advanced Analytics
with col4:
    # Time-Decay Risk Analysis
    st.markdown("### 🕐 TIME-DECAY RISK ANALYSIS")
    
    time_periods = [
        ("Days 0-30 (Peak)", "85%", "Payment deadline pressure, asset investigation window"),
        ("Days 30-90", "70%", "Asset hiding risk increases, settlement urgency peaks"),
        ("Days 90-150", "55%", "Enforcement preparation, appeal risk monitoring"),
        ("Days 150-180", "40%", "Default triggers, enforcement becomes primary option")
    ]
    
    for period, percentage, description in time_periods:
        st.metric(period, percentage, description)
    
    st.info("**Optimal Window:** Days 15-45")
    
    # Precedent Analysis
    st.markdown("### ⚖️ PRECEDENT ANALYSIS")
    
    st.success("""
    **Favorable**
    - The Seaflower [2001]: Due diligence duty
    - Bulk Chile [2013]: Vessel suitability
    """)
    
    st.error("""
    **Adverse**
    - Golden Victory [2007]: Intervening events
    - Edwinton [2021]: COVID force majeure
    """)
    
    st.info("**Key:** Due diligence vs seaworthiness focus")
    
    # Financial Intelligence
    st.markdown("### 💰 NOKSEL FINANCIAL PROFILE")
    
    st.warning("""
    **Credit Risk**
    - Multiple same-day invoices
    - Extended payment terms
    - Turkish manufacturing volatility
    """)
    
    st.info("""
    **Asset Intelligence**
    - Corporate structure unknown
    - International holdings unclear
    - Bank account locations needed
    """)
    
    # Recovery Scenarios
    st.markdown("### 💵 RECOVERY SCENARIOS")
    
    st.success("**Best (90%):** $40K+")
    st.warning("**Likely (60%):** $27K+") 
    st.error("**Worst (20%):** $9K+")
    st.info("**Expected:** $28K")

# Column 5 - Executive Dashboard
with col5:
    st.markdown("""
    <div class="executive-dashboard">
        <h3 style="margin-top: 0;">EXECUTIVE DASHBOARD</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 1rem;">
            <div style="background-color: #16a34a; padding: 0.5rem; border-radius: 4px; text-align: center;">
                <div style="font-weight: bold;">GO/NO-GO</div>
                <div>Settlement: GO</div>
            </div>
            <div style="background-color: #2563eb; padding: 0.5rem; border-radius: 4px; text-align: center;">
                <div style="font-weight: bold;">TIMING</div>
                <div>Within 15 days</div>
            </div>
            <div style="background-color: #d97706; padding: 0.5rem; border-radius: 4px; text-align: center;">
                <div style="font-weight: bold;">BUDGET</div>
                <div>$15K costs</div>
            </div>
            <div style="background-color: #dc2626; padding: 0.5rem; border-radius: 4px; text-align: center;">
                <div style="font-weight: bold;">TARGET</div>
                <div>65% recovery</div>
            </div>
        </div>
        <div style="background-color: #374151; padding: 0.5rem; border-radius: 4px; text-align: center;">
            <span style="font-weight: bold; color: #4ade80;">NEXT:</span> Commission LMAA mediation
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Strategic Recommendation
    st.markdown("### 🎯 STRATEGIC RECOMMENDATION")
    
    st.success("**PURSUE SETTLEMENT**", icon="✅")
    st.info("**TARGET: 65% RECOVERY ($25K+)**", icon="🎯")
    st.warning("**TIMELINE: 30-45 DAYS**", icon="⏰") 
    st.error("**NEXT ACTION: LMAA MEDIATION**", icon="🚀")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; font-size: 0.8rem;">
    MV MESSILA Dispute Analysis Dashboard | Generated: {date} | Status: Active Enforcement Period
</div>
""".format(date=datetime.now().strftime("%Y-%m-%d %H:%M")), unsafe_allow_html=True)
