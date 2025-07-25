import streamlit as st
import pandas as pd
from datetime import datetime
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="MV MESSILA Strategic Decision Dashboard",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visual hierarchy
st.markdown("""
<style>
    .big-metric {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
    }
    .decision-card {
        border: 2px solid;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
    }
    .go-card { border-color: #10b981; background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); }
    .caution-card { border-color: #f59e0b; background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); }
    .stop-card { border-color: #ef4444; background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%); }
    
    .key-insight {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: white;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .risk-high { background-color: #fee2e2; border-left: 4px solid #ef4444; padding: 10px; }
    .risk-medium { background-color: #fef3c7; border-left: 4px solid #f59e0b; padding: 10px; }
    .risk-low { background-color: #dcfce7; border-left: 4px solid #10b981; padding: 10px; }
</style>
""", unsafe_allow_html=True)

# Sidebar for user context
with st.sidebar:
    st.markdown("### 👤 Your Role")
    user_role = st.selectbox("I am a:", [
        "Executive (need decision)",
        "Legal Counsel (need strategy)", 
        "Financial Analyst (need numbers)",
        "Risk Manager (need assessment)"
    ])
    
    st.markdown("### ⏰ Timeline Pressure")
    urgency = st.select_slider("How urgent is this decision?", 
                              ["Low", "Medium", "High", "Critical"], 
                              value="High")
    
    st.markdown("### 💰 Risk Tolerance")
    risk_tolerance = st.select_slider("Risk appetite for this case:", 
                                     ["Conservative", "Moderate", "Aggressive"], 
                                     value="Moderate")

# EXECUTIVE DECISION LAYER (Always visible)
st.markdown("# ⚖️ MV MESSILA: Strategic Decision Required")

# The ONE key decision
decision_col1, decision_col2, decision_col3 = st.columns([1, 2, 1])
with decision_col2:
    st.markdown('<div class="big-metric" style="color: #1e293b;">$37,317</div>', unsafe_allow_html=True)
    st.markdown("**SETTLEMENT vs LITIGATION DECISION**")
    st.markdown("*Noksel owes demurrage • Award issued • 180 days to collect*")

# Clear recommendation based on user inputs
if urgency in ["High", "Critical"] and risk_tolerance != "Aggressive":
    recommendation = "SETTLE"
    rec_color = "go"
    rec_confidence = "85%"
    rec_timeline = "15-30 days"
    rec_amount = "$24-27K"
elif risk_tolerance == "Aggressive":
    recommendation = "LITIGATE"
    rec_color = "caution"
    rec_confidence = "65%"
    rec_timeline = "6-12 months"
    rec_amount = "$30-37K"
else:
    recommendation = "NEGOTIATE"
    rec_color = "caution"
    rec_confidence = "75%"
    rec_timeline = "45-60 days"
    rec_amount = "$20-30K"

st.markdown(f"""
<div class="decision-card {rec_color}-card">
    <h2>RECOMMENDED ACTION: {recommendation}</h2>
    <p><strong>Confidence:</strong> {rec_confidence} | <strong>Timeline:</strong> {rec_timeline} | <strong>Expected Recovery:</strong> {rec_amount}</p>
</div>
""", unsafe_allow_html=True)

# Key insight based on role
if user_role == "Executive (need decision)":
    insight = "💡 **Bottom Line:** Noksel failed basic due diligence checking vessel specs before chartering. Engine problems are red herring - vessel would have been rejected anyway. Settlement gets money faster with less risk."
elif user_role == "Legal Counsel (need strategy)":
    insight = "💡 **Legal Edge:** Due diligence breach is clear liability. Respondent's force majeure defense weak on causation. Precedents favor claimant on vessel suitability standards."
elif user_role == "Financial Analyst (need numbers)":
    insight = "💡 **Financial Reality:** $37K award minus $15K costs = $22K net if litigated. Settlement at 65% = $24K with lower costs. NPV favors settlement even with time value."
else:  # Risk Manager
    insight = "💡 **Risk Assessment:** Turkish enforcement uncertain, asset location unknown, debtor's financial condition declining. Collection risk increases significantly after day 90."

st.markdown(f'<div class="key-insight">{insight}</div>', unsafe_allow_html=True)

