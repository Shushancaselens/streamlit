import streamlit as st
import pandas as pd
from PIL import Image
import plotly.graph_objects as go

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
    .center-text {
        text-align: center;
    }
    .success-text {
        color: #10B981;
    }
    .warning-text {
        color: #F59E0B;
    }
    .error-text {
        color: #EF4444;
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
penalties_df = pd.DataFrame([
    {"Rule": "Rule 5.5", "Description": "Missing Prayer for Relief", "Points": 4, "R": 2},
    {"Rule": "Rule 5.17", "Description": "Non-Permitted Abbreviations (5 found)", "Points": 3, "R": 0},
    {"Rule": "Rule 5.13", "Description": "Improper Citation", "Points": 3, "R": 0}
])
st.dataframe(penalties_df, hide_index=True)

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
cols = st.columns(2)

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = "#EF4444" if percentage > 100 else "#F59E0B" if percentage > 90 else "#10B981"
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percentage,
        number = {"suffix": "%", "font": {"size": 24}},
        gauge = {
            "axis": {"range": [0, 100], "tickwidth": 1},
            "bar": {"color": color},
            "borderwidth": 2,
            "bordercolor": "white",
        },
        domain = {'x': [0, 1], 'y': [0, 1]}
    ))
    
    fig.update_layout(
        height=150,
        margin=dict(l=10, r=10, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )
    
    return fig

for i, (section, data) in enumerate(initial_data["wordCounts"].items()):
    col_idx = i % 2
    with cols[col_idx]:
        st.markdown(f"**{section}**")
        st.markdown(f"Count: {data['count']} / {data['limit']}")
        st.plotly_chart(create_progress_bar(data['count'], data['limit']), use_container_width=True)

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
