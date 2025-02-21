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
    }
    .sub-argument-content {
        padding: 1rem;
        border-top: 1px solid rgb(229, 231, 235);
    }
    </style>
""", unsafe_allow_html=True)

# Component rendering functions from before...
[Previous render_fact_item, render_supporting_point, and render_exhibit_item functions remain the same]

def render_case_law(case_number, paragraphs, summary):
    with st.container():
        st.markdown(f"""
            <div class="case-law-item">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <p style="margin: 0; font-weight: 500;">{case_number}</p>
                        <p style="font-size: 0.75rem; color: rgb(75, 85, 99); margin-top: 0.25rem;">
                            ¶{paragraphs}
                        </p>
                        <p style="margin-top: 0.5rem; color: rgb(55, 65, 81);">{summary}</p>
                    </div>
                    <button style="background: none; border: none; color: rgb(107, 114, 128); cursor: pointer;">🔗</button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def render_sub_argument_section(title, paragraphs):
    with st.expander(f"{title} (¶{paragraphs})", expanded=False):
        return st.container()

def main():
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["📅 Timeline", "⚖️ Arguments", "🔗 Evidence"])
    
    with tab1:
        # [Timeline tab content remains the same]
        pass

    with tab2:
        # Search and filters
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.text_input("Search arguments...", placeholder="Enter keywords...")
        with col2:
            st.selectbox("View Type", ["Detailed", "Table"])
        with col3:
            col3_1, col3_2 = st.columns(2)
            with col3_1:
                st.button("📋 Copy")
            with col3_2:
                st.download_button("📥 Export", "data", "arguments.xlsx")

        # Arguments content
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
                st.write("""
                    Public perception strongly supports recognition as sporting successor, 
                    demonstrated through consistent fan support and media treatment.
                """)
                
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

            # Detailed Analysis
            st.markdown("### Detailed Analysis")
            
            # Club Name Analysis
            with render_sub_argument_section("1. Club Name Analysis", "20-45"):
                st.markdown("#### Overview")
                st.write("Analysis of the club name demonstrates clear historical continuity and legal protection of naming rights.")
                
                st.markdown("#### Direct Legal Points")
                render_supporting_point(
                    "Name registration complies with regulations",
                    "20-22",
                    is_legal=True
                )
                render_supporting_point(
                    "Trademark protection since 1960",
                    "23-25",
                    is_legal=True
                )
                
                st.markdown("#### Direct Factual Points")
                render_supporting_point(
                    "Continuous use of name in official documents since 1950",
                    "28-29",
                    is_legal=False
                )
                
                st.markdown("#### Evidence")
                render_exhibit_item(
                    "A-1",
                    "Historical Registration Documents",
                    "Official records showing continuous name usage since 1950",
                    ["20", "21", "24"]
                )
                
                st.markdown("#### Counter-Arguments")
                st.markdown("""
                    <div style="background-color: rgb(254, 242, 242); padding: 1rem; border-radius: 0.5rem;">
                        <p>Respondent argues that minor variations in name usage and registration gaps weaken the continuity claim.</p>
                    </div>
                """, unsafe_allow_html=True)
                render_supporting_point(
                    "Registration lapse during 1975-1976",
                    "34-35",
                    is_legal=True
                )

            # Club Colors Analysis
            with render_sub_argument_section("2. Club Colors Analysis", "46-65"):
                st.markdown("#### Overview")
                st.write("Club colors represent a fundamental element of identity, maintained consistently since establishment.")
                
                st.markdown("#### Direct Legal Points")
                render_supporting_point(
                    "Color trademark registration",
                    "46-48",
                    is_legal=True
                )

            # Club Logo Analysis
            with render_sub_argument_section("3. Club Logo Analysis", "66-85"):
                st.markdown("#### Overview")
                st.write("Logo maintains core elements demonstrating succession despite minor modernization.")
                
                st.markdown("#### Direct Legal Points")
                render_supporting_point(
                    "Logo trademark protection",
                    "66-68",
                    is_legal=True
                )

            # Case Law
            st.markdown("### Case Law")
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
                st.write("""
                    Public perception alone insufficient to establish sporting succession; 
                    substantial operational discontinuities override superficial recognition.
                """)
                
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

            # Detailed Analysis
            st.markdown("### Detailed Analysis")
            
            # Club Name Analysis Response
            with render_sub_argument_section("1. Club Name Analysis Response", "50-65"):
                st.markdown("#### Overview")
                st.write("Direct response to alleged name continuity, highlighting registration gaps and unauthorized usage.")
                
                st.markdown("#### Direct Legal Points")
                render_supporting_point(
                    "Name registration voided during 1975-1976 period",
                    "50-52",
                    is_legal=True
                )
                
                st.markdown("#### Evidence")
                render_exhibit_item(
                    "R-1",
                    "Historical Registration Records",
                    "Documents showing registration gaps and changes",
                    ["50", "51", "54"]
                )

            # Case Law
            st.markdown("### Case Law")
            render_case_law(
                "CAS 2017/A/5465",
                "55-58",
                "Establishes primacy of operational continuity over superficial similarities"
            )

    with tab3:
        st.header("Evidence Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
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
            
        with col2:
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