# Progressive disclosure based on role
if user_role == "Executive (need decision)":
    # EXECUTIVE VIEW - High level only
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Success Probability")
        prob_data = pd.DataFrame({
            'Outcome': ['Settlement Success', 'Litigation Win', 'Collection Risk', 'Appeal Risk'],
            'Probability': [0.85, 0.75, 0.35, 0.15],
            'Impact': ['Medium', 'High', 'High', 'Medium']
        })
        fig = px.bar(prob_data, x='Outcome', y='Probability', 
                    color='Impact', color_discrete_map={'Medium': '#fbbf24', 'High': '#ef4444'})
        fig.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### ⏱️ Time vs Recovery")
        timeline_data = pd.DataFrame({
            'Days': [30, 60, 90, 180, 365],
            'Settlement %': [85, 75, 65, 50, 30],
            'Litigation %': [20, 35, 45, 65, 75]
        })
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=timeline_data['Days'], y=timeline_data['Settlement %'], 
                               name='Settlement', line=dict(color='#10b981', width=3)))
        fig.add_trace(go.Scatter(x=timeline_data['Days'], y=timeline_data['Litigation %'], 
                               name='Litigation', line=dict(color='#ef4444', width=3)))
        fig.update_layout(height=300, xaxis_title="Days", yaxis_title="Recovery Probability %")
        st.plotly_chart(fig, use_container_width=True)
    
    # Executive-level risks only
    st.markdown("#### ⚠️ Key Risks to Monitor")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="risk-high"><strong>Asset Flight Risk</strong><br/>Noksel may hide assets if litigation drags</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="risk-medium"><strong>Enforcement Risk</strong><br/>Turkish courts may not recognize UK award</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="risk-low"><strong>Precedent Value</strong><br/>Strong case could set favorable precedent</div>', unsafe_allow_html=True)

elif user_role == "Legal Counsel (need strategy)":
    # LEGAL VIEW - Strategy focused
    legal_tab1, legal_tab2, legal_tab3 = st.tabs(["🎯 Legal Strategy", "📚 Case Analysis", "⚖️ Precedents"])
    
    with legal_tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Our Strongest Arguments")
            st.success("**Due Diligence Breach** - Noksel failed to verify basic vessel specifications against publicly available port regulations")
            st.success("**Causation Clear** - Rejection was inevitable regardless of engine problems")
            st.success("**Industry Standard** - Charterer responsible for destination compliance verification")
            st.success("**Mitigation Efforts** - We immediately found alternative discharge port")
        
        with col2:
            st.markdown("#### Their Best Defenses")
            st.warning("**Force Majeure** - Engine failure + COVID supply chain disruption")
            st.warning("**Vessel Misrepresentation** - Multiple name changes suggest concealment")
            st.warning("**Regulatory Timing** - Futuna rules changed day before rejection")
            st.warning("**Seaworthiness Issues** - 4-month repairs contradict vessel condition claims")
        
        st.markdown("#### Recommended Legal Strategy")
        st.info("""
        **Phase 1:** Demand letter emphasizing due diligence breach (Week 1)
        **Phase 2:** LMAA mediation with settlement authority 60-70% (Weeks 2-4)  
        **Phase 3:** If no settlement, immediate enforcement preparation (Week 5)
        **Fallback:** Turkish court recognition proceedings if needed (Month 2+)
        """)
    
    with legal_tab2:
        # Detailed case analysis for legal team
        st.markdown("#### Case Strengths vs Weaknesses")
        strengths_weaknesses = pd.DataFrame({
            'Our Position': [
                'Arbitration award already issued',
                'Clear due diligence standard breach', 
                'Vessel rejection documented',
                'Mitigation efforts demonstrated'
            ],
            'Strength': ['Very Strong', 'Strong', 'Strong', 'Medium'],
            'Their Counter': [
                'Challenge enforcement jurisdiction',
                'Force majeure defense',
                'Vessel misrepresentation claim', 
                'Damages too remote'
            ],
            'Threat Level': ['Low', 'Medium', 'Medium', 'Low']
        })
        st.dataframe(strengths_weaknesses, hide_index=True, use_container_width=True)
    
    with legal_tab3:
        st.markdown("#### Relevant Precedents")
        precedents = [
            ("The Seaflower [2001] EWCA", "Due diligence duty for charterers", "Favorable - establishes our standard"),
            ("Bulk Chile [2013] EWHC", "Vessel suitability verification", "Favorable - supports our position"),
            ("Golden Victory [2007] HL", "Intervening events doctrine", "Neutral - could cut both ways"),
            ("Edwinton [2021] EWHC", "COVID force majeure scope", "Adverse - broader force majeure accepted")
        ]
        for case, principle, assessment in precedents:
            if "Favorable" in assessment:
                st.success(f"**{case}** - {principle}\n\n*{assessment}*")
            elif "Adverse" in assessment:
                st.error(f"**{case}** - {principle}\n\n*{assessment}*")
            else:
                st.warning(f"**{case}** - {principle}\n\n*{assessment}*")

