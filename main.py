import streamlit as st
from datetime import datetime
import pandas as pd

# Set page config
st.set_page_config(layout="wide", page_title="Legal Arguments Analysis")

# Custom CSS to maintain similar styling
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        white-space: pre;
        font-size: 1rem;
        color: rgb(107, 114, 128);
        border-radius: 0.5rem;
        padding: 0 1rem;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: rgb(17, 24, 39);
        background-color: rgb(243, 244, 246);
    }
    .stTabs [aria-selected="true"] {
        color: rgb(17, 24, 39);
        border-bottom-color: rgb(37, 99, 235);
    }
    div.block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .fact-item, .supporting-point, .exhibit-item, .case-law-item {
        background-color: rgb(249, 250, 251);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    .counter-argument {
        background-color: rgb(254, 242, 242);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    .response-argument {
        background-color: rgb(239, 246, 255);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Component rendering functions
def render_fact_item(fact, is_disputed, source="", paragraphs="", classified=True):
    with st.container():
        cols = st.columns([3, 1])
        with cols[0]:
            st.markdown(f"""
                <div class="fact-item">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span>📅</span>
                        <p style="margin: 0; color: rgb(55, 65, 81);">{fact}</p>
                    </div>
                    <div style="margin-top: 0.5rem; padding-left: 1.25rem;">
                        <span style="font-size: 0.875rem; color: {'red' if is_disputed else 'green'}">
                            {f'Disputed by {source}' if is_disputed else 'Undisputed'}
                        </span>
                        <span style="font-size: 0.875rem; color: rgb(107, 114, 128); margin-left: 1rem;">
                            ¶{paragraphs}
                        </span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

def render_supporting_point(content, paragraphs, is_legal=True, is_direct=True):
    with st.container():
        st.markdown(f"""
            <div class="supporting-point">
                <div style="display: flex; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; 
                          background-color: {'rgb(219, 234, 254)' if is_legal else 'rgb(220, 252, 231)'};
                          color: {'rgb(30, 64, 175)' if is_legal else 'rgb(22, 101, 52)'};
                          border-radius: 0.25rem;">
                        {'Legal' if is_legal else 'Factual'}
                    </span>
                    {f'<span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: rgb(243, 244, 246); color: rgb(31, 41, 55); border-radius: 0.25rem;">Indirect</span>' if not is_direct else ''}
                </div>
                <p style="margin: 0; color: rgb(55, 65, 81);">{content}</p>
                <span style="font-size: 0.75rem; color: rgb(107, 114, 128); display: block; margin-top: 0.25rem;">
                    ¶{paragraphs}
                </span>
            </div>
        """, unsafe_allow_html=True)

def render_exhibit_item(id, title, summary, citations):
    with st.container():
        st.markdown(f"""
            <div class="exhibit-item">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <p style="margin: 0; font-weight: 500;">{id}: {title}</p>
                        <p style="font-size: 0.875rem; color: rgb(75, 85, 99); margin-top: 0.25rem;">{summary}</p>
                        <div style="margin-top: 0.5rem;">
                            <span style="font-size: 0.75rem; color: rgb(107, 114, 128);">Cited in: </span>
                            {' '.join([f'<span style="font-size: 0.75rem; background-color: rgb(229, 231, 235); border-radius: 0.25rem; padding: 0.125rem 0.5rem; margin-left: 0.25rem;">¶{cite}</span>' for cite in citations])}
                        </div>
                    </div>
                    <button style="background: none; border: none; color: rgb(107, 114, 128); cursor: pointer;">🔗</button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def render_case_law(case_number, paragraphs, summary):
    with st.container():
        st.markdown(f"""
            <div class="case-law-item">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <p style="margin: 0; font-weight: 500;">{case_number}</p>
                        <p style="font-size: 0.875rem; color: rgb(75, 85, 99);">¶{paragraphs}</p>
                        <p style="margin-top: 0.5rem;">{summary}</p>
                    </div>
                    <button style="background: none; border: none; color: rgb(107, 114, 128); cursor: pointer;">🔗</button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def render_sub_argument_section(title, content, points_data):
    with st.expander(title):
        # Overview
        st.markdown("### Overview")
        st.write(content)
        
        # Legal Points
        st.markdown("### Legal Supporting Points")
        st.markdown("#### Direct Legal Points")
        for point in points_data.get('legal_direct', []):
            render_supporting_point(point['content'], point['paragraphs'], is_legal=True, is_direct=True)
            
        if points_data.get('legal_indirect'):
            st.markdown("#### Indirect Legal Points")
            for point in points_data['legal_indirect']:
                render_supporting_point(point['content'], point['paragraphs'], is_legal=True, is_direct=False)
        
        # Factual Points
        st.markdown("### Factual Supporting Points")
        st.markdown("#### Direct Factual Points")
        for point in points_data.get('factual_direct', []):
            render_supporting_point(point['content'], point['paragraphs'], is_legal=False, is_direct=True)
            
        if points_data.get('factual_indirect'):
            st.markdown("#### Indirect Factual Points")
            for point in points_data['factual_indirect']:
                render_supporting_point(point['content'], point['paragraphs'], is_legal=False, is_direct=False)
        
        # Evidence if present
        if points_data.get('evidence'):
            st.markdown("### Evidence")
            for exhibit in points_data['evidence']:
                render_exhibit_item(**exhibit)

def main():
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["📅 Timeline", "⚖️ Arguments", "🔗 Evidence"])
    
    with tab1:
        # Timeline tab content
        st.header("Event Timeline")
        
        # Add filter and export buttons
        col1, col2 = st.columns([8, 2])
        with col2:
            st.button("Show Disputed Only")
            st.download_button("Export", "data", "timeline.xlsx")
        
        timeline_col1, timeline_col2 = st.columns(2)
        
        with timeline_col1:
            st.subheader("Appellant's Timeline")
            render_fact_item(
                "Agreement signed on February 19, 2025",
                False,
                paragraphs="15-16"
            )
            render_fact_item(
                "Notice of Appeal filed on March 1, 2025",
                True,
                source="Respondent",
                paragraphs="17-18"
            )
            
        with timeline_col2:
            st.subheader("Respondent's Timeline")
            render_fact_item(
                "Authorization request filed on February 15, 2025",
                True,
                source="Appellant",
                paragraphs="22-23"
            )

    with tab2:
        # Search and filters
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.text_input("Search arguments...", placeholder="Enter keywords...")
        with col2:
            view_type = st.selectbox("View Type", ["Detailed", "Table"])
        with col3:
            col3_1, col3_2 = st.columns(2)
            with col3_1:
                st.button("📋 Copy")
            with col3_2:
                st.download_button("📥 Export", "data", "arguments.xlsx")

        # Sporting Succession section
        st.header("Sporting Succession")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Appellant's Position")
            
            # General Introduction
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                    Assessment of sporting succession requires comprehensive analysis of multiple 
                    established criteria, including but not limited to the club's name, colors, 
                    logo, and public perception. Each element must be evaluated both independently 
                    and as part of the broader succession context.
                    
                    The analysis follows CAS jurisprudence on sporting succession, particularly 
                    focusing on continuous use and public recognition of club identity elements.
                """)
            
            # Public Perception Analysis
            with st.expander("Public Perception Analysis"):
                st.markdown("### Overview")
                st.write("Public perception strongly supports recognition as sporting successor, demonstrated through consistent fan support and media treatment.")
                
                st.markdown("### Legal Supporting Points")
                render_supporting_point(
                    "Public perception as key factor in CAS jurisprudence",
                    "15-17",
                    is_legal=True
                )
                
                st.markdown("### Factual Supporting Points")
                render_supporting_point(
                    "Consistent media recognition since 1950",
                    "18-19",
                    is_legal=False
                )
                render_supporting_point(
                    "Uninterrupted fan support and recognition",
                    "20-21",
                    is_legal=False,
                    is_direct=False
                )

            # Club Name Analysis
            club_name_data = {
                'legal_direct': [
                    {'content': "Name registration complies with regulations", 'paragraphs': "20-22"},
                    {'content': "Trademark protection since 1960", 'paragraphs': "23-25"}
                ],
                'legal_indirect': [
                    {'content': "Compliance with association naming guidelines", 'paragraphs': "26-27"}
                ],
                'factual_direct': [
                    {'content': "Continuous use of name in official documents since 1950", 'paragraphs': "28-29"},
                    {'content': "Consistent media references under same name", 'paragraphs': "30-31"}
                ],
                'factual_indirect': [
                    {'content': "Fan recognition and merchandise sales under the name", 'paragraphs': "32-33"}
                ],
                'evidence': [
                    {
                        'id': "A-1",
                        'title': "Historical Registration Documents",
                        'summary': "Official records showing continuous name usage since 1950",
                        'citations': ["20", "21", "24"]
                    }
                ]
            }
            render_sub_argument_section("1. Club Name Analysis", 
                "Analysis of the club name demonstrates clear historical continuity and legal protection of naming rights.",
                club_name_data)

            # Counter-Arguments section
            with st.expander("Counter-Arguments"):
                st.markdown("""
                    <div class="counter-argument">
                        <p>Respondent argues that minor variations in name usage and registration gaps weaken the continuity claim.</p>
                        
                        <div style="margin-top: 1rem;">
                            <span style="font-size: 0.75rem; padding: 0.25rem 0.75rem; background-color: rgb(254, 226, 226); color: rgb(185, 28, 28); border-radius: 0.25rem;">
                                Registration lapse during 1975-1976
                            </span>
                            <span style="font-size: 0.75rem; color: rgb(107, 114, 128); margin-left: 0.5rem;">
                                ¶34-35
                            </span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            # Response to Counter-Arguments
            with st.expander("Response to Counter-Arguments"):
                st.markdown("""
                    <div class="response-argument">
                        <p>Brief administrative gap does not negate decades of consistent usage and recognition.</p>
                        
                        <div style="margin-top: 1rem;">
                            <span style="font-size: 0.75rem; padding: 0.25rem 0.75rem; background-color: rgb(219, 234, 254); color: rgb(29, 78, 216); border-radius: 0.25rem;">
                                Administrative gap explained by force majeure
                            </span>
                            <span style="font-size: 0.75rem; color: rgb(107, 114, 128); margin-left: 0.5rem;">
                                ¶36-37
                            </span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            # Case Law
            with st.expander("Case Law"):
                render_case_law(
                    "CAS 2016/A/4576",
                    "45-48",
                    "Establishes key factors for determining sporting succession"
                )

        with col2:
            st.subheader("Respondent's Position")
            
            # General Introduction
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                    Sporting succession analysis must consider practical realities beyond superficial 
                    similarities. Historical gaps and substantive changes in operations preclude 
                    finding of succession.
                    
                    Recent CAS jurisprudence emphasizes the need for continuous operational 
                    connection, not merely similar identifying elements.
                """)
            
            # Public Perception Analysis
            with st.expander("Public Perception Analysis"):
                st.markdown("### Overview")
                st.write("Public perception alone insufficient to establish sporting succession; substantial operational discontinuities override superficial recognition.")
                
                st.markdown("### Legal Supporting Points")
                render_supporting_point(
                    "CAS jurisprudence: public perception secondary to operational continuity",
                    "40-42",
                    is_legal=True
                )
                render_supporting_point(
                    "Legal precedent requiring comprehensive analysis beyond public opinion",
                    "43-44",
                    is_legal=True
                )
                
                st.markdown("### Factual Supporting Points")
                render_supporting_point(
                    "Media coverage gaps between 1975-1976",
                    "45-46",
                    is_legal=False
                )
                render_supporting_point(
                    "Fan support divided between multiple claiming entities",
                    "47-48",
                    is_legal=False
                )

            # Club Name Analysis Response
            club_name_response_data = {
                'legal_direct': [
                    {'content': "Name registration voided during 1975-1976 period", 'paragraphs': "50-52"},
                    {'content': "Trademark protection lapsed and obtained by different entity", 'paragraphs': "53-55"}
                ],
                'evidence': [
                    {
                        'id': "R-1",
                        'title': "Historical Registration Records",
                        'summary': "Documents showing registration gaps and changes",
                        'citations': ["50", "51", "54"]
                    }
                ]
            }
            render_sub_argument_section("1. Club Name Analysis Response",
                "Direct response to alleged name continuity, highlighting registration gaps and unauthorized usage.",
                club_name_response_data)

            # Case Law
            with st.expander("Case Law"):
                render_case_law(
                    "CAS 2017/A/5465",
                    "55-58",
                    "Establishes primacy of operational continuity over superficial similarities"
                )

    with tab3:
        # Evidence tab content
        st.header("Evidence Summary")
        col1, col2 = st.columns([8, 2])
        with col2:
            st.download_button("📥 Export", "data", "evidence.xlsx")
        
        evidence_col1, evidence_col2 = st.columns(2)
        
        with evidence_col1:
            st.subheader("Appellant's Exhibits")
            render_exhibit_item(
                "A-1",
                "Historical Registration Documents",
                "Official records showing club name usage since 1950",
                ["20", "21", "24"]
            )
            render_exhibit_item(
                "A-2",
                "Media Archive Collection",
                "Press coverage demonstrating consistent name usage",
                ["28", "29", "30"]
            )
            
        with evidence_col2:
            st.subheader("Respondent's Exhibits")
            render_exhibit_item(
                "R-1",
                "Historical Registration Records",
                "Documents showing registration gaps and changes",
                ["50", "51", "54"]
            )
            render_exhibit_item(
                "R-2",
                "Historical Color Documentation",
                "Records showing variations in club colors",
                ["66", "67", "68"]
            )

if __name__ == "__main__":
    main()
