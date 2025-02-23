import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .container {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        background-color: #f9fafb;
    }
    .header {
        margin-bottom: 16px;
        font-weight: 600;
    }
    .subheader {
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 12px;
        color: #374151;
    }
    .content {
        font-size: 14px;
        color: #4b5563;
        margin-bottom: 12px;
    }
    .badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    .badge-legal {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .badge-factual {
        background-color: #dcfce7;
        color: #15803d;
    }
    .paragraph-ref {
        color: #6b7280;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

def render_supporting_point(content, paragraphs, point_type="legal", is_direct=True):
    badge_class = "badge-legal" if point_type == "legal" else "badge-factual"
    point_type_text = "Legal" if point_type == "legal" else "Factual"
    
    st.markdown(f"""
        <div class="container">
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <span class="badge {badge_class}">{point_type_text}</span>
                {"" if is_direct else '<span class="badge" style="background-color: #f3f4f6; color: #374151;">Indirect</span>'}
            </div>
            <div class="content">{content}</div>
            <div class="paragraph-ref">¶{paragraphs}</div>
        </div>
    """, unsafe_allow_html=True)

def render_argument_section(title, content):
    st.markdown(f'<div class="header">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="content">{content}</div>', unsafe_allow_html=True)

def render_exhibit_item(id, title, summary, citations):
    st.markdown(f"""
        <div class="container">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div>
                    <p style="font-size: 14px; font-weight: 500;">{id}: {title}</p>
                    <p style="font-size: 12px; color: #6b7280; margin-top: 4px;">{summary}</p>
                    <div style="margin-top: 8px;">
                        <span style="font-size: 12px; color: #6b7280;">Cited in: </span>
                        {"".join([f'<span style="font-size: 12px; background-color: #f3f4f6; border-radius: 4px; padding: 4px 8px; margin-left: 4px;">¶{cite}</span>' for cite in citations])}
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main application layout
st.title("Arguments Analysis Interface")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Timeline", "Arguments", "Evidence"])

with tab2:  # Arguments tab
    # Arguments view selector
    col_search, col_view, col_export = st.columns([4, 2, 4])
    
    with col_search:
        st.text_input("🔍 Search arguments...", placeholder="Search...")
    
    with col_view:
        view_type = st.radio("View:", ["Detailed", "Table"], horizontal=True)
    
    with col_export:
        col_copy, col_export = st.columns(2)
        with col_copy:
            st.button("📋 Copy")
        with col_export:
            st.button("📥 Export to Excel")

    # Main argument content
    if view_type == "Detailed":
        with st.expander("Sporting Succession ¶15-18", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<h3 style="color: #2563eb; font-weight: 600; margin-bottom: 24px;">Appellant\'s Position</h3>', unsafe_allow_html=True)
                
                # General Introduction
                with st.expander("General Introduction", expanded=True):
                    st.markdown("""
                        Assessment of sporting succession requires comprehensive analysis of multiple established criteria, 
                        including but not limited to the club's name, colors, logo, and public perception. Each element 
                        must be evaluated both independently and as part of the broader succession context.
                        
                        The analysis follows CAS jurisprudence on sporting succession, particularly focusing on continuous 
                        use and public recognition of club identity elements.
                    """)
                
                # Public Perception Analysis
                with st.expander("Public Perception Analysis", expanded=True):
                    render_argument_section("Overview", 
                        "Public perception strongly supports recognition as sporting successor, demonstrated through consistent fan support and media treatment.")
                    
                    st.markdown('<div class="subheader">Legal Supporting Points</div>', unsafe_allow_html=True)
                    render_supporting_point(
                        "Public perception as key factor in CAS jurisprudence",
                        "15-17",
                        "legal",
                        True
                    )
                    
                    st.markdown('<div class="subheader">Factual Supporting Points</div>', unsafe_allow_html=True)
                    render_supporting_point(
                        "Consistent media recognition since 1950",
                        "18-19",
                        "factual",
                        True
                    )
                    render_supporting_point(
                        "Uninterrupted fan support and recognition",
                        "20-21",
                        "factual",
                        False
                    )
                    
                    st.markdown('<div class="subheader">Evidence</div>', unsafe_allow_html=True)
                    render_exhibit_item(
                        "A-1",
                        "Historical Registration Documents",
                        "Official records showing continuous name usage since 1950",
                        ["20", "21", "24"]
                    )
            
            with col2:
                st.markdown('<h3 style="color: #dc2626; font-weight: 600; margin-bottom: 24px;">Respondent\'s Position</h3>', unsafe_allow_html=True)
                
                # General Introduction
                with st.expander("General Introduction", expanded=True):
                    st.markdown("""
                        Sporting succession analysis must consider practical realities beyond superficial similarities. 
                        Historical gaps and substantive changes in operations preclude finding of succession.
                        
                        Recent CAS jurisprudence emphasizes the need for continuous operational connection, not merely 
                        similar identifying elements.
                    """)
                
                # Public Perception Analysis
                with st.expander("Public Perception Analysis", expanded=True):
                    render_argument_section("Overview", 
                        "Public perception alone insufficient to establish sporting succession; substantial operational discontinuities override superficial recognition.")
                    
                    st.markdown('<div class="subheader">Legal Supporting Points</div>', unsafe_allow_html=True)
                    render_supporting_point(
                        "CAS jurisprudence: public perception secondary to operational continuity",
                        "40-42",
                        "legal",
                        True
                    )
                    render_supporting_point(
                        "Legal precedent requiring comprehensive analysis beyond public opinion",
                        "43-44",
                        "legal",
                        True
                    )
                    
                    st.markdown('<div class="subheader">Factual Supporting Points</div>', unsafe_allow_html=True)
                    render_supporting_point(
                        "Media coverage gaps between 1975-1976",
                        "45-46",
                        "factual",
                        True
                    )
                    render_supporting_point(
                        "Fan support divided between multiple claiming entities",
                        "47-48",
                        "factual",
                        True
                    )
                    
                    st.markdown('<div class="subheader">Evidence</div>', unsafe_allow_html=True)
                    render_exhibit_item(
                        "R-1",
                        "Historical Documentation",
                        "Records showing operational discontinuities",
                        ["45", "46", "48"]
                    )
    else:
        # Table view
        df = pd.DataFrame({
            'Issue': ['Jurisdiction', 'Public Perception', 'Name Continuity'],
            'Appellant Position': [
                'Cast has jurisdiction based on signed agreement',
                'Strong public recognition supports succession',
                'Continuous use of name since 1950'
            ],
            'Respondent Position': [
                'Cast lacks jurisdiction due to proper notice',
                'Public perception insufficient without operational continuity',
                'Registration gaps invalidate continuity claim'
            ]
        })
        st.dataframe(df, use_container_width=True)
