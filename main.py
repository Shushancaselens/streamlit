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
    .fact-item {
        background-color: rgb(249, 250, 251);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    .supporting-point {
        background-color: rgb(249, 250, 251);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    .exhibit-item {
        background-color: rgb(249, 250, 251);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 0.75rem;
    }
    </style>
""", unsafe_allow_html=True)

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

def main():
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["📅 Timeline", "⚖️ Arguments", "🔗 Evidence"])
    
    with tab1:
        st.header("Event Timeline")
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
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.text_input("Search arguments...", placeholder="Enter keywords...")
        with col2:
            st.selectbox("View Type", ["Detailed", "Table"])
        with col3:
            st.download_button("Export to Excel", "data", "arguments.xlsx")

        # Arguments content
        st.header("Sporting Succession")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Appellant's Position")
            
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                    Assessment of sporting succession requires comprehensive analysis of multiple 
                    established criteria, including but not limited to the club's name, colors, 
                    logo, and public perception.
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

        with col2:
            st.subheader("Respondent's Position")
            
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                    Sporting succession analysis must consider practical realities beyond 
                    superficial similarities. Historical gaps and substantive changes in 
                    operations preclude finding of succession.
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

            with st.expander("Key Facts"):
                render_fact_item(
                    "Significant changes in club identity since 1975",
                    True,
                    source="Appellant",
                    paragraphs="30-31"
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
            
        with col2:
            st.subheader("Respondent's Exhibits")
            render_exhibit_item(
                "R-1",
                "Historical Color Documentation",
                "Records showing changes in club colors",
                ["63", "64", "65"]
            )

if __name__ == "__main__":
    main()