elif user_role == "Financial Analyst (need numbers)":
    # FINANCIAL VIEW - Numbers focused
    fin_tab1, fin_tab2 = st.tabs(["💰 Financial Model", "📈 Scenario Analysis"])
    
    with fin_tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Award Principal", "$37,318", "Base amount")
            st.metric("Accrued Interest", "$3,750", "5% annually")
            st.metric("Legal Fees", "$3,000", "Arbitration costs")
        
        with col2:
            st.metric("Gross Claim", "$44,068", "Total recoverable")
            st.metric("Collection Costs", "$15,000", "Estimated")
            st.metric("Net Recovery (65%)", "$24,000", "Settlement target")
        
        with col3:
            st.metric("NPV Settlement", "$21,600", "30-day timeline")
            st.metric("NPV Litigation", "$19,200", "12-month timeline")
            st.metric("Risk-Adjusted NPV", "$18,000", "Including collection risk")
    
    with fin_tab2:
        # Monte Carlo-style scenario analysis
        scenario_data = pd.DataFrame({
            'Scenario': ['Best Case', 'Most Likely', 'Worst Case'],
            'Settlement': ['$30K (80%)', '$24K (65%)', '$15K (40%)'],
            'Litigation': ['$37K (90%)', '$28K (75%)', '$5K (15%)'],
            'Probability': ['15%', '70%', '15%']
        })
        st.dataframe(scenario_data, hide_index=True, use_container_width=True)
        
        # Cash flow timing
        st.markdown("#### Cash Flow Timing")
        cash_flow_data = pd.DataFrame({
            'Month': ['Month 1', 'Month 3', 'Month 6', 'Month 12'],
            'Settlement Path': [24000, 0, 0, 0],
            'Litigation Path': [0, 0, 0, 28000]
        })
        fig = px.bar(cash_flow_data, x='Month', y=['Settlement Path', 'Litigation Path'], 
                    title="Expected Cash Flow by Strategy")
        st.plotly_chart(fig, use_container_width=True)

else:  # Risk Manager
    # RISK VIEW - Risk assessment focused
    risk_tab1, risk_tab2 = st.tabs(["🎯 Risk Matrix", "📊 Risk Timeline"])
    
    with risk_tab1:
        # Risk heat map
        risks_data = pd.DataFrame({
            'Risk': ['Asset Flight', 'Non-Payment', 'Enforcement Failure', 'Appeal Filed', 'Countersuit'],
            'Probability': [0.4, 0.3, 0.25, 0.2, 0.15],
            'Impact': [0.8, 0.9, 0.7, 0.6, 0.4],
            'Risk Score': [0.32, 0.27, 0.175, 0.12, 0.06]
        })
        fig = px.scatter(risks_data, x='Probability', y='Impact', size='Risk Score', 
                        hover_name='Risk', title="Risk Assessment Matrix")
        st.plotly_chart(fig, use_container_width=True)
    
    with risk_tab2:
        st.markdown("#### Risk Evolution Over Time")
        st.markdown('<div class="risk-high"><strong>Days 1-30:</strong> Asset discovery window - act fast</div>', unsafe_allow_html=True)
        st.markdown('<div class="risk-medium"><strong>Days 30-90:</strong> Settlement sweet spot - maximum leverage</div>', unsafe_allow_html=True)
        st.markdown('<div class="risk-high"><strong>Days 90-180:</strong> Enforcement preparation - rising costs</div>', unsafe_allow_html=True)
        st.markdown('<div class="risk-high"><strong>Days 180+:</strong> Default scenario - enforcement becomes primary option</div>', unsafe_allow_html=True)

# Next Steps - Always visible regardless of role
st.divider()
st.markdown("## 🎯 Immediate Next Steps")

next_steps_col1, next_steps_col2, next_steps_col3 = st.columns(3)

with next_steps_col1:
    st.markdown("**📅 Week 1**")
    st.write("• Send formal demand letter")
    st.write("• Conduct asset investigation") 
    st.write("• Prepare settlement authority")

with next_steps_col2:
    st.markdown("**📅 Week 2-3**")
    st.write("• Initiate LMAA mediation")
    st.write("• Negotiate settlement terms")
    st.write("• Prepare enforcement backup")

with next_steps_col3:
    st.markdown("**📅 Week 4+**")
    st.write("• Execute chosen strategy")
    st.write("• Monitor compliance")
    st.write("• Escalate if necessary")

# Decision buttons
if st.button("📋 APPROVE SETTLEMENT STRATEGY", type="primary"):
    st.success("✅ Settlement strategy approved. Initiating demand letter and mediation process.")

if st.button("⚠️ REQUEST MORE ANALYSIS"):
    st.info("📊 Additional analysis requested. Legal team will provide supplementary brief within 24 hours.")

# Footer
st.markdown("---")
st.caption(f"Dashboard generated for {user_role} | Risk tolerance: {risk_tolerance} | Urgency: {urgency}")
