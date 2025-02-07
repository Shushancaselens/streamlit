import streamlit as st
import pandas as pd
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for improved styling
st.markdown("""
    <style>
    /* Main container */
    .main {
        background-color: #f8fafc;
    }
    
    /* Cards */
    div[data-testid="stVerticalBlock"] > div {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #1e293b;
        font-weight: 600;
    }
    
    /* Status badges */
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .status-success { 
        background-color: #dcfce7;
        color: #166534;
    }
    .status-error { 
        background-color: #fee2e2;
        color: #991b1b;
    }
    .status-warning {
        background-color: #fef3c7;
        color: #92400e;
    }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        height: 0.5rem !important;
        border-radius: 9999px !important;
    }
    
    /* Tables */
    .styled-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 1rem 0;
    }
    .styled-table th {
        background-color: #f8fafc;
        padding: 0.75rem;
        text-align: left;
        font-weight: 600;
        color: #475569;
        border-bottom: 2px solid #e2e8f0;
    }
    .styled-table td {
        padding: 0.75rem;
        border-bottom: 1px solid #e2e8f0;
        color: #1e293b;
    }
    .styled-table tr:hover {
        background-color: #f8fafc;
    }
    
    /* Sidebar improvements */
    section[data-testid="stSidebar"] > div {
        background-color: #1e293b;
        padding: 2rem 1rem;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: #f8fafc;
    }
    
    /* Metrics */
    [data-testid="metric-container"] {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 0.375rem;
        padding: 0.5rem 1rem;
        background-color: #2563eb;
        color: white;
        font-weight: 500;
    }
    .stButton > button:hover {
        background-color: #1d4ed8;
    }
    
    /* File uploader */
    .stFileUploader {
        padding: 1rem;
        border: 2px dashed #e2e8f0;
        border-radius: 0.5rem;
        background-color: #f8fafc;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = 'overview'
if 'total_penalties' not in st.session_state:
    st.session_state.total_penalties = 10

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h1 style='color: #f8fafc; font-size: 1.5rem; margin-bottom: 0.5rem;'>
                Jessup Checker
            </h1>
            <p style='color: #cbd5e1; font-size: 0.875rem;'>
                2025 Edition
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Memorial Type Selector
    memorial_type = st.selectbox(
        "Memorial Type",
        ["Applicant", "Respondent"],
        index=0,
        key="memorial_type"
    )
    
    # Total Penalties Metric
    st.metric(
        "Total Penalties",
        f"{st.session_state.total_penalties} points",
        delta="-2 from previous check",
        delta_color="inverse"
    )
    
    # Navigation
    st.markdown("### Navigation")
    tabs = {
        'overview': '📊 Overview',
        'document': '📄 Document Check',
        'word_count': '📏 Word Count',
        'citations': '📚 Citations',
        'format': '🎨 Formatting',
        'plagiarism': '⚠️ Plagiarism'
    }
    
    for key, label in tabs.items():
        if st.button(label, key=f"btn_{key}"):
            st.session_state.selected_tab = key

# Main content
st.title("Jessup Memorial Penalty Checker")

# Overview Tab
if st.session_state.selected_tab == 'overview':
    # Summary metrics in a row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Document Score", "92%", "+5%")
    with col2:
        st.metric("Word Count", "9,424/9,500", "76 words remaining")
    with col3:
        st.metric("Citation Errors", "3", "-2")
    
    # Penalty Breakdown
    st.markdown("### Penalty Breakdown")
    penalties_df = pd.DataFrame([
        {"Rule": "5.5", "Description": "Missing Prayer for Relief", "Points": 4, "Status": "⚠️ Review Needed"},
        {"Rule": "5.17", "Description": "Non-Permitted Abbreviations", "Points": 3, "Status": "❌ Failed"},
        {"Rule": "5.13", "Description": "Improper Citations", "Points": 3, "Status": "✅ Passed"}
    ])
    st.dataframe(
        penalties_df,
        column_config={
            "Rule": st.column_config.TextColumn("Rule", help="Jessup Rule Reference"),
            "Description": "Description",
            "Points": st.column_config.NumberColumn("Points", format="%d pts"),
            "Status": st.column_config.TextColumn("Status", width="medium")
        },
        hide_index=True,
        use_container_width=True
    )

    # Word Count Analysis
    st.markdown("### Word Count Analysis")
    word_counts = {
        "Statement of Facts": {"current": 1196, "limit": 1200},
        "Summary of Pleadings": {"current": 642, "limit": 700},
        "Pleadings": {"current": 9424, "limit": 9500},
        "Prayer for Relief": {"current": 0, "limit": 200}
    }
    
    for section, counts in word_counts.items():
        percentage = (counts["current"] / counts["limit"]) * 100
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{section}**")
            st.progress(min(percentage / 100, 1.0))
        
        with col2:
            st.markdown(f"""
                <div style='text-align: right;'>
                    <span style='color: {"#dc2626" if percentage > 100 else "#2563eb"}; font-weight: 500;'>
                        {counts["current"]} / {counts["limit"]}
                    </span>
                </div>
            """, unsafe_allow_html=True)

# Document Check Tab
elif st.session_state.selected_tab == 'document':
    st.markdown("### Document Analysis")
    uploaded_file = st.file_uploader("Upload your memorial", type=['docx', 'pdf'])
    
    if uploaded_file:
        st.success("Document uploaded successfully!")
        
        # Document Info
        st.markdown("#### Document Information")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **File Name**: example_memorial.docx")
            st.markdown("- **File Size**: 2.3 MB")
            st.markdown("- **Last Modified**: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
        with col2:
            st.markdown("- **Document Type**: DOCX")
            st.markdown("- **Pages**: 42")
            st.markdown("- **Total Words**: 12,463")
        
        # Status Checks
        checks = {
            "Cover Page": True,
            "Table of Contents": True,
            "Index of Authorities": True,
            "Statement of Jurisdiction": True,
            "Statement of Facts": True,
            "Prayer for Relief": False
        }
        
        st.markdown("#### Document Structure")
        cols = st.columns(3)
        for i, (item, status) in enumerate(checks.items()):
            with cols[i % 3]:
                st.markdown(f"""
                    <div style='padding: 0.5rem; background-color: {"#dcfce7" if status else "#fee2e2"}; 
                         border-radius: 0.375rem; margin-bottom: 0.5rem;'>
                        <span style='color: {"#166534" if status else "#991b1b"}'>
                            {"✓" if status else "×"} {item}
                        </span>
                    </div>
                """, unsafe_allow_html=True)

# Add more tabs as needed
else:
    st.info(f"Selected tab: {st.session_state.selected_tab}")
    st.markdown("Content for this section is under development.")
