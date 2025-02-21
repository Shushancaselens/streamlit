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
    .sub-argument {
        border: 1px solid rgb(229, 231, 235);
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .sub-argument-header {
        background-color: rgb(249, 250, 251);
        padding: 0.75rem;
        cursor: pointer;
        border-top-left-radius: 0.5rem;
        border-top-right-radius: 0.5rem;
    }
    .counter-argument {
        background-color: rgb(254, 242, 242);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .response-argument {
        background-color: rgb(239, 246, 255);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def render_fact_item(fact, is_disputed, source="", paragraphs="", classified=True):
    with st.container():
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
                        <p style="font-size: 0.875rem; color: rgb(75, 85, 99); margin-top: 0.25rem;">
                            ¶{paragraphs}
                        </p>
                        <p style="margin-top: 0.5rem; color: rgb(55, 65, 81);">{summary}</p>
                    </div>
                    <button style="background: none; border: none; color: rgb(107, 114, 128); cursor: pointer;">🔗</button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def render_sub_argument_section(title, overview_text):
    with st.expander(title, expanded=False):
        st.markdown("### Overview")
        st.markdown(overview_text)
        
        st.markdown("### Legal Supporting Points")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Direct Legal Points")
            render_supporting_point(
                "Name registration complies with regulations",
                "20-22",
                is_legal=True,
                is_direct=True
            )
        with col2:
            st.markdown("#### Indirect Legal Points")
            render_supporting_point(
                "Compliance with association naming guidelines",
                "26-27",
                is_legal=True,
                is_direct=False
            )
        
        st.markdown("### Factual Supporting Points")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Direct Factual Points")
            render_supporting_point(
                "Continuous use of name in official documents since 1950",
                "28-29",
                is_legal=False,
                is_direct=True
            )
        with col2:
            st.markdown("#### Indirect Factual Points")
            render_supporting_point(
                "Fan recognition and merchandise sales under the name",
                "32-33",
                is_legal=False,
                is_direct=False
            )
        
        st.markdown("### Evidence")
        render_exhibit_item(
            "A-1",
            "Historical Registration Documents",
            "Official records showing continuous name usage since 1950",
            ["20", "21", "24"]
        )
        
        st.markdown("### Counter-Arguments")
        with st.container():
            st.markdown("""
                <div class="counter-argument">
                    <p>Respondent argues that minor variations in name usage and registration gaps weaken the continuity claim.</p>
                </div>
            """, unsafe_allow_html=True)
            render_supporting_point(
                "Registration lapse during 1975-1976",
                "34-35",
                is_legal=True,
                is_direct=True
            )
        
        st.markdown("### Response to Counter-Arguments")
        with st.container():
            st.markdown("""
                <div class="response-argument">
                    <p>Brief administrative gap does not negate decades of consistent usage and recognition.</p>
                </div>
            """, unsafe_allow_html=True)
            render_supporting_point(
                "Administrative gap explained by force majeure",
                "36-37",
                is_legal=True,
                is_direct=True
            )

def main():
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["📅 Timeline", "⚖️ Arguments", "🔗 Evidence"])
    
    with tab1:
        col1, col2, col3 = st.columns([6, 2, 2])
        with col1:
            st.header("Event Timeline")
        with col2:
            st.button("📊 Show Disputed Only")
        with col3:
            st.download_button("📥 Export", "data", "timeline.csv")
            
        col1, col2 = st.columns(2)
        
        with col1:
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
            
        with col2:
            st.subheader("Respondent's Timeline")
            render_fact_item(
                "Authorization request filed on February 15, 2025",
                True,
                source="Appellant",
                paragraphs="22-23"
            )

    with tab2:
        # Search and view options
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.text_input("🔍 Search arguments...", placeholder="Enter keywords...")
        with col2:
            st.selectbox("View Type", ["Detailed", "Table"])
        with col3:
            st.button("📋 Copy")
        with col4:
            st.download_button("📥 Export to Excel", "data", "arguments.xlsx")

        # Arguments content
        st.header("Sporting Succession")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Appellant's Position")
            
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                    Assessment of sporting succession requires comprehensive analysis of multiple 
                    established criteria, including but not limited to the club's name, colors, 
                    logo, and public perception. Each element must be evaluated both independently 
                    and as part of the broader succession context.
                    
                    The analysis follows CAS jurisprudence on sporting succession, particularly 
                    focusing on continuous use and public recognition of club identity elements.
                """)
                
            with st.expander("Public Perception Analysis"):
                st.markdown("### Overview")
                st.write("Public perception strongly supports recognition as sporting successor.")
                
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

            with st.expander("Key Facts"):
                render_fact_item(
                    "Club has maintained same name since 1950",
                    False,
                    paragraphs="20-21"
                )
                render_fact_item(
                    "Colors and logo unchanged since founding",
                    True,
                    source="Respondent",
                    paragraphs="22-23"
                )
                render_fact_item(
                    "Continuous fan support and membership records",
                    False,
                    paragraphs="24-25"
                )

            render_sub_argument_section(
                "1. Club Name Analysis",
                "Analysis of the club name demonstrates clear historical continuity and legal protection of naming rights."
            )
            
            render_sub_argument_section(
                "2. Club Colors Analysis",
                "Club colors represent a fundamental element of identity, maintained consistently since establishment."
            )
            
            render_sub_argument_section(
                "3. Club Logo Analysis",
                "Logo maintains core elements demonstrating succession despite minor modernization."
            )

            st.markdown("### Case Law")
            render_case_law(
                "CAS 2016/A/4576",
                "45-48",
                "Establishes key factors for determining sporting succession"
            )

        with col2:
            st.subheader("Respondent's Position")
            
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                    Sporting succession analysis must consider practical realities beyond 
                    superficial similarities. Historical gaps and substantive changes in 
                    operations preclude finding of succession.
                    
                    Recent CAS jurisprudence emphasizes the need for continuous operational 
                    connection, not merely similar identifying elements.
                """)
                
            with st.expander("Public Perception Analysis"):
                st.markdown("### Overview")
                st.write("Public perception alone insufficient to establish sporting succession.")
                
                st.markdown("### Legal Supporting Points")
                render_supporting_point(
                    "CAS jurisprudence: public perception secondary to operational continuity",
                    "40-42",
                    is_legal=True
                )
                render_supporting_point(
                    "Legal precedent
