import streamlit as st
import pandas as pd
from PIL import Image

# Configure the page
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to match the original design
st.markdown("""
    <style>
    .stApp {
        background-color: #f9fafb;
    }
    .css-1d391kg {
        background-color: white;
    }
    .stat-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    .stProgress > div > div > div > div {
        background-color: #10B981;
    }
    .warning .stProgress > div > div > div > div {
        background-color: #F59E0B;
    }
    .error .stProgress > div > div > div > div {
        background-color: #EF4444;
    }
    </style>
    """, unsafe_allow_html=True)

# Initial data
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
    }
}

# Sidebar
with st.sidebar:
    st.title("Jessup Penalty Checker")
    st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
    
    # Penalty points summary
    st.markdown("""
    <div style='background-color: #f3f4f6; padding: 1rem; border-radius: 0.5rem;'>
        <p style='color: #4B5563; font-size: 0.875rem; font-weight: 600;'>Penalty Points</p>
        <div style='display: flex; align-items: baseline; gap: 0.25rem;'>
            <span style='color: #DC2626; font-size: 1.5rem; font-weight: 700;'>10</span>
            <span style='color: #6B7280; font-size: 0.875rem;'>points</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.title("Jessup Memorial Penalty Checker")

# Penalty Score Summary
st.markdown("### Penalty Score Summary")
penalties = [
    {"Rule": "Rule 5.5", "Description": "Missing Prayer for Relief", "Points": 4, "R": 2, "Details": "2 points per part"},
    {"Rule": "Rule 5.17", "Description": "Non-Permitted Abbreviations (5 found)", "Points": 3, "R": 0, "Details": "1 point each, max 3"},
    {"Rule": "Rule 5.13", "Description": "Improper Citation", "Points": 3, "R": 0, "Details": "1 point per violation, max 5"}
]

# Create a custom table for penalties
st.markdown("""
<table style="width: 100%; border-collapse: collapse; margin-bottom: 1rem;">
    <thead>
        <tr style="border-bottom: 1px solid #e5e7eb;">
            <th style="text-align: left; padding: 0.5rem;">Rule</th>
            <th style="text-align: left; padding: 0.5rem;">Description</th>
            <th style="text-align: center; padding: 0.5rem;">A</th>
            <th style="text-align: center; padding: 0.5rem;">R</th>
        </tr>
    </thead>
    <tbody>
""", unsafe_allow_html=True)

for penalty in penalties:
    st.markdown(f"""
    <tr style="border-bottom: 1px solid #e5e7eb;">
        <td style="padding: 0.5rem;">{penalty['Rule']}</td>
        <td style="padding: 0.5rem;">
            {penalty['Description']}<br/>
            <span style="font-size: 0.75rem; color: #6B7280;">{penalty['Details']}</span>
        </td>
        <td style="text-align: center; padding: 0.5rem;">{penalty['Points']}</td>
        <td style="text-align: center; padding: 0.5rem;">{penalty['R']}</td>
    </tr>
    """, unsafe_allow_html=True)

st.markdown("""
    <tr style="font-weight: bold; background-color: #f9fafb;">
        <td colspan="2" style="text-align: right; padding: 0.5rem;">TOTAL</td>
        <td style="text-align: center; padding: 0.5rem;">10</td>
        <td style="text-align: center; padding: 0.5rem;">2</td>
    </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)

# Create two columns for the layout
col1, col2 = st.columns(2)

# Cover Page Information
with col1:
    st.markdown("### Cover Page Information")
    for key, value in initial_data["coverPage"].items():
        status = "✅" if value["present"] else "❌"
        st.markdown(f"{status} {key}: {value['found']}")

# Memorial Parts
with col2:
    st.markdown("### Memorial Parts")
    cols = st.columns(2)
    items = list(initial_data["memorialParts"].items())
    mid = len(items) // 2
    
    for i, (part, present) in enumerate(items):
        col_idx = 0 if i < mid else 1
        with cols[col_idx]:
            status = "✅" if present else "❌"
            st.markdown(f"{status} {part}")

# Word Count Analysis
st.markdown("### Word Count Analysis")
word_count_cols = st.columns(2)

for i, (section, data) in enumerate(initial_data["wordCounts"].items()):
    col_idx = i % 2
    with word_count_cols[col_idx]:
        st.markdown(f"**{section}**")
        percentage = (data["count"] / data["limit"]) * 100
        
        # Add the appropriate CSS class based on the percentage
        progress_class = ""
        if percentage > 100:
            progress_class = "error"
        elif percentage > 90:
            progress_class = "warning"
            
        st.markdown(f'<div class="{progress_class}">', unsafe_allow_html=True)
        st.progress(min(percentage / 100, 1.0))
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; font-size: 0.875rem;">
            <span>{data['count']} words</span>
            <span style="color: {'#EF4444' if percentage > 100 else '#F59E0B' if percentage > 90 else '#10B981'}">
                {percentage:.1f}%
            </span>
        </div>
        <div style="font-size: 0.75rem; color: #6B7280;">Limit: {data['limit']}</div>
        """, unsafe_allow_html=True)

# Abbreviations
st.markdown("### Non-Permitted Abbreviations")
for abbr, info in initial_data["abbreviations"].items():
    with st.expander(f"❌ {abbr} ({info['count']} occurrence{'s' if info['count'] > 1 else ''})"):
        st.markdown(f"Found in: {', '.join(info['sections'])}")

# Function to handle file upload
def process_memorial_file():
    st.markdown("### Upload Memorial")
    uploaded_file = st.file_uploader("Choose a file...", type=['docx', 'pdf'])
    if uploaded_file is not None:
        st.success("File uploaded successfully! Processing...")
        # Add file processing logic here

# Add file upload section at the bottom
process_memorial_file()

# Footer
st.markdown("---")
st.markdown("Jessup Memorial Penalty Checker © 2025")
