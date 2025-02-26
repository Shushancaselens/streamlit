import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Legal Arguments Summary",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stButton button {
        width: 100%;
        text-align: left;
        background-color: white;
        color: black;
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        padding: 10px;
    }
    .appellant-header {
        color: #4285F4;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .respondent-header {
        color: #EA4335;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .appellant-section {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 10px;
        margin: 5px 0;
        border-left: 3px solid #4285F4;
    }
    .respondent-section {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 10px;
        margin: 5px 0;
        border-left: 3px solid #EA4335;
    }
    .blue-page {
        background-color: #e8f0fe;
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.8rem;
        color: #4285F4;
    }
    .red-page {
        background-color: #fce8e6;
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.8rem;
        color: #EA4335;
    }
    .sidebar-section {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 10px;
        text-align: center;
    }
    .icon-text {
        font-size: 0.9rem;
        color: #5f6368;
    }
</style>
""", unsafe_allow_html=True)

# Create the GitHub-style header with fork button
col1, col2, col3 = st.columns([6, 1, 1])
with col3:
    st.markdown("""
    <div style="display: flex; justify-content: flex-end; gap: 10px;">
        <button style="background: none; border: 1px solid #e0e0e0; border-radius: 5px; padding: 5px 10px; cursor: pointer;">
            Fork <span>⑂</span>
        </button>
        <button style="background: none; border: none; padding: 5px; cursor: pointer;">
            ⋮
        </button>
    </div>
    """, unsafe_allow_html=True)

# Layout: sidebar and main content
col_sidebar, col_main = st.columns([1, 4])

# Sidebar
with col_sidebar:
    st.markdown("<h2>Summary of Arguments</h2>", unsafe_allow_html=True)
    
    # Arguments button
    st.markdown("""
    <div class="sidebar-section">
        <div>📄 Arguments</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Facts button
    st.markdown("""
    <div class="sidebar-section">
        <div>📊 Facts</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline button
    st.markdown("""
    <div class="sidebar-section">
        <div>📅 Timeline</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Exhibits button
    st.markdown("""
    <div class="sidebar-section">
        <div>📂 Exhibits</div>
    </div>
    """, unsafe_allow_html=True)

# Main content
with col_main:
    # Two columns for appellant and respondent
    appellant, respondent = st.columns(2)
    
    with appellant:
        st.markdown("<div class='appellant-header'>Appellant's Position</div>", unsafe_allow_html=True)
        
        # 1. Sporting Succession
        st.markdown("""
        <div class="appellant-section">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1. Sporting Succession</div>
                <span class="blue-page">¶15-18</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.1 Club Name Analysis
        st.markdown("""
        <div class="appellant-section" style="margin-left: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.1. Club Name Analysis</div>
                <span class="blue-page">¶20-45</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.1.1 Registration History
        st.markdown("""
        <div class="appellant-section" style="margin-left: 40px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.1.1. Registration History</div>
                <span class="blue-page">¶25-30</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.2 Club Colors Analysis
        st.markdown("""
        <div class="appellant-section" style="margin-left: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.2. Club Colors Analysis</div>
                <span class="blue-page">¶46-65</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.2.1 Color Variations Analysis
        st.markdown("""
        <div class="appellant-section" style="margin-left: 40px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.2.1. Color Variations Analysis</div>
                <span class="blue-page">¶56-60</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.2.1.1 Historical Color Documentation
        st.markdown("""
        <div class="appellant-section" style="margin-left: 60px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.2.1.1. Historical Color Documentation</div>
                <span class="blue-page">¶61-65</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with respondent:
        st.markdown("<div class='respondent-header'>Respondent's Position</div>", unsafe_allow_html=True)
        
        # 1. Sporting Succession Rebuttal
        st.markdown("""
        <div class="respondent-section">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1. Sporting Succession Rebuttal</div>
                <span class="red-page">¶200-218</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.1 Club Name Analysis Rebuttal
        st.markdown("""
        <div class="respondent-section" style="margin-left: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.1. Club Name Analysis Rebuttal</div>
                <span class="red-page">¶220-240</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.1.1 Registration Gap Evidence
        st.markdown("""
        <div class="respondent-section" style="margin-left: 40px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.1.1. Registration Gap Evidence</div>
                <span class="red-page">¶226-230</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.2 Club Colors Analysis Rebuttal
        st.markdown("""
        <div class="respondent-section" style="margin-left: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.2. Club Colors Analysis Rebuttal</div>
                <span class="red-page">¶241-249</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.2.1 Color Changes Analysis
        st.markdown("""
        <div class="respondent-section" style="margin-left: 40px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.2.1. Color Changes Analysis</div>
                <span class="red-page">¶247-249</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 1.2.1.1 Color Identity Documentation
        st.markdown("""
        <div class="respondent-section" style="margin-left: 60px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>➤ 1.2.1.1. Color Identity Documentation</div>
                <span class="red-page">¶250-255</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer area with decorative elements
st.markdown("""
<div style="position: fixed; bottom: 10px; right: 10px;">
    <span style="font-size: 24px; color: #ddd;">⚖️</span>
</div>
""", unsafe_allow_html=True)
