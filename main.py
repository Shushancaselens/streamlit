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
    .legal-tag {
        font-size: 0.75rem;
        padding: 0.125rem 0.5rem;
        background-color: rgb(219, 234, 254);
        color: rgb(30, 64, 175);
        border-radius: 0.25rem;
    }
    .factual-tag {
        font-size: 0.75rem;
        padding: 0.125rem 0.5rem;
        background-color: rgb(220, 252, 231);
        color: rgb(22, 101, 52);
        border-radius: 0.25rem;
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
                    <span class="{'legal-tag' if is_legal else 'factual-tag'}">
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
    # [Rest of the main function content remains the same as in the previous version]
    pass

if __name__ == "__main__":
    main()
