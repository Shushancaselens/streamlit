```python
import streamlit as st
import pandas as pd

# Data initialization 
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

st.set_page_config(layout="wide", page_title="Jessup Penalty Checker")

st.markdown("""
<style>
    .main { padding-top: 0; }
    .metric-card {
        background: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://via.placeholder.com/150x80?text=Jessup", use_column_width=True)
    st.markdown(f"### {initial_data['memorialType']} Memorial")
    st.markdown("""
    <div class='metric-card'>
        <h4>Total Penalty Points</h4>
        <h2 style='color: #f44336;'>10 points</h2>
    </div>
    """, unsafe_allow_html=True)

st.title("Jessup Memorial Penalty Checker")

tab1, tab2 = st.tabs(["Overview", "Detailed Analysis"])

with tab1:
    cols = st.columns(4)
    metrics = [
        ("Total Violations", "7", "Critical"),
        ("Word Count Status", "98%", "Safe"),
        ("Missing Parts", "1", "Prayer for Relief"),
        ("Abbreviation Issues", "5", "3 points")
    ]
    
    for col, (label, value, delta) in zip(cols, metrics):
        with col:
            st.metric(label, value, delta)

    st.subheader("Word Count Analysis")
    for section, data in initial_data["wordCounts"].items():
        percentage = (data["count"] / data["limit"]) * 100
        st.markdown(f"**{section}**")
        st.progress(min(percentage/100, 1.0))
        st.caption(f"{data['count']} words ({percentage:.1f}%) - Limit: {data['limit']}")

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Cover Page Information")
        for key, value in initial_data["coverPage"].items():
            st.markdown(f"{'✅' if value['present'] else '❌'} **{key}**: {value['found']}")
        
        st.subheader("Memorial Parts")
        for part, present in initial_data["memorialParts"].items():
            st.markdown(f"{'✅' if present else '❌'} {part}")
    
    with col2:
        st.subheader("Abbreviations")
        for abbr, info in initial_data["abbreviations"].items():
            with st.expander(f"{abbr} ({info['count']} occurrences)"):
                st.write(f"Found in: {', '.join(info['sections'])}")

    st.subheader("Compliance Checks")
    check_cols = st.columns(3)
    with check_cols[0]:
        st.error("Citations: 5 improper formats detected")
    with check_cols[1]:
        st.warning("Media: Found in Cover Page")
    with check_cols[2]:
        st.success("Plagiarism: No issues detected")

if st.button("Generate Report"):
    st.download_button(
        "Download Full Report",
        "Report data here",
        file_name="jessup_penalty_report.pdf"
    )
```
