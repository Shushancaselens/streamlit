import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Caselens",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    # Logo
    st.markdown("## 🔷 caselens")
    st.markdown("---")
    
    # Navigation
    st.markdown("#### Navigation")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("👤", help="Profile"):
            st.session_state.nav = "profile"
    with col2:
        if st.button("📅", help="Events", type="primary"):
            st.session_state.nav = "events"
    with col3:
        if st.button("📄", help="Documents"):
            st.session_state.nav = "documents"
    
    st.markdown("---")
    
    # Case Filter
    with st.container():
        st.markdown("#### 🔽 Case Filter")
        st.selectbox("Select Case", ["Admissibility"])
    
    # Date Range
    with st.container():
        st.markdown("#### 📅 Date Range")
        st.text_input("Start Date", value="1724/01/01")
        st.text_input("End Date", value="2025/07/21")
    
    # Submissions Filter
    with st.container():
        st.markdown("#### ⚙️ Submissions Filter")
        st.checkbox("Addressed by party")
        st.checkbox("Disputed by parties")
    
    st.button("Download", type="primary", use_container_width=True)

# Main content area
col1, col2 = st.columns([1, 20])
with col2:
    st.markdown("### Case name: admissability; challenge; request_for_a_stay; statement_of_appeal")

# Create tabs
tab1, tab2 = st.tabs(["Card View", "Table View"])

with tab1:
    # Search box
    st.text_input("🔍", placeholder="Search...", label_visibility="collapsed")
    
    # Timeline items using expanders
    timeline_items = [
        ("2017-00-00", "In 2017, Antani Ivanov participated in the 50m, 100m, and 200m butterfly events at the World Championships, set a national record, and qualified for the 200m butterfly at the 2020 Olympic Games."),
        ("2017-00-00", "At the time of adoption of this Constitution, any term of office completed before 2017 shall be disregarded in calculating the number of full terms that a person has served as a Bureau or Executive Member."),
        ("2020-00-00", "In 2020 Antani Ivanov qualified for the 200m butterfly at the Summer Olympic Games."),
        ("2022-12-12", "On 2022-12-12, the World Aquatics Integrity Code was issued and signed in Melbourne by Husain Al Musallam and Brent J. Nowicki for the Bureau."),
        ("2023-01-01", "On 2023-01-01 the Constitution of World Aquatics came into force."),
        ("2023-01-01", "On 2023-01-01 the new composition of the Bureau as set out in Article 14 came into effect with the new additional positions within the Bureau.")
    ]
    
    # Display each timeline item
    for date, content in timeline_items:
        with st.container():
            col1, col2, col3 = st.columns([2, 15, 1])
            with col1:
                st.markdown(f"**{date}**")
            with col2:
                st.write(content)
            with col3:
                st.markdown("🔽")
            st.markdown("---")

with tab2:
    # Table view
    df = pd.DataFrame(timeline_items, columns=["Date", "Event Description"])
    st.dataframe(df, use_container_width=True, hide_index=True)

# Settings menu (three dots)
with st.sidebar:
    st.markdown("---")
    if st.button("⋮", help="More options"):
        st.write("Settings menu")
