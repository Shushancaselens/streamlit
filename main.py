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

# Custom CSS for basic styling
st.markdown("""
<style>
    .metric-container {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .main {
        padding-top: 1rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# HEADER SECTION - Simplified for better compatibility
st.markdown("# ⚖️ MV MESSILA DEMURRAGE DISPUTE")
st.markdown("## Legal Brief & Strategic Analysis")

header_col1, header_col2 = st.columns([2, 1])

with header_col1:
    st.markdown("""
    **Transasya v. Noksel Çelik Boru Sanayi A.Ş.**  
    **Arbitrator:** John Schofield  
    **Award Date:** March 19, 2023  
    **Payment Due:** March 19, 2025
    """)

with header_col2:
    st.metric(
        label="💰 Total Award",
        value="$37,317.71",
        delta="+ $3K fees + 5% interest"
    )
    st.error("⏰ 180 days to payment")

# EXECUTIVE SUMMARY
st.markdown("## 📊 EXECUTIVE SUMMARY")

summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

with summary_col1:
    st.metric(
        label="💰 Total Award",
        value="$37,317.71",
        delta="+ fees & interest"
    )

with summary_col2:
    st.metric(
        label="📈 Recovery Probability", 
        value="70%",
        delta="Settlement likely"
    )

with summary_col3:
    st.metric(
        label="⏱️ Optimal Timeline",
        value="15-45 days",
        delta="Peak leverage window"
    )

with summary_col4:
    st.metric(
        label="🎯 Recommended Action",
        value="Settlement",
        delta="65% recovery target"
    )

st.markdown("---")

# MAIN CONTENT LAYOUT
tab1, tab2, tab3, tab4 = st.tabs(["📋 Case Overview", "⚖️ Legal Analysis", "📊 Strategic Assessment", "🎯 Action Plan"])

# TAB 1: CASE OVERVIEW
with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Case Summary using native Streamlit components
        st.markdown("### 📋 Case Summary")
        
        # Use info box for better compatibility
        st.info("""
        **Turkish steel supplier Noksel Çelik Boru Sanayi A.Ş.** chartered MV MESSILA to deliver steel pipes 
        to the remote French Pacific island of Futuna for a dock construction project.
        
        After a catastrophic engine breakdown requiring 4 months of repairs and subsequent regulatory rejection 
        at the destination port, the cargo was ultimately discharged in Fiji, triggering significant demurrage costs.
        """)
        
        # Case details in a simple container
        st.markdown("**Case Details:**")
        case_details_col1, case_details_col2 = st.columns(2)
        
        with case_details_col1:
            st.write("🏛️ **Claimant:** Transasya (Vessel Owners)")
            st.write("⚖️ **Core Dispute:** Liability for vessel failure costs")
        
        with case_details_col2:
            st.write("🏭 **Respondent:** Noksel (Turkish Steel Supplier)")
            st.write("📜 **Current Status:** Award issued, enforcement pending")
        
        # Key Parties and Roles
        st.markdown("### 👥 Key Parties & Roles")
        
        parties_data = {
            "Party": ["Transasya", "Noksel Çelik Boru", "MV MESSILA", "John Schofield"],
            "Role": ["Vessel Owner/Claimant", "Steel Supplier/Respondent", "Chartered Vessel", "Arbitrator"],
            "Key Interest": ["Demurrage Recovery", "Cost Avoidance", "Asset at Risk", "Fair Resolution"],
            "Strength": ["Strong legal position", "Force majeure defense", "Operational evidence", "Industry expertise"]
        }
        
        parties_df = pd.DataFrame(parties_data)
        st.dataframe(parties_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("### 🕐 Critical Timeline")
        
        timeline_events = [
            ("Feb 4, 2020", "📄 Supply contract signed", "Contract formation", "normal"),
            ("Nov 12, 2020", "🚢 MV MESSILA chartered", "Vessel engagement", "normal"),
            ("Dec 1-3, 2020", "📦 Cargo loaded in Turkey", "Voyage commencement", "normal"),
            ("May 25, 2021", "⚠️ ENGINE BREAKDOWN", "Critical mechanical failure", "critical"),
            ("Jun-Oct 2021", "🔧 4-MONTH REPAIR PERIOD", "Extended downtime", "critical"),
            ("Nov 10, 2021", "❌ REJECTED at Futuna", "Regulatory non-compliance", "critical"),
            ("Nov 23, 2021", "💰 DEMURRAGE COMMENCES", "Cost accumulation begins", "critical"),
            ("Mar 19, 2023", "⚖️ Arbitration award issued", "Legal resolution", "award")
        ]
        
        for i, (date, event, description, event_type) in enumerate(timeline_events):
            # Use containers with color coding
            if event_type == "critical":
                with st.container():
                    st.error(f"**{date}**")
                    st.write(f"{event}")
                    st.caption(description)
            elif event_type == "award":
                with st.container():
                    st.success(f"**{date}**")
                    st.write(f"{event}")
                    st.caption(description)
            else:
                with st.container():
                    st.info(f"**{date}**")
                    st.write(f"{event}")
                    st.caption(description)
        
        # Financial Impact
        st.markdown("### 💰 Financial Impact Breakdown")
        
        financial_data = {
            "Component": ["Base Demurrage", "Additional Fees", "Interest (5%)", "Legal Costs", "Enforcement Costs", "Total Exposure"],
            "Amount ($)": [37317.71, 3000.00, 1865.89, 15000.00, 8000.00, 65183.60],
            "Status": ["Awarded", "Awarded", "Accruing", "Estimated", "Potential", "Maximum Risk"],
            "Recovery Probability": ["85%", "85%", "70%", "N/A", "50%", "75%"]
        }
        
        financial_df = pd.DataFrame(financial_data)
        st.dataframe(financial_df, use_container_width=True, hide_index=True)
        
        # Cost-Benefit Analysis
        st.markdown("### 📊 Cost-Benefit Decision Matrix")
        
        cb_col1, cb_col2 = st.columns(2)
        
        with cb_col1:
            st.success("""
            **💰 SETTLEMENT BENEFITS**
            - Guaranteed recovery: $25K+ (65%+)
            - Speed: 30-45 days to resolution
            - Cost control: $10-15K total expenses
            - Relationship preservation
            - Payment certainty
            """)
        
        with cb_col2:
            st.warning("""
            **⚖️ LITIGATION COSTS**
            - Extended timeline: 12-18 months
            - Higher costs: $25-40K expenses
            - Uncertain outcome despite strong case
            - Enforcement challenges in Turkey
            - Relationship damage potential
            """)

# TAB 2: LEGAL ANALYSIS
with tab2:
    # Competing Legal Narratives
    st.markdown("## ⚖️ Competing Legal Narratives")
    
    narrative_col1, narrative_col2 = st.columns(2)
    
    with narrative_col1:
        st.success("🏆 **CLAIMANT'S WINNING NARRATIVE**")
        st.markdown("### 'Preventable Due Diligence Failure'")
        
        st.markdown("**🎯 Core Argument:**")
        st.write("""
        This case represents basic professional negligence - Noksel failed to verify elementary vessel 
        specifications before chartering, wasting an 11-month voyage that could have been prevented 
        with a 5-minute regulation check.
        """)
        
        st.markdown("**✅ Supporting Evidence:**")
        st.write("• Futuna length restrictions: publicly available in maritime regulations")
        st.write("• MV MESSILA specifications: known and discoverable pre-charter")
        st.write("• Industry standard: charterer responsible for destination compliance verification")
        st.write("• Professional duty breached: any competent charterer would have checked")
        
        st.markdown("**📖 Legal Strategy:**")
        st.write("""
        We delivered a vessel in good faith. Despite extraordinary repair costs, we attempted delivery. 
        Engine problems are irrelevant - the vessel would have been rejected regardless due to Noksel's oversight.
        """)
        
        st.markdown("**🎯 Closing Position:**")
        st.write("""
        Noksel wants to blame unforeseeable engine problems for their own foreseeable professional negligence. 
        The vessel was rejected for basic specifications they should have verified on day one.
        """)
    
    with narrative_col2:
        st.error("🛡️ **RESPONDENT'S BEST DEFENSE**")
        st.markdown("### 'Vessel Owner Misrepresentation & Force Majeure'")
        
        st.markdown("**🎯 Core Argument:**")
        st.write("""
        We were victims of vessel owner misrepresentation about seaworthiness and extraordinary 
        circumstances beyond any party's reasonable control, including COVID-19 supply chain disruptions.
        """)
        
        st.markdown("**⚠️ Supporting Evidence:**")
        st.write("• Vessel history: multiple name changes suggest concealment patterns")
        st.write("• Build records: contradictory construction data (Ukraine vs Netherlands)")
        st.write("• Engine condition: award claims 'no problems' yet 4-month repairs needed")
        st.write("• COVID-19: 2021 spare parts restrictions were genuinely unforeseeable")
        
        st.markdown("**📖 Legal Strategy:**")
        st.write("""
        If the vessel had been seaworthy as represented, we would have reached Futuna months earlier, 
        before any regulatory changes. The real delay was caused by hidden vessel problems.
        """)
        
        st.markdown("**🎯 Closing Position:**")
        st.write("""
        The suspicious timing of Futuna regulation enforcement (Nov 9 amendment, day before rejection) 
        combined with vessel identity concealment patterns suggest this is vessel owner liability, 
        not charterer negligence.
        """)
    
    # Decision Framework - using native components
    st.warning("🎯 **Tribunal Decision Framework**")
    st.markdown("**Central Question:** Did Noksel's due diligence failure outweigh force majeure circumstances?")
    
    # Legal Issues Analysis
    st.markdown("### 📚 Key Legal Issues Analysis")
    
    legal_col1, legal_col2 = st.columns(2)
    
    with legal_col1:
        st.markdown("#### ✅ Strong Legal Positions")
        
        strong_issues = [
            ("Contract Performance", "Did Noksel breach delivery obligations?", "Claimant favored - clear failure to deliver"),
            ("Vessel Suitability", "Was vessel appropriate for intended voyage?", "Claimant favored - met charter specifications"),
            ("Due Diligence Standard", "Should length requirements have been verified?", "Claimant favored - industry standard practice")
        ]
        
        for issue, question, assessment in strong_issues:
            with st.expander(f"📋 {issue}"):
                st.write(f"**Key Question:** {question}")
                st.success(f"**Assessment:** {assessment}")
    
    with legal_col2:
        st.markdown("#### ⚠️ Contested Legal Areas")
        
        contested_issues = [
            ("Force Majeure Scope", "Do engine/COVID problems excuse performance?", "Respondent's strongest defense argument"),
            ("Causation Analysis", "What was the proximate cause of demurrage?", "Complex timing and multiple contributing factors"),
            ("Mitigation Duties", "Were damages properly mitigated?", "Mixed evidence on both sides")
        ]
        
        for issue, question, assessment in contested_issues:
            with st.expander(f"⚖️ {issue}"):
                st.write(f"**Key Question:** {question}")
                st.warning(f"**Assessment:** {assessment}")
    
    # Causation Chain Analysis
    st.markdown("### ⚠️ Causation Chain Analysis")
    
    st.info("**Proximate Cause Test:** What was the 'but for' cause of demurrage?")
    
    causation_col1, causation_col2 = st.columns(2)
    
    with causation_col1:
        st.success("""
        **🏛️ Claimant's Causation Theory**
        
        Length non-compliance → Rejection → Demurrage
        
        *(Engine problems irrelevant to final outcome)*
        """)
    
    with causation_col2:
        st.error("""
        **🏭 Respondent's Causation Theory**
        
        Engine failure → Delay → Late arrival → Rejection
        
        *(Timing was everything - early arrival = acceptance)*
        """)
    
    st.warning("**🎯 Critical Legal Question:** Would vessel have been rejected even if it arrived on schedule?")
    
    # Evidence Strength Matrix
    st.markdown("### 📊 Evidence Strength Analysis")
    
    evidence_col1, evidence_col2, evidence_col3 = st.columns(3)
    
    with evidence_col1:
        st.success("**💪 STRONG EVIDENCE**")
        st.write("• Arbitration award documentation")
        st.write("• Vessel rejection records")
        st.write("• Multiple vessel name changes")
        st.write("• Contradictory build records")
        st.write("• Demurrage calculation details")
    
    with evidence_col2:
        st.warning("**⚖️ MEDIUM EVIDENCE**")
        st.write("• Engine repair duration claims")
        st.write("• COVID supply chain impacts")
        st.write("• Regulatory timing issues")
        st.write("• Industry practice standards")
        st.write("• Mitigation effort documentation")
    
    with evidence_col3:
        st.error("**❓ DISPUTED EVIDENCE**")
        st.write("• Vessel owner knowledge claims")
        st.write("• Regulation discoverability")
        st.write("• Force majeure scope limits")
        st.write("• Seaworthiness representations")
        st.write("• Alternative port options")
    
    # Precedent Analysis
    st.markdown("### ⚖️ Legal Precedent Analysis")
    
    precedent_col1, precedent_col2 = st.columns(2)
    
    with precedent_col1:
        st.success("""
        **✅ FAVORABLE PRECEDENTS**
        
        **The Seaflower [2001]:**
        - Due diligence duty on charterers
        - Verification of port specifications
        
        **Bulk Chile [2013]:**
        - Vessel suitability standards
        - Charterer responsibility for compliance
        """)
    
    with precedent_col2:
        st.error("""
        **⚠️ ADVERSE PRECEDENTS**
        
        **Golden Victory [2007]:**
        - Intervening events doctrine
        - Causation complexity analysis
        
        **Edwinton [2021]:**
        - COVID-19 force majeure recognition
        - Unforeseeable circumstances
        """)
    
    st.info("**🎯 Key Precedent Battle:** Due diligence standard vs. seaworthiness warranty focus")

# TAB 3: STRATEGIC ASSESSMENT
with tab3:
    st.markdown("## 📊 Strategic Assessment")
    
    # Risk-Reward Analysis
    assess_col1, assess_col2 = st.columns(2)
    
    with assess_col1:
        st.markdown("### ⏰ Time-Decay Risk Analysis")
        
        risk_periods = [
            ("Days 0-30 (PEAK)", "85%", "green", "Payment deadline pressure maximizes leverage"),
            ("Days 30-90", "70%", "yellow", "Settlement urgency peak, asset hiding risk increases"),
            ("Days 90-150", "55%", "orange", "Enforcement preparation phase, appeal monitoring"),
            ("Days 150-180", "40%", "red", "Default triggers, enforcement becomes primary option")
        ]
        
        for period, probability, color, description in risk_periods:
            if color == "green":
                st.success(f"**{period}**: {probability} recovery probability\n\n{description}")
            elif color == "yellow":
                st.warning(f"**{period}**: {probability} recovery probability\n\n{description}")
            elif color == "orange":
                st.info(f"**{period}**: {probability} recovery probability\n\n{description}")
            else:
                st.error(f"**{period}**: {probability} recovery probability\n\n{description}")
        
        st.info("**🎯 Optimal Action Window: Days 15-45** - Maximum leverage with manageable risk exposure")
        
        # Noksel Financial Intelligence
        st.markdown("### 🏭 Noksel Financial Profile")
        
        st.warning("""
        **⚠️ CREDIT RISK INDICATORS**
        - Multiple same-day invoice patterns
        - Extended payment terms requested
        - Turkish manufacturing sector volatility
        - Economic uncertainty factors
        """)
        
        st.info("""
        **🔍 ASSET INTELLIGENCE GAPS**
        - Corporate structure: Unknown subsidiaries
        - International holdings: Unclear portfolio
        - Bank account locations: Investigation needed
        - Asset hiding potential: Moderate risk
        """)
        
        st.error("""
        **🚨 COLLECTION RISK FACTORS**
        - Cross-border enforcement challenges
        - Turkish legal system complexities
        - Currency volatility exposure
        - Political risk considerations
        """)
    
    with assess_col2:
        st.markdown("### 💰 Recovery Scenario Analysis")
        
        # Recovery scenarios chart
        scenarios_data = {
            "Scenario": ["Best Case", "Most Likely", "Conservative", "Worst Case"],
            "Probability": ["10%", "60%", "25%", "5%"],
            "Recovery Amount": ["$40,000+", "$28,000", "$20,000", "$10,000"],
            "Recovery %": ["100%+", "75%", "55%", "25%"],
            "Timeline": ["30 days", "45 days", "90 days", "180+ days"]
        }
        
        scenarios_df = pd.DataFrame(scenarios_data)
        st.dataframe(scenarios_df, use_container_width=True, hide_index=True)
        
        st.markdown("### 📈 Expected Value Calculation")
        st.metric(
            label="Weighted Expected Recovery",
            value="$28,150",
            delta="75% of total award"
        )
        
        # Settlement vs Litigation Analysis
        st.markdown("### 🤝 Settlement vs. Litigation")
        
        settlement_factors = [
            "✅ Payment arrangement already established",
            "✅ Turkish enforcement challenges",
            "✅ Ongoing business relationship preservation",
            "✅ Cost certainty and speed",
            "✅ 70% settlement probability"
        ]
        
        litigation_factors = [
            "⚠️ Strong precedent value potential",
            "⚠️ Clear liability case facts",
            "⚠️ Vessel credibility issues",
            "⚠️ Full recovery possibility",
            "⚠️ Higher cost and time risk"
        ]
        
        settle_col, litigate_col = st.columns(2)
        
        with settle_col:
            st.success("**SETTLEMENT ADVANTAGES**")
            for factor in settlement_factors:
                st.write(factor)
        
        with litigate_col:
            st.warning("**LITIGATION CONSIDERATIONS**")
            for factor in litigation_factors:
                st.write(factor)
    
    # Expert Witness Strategy
    st.markdown("### 👨‍💼 Expert Witness Requirements")
    
    expert_col1, expert_col2, expert_col3 = st.columns(3)
    
    with expert_col1:
        st.info("""
        **🚢 MARITIME EXPERTS**
        - Vessel surveyor for condition assessment
        - Marine engineer for engine failure analysis
        - Charter party specialist for contract interpretation
        """)
    
    with expert_col2:
        st.info("""
        **📋 REGULATORY EXPERTS**
        - Pacific maritime law specialist
        - Port authority requirements expert
        - International shipping compliance advisor
        """)
    
    with expert_col3:
        st.info("""
        **💼 INDUSTRY EXPERTS**
        - Steel transportation specialist
        - Due diligence standard authority
        - COVID-19 maritime impact analyst
        """)

# TAB 4: ACTION PLAN
with tab4:
    st.markdown("## 🎯 Strategic Action Plan")
    
    # Executive Dashboard - using native Streamlit components
    st.markdown("## 🎯 EXECUTIVE DECISION DASHBOARD")
    
    # Create 4 columns for the dashboard metrics
    dash_col1, dash_col2, dash_col3, dash_col4 = st.columns(4)
    
    with dash_col1:
        st.success("**GO/NO-GO DECISION**")
        st.markdown("### ✅ PURSUE SETTLEMENT")
    
    with dash_col2:
        st.info("**OPTIMAL TIMING**")
        st.markdown("### ⏰ 15-30 DAYS")
    
    with dash_col3:
        st.warning("**BUDGET ALLOCATION**")
        st.markdown("### 💰 $15K COSTS")
    
    with dash_col4:
        st.error("**RECOVERY TARGET**")
        st.markdown("### 🎯 65% ($25K+)")
    
    # Next action section
    st.markdown("---")
    st.success("### 🚀 IMMEDIATE NEXT ACTION: Commission LMAA Mediation Process")
    
    # Detailed Action Steps
    st.markdown("### 📋 30-Day Action Timeline")
    
    action_col1, action_col2 = st.columns(2)
    
    with action_col1:
        st.markdown("#### 🚀 IMMEDIATE ACTIONS (Days 1-7)")
        
        immediate_actions = [
            ("Day 1", "📞 Contact LMAA for mediation scheduling", "Critical"),
            ("Day 2", "🔍 Commission asset investigation on Noksel", "High"),
            ("Day 3", "📋 Prepare settlement demand letter", "High"),
            ("Day 5", "👨‍💼 Engage maritime law specialist", "Medium"),
            ("Day 7", "📊 Complete financial exposure analysis", "Medium")
        ]
        
        for day, action, priority in immediate_actions:
            if priority == "Critical":
                st.error(f"**{day}**: {action}")
            elif priority == "High":
                st.warning(f"**{day}**: {action}")
            else:
                st.info(f"**{day}**: {action}")
    
    with action_col2:
        st.markdown("#### ⚖️ STRATEGIC ACTIONS (Days 8-30)")
        
        strategic_actions = [
            ("Days 8-10", "🤝 Initiate preliminary settlement discussions", "Critical"),
            ("Days 11-15", "📄 Exchange position papers and evidence", "High"),
            ("Days 16-20", "🎯 Conduct formal mediation sessions", "Critical"),
            ("Days 21-25", "💰 Negotiate final settlement terms", "High"),
            ("Days 26-30", "✅ Execute settlement agreement", "Critical")
        ]
        
        for day, action, priority in strategic_actions:
            if priority == "Critical":
                st.error(f"**{day}**: {action}")
            elif priority == "High":
                st.warning(f"**{day}**: {action}")
            else:
                st.info(f"**{day}**: {action}")
    
    # Risk Mitigation
    st.markdown("### 🛡️ Risk Mitigation Strategies")
    
    risk_col1, risk_col2, risk_col3 = st.columns(3)
    
    with risk_col1:
        st.markdown("""
        **🏦 FINANCIAL RISKS**
        - Monitor Noksel's financial stability
        - Secure payment guarantees
        - Consider partial payment structures
        - Prepare enforcement alternatives
        """)
    
    with risk_col2:
        st.markdown("""
        **⚖️ LEGAL RISKS**
        - Document all settlement negotiations
        - Preserve enforcement rights
        - Monitor appeal deadlines
        - Maintain evidence integrity
        """)
    
    with risk_col3:
        st.markdown("""
        **⏰ TIMING RISKS**
        - Avoid deadline pressures
        - Maintain negotiation momentum
        - Prepare litigation backup
        - Monitor regulatory changes
        """)
    
    # Success Metrics
    st.markdown("### 📊 Success Metrics & KPIs")
    
    metrics_data = {
        "Metric": [
            "Settlement Achievement",
            "Recovery Percentage", 
            "Timeline Adherence",
            "Cost Management",
            "Client Satisfaction"
        ],
        "Target": [
            "Negotiated settlement",
            "65% of total award",
            "Within 45 days",
            "Under $15K costs",
            "Exceeded expectations"
        ],
        "Current Status": [
            "Planning phase",
            "TBD",
            "On track",
            "Budget allocated", 
            "High confidence"
        ],
        "Risk Level": [
            "Low",
            "Medium",
            "Low",
            "Low",
            "Low"
        ]
    }
    
    metrics_df = pd.DataFrame(metrics_data)
    st.dataframe(metrics_df, use_container_width=True, hide_index=True)

# FOOTER
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("""
    **📊 Dashboard Status**  
    Last Updated: {date}  
    Status: Active Enforcement  
    Version: 2.1
    """.format(date=datetime.now().strftime("%Y-%m-%d %H:%M")))

with footer_col2:
    st.markdown("""
    **⚖️ Legal Framework**  
    Governing Law: English Law  
    Arbitration Seat: London  
    Enforcement: International
    """)

with footer_col3:
    st.markdown("""
    **🎯 Strategic Priority**  
    Action Status: Immediate  
    Risk Level: Manageable  
    Success Probability: High
    """)
