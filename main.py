import streamlit as st
import pandas as pd
from datetime import datetime

def render_fact_item(fact, is_disputed, source=None, paragraphs=None, classified=True):
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"📅 {fact}")
            if not classified:
                st.markdown("🏷️ **Unclassified**")
        with col2:
            if is_disputed:
                st.markdown(f"❌ Disputed by {source}")
            else:
                st.markdown("✅ Undisputed")
            if paragraphs:
                st.markdown(f"¶{paragraphs}")
        st.markdown("---")

def render_supporting_point(content, paragraphs, is_legal=True, is_direct=True):
    with st.container():
        cols = st.columns([2, 2, 4])
        with cols[0]:
            st.markdown("🔷 Legal" if is_legal else "📊 Factual")
        with cols[1]:
            if not is_direct:
                st.markdown("↪️ Indirect")
        st.markdown(content)
        st.markdown(f"¶{paragraphs}")
        st.markdown("---")

def render_exhibit_item(id, title, summary, citations):
    with st.container():
        st.markdown(f"**{id}: {title}**")
        st.markdown(summary)
        citation_text = ", ".join([f"¶{cite}" for cite in citations])
        st.markdown(f"*Cited in: {citation_text}*")
        st.markdown("---")

def main():
    st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")
    st.title("Legal Arguments Analysis Interface")

    # Main tabs
    tab1, tab2, tab3 = st.tabs(["📅 Timeline", "⚖️ Arguments", "📑 Evidence"])

    with tab1:
        st.header("Event Timeline")
        
        # Filter and Export buttons in the same row
        col1, col2 = st.columns([3, 1])
        with col1:
            show_disputed = st.checkbox("Show Disputed Only")
        with col2:
            st.download_button("📥 Export", "timeline_data", "timeline.csv")

        # Timeline columns
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
                "Respondent",
                "17-18"
            )

        with timeline_col2:
            st.subheader("Respondent's Timeline")
            render_fact_item(
                "Authorization request filed on February 15, 2025",
                True,
                "Appellant",
                "22-23"
            )

    with tab2:
        st.header("Arguments Analysis")
        
        # Search and view type selection
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            search_query = st.text_input("🔍 Search arguments...")
        with col2:
            view_type = st.selectbox("View Type", ["Detailed", "Table"])
        with col3:
            st.download_button("📥 Export to Excel", "arguments_data", "arguments.xlsx")

        # Sporting Succession section
        with st.expander("Sporting Succession ¶15-18"):
            arg_col1, arg_col2 = st.columns(2)
            
            with arg_col1:
                st.subheader("Appellant's Position")
                
                # General Introduction
                st.markdown("### General Introduction")
                st.markdown("""
                Assessment of sporting succession requires comprehensive analysis of multiple 
                established criteria, including but not limited to the club's name, colors, 
                logo, and public perception.
                """)

                # Public Perception Analysis
                with st.expander("Public Perception Analysis"):
                    st.markdown("#### Overview")
                    st.markdown("Public perception strongly supports recognition as sporting successor.")
                    
                    st.markdown("#### Legal Supporting Points")
                    render_supporting_point(
                        "Public perception as key factor in CAS jurisprudence",
                        "15-17",
                        is_legal=True
                    )
                    
                    st.markdown("#### Factual Supporting Points")
                    render_supporting_point(
                        "Consistent media recognition since 1950",
                        "18-19",
                        is_legal=False
                    )

                # Club Name Analysis
                with st.expander("1. Club Name Analysis ¶20-45"):
                    st.markdown("#### Overview")
                    st.markdown("Analysis of club name demonstrates clear historical continuity.")
                    
                    st.markdown("#### Legal Supporting Points")
                    render_supporting_point(
                        "Name registration complies with regulations",
                        "20-22",
                        is_legal=True
                    )
                    
                    st.markdown("#### Evidence")
                    render_exhibit_item(
                        "A-1",
                        "Historical Registration Documents",
                        "Official records showing continuous name usage since 1950",
                        ["20", "21", "24"]
                    )

            with arg_col2:
                st.subheader("Respondent's Position")
                
                # General Introduction
                st.markdown("### General Introduction")
                st.markdown("""
                Sporting succession analysis must consider practical realities beyond 
                superficial similarities. Historical gaps and substantive changes in 
                operations preclude finding of succession.
                """)

                # Public Perception Analysis Response
                with st.expander("Public Perception Analysis Response"):
                    st.markdown("#### Overview")
                    st.markdown("Public perception alone insufficient to establish sporting succession.")
                    
                    st.markdown("#### Legal Supporting Points")
                    render_supporting_point(
                        "CAS jurisprudence: public perception secondary to operational continuity",
                        "40-42",
                        is_legal=True
                    )

    with tab3:
        st.header("Evidence Summary")
        
        evidence_col1, evidence_col2 = st.columns(2)
        
        with evidence_col1:
            st.subheader("Appellant's Exhibits")
            render_exhibit_item(
                "A-1",
                "Historical Registration Documents",
                "Official records showing club name usage since 1950",
                ["20", "21", "24"]
            )
            
        with evidence_col2:
            st.subheader("Respondent's Exhibits")
            render_exhibit_item(
                "R-1",
                "Historical Color Documentation",
                "Records showing changes in club colors",
                ["63", "64", "65"]
            )

if __name__ == "__main__":
    main()
