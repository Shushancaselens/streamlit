import streamlit as st
import pandas as pd
from pathlib import Path

# Initial data setup
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

# Custom CSS for styling
st.markdown("""
<style>
    /* Main container */
    .main {
        padding: 1rem;
    }
    
    /* Card styling */
    .stCard {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Progress bar colors */
    .stProgress > div > div > div {
        background-color: #4CAF50;
    }
    
    .stProgress.warning > div > div > div {
        background-color: #FFA726;
    }
    
    .stProgress.danger > div > div > div {
        background-color: #EF5350;
    }
    
    /* Status indicators */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-success {
        background-color: #4CAF50;
    }
    
    .status-error {
        background-color: #EF5350;
    }
    
    .status-warning {
        background-color: #FFA726;
    }
    
    /* Custom header */
    .custom-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

def create_progress_bar(count, limit):
    """Create a styled progress bar based on word count"""
    percentage = (count / limit) * 100
    color = "normal"
    if percentage > 90:
        color = "warning"
    if percentage > 100:
        color = "danger"
    
    return st.progress(min(percentage / 100, 1.0), text=f"{count} / {limit} words ({percentage:.1f}%)")

def main():
    # Set page config
    st.set_page_config(
        page_title="Jessup Memorial Penalty Checker",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Sidebar
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
        
        st.markdown("### Penalty Points")
        st.markdown("""
        <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 0.5rem;'>
            <h3 style='color: #dc3545; font-size: 2rem; margin: 0;'>10 points</h3>
        </div>
        """, unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")

    # Score Breakdown
    with st.expander("Penalty Score Summary", expanded=True):
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown("### Rule Violations")
        with col2:
            st.markdown("### Points")
        with col3:
            st.markdown("### Reviewed")
            
        st.markdown("---")
        
        # Display penalties
        st.markdown("Missing Prayer for Relief (Rule 5.5) - 4 points")
        st.markdown("Non-Permitted Abbreviations (Rule 5.17) - 3 points")
        st.markdown("Improper Citations (Rule 5.13) - 3 points")
        
        st.markdown("**Total: 10 points**")

    # Create two columns for the layout
    col1, col2 = st.columns(2)

    # Cover Page Check
    with col1:
        st.markdown("### Cover Page Information")
        for key, value in initial_data["coverPage"].items():
            status = "✅" if value["present"] else "❌"
            st.markdown(f"{status} {key}: {value['found']}")

    # Memorial Parts
    with col2:
        st.markdown("### Memorial Parts")
        for part, present in initial_data["memorialParts"].items():
            status = "✅" if present else "❌"
            st.markdown(f"{status} {part}")

    # Word Count Analysis
    st.markdown("### Word Count Analysis")
    word_count_cols = st.columns(2)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with word_count_cols[idx % 2]:
            st.markdown(f"**{section}**")
            create_progress_bar(data["count"], data["limit"])

    # Abbreviations
    st.markdown("### Non-Permitted Abbreviations")
    for abbr, info in initial_data["abbreviations"].items():
        with st.expander(f"{abbr} ({info['count']} occurrences)"):
            st.markdown(f"Found in: {', '.join(info['sections'])}")

    # Citations
    st.markdown("### Citations")
    st.warning("5 instances of improper citation format detected")

    # Media Check
    st.markdown("### Media Check")
    for item in initial_data["media"]:
        st.warning(f"Found media in {item['section']}: {item['text']}")

    # Plagiarism Check
    st.markdown("### Plagiarism Check")
    st.success("No plagiarism detected")

if __name__ == "__main__":
    main()
