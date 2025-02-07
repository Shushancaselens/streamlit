import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Data structures (same as React version)
applicant_data = {
    "memorialType": "Applicant",
    "coverPage": {
        "Team Number": {"present": True, "found": "349A"},
        "Court Name": {"present": True, "found": "International Court of Justice"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
        "Memorial Type": {"present": True, "found": "Memorial for the Applicant"}
    },
    "wordCounts": {
        "Statement of Facts": {"count": 1196, "limit": 1200},
        "Summary of Pleadings": {"count": 642, "limit": 700},
        "Pleadings": {"count": 9424, "limit": 9500},
        "Prayer for Relief": {"count": 198, "limit": 200}
    },
    "penalties": [
        {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations", "points": 3, "details": "1 point each"},
        {"rule": "Rule 5.13", "description": "Improper Citation", "points": 2, "details": "2 instances"}
    ],
    "totalPenalties": 5
}

respondent_data = {
    "memorialType": "Respondent",
    "coverPage": {
        "Team Number": {"present": True, "found": "349B"},
        "Court Name": {"present": True, "found": "International Court of Justice"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
        "Memorial Type": {"present": True, "found": "Memorial for the Respondent"}
    },
    "wordCounts": {
        "Statement of Facts": {"count": 1180, "limit": 1200},
        "Summary of Pleadings": {"count": 695, "limit": 700},
        "Pleadings": {"count": 9490, "limit": 9500},
        "Prayer for Relief": {"count": 195, "limit": 200}
    },
    "penalties": [
        {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations", "points": 2, "details": "2 instances"},
        {"rule": "Rule 5.14", "description": "Anonymity Violation", "points": 5, "details": "School name mentioned"}
    ],
    "totalPenalties": 7
}

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = 'red' if percentage > 100 else 'orange' if percentage > 90 else 'green'
    return go.Figure(data=[go.Bar(
        x=[percentage],
        text=[f"{percentage:.1f}%"],
        textposition='auto',
        marker_color=color,
        width=[0.3]
    )]).update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        height=30,
        xaxis=dict(range=[0, 100], showticklabels=False),
        yaxis=dict(showticklabels=False)
    )

# Page configuration
st.set_page_config(layout="wide", page_title="Jessup Memorial Penalty Checker")

# Header
st.title("Jessup Memorial Penalty Checker")
st.markdown("---")

# Main content
col1, col2 = st.columns(2)

# Applicant Section
with col1:
    st.subheader(f"{applicant_data['memorialType']} Memorial")
    st.error(f"Total Penalties: {applicant_data['totalPenalties']} points")
    
    # Penalties
    st.write("### Penalties")
    for penalty in applicant_data['penalties']:
        with st.expander(f"{penalty['description']} ({penalty['points']} points)"):
            st.write(f"Rule: {penalty['rule']}")
            st.write(f"Details: {penalty['details']}")
    
    # Word Counts
    st.write("### Word Counts")
    for section, data in applicant_data['wordCounts'].items():
        st.write(f"**{section}**")
        st.write(f"{data['count']} / {data['limit']} words")
        st.plotly_chart(create_progress_bar(data['count'], data['limit']), use_container_width=True)

# Respondent Section
with col2:
    st.subheader(f"{respondent_data['memorialType']} Memorial")
    st.error(f"Total Penalties: {respondent_data['totalPenalties']} points")
    
    # Penalties
    st.write("### Penalties")
    for penalty in respondent_data['penalties']:
        with st.expander(f"{penalty['description']} ({penalty['points']} points)"):
            st.write(f"Rule: {penalty['rule']}")
            st.write(f"Details: {penalty['details']}")
    
    # Word Counts
    st.write("### Word Counts")
    for section, data in respondent_data['wordCounts'].items():
        st.write(f"**{section}**")
        st.write(f"{data['count']} / {data['limit']} words")
        st.plotly_chart(create_progress_bar(data['count'], data['limit']), use_container_width=True)

# Comparison Alert
if respondent_data['totalPenalties'] > applicant_data['totalPenalties']:
    st.warning(f"⚠️ Respondent memorial has higher penalties ({respondent_data['totalPenalties']} points vs {applicant_data['totalPenalties']} points)")
elif applicant_data['totalPenalties'] > respondent_data['totalPenalties']:
    st.warning(f"⚠️ Applicant memorial has higher penalties ({applicant_data['totalPenalties']} points vs {respondent_data['totalPenalties']} points)")

# Add CSS for better styling
st.markdown("""
    <style>
    .stExpander {
        border: 1px solid #e6e6e6;
        border-radius: 4px;
        margin-bottom: 10px;
    }
    .stProgress > div > div > div {
        height: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)
