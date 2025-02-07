import streamlit as st
import pandas as pd
from pathlib import Path

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initial data setup [same as before]
initial_data = {
    "memorialType": "Applicant",
    "coverPage": {
        "Team Number": {"present": True, "found": "349A"},
        "Court Name": {"present": True, "found": "International Court of Justice"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
        "Memorial Type": {"present": True, "found": "Memorial for the Applicant"}
    },
    "memorialParts": {
        "Cover Page": True,
        "Table of Contents": True,
        "Index of Authorities": True,
        "Statement of Jurisdiction": True,
        "Statement of Facts": True,
        "Summary of Pleadings": True,
        "Pleadings": True,
        "Prayer for Relief": False
    },
    "wordCounts": {
        "Statement of Facts": {"count": 1196, "limit": 1200},
        "Summary of Pleadings": {"count": 642, "limit": 700},
        "Pleadings": {"count": 9424, "limit": 9500},
        "Prayer for Relief": {"count": 0, "limit": 200}
    },
    "abbreviations": {
        "ISECR": {"count": 2, "sections": ["Pleadings"]},
        "ICCPED": {"count": 1, sections: ["Summary of Pleadings"]},
        "ICC": {"count": 1, "sections": ["Pleadings"]},
        "LOSC": {"count": 1, "sections": ["Pleadings"]},
        "AFRC": {"count": 1, "sections": ["Pleadings"]}
    },
    "media": [{"section": "Cover Page", "index": 6, "text": "----media/image1.png----"}]
}

# Enhanced CSS for better UI
st.markdown("""
<style>
    /* Global styles */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Main container styles */
    .main-container {
        background-color: white;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }
    
    /* Section headers */
    .section-header {
        color: #1a1f36;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    /* Status indicators */
    .status-success {
        color: #10b981;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .status-error {
        color: #ef4444;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .status-warning {
        color: #f59e0b;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Cards */
    .card {
        background-color: white;
        border-radius: 0.75rem;
        padding: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        border: 1px solid #f0f0f0;
    }
    
    /* Progress bars */
    .progress-container {
        background-color: #f9fafb;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    
    .progress-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    
    /* Tables */
    .custom-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 1rem 0;
    }
    
    .custom-table th {
        background-color: #f9fafb;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .custom-table td {
        padding: 1rem;
        border-bottom: 1px solid #f0f0f0;
    }
    
    /* Sidebar enhancements */
    .sidebar-section {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Navigation items */
    .nav-item {
        display: flex;
        align-items: center;
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .nav-item:hover {
        background-color: #f9fafb;
    }
    
    /* Custom button styles */
    .custom-button {
        background-color: #3b82f6;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        border: none;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .custom-button:hover {
        background-color: #2563eb;
    }
</style>
""", unsafe_allow_html=True)

def create_section_header(title, icon="", subtitle=""):
    """Create a consistent section header"""
    return st.markdown(f"""
        <div class="section-header">
            {icon} {title}
            {f'<span style="font-size: 0.8rem; color: #6b7280; margin-left: 0.5rem;">({subtitle})</span>' if subtitle else ''}
        </div>
    """, unsafe_allow_html=True)

def create_status_indicator(status, text):
    """Create a consistent status indicator"""
    icons = {
        "success": "✅",
        "error": "❌",
        "warning": "⚠️"
    }
    return f'<div class="status-{status}">{icons[status]} {text}</div>'

def create_progress_bar(count, limit):
    """Create an enhanced progress bar"""
    percentage = (count / limit) * 100
    status = "success"
    if percentage > 90:
        status = "warning"
    if percentage > 100:
        status = "error"
    
    st.markdown(f"""
        <div class="progress-container">
            <div class="progress-header">
                <span>{count} words</span>
                <span class="status-{status}">{percentage:.1f}%</span>
            </div>
            <div style="width: 100%; background-color: #e5e7eb; height: 0.5rem; border-radius: 0.25rem;">
                <div style="width: {min(percentage, 100)}%; height: 100%; border-radius: 0.25rem; 
                     background-color: {{'success': '#10b981', 'warning': '#f59e0b', 'error': '#ef4444'}[status]};">
                </div>
            </div>
            <div style="text-align: right; font-size: 0.8rem; color: #6b7280; margin-top: 0.25rem;">
                Limit: {limit}
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div class="sidebar-section">
                <h1 style="margin-bottom: 1rem;">Jessup Penalty Checker</h1>
                <div style="font-size: 1.1rem; color: #4b5563;">
                    Memorandum for the {initial_data['memorialType']}
                </div>
                <div style="background-color: #fee2e2; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem;">
                    <div style="font-size: 0.9rem; color: #991b1b;">Penalty Points</div>
                    <div style="font-size: 2rem; font-weight: bold; color: #dc2626;">10</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation
        create_section_header("Sections")
        sections = [
            ("📄", "Cover Page", "Rule 5.6", "2 points"),
            ("✓", "Memorial Parts", "Rule 5.5", "2 points per part"),
            ("📏", "Length Check", "Rule 5.12", "varies"),
            ("🔒", "Anonymity", "Rule 5.14", "up to 10 points"),
            ("📝", "Tracked Changes", "Rule 5.4", "up to 5 points"),
            ("📚", "Citations", "Rule 5.13", "up to 5 points"),
            ("🖼️", "Media", "Rule 5.5(c)", "up to 5 points"),
            ("📑", "Abbreviations", "Rule 5.17", "1 point each, max 3"),
            ("🔍", "Plagiarism", "Rule 11.2", "1-50 points")
        ]
        
        for icon, section, rule, points in sections:
            st.markdown(f"""
                <div class="nav-item">
                    <div style="margin-right: 0.75rem;">{icon}</div>
                    <div>
                        <div style="font-weight: 500;">{section}</div>
                        <div style="font-size: 0.8rem; color: #6b7280;">{rule} - {points}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Main content area
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header
    st.markdown("""
        <h1 style="font-size: 2rem; margin-bottom: 2rem;">
            Jessup Memorial Penalty Checker
        </h1>
    """, unsafe_allow_html=True)
    
    # Penalty Score Summary
    create_section_header("Penalty Score Summary", "⚠️")
    st.markdown("""
        <table class="custom-table">
            <thead>
                <tr>
                    <th>Rule</th>
                    <th>Description</th>
                    <th style="text-align: center;">A</th>
                    <th style="text-align: center;">R</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Rule 5.5</td>
                    <td>
                        Missing Prayer for Relief
                        <div style="font-size: 0.8rem; color: #6b7280;">2 points per part</div>
                    </td>
                    <td style="text-align: center;">4</td>
                    <td style="text-align: center;">2</td>
                </tr>
                <tr>
                    <td>Rule 5.17</td>
                    <td>
                        Non-Permitted Abbreviations (5 found)
                        <div style="font-size: 0.8rem; color: #6b7280;">1 point each, max 3</div>
                    </td>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">0</td>
                </tr>
                <tr>
                    <td>Rule 5.13</td>
                    <td>
                        Improper Citation
                        <div style="font-size: 0.8rem; color: #6b7280;">1 point per violation, max 5</div>
                    </td>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">0</td>
                </tr>
                <tr style="background-color: #f9fafb; font-weight: 600;">
                    <td colspan="2" style="text-align: right;">TOTAL</td>
                    <td style="text-align: center;">10</td>
                    <td style="text-align: center;">2</td>
                </tr>
            </tbody>
        </table>
    """, unsafe_allow_html=True)
    
    # Document Sections
    col1, col2 = st.columns(2)
    
    with col1:
        # Cover Page Section
        create_section_header("Cover Page Information", "📄", "Rule 5.6")
        for key, value in initial_data["coverPage"].items():
            st.markdown(f"""
                <div class="card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span>{key}</span>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            {create_status_indicator('success' if value['present'] else 'error', value['found'])}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Memorial Parts Section
        create_section_header("Memorial Parts", "✓", "Rule 5.5")
        st.markdown("""
            <div class="card">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
        """, unsafe_allow_html=True)
        
        for part, present in initial_data["memorialParts"].items():
            st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    {create_status_indicator('success' if present else 'error', part)}
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Word Count Analysis
    create_section_header("Word Count Analysis", "📏", "Rule 5.12")
    word_count_cols = st.columns(2)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with word_count_cols[
