import streamlit as st
import pandas as pd
from pathlib import Path

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

    /* Card-like containers */
    .stMarkdown {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }

    /* Status icons */
    .icon-success {
        color: #4CAF50;
        font-size: 1.2rem;
    }

    .icon-error {
        color: #EF5350;
        font-size: 1.2rem;
    }

    /* Progress container */
    .progress-container {
        margin: 1rem 0;
        padding: 1rem;
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
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
    
    # Create a container for the progress bar
    st.markdown(f"""
        <div class="progress-container">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>{count} words</span>
                <span style="color: {'red' if percentage > 100 else 'orange' if percentage > 90 else 'green'}">
                    {percentage:.1f}%
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    progress = st.progress(min(percentage / 100, 1.0))
    st.markdown(f"<div style='text-align: right; font-size: 0.8rem; color: #666;'>Limit: {limit}</div>", 
               unsafe_allow_html=True)

def create_card(title, content):
    """Create a card-like container"""
    st.markdown(f"""
        <div class="stCard">
            <h3>{title}</h3>
            <div>{content}</div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
        
        st.markdown("""
        <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 0.5rem;'>
            <div style='color: #666; font-size: 0.9rem;'>Penalty Points</div>
            <div style='color: #dc3545; font-size: 2rem; font-weight: bold;'>10</div>
            <div style='color: #666; font-size: 0.8rem;'>points</div>
        </div>
        """, unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")

    # Score Breakdown
    with st.expander("Penalty Score Summary", expanded=True):
        penalties_df = pd.DataFrame({
            'Rule': ['Rule 5.5', 'Rule 5.17', 'Rule 5.13'],
            'Description': [
                'Missing Prayer for Relief',
                'Non-Permitted Abbreviations (5 found)',
                'Improper Citation'
            ],
            'Points': [4, 3, 3],
            'Reviewed': ['Yes', 'No', 'No']
        })
        st.table(penalties_df)
        st.markdown("**Total Penalty Points: 10**")

    # Create two columns for the layout
    col1, col2 = st.columns(2)

    # Cover Page Check
    with col1:
        st.markdown("""
            <div class="stCard">
                <h3>Cover Page Information</h3>
        """, unsafe_allow_html=True)
        
        for key, value in initial_data["coverPage"].items():
            icon = "✅" if value["present"] else "❌"
            st.markdown(f"{icon} **{key}:** {value['found']}")
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Memorial Parts
    with col2:
        st.markdown("""
            <div class="stCard">
                <h3>Memorial Parts</h3>
        """, unsafe_allow_html=True)
        
        for part, present in initial_data["memorialParts"].items():
            icon = "✅" if present else "❌"
            st.markdown(f"{icon} {part}")
        
        st.markdown("</div>", unsafe_allow_html=True)

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

    # Citations, Media, and Plagiarism sections in cards
    col1, col2 = st.columns(2)
    
    with col1:
        create_card("Citations Check", """
            <div class="status-error">
                ⚠️ 5 instances of improper citation format detected
            </div>
        """)
        
        create_card("Media Check", "\n".join(
            f"⚠️ Found in {item['section']}: {item['text']}"
            for item in initial_data["media"]
        ))
    
    with col2:
        create_card("Plagiarism Check", """
            <div class="status-success">
                ✅ No plagiarism detected
            </div>
        """)

if __name__ == "__main__":
    main()
