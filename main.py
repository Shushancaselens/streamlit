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

# Custom CSS to match the design
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    
    .stSidebar {
        background-color: #e8e8ed;
    }
    
    .sidebar-logo {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    .timeline-item {
        background-color: white;
        border: 1px solid #d1d1d6;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .timeline-date {
        background-color: #007AFF;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        margin-right: 12px;
        display: inline-block;
    }
    
    .timeline-content {
        font-size: 14px;
        line-height: 1.4;
        margin-top: 8px;
    }
    
    .case-title {
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 20px;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Logo
    st.markdown('<div class="sidebar-logo">🔷 caselens</div>', unsafe_allow_html=True)
    
    # Navigation
    st.markdown("### Navigation")
    nav_options = ["👤 Profile", "📅 Events", "📄 Documents"]
    selected_nav = st.radio("", nav_options, index=1, label_visibility="collapsed")
    
    st.markdown("---")
    
    # Case Filter
    st.markdown("### 🔽 Case Filter")
    st.markdown("**Select Case**")
    case_selection = st.selectbox("", ["Admissibility"], label_visibility="collapsed")
    
    # Date Range
    st.markdown("### 📅 Date Range")
    st.markdown("**Start Date**")
    start_date = st.text_input("", value="1724/01/01", label_visibility="collapsed", key="start_date")
    
    st.markdown("**End Date**")
    end_date = st.text_input("", value="2025/07/21", label_visibility="collapsed", key="end_date")
    
    # Submissions Filter
    st.markdown("### ⚙️ Submissions Filter")
    addressed_by_party = st.checkbox("Addressed by party")
    disputed_by_parties = st.checkbox("Disputed by parties")
    
    # Download button
    st.button("Download", type="primary", use_container_width=True)

# Main content
st.markdown('<div class="case-title">Case name: admissability; challenge; request_for_a_stay; statement_of_appeal</div>', unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["Card View", "Table View"])

with tab1:
    # Search box
    search_query = st.text_input("Search...", placeholder="Search...")
    
    # Timeline data
    timeline_data = [
        {
            "date": "2017-00-00",
            "content": "In 2017, Antani Ivanov participated in the 50m, 100m, and 200m butterfly events at the World Championships, set a national record, and qualified for the 200m butterfly at the 2020 Olympic Games."
        },
        {
            "date": "2017-00-00", 
            "content": "At the time of adoption of this Constitution, any term of office completed before 2017 shall be disregarded in calculating the number of full terms that a person has served as a Bureau or Executive Member."
        },
        {
            "date": "2020-00-00",
            "content": "In 2020 Antani Ivanov qualified for the 200m butterfly at the Summer Olympic Games."
        },
        {
            "date": "2022-12-12",
            "content": "On 2022-12-12, the World Aquatics Integrity Code was issued and signed in Melbourne by Husain Al Musallam and Brent J. Nowicki for the Bureau."
        },
        {
            "date": "2023-01-01",
            "content": "On 2023-01-01 the Constitution of World Aquatics came into force."
        },
        {
            "date": "2023-01-01",
            "content": "On 2023-01-01 the new composition of the Bureau as set out in Article 14 came into effect with the new additional positions within the Bureau."
        }
    ]
    
    # Display timeline items
    for item in timeline_data:
        with st.container():
            st.markdown(f"""
            <div class="timeline-item">
                <span class="timeline-date">{item['date']}</span>
                <div class="timeline-content">{item['content']}</div>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    # Table view
    df = pd.DataFrame(timeline_data)
    df.columns = ["Date", "Event Description"]
    st.dataframe(df, use_container_width=True, hide_index=True)

# Footer space
st.markdown("<br><br>", unsafe_allow_html=True)
