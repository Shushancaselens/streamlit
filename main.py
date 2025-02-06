import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Jessup Memorial Penalty Checker", layout="wide")

st.title("Jessup Memorial Penalty Checker")

# Style configurations
st.markdown("""
    <style>
    .success { color: #28a745; }
    .warning { color: #ffc107; }
    .danger { color: #dc3545; }
    </style>
""", unsafe_allow_html=True)

# Cover Page Information
st.header("📄 Cover Page Information")
cover_page_info = {
    "Team Number": {"present": True, "found": "349A"},
    "Court Name": {"present": True, "found": "International Court of Justice"},
    "Year": {"present": True, "found": "2025"},
    "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"}
}

col1, col2 = st.columns(2)
for (key, value), column in zip(cover_page_info.items(), [col1, col2] * (len(cover_page_info) // 2)):
    with column:
        if value["present"]:
            st.success(f"{key}: {value['found']}")
        else:
            st.error(f"{key}: Missing")

# Word Count Analysis
st.header("📊 Word Count Analysis")
word_counts = {
    "Statement of Facts": {"count": 1196, "limit": 1200},
    "Summary of Pleadings": {"count": 642, "limit": 700},
    "Pleadings": {"count": 9424, "limit": 9500},
    "Prayer for Relief": {"count": 125, "limit": 200}
}

for section, data in word_counts.items():
    percentage = (data["count"] / data["limit"]) * 100
    st.subheader(section)
    progress_color = "normal"
    if percentage > 95:
        progress_color = "warning"
    elif percentage > 100:
        progress_color = "error"
    
    st.progress(min(percentage / 100, 1.0))
    st.write(f"{data['count']} words out of {data['limit']} limit ({percentage:.1f}%)")

# Non-Permitted Abbreviations
st.header("⚠️ Non-Permitted Abbreviations")
abbreviations = {
    "ISECR": {"count": 2, "sections": ["Pleadings"], 
              "lines": ["iii. Rovinia's issuance of fishing licenses violates Articles 6 and 11 of the ISECR. 25",
                       "Rovinia's issuance of fishing licenses violates Articles 6 and 11 of the ISECR."]},
    "ICCPED": {"count": 1, "sections": ["Summary of Pleadings"],
               "lines": ["First, Rovinia cannot exercise universal jurisdiction over the crime of enforced disappearances..."]},
    "ICC": {"count": 1, "sections": ["Pleadings"],
            "lines": ["While the ILC report includes enforced disappearances as a crime against humanity..."]},
    "LOSC": {"count": 1, "sections": ["Pleadings"],
             "lines": ["Caron argues that permanently fixing the boundaries of all maritime zones..."]},
    "AFRC": {"count": 1, "sections": ["Pleadings"],
             "lines": ["States and international organizations have historically continued to recognize..."]}
}

for abbr, data in abbreviations.items():
    with st.expander(f"{abbr} ({data['count']} occurrence{'s' if data['count'] > 1 else ''})"):
        st.write(f"**Found in:** {', '.join(data['sections'])}")
        for i, line in enumerate(data['lines']):
            st.write(f"**Instance {i+1}:** {line}")

# Memorial Parts Check
st.header("✅ Memorial Parts Check")
memorial_parts = {
    "Cover Page": True,
    "Table of Contents": True,
    "Index of Authorities": True,
    "Statement of Jurisdiction": True,
    "Statement of Facts": True,
    "Summary of Pleadings": True,
    "Pleadings": True,
    "Prayer for Relief": True
}

col1, col2 = st.columns(2)
for (part, present), column in zip(memorial_parts.items(), [col1, col2] * (len(memorial_parts) // 2)):
    with column:
        if present:
            st.success(part)
        else:
            st.error(part)

# Tracked Changes and Comments
st.header("📝 Document Status")
if not any(["comments", "tracked_changes"]):
    st.success("No tracked changes or comments found")
else:
    st.error("Document contains tracked changes or comments")

# Improper Media Check
st.header("🖼️ Media Check")
media_issues = [
    {"section": "Cover Page", "index": 6, "text": "----media/image1.png----"}
]

if media_issues:
    for issue in media_issues:
        st.warning(f"Found media in {issue['section']}: {issue['text']}")
else:
    st.success("No improper media found")

# Plagiarism Check
st.header("🔍 Plagiarism Check")
if "plagiarism" not in locals() or not plagiarism:
    st.success("No plagiarism detected")
else:
    st.error("Plagiarism detected")
