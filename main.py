import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main-content {
        display: flex;
        flex-direction: row;
    }
    .sidebar {
        width: 25%;
        background-color: #f5f7f9;
        padding: 20px;
        border-right: 1px solid #e6e9ef;
        height: 100vh;
    }
    .document-content {
        width: 75%;
        padding: 20px;
    }
    .menu-item {
        background-color: white;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .argument-section {
        border: 1px solid #e6e9ef;
        border-radius: 5px;
        margin-bottom: 10px;
        overflow: hidden;
    }
    .section-header {
        padding: 10px 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
    }
    .blue-tag {
        background-color: #e6f0ff;
        color: #4285f4;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8em;
    }
    .red-tag {
        background-color: #ffebe6;
        color: #ea4335;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8em;
    }
    .position-title {
        color: #4285f4;
        font-size: 1.5em;
        margin-bottom: 20px;
    }
    .position-title-red {
        color: #ea4335;
        font-size: 1.5em;
        margin-bottom: 20px;
    }
    .fork-button {
        float: right;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Main layout
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.markdown('<h2>Summary of Arguments</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="menu-item">📝 Arguments</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📊 Facts</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📅 Timeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📁 Exhibits</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Fork button and navigation
    st.markdown('<div class="fork-button"><button>Fork</button> <span style="margin-left: 10px;">⚙️</span></div>', unsafe_allow_html=True)
    
    # Create two columns for the positions
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.markdown('<div class="position-title">Appellant\'s Position</div>', unsafe_allow_html=True)
        
        # Sporting Succession
        st.markdown("""
        <div class="argument-section">
            <div class="section-header">
                <span>➤ 1. Sporting Succession</span>
                <span class="blue-tag">§15-18</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Club Name Analysis
        st.markdown("""
        <div class="argument-section" style="margin-left: 20px;">
            <div class="section-header">
                <span>➤ 1.1. Club Name Analysis</span>
                <span class="blue-tag">§20-45</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Registration History
        st.markdown("""
        <div class="argument-section" style="margin-left: 40px;">
            <div class="section-header">
                <span>➤ 1.1.1. Registration History</span>
                <span class="blue-tag">§25-30</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Club Colors Analysis
        st.markdown("""
        <div class="argument-section" style="margin-left: 20px;">
            <div class="section-header">
                <span>➤ 1.2. Club Colors Analysis</span>
                <span class="blue-tag">§46-65</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Color Variations Analysis
        st.markdown("""
        <div class="argument-section" style="margin-left: 40px;">
            <div class="section-header">
                <span>➤ 1.2.1. Color Variations Analysis</span>
                <span class="blue-tag">§56-60</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Historical Color Documentation
        st.markdown("""
        <div class="argument-section" style="margin-left: 60px;">
            <div class="section-header">
                <span>➤ 1.2.1.1. Historical Color Documentation</span>
                <span class="blue-tag">§61-65</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with right_col:
        st.markdown('<div class="position-title-red">Respondent\'s Position</div>', unsafe_allow_html=True)
        
        # Sporting Succession Rebuttal
        st.markdown("""
        <div class="argument-section">
            <div class="section-header">
                <span>➤ 1. Sporting Succession Rebuttal</span>
                <span class="red-tag">§200-218</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Club Name Analysis Rebuttal
        st.markdown("""
        <div class="argument-section" style="margin-left: 20px;">
            <div class="section-header">
                <span>➤ 1.1. Club Name Analysis Rebuttal</span>
                <span class="red-tag">§220-240</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Registration Gap Evidence
        st.markdown("""
        <div class="argument-section" style="margin-left: 40px;">
            <div class="section-header">
                <span>➤ 1.1.1. Registration Gap Evidence</span>
                <span class="red-tag">§226-230</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Club Colors Analysis Rebuttal
        st.markdown("""
        <div class="argument-section" style="margin-left: 20px;">
            <div class="section-header">
                <span>➤ 1.2. Club Colors Analysis Rebuttal</span>
                <span class="red-tag">§241-249</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Color Changes Analysis
        st.markdown("""
        <div class="argument-section" style="margin-left: 40px;">
            <div class="section-header">
                <span>➤ 1.2.1. Color Changes Analysis</span>
                <span class="red-tag">§247-249</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Color Identity Documentation
        st.markdown("""
        <div class="argument-section" style="margin-left: 60px;">
            <div class="section-header">
                <span>➤ 1.2.1.1. Color Identity Documentation</span>
                <span class="red-tag">§250-255</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Add footer icons
st.markdown('<div style="position: fixed; bottom: 20px; right: 20px;"><span>🏆</span> <span style="margin-left: 20px;">🔍</span></div>', unsafe_allow_html=True)
