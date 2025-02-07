import streamlit as st
import pandas as pd

# Configure page
st.set_page_config(layout="wide", page_title="Jessup Penalty Checker")

# Custom CSS
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

# Data initialization (your existing initial_data dictionary here)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x80?text=Jessup", use_column_width=True)
    st.markdown(f"### {initial_data['memorialType']} Memorial")
    st.markdown("""
    <div class='metric-card'>
        <h4>Total Penalty Points</h4>
        <h2 style='color: #f44336;'>10 points</h2>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.title("Jessup Memorial Penalty Checker")

# Overview and Details tabs
tab1, tab2 = st.tabs(["Overview", "Detailed Analysis"])

with tab1:
    # Summary metrics
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

    # Word count analysis
    st.subheader("Word Count Analysis")
    for section, data in initial_data["wordCounts"].items():
        percentage = (data["count"] / data["limit"]) * 100
        st.markdown(f"**{section}**")
        st.progress(min(percentage/100, 1.0))
        st.caption(f"{data['count']} words ({percentage:.1f}%) - Limit: {data['limit']}")

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        # Cover Page Information
        st.subheader("Cover Page Information")
        for key, value in initial_data["coverPage"].items():
            st.markdown(f"{'✅' if value['present'] else '❌'} **{key}**: {value['found']}")
        
        # Memorial Parts
        st.subheader("Memorial Parts")
        for part, present in initial_data["memorialParts"].items():
            st.markdown(f"{'✅' if present else '❌'} {part}")
    
    with col2:
        # Abbreviations
        st.subheader("Abbreviations")
        for abbr, info in initial_data["abbreviations"].items():
            with st.expander(f"{abbr} ({info['count']} occurrences)"):
                st.write(f"Found in: {', '.join(info['sections'])}")

    # Compliance Checks
    st.subheader("Compliance Checks")
    check_cols = st.columns(3)
    with check_cols[0]:
        st.error("Citations: 5 improper formats detected")
    with check_cols[1]:
        st.warning("Media: Found in Cover Page")
    with check_cols[2]:
        st.success("Plagiarism: No issues detected")

# Report generation
if st.button("Generate Report"):
    st.download_button(
        "Download Full Report",
        "Report data here",
        file_name="jessup_penalty_report.pdf"
    )
