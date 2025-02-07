import streamlit as st
import pandas as pd
from streamlit_card import card
import plotly.graph_objects as go

# Custom CSS
st.markdown("""
<style>
    .css-18e3th9 { padding-top: 0; }
    .css-1d391kg { padding-top: 1rem; }
    .stProgress .st-bo { background-color: #4CAF50; }
    .warning-gauge { background-color: #ff9800; }
    .error-gauge { background-color: #f44336; }
    .card { 
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

def create_gauge(value, title, max_value=100):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title},
        gauge={
            'axis': {'range': [0, max_value]},
            'bar': {'color': "#4CAF50" if value < 90 else "#ff9800" if value < 100 else "#f44336"},
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_value
            }
        }
    ))
    fig.update_layout(height=150, margin=dict(l=10, r=10, t=40, b=10))
    return fig

# Data initialization (your existing initial_data here)

# App layout
st.set_page_config(layout="wide", page_title="Jessup Penalty Checker")

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x80?text=Jessup", use_column_width=True)
    st.markdown(f"### {initial_data['memorialType']} Memorial")
    
    with st.container():
        st.markdown("""
        <div class='metric-card'>
            <h4>Total Penalty Points</h4>
            <h2 style='color: #f44336;'>10 points</h2>
        </div>
        """, unsafe_allow_html=True)

# Main content
st.title("Jessup Memorial Penalty Checker")

# Summary Tab
tab1, tab2 = st.tabs(["Overview", "Detailed Analysis"])

with tab1:
    # Penalty Summary
    st.subheader("Quick Summary")
    cols = st.columns(4)
    with cols[0]:
        st.metric("Total Violations", "7", "Critical")
    with cols[1]:
        st.metric("Word Count Status", "98%", "Safe")
    with cols[2]:
        st.metric("Missing Parts", "1", "Prayer for Relief")
    with cols[3]:
        st.metric("Abbreviation Issues", "5", "3 points")

    # Word Count Gauges
    st.subheader("Word Count Analysis")
    gauge_cols = st.columns(4)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with gauge_cols[idx]:
            percentage = (data["count"] / data["limit"]) * 100
            st.plotly_chart(create_gauge(percentage, section), use_container_width=True)

with tab2:
    # Detailed Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("Cover Page Information", expanded=True):
            for key, value in initial_data["coverPage"].items():
                st.markdown(f"{'✅' if value['present'] else '❌'} **{key}**: {value['found']}")
        
        with st.expander("Memorial Parts", expanded=True):
            for part, present in initial_data["memorialParts"].items():
                st.markdown(f"{'✅' if present else '❌'} {part}")
    
    with col2:
        with st.expander("Abbreviations", expanded=True):
            for abbr, info in initial_data["abbreviations"].items():
                st.markdown(f"""
                <div class='card'>
                    <h4>{abbr}</h4>
                    <p>Count: {info['count']}<br>
                    Sections: {', '.join(info['sections'])}</p>
                </div>
                """, unsafe_allow_html=True)

    # Citations and Media
    st.subheader("Compliance Checks")
    check_cols = st.columns(3)
    
    with check_cols[0]:
        st.error("⚠️ Citations: 5 improper formats detected")
    with check_cols[1]:
        st.warning("📎 Media: Found in Cover Page")
    with check_cols[2]:
        st.success("✅ Plagiarism: No issues detected")

# Add interactivity
if st.button("Generate Report"):
    st.download_button(
        "Download Full Report",
        "Report data here",
        file_name="jessup_penalty_report.pdf"
    )
