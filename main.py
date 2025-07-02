import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Caselens",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    
    .logo-icon {
        background-color: #4f46e5;
        color: white;
        padding: 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 16px;
    }
    
    .case-title {
        font-size: 18px;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 8px;
    }
    
    .tag {
        display: inline-block;
        font-size: 11px;
        font-weight: 500;
        padding: 3px 8px;
        margin: 2px 4px 2px 0;
        border-radius: 12px;
        background-color: #f1f5f9;
        color: #475569;
        border: 1px solid #e2e8f0;
    }
    
    .tag-date {
        background-color: #eff6ff;
        color: #1d4ed8;
        border-color: #dbeafe;
    }
    
    .tag-outcome-dismissed {
        background-color: #fef2f2;
        color: #991b1b;
        border-color: #fecaca;
    }
    
    .tag-sport-football {
        background-color: #f0fdf4;
        color: #166534;
        border-color: #bbf7d0;
    }
    
    .case-meta {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 12px;
    }
    
    .section-content {
        background-color: #f8fafc;
        padding: 12px;
        border-radius: 6px;
        border-left: 3px solid #4f46e5;
        margin: 8px 0;
    }
    
    .results-summary {
        background-color: #d1fae5;
        border: 1px solid #a7f3d0;
        border-radius: 6px;
        padding: 12px 16px;
        margin: 16px 0;
        color: #065f46;
    }
    
    .stSelectbox > div > div {
        background-color: #f8fafc;
    }
    
    .sidebar-section {
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Logo
    st.markdown("""
    <div class="main-header">
        <span class="logo-icon">C</span>
        <h2 style="margin: 0; color: #1f2937;">caselens</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### Navigation")
    nav_option = st.radio(
        "",
        ["👤 Admin", "📄 Documents", "🔍 Search"],
        index=2,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Search Options
    st.markdown("### Search Options")
    
    with st.container():
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("**Max Results**")
        max_results = st.number_input("", min_value=1, max_value=100, value=20, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("**Similarity Threshold**")
        similarity = st.slider("", min_value=0.0, max_value=1.0, value=0.55, step=0.01, label_visibility="collapsed")
        st.write(f"Current value: {similarity}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    show_similarity = st.checkbox("Show Similarity Scores ⓘ")

# Main content
st.markdown("### Enter your search query")
search_query = st.text_input("", value="just cause", placeholder="Enter your search query", label_visibility="collapsed")

if search_query:
    # Search results summary
    st.markdown("""
    <div class="results-summary">
        <strong>✓ Found 4 results</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("Found 4 relevant passages in 2 decisions")
    
    # Case results
    with st.container():
        # Case 1
        with st.expander("**CAS 2013/A/3165 - CAS 2013/A/3165**", expanded=True):
            # Tags
            st.markdown("""
            <div>
                <span class="tag tag-date">2014-01-14</span>
                <span class="tag">Appeal Arbitration</span>
                <span class="tag">Contract</span>
                <span class="tag">Award</span>
                <span class="tag tag-outcome-dismissed">Dismissed</span>
                <span class="tag tag-sport-football">Football</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Case metadata
            st.markdown("""
            <div class="case-meta">
                <strong>Appellants:</strong> FC Volyn | <strong>Respondents:</strong> Issa Ndoye | <strong>President:</strong> Petros Mavroidis | <strong>Arbitrator 1:</strong> Geraint Jones | <strong>Arbitrator 2:</strong> Raymond Hack
            </div>
            """, unsafe_allow_html=True)
            
            # Summary section
            st.markdown("**Summary:**")
            st.markdown("""
            <div class="section-content">
                The case involves a contractual dispute between FC Volyn, a Ukrainian football club, and Issa Ndoye, a Senegalese footballer. 
                Ndoye terminated his employment with FC Volyn in June 2011, claiming unpaid salary and contract breach, subsequently bringing a 
                claim before FIFA's Dispute Resolution Chamber (DRC), which ruled in his favor, ordering the club to pay outstanding remuneration 
                and compensation. FC Volyn appealed to the CAS, arguing that Ndoye had no just cause due to his alleged breaches (mainly late 
                returns to training), while Ndoye countered that non-payment constituted just cause and sought increased compensation. Both parties 
                debated applicable law and timing of appeals/counterclaims.
            </div>
            """, unsafe_allow_html=True)
            
            # Court Reasoning section
            st.markdown("**Court Reasoning:**")
            st.markdown("""
            <div class="section-content">
                The CAS panel found that FIFA regulations take precedence over national law due to the contract's terms and parties' submission 
                to FIFA/CAS jurisdiction. The Club's repeated failure to pay Ndoye's salary for over three months was a substantial breach, 
                constituting just cause for contract termination. Alleged late returns by Ndoye did not nullify this breach, and there was no 
                evidence he agreed to delay payment. Counterclaims by respondents were inadmissible per CAS procedural rules. The compensation 
                set by the FIFA DRC was appropriate.
            </div>
            """, unsafe_allow_html=True)
            
            if show_similarity:
                st.markdown("**Similarity Score:** 0.87")

# Footer with some additional info
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("*Caselens Legal Research Platform*")

# Sample data for potential filtering/sorting
if st.sidebar.button("Show Advanced Filters"):
    with st.sidebar:
        st.markdown("### Advanced Filters")
        
        date_range = st.date_input(
            "Date Range",
            value=[datetime(2010, 1, 1), datetime(2024, 12, 31)],
            key="date_filter"
        )
        
        sport_filter = st.multiselect(
            "Sport",
            ["Football", "Basketball", "Tennis", "Swimming", "Athletics"],
            default=["Football"]
        )
        
        outcome_filter = st.multiselect(
            "Outcome",
            ["Dismissed", "Upheld", "Partially Upheld", "Settled"],
            default=["Dismissed"]
        )
        
        procedure_filter = st.selectbox(
            "Procedure Type",
            ["All", "Appeal Arbitration", "Ordinary Arbitration", "Fast-Track"]
        )
