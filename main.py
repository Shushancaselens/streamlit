import streamlit as st
import pandas as pd
from pathlib import Path

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
        "ICCPED": {"count": 1, sections: ["Summary of Pleadings"]},
        "ICC": {"count": 1, "sections": ["Pleadings"]},
        "LOSC": {"count": 1, "sections": ["Pleadings"]},
        "AFRC": {"count": 1, "sections": ["Pleadings"]}
    },
    "media": [{"section": "Cover Page", "index": 6, "text": "----media/image1.png----"}]
}

# Custom CSS with enhanced styling
st.markdown("""
<style>
    /* Main container styles */
    .main {
        padding: 1rem;
        background-color: #f8f9fa;
    }
    
    /* Card styling */
    .stCard {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Progress bar styling */
    .progress-container {
        margin: 1rem 0;
    }
    
    .progress-bar {
        height: 6px;
        background-color: #e9ecef;
        border-radius: 3px;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        transition: width 0.3s ease;
    }
    
    /* Sidebar navigation styling */
    .nav-item {
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 0.375rem;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .nav-item:hover {
        background-color: #f8f9fa;
    }
    
    /* Status indicators */
    .status-icon {
        display: inline-flex;
        align-items: center;
        margin-right: 0.5rem;
    }
    
    /* Header styling */
    .section-header {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #1a1a1a;
    }
</style>
""", unsafe_allow_html=True)

def create_navigation_item(icon, label, rule, points):
    """Create a styled navigation item"""
    return f"""
    <div class="nav-item">
        <div class="d-flex align-items-center">
            {icon} {label}
        </div>
        <div class="text-muted small">
            {rule} - {points}
        </div>
    </div>
    """

def main():
    # Sidebar
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
        
        # Penalty Points Display
        st.markdown("""
        <div class="stCard">
            <div class="text-muted">Penalty Points</div>
            <div style="font-size: 2rem; color: #dc3545; font-weight: bold;">10</div>
            <div class="text-muted small">points</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Items
        st.markdown("### Navigation")
        nav_items = [
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
        
        for icon, label, rule, points in nav_items:
            st.markdown(create_navigation_item(icon, label, rule, points), unsafe_allow_html=True)

    # Main Content
    st.title("Jessup Memorial Penalty Checker")
    
    # Penalty Score Summary
    with st.expander("Penalty Score Summary", expanded=True):
        st.markdown("""
        <div class="stCard">
            <table class="table">
                <thead>
                    <tr>
                        <th>Rule</th>
                        <th>Description</th>
                        <th class="text-center">Points</th>
                        <th class="text-center">Reviewed</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Rule 5.5</td>
                        <td>Missing Prayer for Relief</td>
                        <td class="text-center">4</td>
                        <td class="text-center">✓</td>
                    </tr>
                    <tr>
                        <td>Rule 5.17</td>
                        <td>Non-Permitted Abbreviations (5 found)</td>
                        <td class="text-center">3</td>
                        <td class="text-center">-</td>
                    </tr>
                    <tr>
                        <td>Rule 5.13</td>
                        <td>Improper Citation</td>
                        <td class="text-center">3</td>
                        <td class="text-center">-</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

    # Grid Layout for Content
    col1, col2 = st.columns(2)

    with col1:
        # Cover Page Check
        with st.container():
            st.markdown("### Cover Page Information")
            for key, value in initial_data["coverPage"].items():
                st.markdown(f"""
                <div class="stCard">
                    <div class="d-flex justify-content-between align-items-center">
                        <span>{key}</span>
                        <span>{'✅' if value['present'] else '❌'} {value['found']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        # Memorial Parts
        with st.container():
            st.markdown("### Memorial Parts")
            for part, present in initial_data["memorialParts"].items():
                st.markdown(f"""
                <div class="stCard">
                    <span>{'✅' if present else '❌'} {part}</span>
                </div>
                """, unsafe_allow_html=True)

    # Word Count Analysis
    st.markdown("### Word Count Analysis")
    word_count_cols = st.columns(2)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with word_count_cols[idx % 2]:
            percentage = (data["count"] / data["limit"]) * 100
            st.markdown(f"""
            <div class="stCard">
                <div class="section-header">{section}</div>
                <div class="progress-container">
                    <div class="d-flex justify-content-between">
                        <span>{data['count']} words</span>
                        <span style="color: {'#dc3545' if percentage > 100 else '#ffc107' if percentage > 90 else '#28a745'}">
                            {percentage:.1f}%
                        </span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {min(percentage, 100)}%;
                             background-color: {'#dc3545' if percentage > 100 else '#ffc107' if percentage > 90 else '#28a745'}">
                        </div>
                    </div>
                    <div class="text-muted small">Limit: {data['limit']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Additional Sections
    col1, col2 = st.columns(2)
    
    with col1:
        # Anonymity Check
        st.markdown("""
        <div class="stCard">
            <div class="section-header">Anonymity Check</div>
            <div class="status-success">✅ No anonymity violations found</div>
            <div class="text-muted small">No disclosure of school, team members, or country</div>
        </div>
        """, unsafe_allow_html=True)

        # Citations
        st.markdown("""
        <div class="stCard">
            <div class="section-header">Citations</div>
            <div class="status-warning">⚠️ 5 instances of improper citation format detected</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Tracked Changes
        st.markdown("""
        <div class="stCard">
            <div class="section-header">Tracked Changes</div>
            <div class="status-success">
                ✅ No tracked changes found<br>
                ✅ No comments found
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Plagiarism
        st.markdown("""
        <div class="stCard">
            <div class="section-header">Plagiarism Check</div>
            <div class="status-success">✅ No plagiarism detected</div>
        </div>
        """, unsafe_allow_html=True)

    # Abbreviations
    st.markdown("### Non-Permitted Abbreviations")
    for abbr, info in initial_data["abbreviations"].items():
        with st.expander(f"{abbr} ({info['count']} occurrences)"):
            st.markdown(f"""
            <div class="stCard">
                <div class="text-danger">❌ Non-permitted abbreviation</div>
                <div class="text-muted small">Found in: {', '.join(info['sections'])}</div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
