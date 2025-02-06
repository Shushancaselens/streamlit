import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Jessup Memorial Penalty Checker", layout="wide")

# Data
data = {
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

penalties = [
    {"rule": "Rule 5.5", "description": "Missing Prayer for Relief", "points": 4, "r": 2, "details": "2 points per part"},
    {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations (5 found)", "points": 3, "r": 0, "details": "1 point each, max 3"},
    {"rule": "Rule 5.13", "description": "Improper Citation", "points": 3, "r": 0, "details": "1 point per violation, max 5"}
]

# Custom CSS
st.markdown("""
<style>
    section[data-testid="stSidebar"] > div {
        background-color: white;
        padding: 1rem;
    }
    .block-container {
        padding-top: 1rem !important;
    }
    .css-1y4p8pa {
        padding-top: 0rem;
    }
    [data-testid="stExpander"] {
        border: 1px solid #ddd !important;
        border-radius: 0.5rem !important;
        margin-bottom: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### Penalty Points")
    st.markdown("""
        <div style="background-color: #f3f4f6; padding: 1rem; border-radius: 0.5rem;">
            <span style="font-size: 2rem; font-weight: bold; color: #ef4444;">10</span>
            <span style="color: #6b7280;"> points</span>
        </div>
    """, unsafe_allow_html=True)

# Main content
st.title("Jessup Memorial Penalty Checker")

# Score Breakdown
st.markdown("### Penalty Score Summary")
df = pd.DataFrame(penalties)
st.table(df[["rule", "description", "points", "r"]])
st.markdown("**Total Points: 10**")

# Create two columns for layout
col1, col2 = st.columns(2)

# Cover Page Check
with col1:
    st.markdown("### Cover Page Information")
    st.markdown("*Rule 5.6 - 2 points*")
    for key, value in data["coverPage"].items():
        status = "✅" if value["present"] else "❌"
        st.markdown(f"{status} {key}: {value['found']}")

# Memorial Parts
with col2:
    st.markdown("### Memorial Parts")
    st.markdown("*Rule 5.5 - 2 points per part*")
    cols = st.columns(2)
    items = list(data["memorialParts"].items())
    mid = len(items) // 2
    
    for i, (part, present) in enumerate(items):
        col = cols[0] if i < mid else cols[1]
        status = "✅" if present else "❌"
        col.markdown(f"{status} {part}")

# Word Count Analysis
st.markdown("### Word Count Analysis")
st.markdown("*Rule 5.12*")
cols = st.columns(2)
for idx, (section, info) in enumerate(data["wordCounts"].items()):
    col = cols[idx % 2]
    percentage = (info["count"] / info["limit"]) * 100
    col.markdown(f"**{section}**")
    col.progress(min(percentage / 100, 1.0))
    
    if percentage > 100:
        color = "red"
    elif percentage > 90:
        color = "orange"
    else:
        color = "green"
        
    col.markdown(f'<span style="color: {color}">{info["count"]} words ({percentage:.1f}%)</span>',
                unsafe_allow_html=True)
    col.markdown(f"Limit: {info['limit']}")

# Anonymity Check
with col1:
    st.markdown("### Anonymity")
    st.markdown("*Rule 5.14 - up to 10 points*")
    st.success("✅ No anonymity violations found\n\nNo disclosure of school, team members, or country")

# Tracked Changes
with col2:
    st.markdown("### Tracked Changes")
    st.markdown("*Rule 5.4 - up to 5 points*")
    st.success("✅ No tracked changes found\n\n✅ No comments found")

# Citations
with col1:
    st.markdown("### Citations")
    st.markdown("*Rule 5.13 - 1 point per violation, max 5*")
    st.warning("❌ Found improper citations\n\n5 instances of improper citation format detected")

# Media Check
with col2:
    st.markdown("### Media")
    st.markdown("*Rule 5.5(c) - up to 5 points*")
    for item in data["media"]:
        st.warning(f"Found in {item['section']}\n\n{item['text']}")

# Abbreviations
st.markdown("### Non-Permitted Abbreviations")
st.markdown("*Rule 5.17 - 1 point each, max 3*")
for abbr, info in data["abbreviations"].items():
    with st.expander(f"❌ {abbr} ({info['count']} occurrence{'s' if info['count'] != 1 else ''})"):
        st.markdown(f"Found in: {', '.join(info['sections'])}")

# Plagiarism
with col1:
    st.markdown("### Plagiarism")
    st.markdown("*Rule 11.2 - 1-50 points*")
    st.success("✅ No plagiarism detected")
