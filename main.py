import streamlit as st
import pandas as pd
from typing import Dict, Any, List, Tuple, Optional

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initial data
initial_data = {
    "memorialType": "Applicant",
    "coverPage": {
        "Team Number": {"present": True, "found": "349A"},
        "Court Name": {"present": True, "found": "International Court of Justice"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
        "Memorial Type": {"present": True, found: "Memorial for the Applicant"}
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

def load_custom_css():
    st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 2rem;
        }
        
        .card {
            background-color: white;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border: 1px solid #e5e7eb;
        }
        
        .progress-bar {
            width: 100%;
            height: 6px;
            background-color: #e5e7eb;
            border-radius: 3px;
            margin: 0.5rem 0;
        }
        
        .progress-fill {
            height: 100%;
            border-radius: 3px;
            transition: width 0.3s ease;
        }
        
        .status-success { color: #10b981; }
        .status-error { color: #ef4444; }
        .status-warning { color: #f59e0b; }
        
        .sidebar-nav {
            padding: 1rem;
            background-color: white;
        }
        
        .section-header {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

def create_word_count_bar(count: int, limit: int) -> None:
    percentage = (count / limit) * 100
    color = "#10b981"  # Success green
    if percentage > 90:
        color = "#f59e0b"  # Warning yellow
    if percentage > 100:
        color = "#ef4444"  # Error red
    
    st.markdown(f"""
        <div class="card">
            <div style="display: flex; justify-content: space-between;">
                <span>{count:,} words</span>
                <span style="color: {color}">{percentage:.1f}%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" 
                     style="width: {min(percentage, 100)}%; background-color: {color}">
                </div>
            </div>
            <div style="text-align: right; font-size: 0.875rem; color: #6b7280">
                Limit: {limit:,} words
            </div>
        </div>
    """, unsafe_allow_html=True)

def create_status_card(title: str, content: str, status: str = "default") -> None:
    st.markdown(f"""
        <div class="card">
            <div class="section-header">{title}</div>
            <div class="status-{status}">{content}</div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Load custom CSS
    load_custom_css()
    
    # Sidebar
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
        
        st.markdown("""
            <div class="card" style="text-align: center;">
                <div style="color: #6b7280;">Total Penalty Points</div>
                <div style="color: #ef4444; font-size: 2.5rem; font-weight: bold;">10</div>
            </div>
        """, unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")
    
    # Score Breakdown
    with st.expander("Penalty Score Summary", expanded=True):
        st.markdown("""
            <table style="width: 100%;">
                <tr>
                    <th>Rule</th>
                    <th>Description</th>
                    <th>Points</th>
                </tr>
                <tr>
                    <td>Rule 5.5</td>
                    <td>Missing Prayer for Relief</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td>Rule 5.17</td>
                    <td>Non-Permitted Abbreviations</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td>Rule 5.13</td>
                    <td>Improper Citations</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td colspan="2" style="text-align: right;"><strong>Total</strong></td>
                    <td><strong>10</strong></td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

    # Create columns for layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Cover Page Check
        create_status_card(
            "Cover Page Information",
            "\n".join(
                f"{'✓' if v['present'] else '✗'} {k}: {v['found']}"
                for k, v in initial_data['coverPage'].items()
            )
        )
        
        # Word Count Analysis
        st.markdown("### Word Count Analysis")
        for section, data in initial_data['wordCounts'].items():
            create_word_count_bar(data['count'], data['limit'])
    
    with col2:
        # Memorial Parts
        create_status_card(
            "Memorial Parts",
            "\n".join(
                f"{'✓' if present else '✗'} {part}"
                for part, present in initial_data['memorialParts'].items()
            )
        )
        
        # Anonymity Check
        create_status_card(
            "Anonymity Check",
            "✓ No anonymity violations found\nNo disclosure of school, team members, or country",
            "success"
        )
        
        # Tracked Changes Check
        create_status_card(
            "Tracked Changes",
            "✓ No tracked changes found\n✓ No comments found",
            "success"
        )
    
    # Abbreviations section
    st.markdown("### Non-Permitted Abbreviations")
    for abbr, info in initial_data['abbreviations'].items():
        with st.expander(f"{abbr} ({info['count']} occurrences)"):
            st.markdown(f"Found in: {', '.join(info['sections'])}")
    
    # Citations and Media sections
    col1, col2 = st.columns(2)
    with col1:
        create_status_card(
            "Citations Check",
            "⚠️ 5 instances of improper citation format detected",
            "warning"
        )
        
        create_status_card(
            "Media Check",
            "\n".join(f"⚠️ Found in {item['section']}: {item['text']}"
                     for item in initial_data['media']),
            "warning"
        )
    
    with col2:
        create_status_card(
            "Plagiarism Check",
            "✓ No plagiarism detected",
            "success"
        )

if __name__ == "__main__":
    main()
