import streamlit as st
import pandas as pd

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initial data setup (same as before)
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
        "ICCPED": {"count": 1, "sections": ["Summary of Pleadings"]},
        "ICC": {"count": 1, "sections": ["Pleadings"]},
        "LOSC": {"count": 1, "sections": ["Pleadings"]},
        "AFRC": {"count": 1, "sections": ["Pleadings"]}
    },
    "media": [{"section": "Cover Page", "index": 6, "text": "----media/image1.png----"}]
}

# Custom CSS
st.markdown("""
<style>
    /* Main container styling */
    .main-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Section headers */
    .section-header {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #f0f0f0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Card styling */
    .card {
        background-color: white;
        border: 1px solid #f0f0f0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
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

    /* Table styling */
    .custom-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
    }
    .custom-table th {
        background-color: #f8f9fa;
        padding: 12px;
        text-align: left;
        font-weight: 600;
        border-bottom: 2px solid #e9ecef;
    }
    .custom-table td {
        padding: 12px;
        border-bottom: 1px solid #e9ecef;
    }
    .custom-table tr:last-child td {
        border-bottom: none;
    }

    /* Progress bar container */
    .progress-container {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
    }

    /* Sidebar navigation */
    .nav-item {
        padding: 8px 12px;
        margin: 4px 0;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .nav-item:hover {
        background-color: #f8f9fa;
    }

    /* Custom tabs */
    .custom-tab {
        border-bottom: 2px solid transparent;
        cursor: pointer;
        padding: 8px 16px;
    }
    .custom-tab.active {
        border-bottom-color: #3b82f6;
        color: #3b82f6;
    }

    /* Alert boxes */
    .alert {
        padding: 12px;
        border-radius: 6px;
        margin: 8px 0;
    }
    .alert-success {
        background-color: #d1fae5;
        color: #065f46;
    }
    .alert-warning {
        background-color: #fef3c7;
        color: #92400e;
    }
    .alert-error {
        background-color: #fee2e2;
        color: #991b1b;
    }
</style>
""", unsafe_allow_html=True)

def create_section_header(icon, title, subtitle=""):
    st.markdown(f"""
        <div class="section-header">
            {icon} {title}
            {f'<span style="font-size: 0.8rem; color: #6b7280;">({subtitle})</span>' if subtitle else ''}
        </div>
    """, unsafe_allow_html=True)

def create_card(content, status="normal"):
    st.markdown(f"""
        <div class="card">
            {content}
        </div>
    """, unsafe_allow_html=True)

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    status = "success"
    if percentage > 90:
        status = "warning"
    if percentage > 100:
        status = "error"
    
    color_map = {
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444"
    }
    
    st.markdown(f"""
        <div class="progress-container">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <span>{count} words</span>
                <span style="color: {color_map[status]};">{percentage:.1f}%</span>
            </div>
            <div style="width: 100%; background-color: #e5e7eb; height: 6px; border-radius: 3px;">
                <div style="width: {min(percentage, 100)}%; height: 100%; border-radius: 3px; 
                     background-color: {color_map[status]};">
                </div>
            </div>
            <div style="text-align: right; font-size: 0.8rem; color: #6b7280; margin-top: 4px;">
                Limit: {limit}
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div style="padding: 20px 10px;">
                <h1 style="margin-bottom: 20px;">Jessup Penalty Checker</h1>
                <div style="font-size: 1.1rem; color: #4b5563;">
                    Memorandum for the Applicant
                </div>
                <div style="background-color: #fee2e2; padding: 16px; border-radius: 8px; margin-top: 16px;">
                    <div style="font-size: 0.9rem; color: #991b1b;">Total Penalty Points</div>
                    <div style="font-size: 2rem; font-weight: bold; color: #dc2626;">10</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Navigation Items
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
                    <div style="display: flex; gap: 8px; align-items: center;">
                        <div>{icon}</div>
                        <div>
                            <div style="font-weight: 500;">{section}</div>
                            <div style="font-size: 0.8rem; color: #6b7280;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")

    # Penalty Score Summary
    create_section_header("⚠️", "Penalty Score Summary")
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
                <tr style="background-color: #f8f9fa; font-weight: 600;">
                    <td colspan="2" style="text-align: right;">TOTAL</td>
                    <td style="text-align: center;">10</td>
                    <td style="text-align: center;">2</td>
                </tr>
            </tbody>
        </table>
    """, unsafe_allow_html=True)

    # Create columns for the layout
    col1, col2 = st.columns(2)

    # Cover Page Information
    with col1:
        create_section_header("📄", "Cover Page Information", "Rule 5.6")
        for key, value in initial_data["coverPage"].items():
            st.markdown(f"""
                <div class="card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span>{key}</span>
                        <div class="status-{'success' if value['present'] else 'error'}">
                            {'✅' if value['present'] else '❌'} {value['found']}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Memorial Parts
    with col2:
        create_section_header("✓", "Memorial Parts", "Rule 5.5")
        st.markdown("""
            <div class="card">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
        """, unsafe_allow_html=True)
        
        for part, present in initial_data["memorialParts"].items():
            st.markdown(f"""
                <div class="status-{'success' if present else 'error'}">
                    {'✅' if present else '❌'} {part}
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

    # Word Count Analysis
    create_section_header("📏", "Word Count Analysis", "Rule 5.12")
    word_count_cols = st.columns(2)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with word_count_cols[idx % 2]:
            st.markdown(f"<div style='font-weight: 500; margin-bottom: 8px;'>{section}</div>", 
                       unsafe_allow_html=True)
            create_progress_bar(data["count"], data["limit"])

    # Tracked Changes Check
    create_section_header("📝", "Tracked Changes", "Rule 5.4")
    st.markdown("""
        <div class="card">
            <div class="status-success">
                ✅ No tracked changes found
            </div>
            <div class="status-success" style="margin-top: 8px;">
                ✅ No comments found
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Anonymity Check
    create_section_header("🔒", "Anonymity Check", "Rule 5.14")
    st.markdown("""
        <div class="alert alert-success">
            ✅ No anonymity violations found
            <div style="font-size: 0.9rem;
