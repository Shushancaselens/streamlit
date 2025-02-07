import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

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

with st.sidebar:
    st.image("https://via.placeholder.com/100x50.png?text=Logo", width=200)
    st.markdown(f"**Memorandum for the {initial_data['memorialType']}**")
    
    with st.container():
        st.markdown("### Penalty Points")
        col1, col2 = st.columns([1,2])
        with col1:
            st.markdown("### 10")
        with col2:
            st.markdown("points")

st.title("Jessup Memorial Penalty Checker")

st.markdown("### Penalty Score Summary")
penalties = pd.DataFrame([
    {"Rule": "Rule 5.5", "Description": "Missing Prayer for Relief", "Points": 4, "R": 2},
    {"Rule": "Rule 5.17", "Description": "Non-Permitted Abbreviations (5 found)", "Points": 3, "R": 0},
    {"Rule": "Rule 5.13", "Description": "Improper Citation", "Points": 3, "R": 0}
])
st.dataframe(penalties, hide_index=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Cover Page Information (Rule 5.6 - 2 points)")
    for key, value in initial_data["coverPage"].items():
        status = "✅" if value["present"] else "❌"
        st.markdown(f"{key}: {status} {value['found']}")

with col2:
    st.markdown("### Memorial Parts (Rule 5.5 - 2 points per part)")
    cols = st.columns(2)
    for i, (part, present) in enumerate(initial_data["memorialParts"].items()):
        with cols[i % 2]:
            status = "✅" if present else "❌"
            st.markdown(f"{status} {part}")

st.markdown("### Word Count Analysis (Rule 5.12)")
word_count_cols = st.columns(2)
for i, (section, data) in enumerate(initial_data["wordCounts"].items()):
    with word_count_cols[i % 2]:
        percentage = (data["count"] / data["limit"]) * 100
        color = "red" if percentage > 100 else "orange" if percentage > 90 else "green"
        st.markdown(f"**{section}**")
        st.progress(min(percentage/100, 1.0))
        st.markdown(f"{data['count']} words ({percentage:.1f}%) - Limit: {data['limit']}")

col3, col4 = st.columns(2)
with col3:
    st.markdown("### Citations (Rule 5.13 - 1 point per violation, max 5)")
    st.warning("Found improper citations: 5 instances detected")

with col4:
    st.markdown("### Media (Rule 5.5(c) - up to 5 points)")
    for item in initial_data["media"]:
        st.warning(f"Found in {item['section']}: {item['text']}")

st.markdown("### Non-Permitted Abbreviations (Rule 5.17 - 1 point each, max 3)")
for abbr, info in initial_data["abbreviations"].items():
    with st.expander(f"{abbr} ({info['count']} occurrences)"):
        st.markdown(f"Found in: {', '.join(info['sections'])}")

st.markdown("### Plagiarism (Rule 11.2 - 1-50 points)")
st.success("No plagiarism detected")
