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

# Custom CSS for better styling and hierarchy
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .section-header {
        background-color: #f8fafc;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    
    .case-summary {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 2px solid #93c5fd;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    .timeline-container {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .timeline-item {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        padding: 0.5rem;
        border-radius: 6px;
        transition: background-color 0.2s;
    }
    
    .timeline-item:hover {
        background-color: #f9fafb;
    }
    
    .timeline-critical {
        background-color: #fef2f2;
        border-left: 4px solid #dc2626;
    }
    
    .timeline-award {
        background-color: #f0fdf4;
        border-left: 4px solid #16a34a;
    }
    
    .timeline-normal {
        background-color: #eff6ff;
        border-left: 4px solid #2563eb;
    }
    
    .narrative-claimant {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border: 2px solid #22c55e;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(34, 197, 94, 0.1);
    }
    
    .narrative-respondent {
        background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%);
        border: 2px solid #ef4444;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(239, 68, 68, 0.1);
    }
    
    .key-facts {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    .evidence-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .evidence-strong {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        border: 1px solid #22c55e;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    
    .evidence-medium {
        background: linear-gradient(135deg, #fefce8 0%, #fde047 100%);
        border: 1px solid #eab308;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    
    .evidence-weak {
        background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%);
        border: 1px solid #ef4444;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    
    .executive-dashboard {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    
    .dashboard-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .dashboard-item {
        padding: 1rem;
        border-radius: 6px;
        text-align: center;
        font-weight: bold;
    }
    
    .metric-container {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #3b82f6, transparent);
        margin: 2rem 0;
        border: none;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde047 100%);
        border: 2px solid #f59e0b;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# HEADER SECTION
st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 300px;">
            <h1 style="margin: 0; font-size: 2rem; font-weight: bold;">⚖️ MV MESSILA DEMURRAGE DISPUTE</h1>
            <h2 style="margin: 0.5rem 0; font-size: 1.2rem; color: #cbd5e1;">Legal Brief & Strategic Analysis</h2>
            <p style="margin: 0; font-size: 0.9rem; color: #94a3b8;">
                Transasya v. Noksel Çelik Boru Sanayi A.Ş. | Arbitrator: John Schofield<br>
                Award Date: March 19, 2023 | Payment Due: March 19, 2025
            </p>
        </div>
        <div style="text-align: right; min-width: 200px;">
            <div style="font-size: 2.5rem; font-weight: bold; color: #fbbf24;">$37,317.71</div>
            <div style="font-size: 1rem; color: #e5e7eb;">+ $3,000 fees + 5% interest</div>
            <div style="font-size: 1rem; color: #fbbf24; font-weight: bold;">⏰ 180 days to payment</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# EXECUTIVE SUMMARY
st.markdown('<div class="section-header"><h2>📊 EXECUTIVE SUMMARY</h2></div>', unsafe_allow_html=True)

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

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# MAIN CONTENT LAYOUT
tab1, tab2, tab3, tab4 = st.tabs(["📋 Case Overview", "⚖️ Legal Analysis", "📊 Strategic Assessment", "🎯 Action Plan"])

# TAB 1: CASE OVERVIEW
with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="case-summary">
            <h3 style="margin-top: 0; color: #1e40af; font-size: 1.3rem;">📋 Case Summary</h3>
            <p style="font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
                Turkish steel supplier <strong>Noksel Çelik Boru Sanayi A.Ş.</strong> chartered MV MESSILA to deliver steel pipes 
                to the remote French Pacific island of Futuna for a dock construction project. 
            </p>
            <p style="font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
                After a catastrophic engine breakdown requiring 4 months of repairs and subsequent regulatory rejection 
                at the destination port, the cargo was ultimately discharged in Fiji, triggering significant demurrage costs.
            </p>
            
            <div style="background-color: rgba(255, 255, 255, 0.7); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; font-size: 0.9rem;">
                    <div><strong>🏛️ Claimant:</strong> Transasya (Vessel Owners)</div>
                    <div><strong>🏭 Respondent:</strong> Noksel (Turkish Steel Supplier)</div>
                    <div><strong>⚖️ Core Dispute:</strong> Liability for vessel failure costs</div>
                    <div><strong>📜 Current Status:</strong> Award issued, enforcement pending</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
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
        st.markdown("""
        <div class="timeline-container">
            <h3 style="margin-top: 0; color: #374151; font-size: 1.3rem;">🕐 Critical Timeline</h3>
        """, unsafe_allow_html=True)
        
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
            css_class = f"timeline-{event_type}"
            st.markdown(f"""
            <div class="timeline-item {css_class}">
                <div style="flex: 1;">
                    <div style="font-weight: bold; font-size: 0.9rem;">{date}</div>
                    <div style="font-size: 1rem; margin: 0.25rem 0;">{event}</div>
                    <div style="font-size: 0.8rem; color: #6b7280; font-style: italic;">{description}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Financial Impact
        st.markdown("### 💰 Financial Impact Breakdown")
        
        financial_data = {
            "Component": ["Base Demurrage", "Additional Fees", "Interest (5%)", "Legal Costs", "Total Exposure"],
            "Amount ($)": [37317.71, 3000.00, 1865.89, 15000.00, 57183.60],
            "Status": ["Awarded", "Awarded", "Accruing", "Estimated", "Total Risk"]
        }
        
        financial_df = pd.DataFrame(financial_data)
        st.dataframe(financial_df, use_container_width=True, hide_index=True)

# TAB 2: LEGAL ANALYSIS
with tab2:
    # Competing Legal Narratives
    st.markdown('<div class="section-header"><h2>⚖️ Competing Legal Narratives</h2></div>', unsafe_allow_html=True)
    
    narrative_col1, narrative_col2 = st.columns(2)
    
    with narrative_col1:
        st.markdown("""
        <div class="narrative-claimant">
            <div style="text-align: center; font-size: 1.2rem; font-weight: bold; color: #166534; margin-bottom: 1rem;">
                🏆 CLAIMANT'S WINNING NARRATIVE
            </div>
            <div style="background-color: rgba(255, 255, 255, 0.9); padding: 1rem; border-radius: 6px; margin-bottom: 1rem;">
                <div style="font-weight: bold; color: #166534; font-size: 1.1rem; text-align: center;">
                    "Preventable Due Diligence Failure"
                </div>
            </div>
            
            <div style="font-size: 0.95rem; line-height: 1.5;">
                <div style="margin-bottom: 1rem;">
                    <strong>🎯 Core Argument:</strong> "This case represents basic professional negligence - Noksel failed to verify elementary vessel specifications before chartering, wasting an 11-month voyage that could have been prevented with a 5-minute regulation check."
                </div>
                
                <div class="key-facts">
                    <div style="font-weight: bold; color: #166534; margin-bottom: 0.5rem;">✅ Supporting Evidence:</div>
                    <ul style="margin: 0; padding-left: 1.2rem;">
                        <li>Futuna length restrictions: publicly available in maritime regulations</li>
                        <li>MV MESSILA specifications: known and discoverable pre-charter</li>
                        <li>Industry standard: charterer responsible for destination compliance verification</li>
                        <li>Professional duty breached: any competent charterer would have checked</li>
                    </ul>
                </div>

                <div style="margin: 1rem 0;">
                    <strong>📖 Legal Strategy:</strong> "We delivered a vessel in good faith. Despite extraordinary repair costs, we attempted delivery. Engine problems are irrelevant - the vessel would have been rejected regardless due to Noksel's oversight."
                </div>
                
                <div style="background-color: rgba(22, 101, 52, 0.1); padding: 1rem; border-radius: 6px; border-left: 4px solid #166534;">
                    <strong>🎯 Closing Position:</strong> "Noksel wants to blame unforeseeable engine problems for their own foreseeable professional negligence. The vessel was rejected for basic specifications they should have verified on day one."
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with narrative_col2:
        st.markdown("""
        <div class="narrative-respondent">
            <div style="text-align: center; font-size: 1.2rem; font-weight: bold; color: #dc2626; margin-bottom: 1rem;">
                🛡️ RESPONDENT'S BEST DEFENSE
            </div>
            <div style="background-color: rgba(255, 255, 255, 0.9); padding: 1rem; border-radius: 6px; margin-bottom: 1rem;">
                <div style="font-weight: bold; color: #dc2626; font-size: 1.1rem; text-align: center;">
                    "Vessel Owner Misrepresentation & Force Majeure"
                </div>
            </div>
            
            <div style="font-size: 0.95rem; line-height: 1.5;">
                <div style="margin-bottom: 1rem;">
                    <strong>🎯 Core Argument:</strong> "We were victims of vessel owner misrepresentation about seaworthiness and extraordinary circumstances beyond any party's reasonable control, including COVID-19 supply chain disruptions."
                </div>
                
                <div class="key-facts">
                    <div style="font-weight: bold; color: #dc2626; margin-bottom: 0.5rem;">⚠️ Supporting Evidence:</div>
                    <ul style="margin: 0; padding-left: 1.2rem;">
                        <li>Vessel history: multiple name changes suggest concealment patterns</li>
                        <li>Build records: contradictory construction data (Ukraine vs Netherlands)</li>
                        <li>Engine condition: award claims 'no problems' yet 4-month repairs needed</li>
                        <li>COVID-19: 2021 spare parts restrictions were genuinely unforeseeable</li>
                    </ul>
                </div>

                <div style="margin: 1rem 0;">
                    <strong>📖 Legal Strategy:</strong> "If the vessel had been seaworthy as represented, we would have reached Futuna months earlier, before any regulatory changes. The real delay was caused by hidden vessel problems."
                </div>
                
                <div style="background-color: rgba(220, 38, 38, 0.1); padding: 1rem; border-radius: 6px; border-left: 4px solid #dc2626;">
                    <strong>🎯 Closing Position:</strong> "The suspicious timing of Futuna regulation enforcement (Nov 9 amendment, day before rejection) combined with vessel identity concealment patterns suggest this is vessel owner liability, not charterer negligence."
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Decision Framework
    st.markdown("""
    <div class="highlight-box">
        <h3 style="margin: 0; color: #92400e;">🎯 Tribunal Decision Framework</h3>
        <p style="margin: 0.5rem 0; font-size: 1.1rem;">
            <strong>Central Question:</strong> Did Noksel's due diligence failure outweigh force majeure circumstances?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Evidence Strength Matrix
    st.markdown("### 📊 Evidence Strength Analysis")
    
    st.markdown("""
    <div class="evidence-grid">
        <div class="evidence-strong">
            <h4 style="margin-top: 0; color: #166534;">💪 STRONG EVIDENCE</h4>
            <ul style="text-align: left; font-size: 0.9rem;">
                <li>Arbitration award documentation</li>
                <li>Vessel rejection records</li>
                <li>Multiple vessel name changes</li>
                <li>Contradictory build records</li>
                <li>Demurrage calculation details</li>
            </ul>
        </div>
        <div class="evidence-medium">
            <h4 style="margin-top: 0; color: #a16207;">⚖️ MEDIUM EVIDENCE</h4>
            <ul style="text-align: left; font-size: 0.9rem;">
                <li>Engine repair duration claims</li>
                <li>COVID supply chain impacts</li>
                <li>Regulatory timing issues</li>
                <li>Industry practice standards</li>
                <li>Mitigation effort documentation</li>
            </ul>
        </div>
        <div class="evidence-weak">
            <h4 style="margin-top: 0; color: #dc2626;">❓ DISPUTED EVIDENCE</h4>
            <ul style="text-align: left; font-size: 0.9rem;">
                <li>Vessel owner knowledge claims</li>
                <li>Regulation discoverability</li>
                <li>Force majeure scope limits</li>
                <li>Seaworthiness representations</li>
                <li>Alternative port options</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# TAB 3: STRATEGIC ASSESSMENT
with tab3:
    st.markdown('<div class="section-header"><h2>📊 Strategic Assessment</h2></div>', unsafe_allow_html=True)
    
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
        
        st.markdown("""
        <div class="highlight-box">
            <strong>🎯 Optimal Action Window: Days 15-45</strong><br>
            Maximum leverage with manageable risk exposure
        </div>
        """, unsafe_allow_html=True)
    
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
    st.markdown('<div class="section-header"><h2>🎯 Strategic Action Plan</h2></div>', unsafe_allow_html=True)
    
    # Executive Dashboard
    st.markdown("""
    <div class="executive-dashboard">
        <h2 style="margin-top: 0; text-align: center;">🎯 EXECUTIVE DECISION DASHBOARD</h2>
        
        <div class="dashboard-grid">
            <div class="dashboard-item" style="background-color: #16a34a;">
                <div style="font-size: 1.2rem;">GO/NO-GO DECISION</div>
                <div style="font-size: 1.5rem; margin-top: 0.5rem;">✅ PURSUE SETTLEMENT</div>
            </div>
            <div class="dashboard-item" style="background-color: #2563eb;">
                <div style="font-size: 1.2rem;">OPTIMAL TIMING</div>
                <div style="font-size: 1.5rem; margin-top: 0.5rem;">⏰ 15-30 DAYS</div>
            </div>
            <div class="dashboard-item" style="background-color: #d97706;">
                <div style="font-size: 1.2rem;">BUDGET ALLOCATION</div>
                <div style="font-size: 1.5rem; margin-top: 0.5rem;">💰 $15K COSTS</div>
            </div>
            <div class="dashboard-item" style="background-color: #dc2626;">
                <div style="font-size: 1.2rem;">RECOVERY TARGET</div>
                <div style="font-size: 1.5rem; margin-top: 0.5rem;">🎯 65% ($25K+)</div>
            </div>
        </div>
        
        <div style="background-color: #374151; padding: 1.5rem; border-radius: 8px; text-align: center; margin-top: 1rem;">
            <div style="font-size: 1.3rem; font-weight: bold;">
                <span style="color: #4ade80;">🚀 IMMEDIATE NEXT ACTION:</span> 
                Commission LMAA Mediation Process
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

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
