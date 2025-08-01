import streamlit as st
import pandas as pd
from datetime import datetime, date

# Page configuration
st.set_page_config(
    page_title="CaseLens",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    
    .case-date {
        color: #1f77b4;
        font-weight: bold;
    }
    
    .definitions-section {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .source-section {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .highlight-text {
        background-color: #d4edda;
        padding: 0.5rem;
        border-radius: 0.3rem;
        border-left: 3px solid #28a745;
    }
    
    .sidebar-section {
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🏛️ caselens")
    
    # Navigation
    st.markdown("### Navigation")
    nav_options = ["👤 Profile", "📅 Events", "📄 Documents"]
    selected_nav = st.radio("", nav_options, index=1)
    
    st.markdown("---")
    
    # Case Filter
    st.markdown("### 🔍 Case Filter")
    st.markdown("**Select Case**")
    case_filter = st.selectbox("", ["All Events", "Active Cases", "Closed Cases", "Pending Review"], index=0)
    
    st.markdown("---")
    
    # Document Type Filter
    st.markdown("### 📋 Document Type Filter")
    st.markdown("**Select Document Types**")
    doc_type_filter = st.selectbox("", ["Choose an option", "Procedural", "Administrative", "Legal Opinion", "Evidence"], index=0)
    
    st.markdown("---")
    
    # Entity Name Filter
    st.markdown("### 🏷️ Entity Name Filter")
    st.markdown("**Select Entity Names**")
    entity_filter = st.selectbox("", ["Choose an option", "High Commissioner", "Government Officials", "Organizations"], index=0)
    
    st.markdown("---")
    
    # Date Range
    st.markdown("### 📅 Date Range")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Start Date**")
        start_date = st.date_input("", value=date(1926, 12, 17), label_visibility="collapsed")
    
    with col2:
        st.markdown("**End Date**")
        end_date = st.date_input("", value=date(2025, 1, 1), label_visibility="collapsed")
    
    st.markdown("---")
    
    # Submissions Filter
    st.markdown("### 📤 Submissions Filter")

# Main content area
st.markdown("""
<div class="main-header">
    <span class="case-date">2006-06-20</span> | On 20 June 06, <strong>Yves Dassonville</strong>, as <strong>High Commissioner of the Republic in New Caledonia</strong>, repealed and replaced order no. 2006-2/AEM of 20 June 2006 with a new order regulating vessel access to the <strong>Leava</strong> wharf in <strong>Futuna</strong>. | <span style="color: #28a745;">1 Source</span>
</div>
""", unsafe_allow_html=True)

# Case details table
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Proceedings:**")
    st.markdown('<span style="color: #6f42c1;">Astute CASE N 28459_v2</span>', unsafe_allow_html=True)

with col2:
    st.markdown("**Addressed by:**")
    st.markdown("None")

with col3:
    st.markdown("**Document Type:**")
    st.markdown('<span style="color: #6f42c1;">procedural</span>', unsafe_allow_html=True)

# Definitions section
st.markdown("""
<div class="definitions-section">
    <h3>Definitions</h3>
</div>
""", unsafe_allow_html=True)

# Create definitions table
definitions_data = {
    "Term": ["High Commissioner of th...", "New Caledonia", "Futuna", "Leava", "Yves Dassonville"],
    "Type": ["organization", "location", "location", "location", "person"],
    "Definition": [
        "French governmental authority in New Caledonia overseeing administrative and legal matters, including maritime regulation.",
        "French overseas territory in the South Pacific, the jurisdiction of the High Commissioner.",
        "Island in the French overseas collectivity of Wallis and Futuna; location of Leava wharf.",
        "Village and port on the island of Futuna, site of the regulated wharf.",
        "High Commissioner of the Republic in New Caledonia at the time of the order's issuance."
    ]
}

df_definitions = pd.DataFrame(definitions_data)
st.dataframe(df_definitions, use_container_width=True, hide_index=True)

# Source section
st.markdown("""
<div class="source-section">
    <h3>Source(s)</h3>
    <h4>📄 Appendix 4 Bis - ENG.pdf</h4>
    
    <p><strong>Summary:</strong> This is an official order (arrêté) dated 16 June 2009, issued by the High Commissioner of the Republic in New Caledonia, regulating the access of vessels to the Leava wharf in Futuna. It establishes procedural requirements for advance notification, operational limitations based on vessel size and equipment, and prescribes authorized procedures for docking, with penalties for violations and references to previous law. The order is signed by Yves Dassonville, High Commissioner, and replaces an earlier order from June 2006.</p>
    
    <p><strong>Citation:</strong> Appendix 4 Bis - ENG.pdf, page 2.</p>
    
    <div class="highlight-text">
        <strong>Excerpt:</strong> This order repeals and replaces order no. 2006-2/AEM dij 20 June 2006.
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("*CaseLens Legal Case Management System*")
