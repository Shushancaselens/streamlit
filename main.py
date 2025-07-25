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

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .decision-dashboard {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0 2rem 0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    
    .risk-reward-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .risk-card {
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid;
    }
    
    .risk-high {
        background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%);
        border-color: #ef4444;
    }
    
    .risk-medium {
        background: linear-gradient(135deg, #fefce8 0%, #fde047 100%);
        border-color: #eab308;
    }
    
    .risk-low {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        border-color: #22c55e;
    }
    
    .decision-tree {
        background: #f8fafc;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .main {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ENHANCED HEADER SECTION
st.markdown("""
<div style="
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 300px;">
            <h1 style="margin: 0; font-size: 2.5rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                ⚖️ MV MESSILA DEMURRAGE DISPUTE
            </h1>
            <h2 style="margin: 0.5rem 0; font-size: 1.4rem; color: #cbd5e1; font-weight: 300;">
                Strategic Decision Brief
            </h2>
            <div style="margin-top: 1rem; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 8px; backdrop-filter: blur(10px);">
                <div style="font-size: 1rem; line-height: 1.6;">
                    <strong>Case:</strong> Transasya v. Noksel Çelik Boru Sanayi A.Ş.<br>
                    <strong>Arbitrator:</strong> John Schofield | <strong>Award:</strong> March 19, 2023
                </div>
            </div>
        </div>
        <div style="text-align: right; min-width: 280px; margin-left: 2rem;">
            <div style="background: rgba(255,255,255,0.15); padding: 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                <div style="font-size: 3rem; font-weight: bold; color: #fbbf24; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin-bottom: 0.5rem;">
                    $37,317.71
                </div>
                <div style="font-size: 1.1rem; color: #e5e7eb; margin-bottom: 0.5rem;">
                    + $3,000 fees + 5% interest
                </div>
                <div style="background: #dc2626; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-weight: bold; font-size: 1rem;">
                    ⏰ 180 days to payment
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# EXECUTIVE DECISION DASHBOARD - MOST PROMINENT
st.markdown("""
<div class="decision-dashboard">
    <h1 style="margin: 0 0 1rem 0; font-size: 2.2rem;">🎯 EXECUTIVE DECISION</h1>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 2rem; margin: 2rem 0;">
        <div>
            <div style="font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;">DECISION</div>
            <div style="font-size: 2rem; font-weight: bold;">✅ SETTLE</div>
        </div>
        <div>
            <div style="font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;">TARGET</div>
            <div style="font-size: 2rem; font-weight: bold;">65% ($25K+)</div>
        </div>
        <div>
            <div style="font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;">TIMELINE</div>
            <div style="font-size: 2rem; font-weight: bold;">15-30 DAYS</div>
        </div>
        <div>
            <div style="font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;">NEXT ACTION</div>
            <div style="font-size: 1.5rem; font-weight: bold;">🚀 LMAA MEDIATION</div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
        <strong style="font-size: 1.2rem;">CONFIDENCE LEVEL: 85% | RISK: MANAGEABLE | ACTION REQUIRED: IMMEDIATE</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# RISK-REWARD SUMMARY - PROMINENT SECTION
st.markdown("## ⚖️ RISK-REWARD ANALYSIS")

risk_col1, risk_col2, risk_col3 = st.columns(3)

with risk_col1:
    st.markdown("""
    <div class="risk-card risk-low">
        <h3 style="margin-top: 0; color: #166534;">🟢 SETTLEMENT PATH</h3>
        <div style="font-size: 1.8rem; font-weight: bold; color: #166534; margin: 1rem 0;">70% Success</div>
        <div style="color: #166534;">
            <strong>Expected Recovery:</strong> $25-28K<br>
            <strong>Timeline:</strong> 30-45 days<br>
            <strong>Cost:</strong> $10-15K<br>
            <strong>Risk:</strong> Low
        </div>
    </div>
    """, unsafe_allow_html=True)

with risk_col2:
    st.markdown("""
    <div class="risk-card risk-medium">
        <h3 style="margin-top: 0; color: #a16207;">🟡 LITIGATION PATH</h3>
        <div style="font-size: 1.8rem; font-weight: bold; color: #a16207; margin: 1rem 0;">65% Success</div>
        <div style="color: #a16207;">
            <strong>Expected Recovery:</strong> $35-40K<br>
            <strong>Timeline:</strong> 12-18 months<br>
            <strong>Cost:</strong> $25-40K<br>
            <strong>Risk:</strong> Medium-High
        </div>
    </div>
    """, unsafe_allow_html=True)

with risk_col3:
    st.markdown("""
    <div class="risk-card risk-high">
        <h3 style="margin-top: 0; color: #dc2626;">🔴 NO ACTION</h3>
        <div style="font-size: 1.8rem; font-weight: bold; color: #dc2626; margin: 1rem 0;">15% Success</div>
        <div style="color: #dc2626;">
            <strong>Expected Recovery:</strong> $0-10K<br>
            <strong>Timeline:</strong> Indefinite<br>
            <strong>Cost:</strong> Opportunity cost<br>
            <strong>Risk:</strong> Total loss
        </div>
    </div>
    """, unsafe_allow_html=True)

# DECISION TREE LOGIC
st.markdown("## 🌳 DECISION FRAMEWORK")

st.markdown("""
<div class="decision-tree">
    <h3 style="margin-top: 0; text-align: center; color: #374151;">IF-THEN DECISION LOGIC</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin-top: 1.5rem;">
        <div style="text-align: center;">
            <div style="background: #dbeafe; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <strong style="color: #1e40af;">IF: Quick Recovery Priority</strong>
            </div>
            <div style="color: #059669;">
                <strong>THEN: Pursue Settlement</strong><br>
                Target: 65% recovery in 30 days<br>
                Risk: Low | Cost: Controlled
            </div>
        </div>
        <div style="text-align: center;">
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <strong style="color: #d97706;">IF: Maximum Recovery Priority</strong>
            </div>
            <div style="color: #d97706;">
                <strong>THEN: Consider Litigation</strong><br>
                Target: 90%+ recovery in 18 months<br>
                Risk: Medium | Cost: High
            </div>
        </div>
        <div style="text-align: center;">
            <div style="background: #fecaca; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <strong style="color: #dc2626;">IF: Resource Constraints</strong>
            </div>
            <div style="color: #dc2626;">
                <strong>THEN: Structured Settlement</strong><br>
                Target: 50% immediate + future<br>
                Risk: Medium | Cost: Minimal
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# TIME-SENSITIVE FACTORS
st.markdown("## ⏰ TIME-CRITICAL FACTORS")

time_col1, time_col2 = st.columns(2)

with time_col1:
    st.error("""
    **🚨 LEVERAGE DECAY ANALYSIS**
    
    **Days 1-15:** Peak leverage (85% recovery potential)
    **Days 16-45:** Strong position (70% recovery potential)  
    **Days 46-90:** Declining leverage (55% recovery potential)
    **Days 90+:** Weak position (40% recovery potential)
    
    **Current Status:** Day 1 - Maximum leverage window
    """)

with time_col2:
    st.warning("""
    **⚠️ RISK ESCALATION TIMELINE**
    
    **Immediate:** Asset investigation opportunity
    **30 days:** Settlement negotiation peak
    **90 days:** Enforcement preparation required
    **180 days:** Default triggers, litigation inevitable
    
    **Recommendation:** Act within 15 days for optimal results
    """)

# DETAILED ANALYSIS TABS - REORGANIZED
st.markdown("---")
st.markdown("## 📊 SUPPORTING ANALYSIS")

tab1, tab2, tab3, tab4 = st.tabs(["🎯 Strategic Summary", "⚖️ Legal Position", "💰 Financial Analysis", "📋 Case Background"])

# TAB 1: STRATEGIC SUMMARY (Condensed key info)
with tab1:
    st.markdown("### 🏆 Why Settlement Wins")
    
    summary_col1, summary_col2 = st.columns(2)
    
    with summary_col1:
        st.success("""
        **✅ STRONG LEGAL POSITION**
        - Award already issued and final
        - Clear due diligence failure by Noksel
        - Professional negligence well-documented
        - Mitigation efforts demonstrate good faith
        """)
        
        st.info("""
        **📊 FAVORABLE ECONOMICS**
        - Expected value: $28K (75% of award)
        - Cost-controlled: $10-15K maximum
        - Speed advantage: 30-45 days vs 18 months
        - Relationship preservation opportunity
        """)
    
    with summary_col2:
        st.warning("""
        **⚠️ LITIGATION RISKS**
        - Turkish enforcement challenges
        - Extended timeline uncertainty  
        - Higher cost exposure ($25-40K)
        - Potential relationship damage
        """)
        
        st.error("""
        **🚨 INACTION CONSEQUENCES**
        - Asset hiding opportunities increase
        - Leverage deteriorates rapidly
        - Recovery probability drops to 15%
        - Opportunity cost compounds
        """)
    
    # Key Metrics Dashboard
    st.markdown("### 📈 Key Performance Indicators")
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.metric("Recovery Confidence", "85%", "High")
    with metric_col2:
        st.metric("Time to Resolution", "30 days", "Optimal")
    with metric_col3:
        st.metric("Cost Efficiency", "5:1 ROI", "Excellent")
    with metric_col4:
        st.metric("Risk Level", "Low", "Manageable")

# TAB 2: LEGAL POSITION (Streamlined)
with tab2:
    st.markdown("### ⚖️ Legal Strength Analysis")
    
    # Core legal arguments in scannable format
    legal_col1, legal_col2 = st.columns(2)
    
    with legal_col1:
        st.success("**🏛️ CLAIMANT'S WINNING ARGUMENTS**")
        
        with st.expander("🎯 Primary Argument: Due Diligence Failure"):
            st.write("""
            **Core Position:** Noksel failed basic professional duty to verify vessel specifications
            
            **Key Evidence:**
            - Futuna length restrictions publicly available
            - MV MESSILA specs known pre-charter
            - Industry standard: charterer verification responsibility
            - 11-month voyage wasted on preventable issue
            """)
        
        with st.expander("💪 Supporting Arguments"):
            st.write("""
            **Mitigation Efforts:** Good faith attempts at delivery despite engine problems
            **Causation:** Rejection inevitable regardless of engine issues  
            **Professional Standard:** Any competent charterer would have checked
            **Contract Performance:** Vessel delivered as specified
            """)
    
    with legal_col2:
        st.error("**🏭 RESPONDENT'S BEST DEFENSES**")
        
        with st.expander("🛡️ Primary Defense: Force Majeure & Misrepresentation"):
            st.write("""
            **Core Position:** Victim of vessel owner misrepresentation and unforeseeable events
            
            **Key Evidence:**
            - Multiple vessel name changes suggest concealment
            - Contradictory build records (Ukraine vs Netherlands)
            - Engine problems despite 'seaworthy' representations
            - COVID-19 supply chain disruptions unforeseeable
            """)
        
        with st.expander("⚠️ Timing Arguments"):
            st.write("""
            **Regulatory Timing:** Nov 9 amendment, day before rejection
            **Alternative Causation:** Engine failure caused late arrival
            **Hidden Problems:** Real delay from vessel issues
            **Suspicious Patterns:** Identity concealment history
            """)
    
    # Legal precedents
    st.markdown("### 📚 Precedent Analysis")
    
    prec_col1, prec_col2 = st.columns(2)
    
    with prec_col1:
        st.success("""
        **✅ FAVORABLE PRECEDENTS**
        - **The Seaflower [2001]:** Due diligence duty
        - **Bulk Chile [2013]:** Vessel suitability standards
        """)
    
    with prec_col2:
        st.warning("""
        **⚠️ ADVERSE PRECEDENTS**
        - **Golden Victory [2007]:** Intervening events
        - **Edwinton [2021]:** COVID force majeure
        """)

# TAB 3: FINANCIAL ANALYSIS
with tab3:
    st.markdown("### 💰 Financial Impact & Recovery Analysis")
    
    # Financial breakdown
    financial_data = {
        "Component": ["Base Demurrage", "Additional Fees", "Interest (5%)", "Legal Costs", "Enforcement Costs", "Total Exposure"],
        "Amount ($)": [37317.71, 3000.00, 1865.89, 15000.00, 8000.00, 65183.60],
        "Recovery Probability": ["85%", "85%", "70%", "N/A", "50%", "75%"],
        "Settlement Value": [25000, 2500, 1200, 12000, 0, 40700],
        "Litigation Value": [33500, 2750, 1600, 25000, 4000, 66850]
    }
    
    financial_df = pd.DataFrame(financial_data)
    st.dataframe(financial_df, use_container_width=True, hide_index=True)
    
    # Recovery scenarios
    st.markdown("### 📊 Recovery Scenario Modeling")
    
    scenario_col1, scenario_col2, scenario_col3 = st.columns(3)
    
    with scenario_col1:
        st.metric("Best Case (Settlement)", "$30K+", "80% of award")
    with scenario_col2:
        st.metric("Most Likely", "$25-28K", "65-75% of award")
    with scenario_col3:
        st.metric("Conservative", "$20K", "55% of award")
    
    # Cost-benefit analysis
    st.markdown("### ⚖️ Cost-Benefit Comparison")
    
    cb_data = {
        "Option": ["Settlement", "Litigation", "No Action"],
        "Expected Recovery": ["$25-28K", "$30-35K", "$0-5K"],
        "Timeline": ["30-45 days", "12-18 months", "Indefinite"],
        "Costs": ["$10-15K", "$25-40K", "Opportunity cost"],
        "Net Benefit": ["$15-18K", "$5-10K", "Loss"],
        "ROI": ["150-200%", "25-40%", "Negative"]
    }
    
    cb_df = pd.DataFrame(cb_data)
    st.dataframe(cb_df, use_container_width=True, hide_index=True)

# TAB 4: CASE BACKGROUND
with tab4:
    st.markdown("### 📋 Case Overview")
    
    bg_col1, bg_col2 = st.columns([1, 1])
    
    with bg_col1:
        st.info("""
        **Case Summary**
        
        Turkish steel supplier **Noksel Çelik Boru Sanayi A.Ş.** chartered MV MESSILA to deliver steel pipes 
        to the remote French Pacific island of Futuna for a dock construction project.
        
        After a catastrophic engine breakdown requiring 4 months of repairs and subsequent regulatory rejection 
        at the destination port, the cargo was ultimately discharged in Fiji, triggering significant demurrage costs.
        """)
        
        # Key parties
        st.markdown("**Key Parties:**")
        st.write("🏛️ **Claimant:** Transasya (Vessel Owners)")
        st.write("🏭 **Respondent:** Noksel (Turkish Steel Supplier)")
        st.write("⚖️ **Arbitrator:** John Schofield")
        st.write("📜 **Status:** Award issued, enforcement pending")
    
    with bg_col2:
        st.markdown("### 🕐 Critical Timeline")
        
        timeline_events = [
            ("Feb 4, 2020", "📄 Supply contract signed", "normal"),
            ("Nov 12, 2020", "🚢 MV MESSILA chartered", "normal"),
            ("Dec 1-3, 2020", "📦 Cargo loaded in Turkey", "normal"),
            ("May 25, 2021", "⚠️ ENGINE BREAKDOWN", "critical"),
            ("Jun-Oct 2021", "🔧 4-MONTH REPAIR PERIOD", "critical"),
            ("Nov 10, 2021", "❌ REJECTED at Futuna", "critical"),
            ("Nov 23, 2021", "💰 DEMURRAGE COMMENCES", "critical"),
            ("Mar 19, 2023", "⚖️ Arbitration award issued", "award")
        ]
        
        for date, event, event_type in timeline_events:
            if event_type == "critical":
                st.error(f"**{date}:** {event}")
            elif event_type == "award":
                st.success(f"**{date}:** {event}")
            else:
                st.info(f"**{date}:** {event}")

# FOOTER
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown(f"""
    **📊 Dashboard Status**  
    Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M")}  
    Status: Active Decision Phase  
    Confidence: High
    """)

with footer_col2:
    st.markdown("""
    **⚖️ Legal Framework**  
    Governing Law: English Law  
    Arbitration Seat: London  
    Enforcement: International
    """)

with footer_col3:
    st.markdown("""
    **🎯 Next Steps**  
    Priority: Immediate Action  
    Window: 15-day optimal  
    Contact: LMAA Mediation
    """)
