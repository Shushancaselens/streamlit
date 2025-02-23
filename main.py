import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(layout="wide")

# Custom CSS to match shadcn/ui styling
st.markdown("""
<style>
    /* Card styles to match shadcn/ui */
    div[data-testid="stExpander"] {
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background-color: white;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        height: 2.5rem;
        padding: 0 1rem;
        background-color: transparent;
        border: 1px solid #e5e7eb;
        border-radius: 0.375rem;
        color: #374151;
        font-weight: 500;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #2563eb;
    }

    /* Supporting point tags */
    .tag {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 0.5rem;
    }

    .legal {
        background-color: #dbeafe;
        color: #1e40af;
    }

    .factual {
        background-color: #dcfce7;
        color: #166534;
    }

    .indirect {
        background-color: #f3f4f6;
        color: #374151;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session states
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'facts'
if 'expanded_arguments' not in st.session_state:
    st.session_state.expanded_arguments = {}
if 'expanded_sub_arguments' not in st.session_state:
    st.session_state.expanded_sub_arguments = {}
if 'show_only_disputed' not in st.session_state:
    st.session_state.show_only_disputed = False
if 'view_type' not in st.session_state:
    st.session_state.view_type = 'detailed'

# Header section with search and buttons
def render_argument_header():
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        st.text_input("Search arguments...", key="search_args")
    with col2:
        st.selectbox("View", ["Detailed", "Table"], key="view_selector")
    with col3:
        col3_1, col3_2 = st.columns(2)
        with col3_1:
            st.button("Copy")
        with col3_2:
            st.button("Export to Excel")

def render_fact_item(fact, is_disputed, source=None, paragraphs=None, classified=True):
    html = f"""
    <div class="bg-gray-50 rounded-lg p-3 mb-2">
        <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
                <span>📅</span>
                <p class="text-sm text-gray-700">{fact}</p>
            </div>
            {"" if classified else '<span class="tag">Unclassified</span>'}
        </div>
        <div class="flex items-center justify-between mt-1 pl-5">
            <span class="text-xs {'text-red-500' if is_disputed else 'text-green-500'}">
                {f'Disputed by {source}' if is_disputed else 'Undisputed'}
            </span>
            <span class="text-xs text-gray-500">¶{paragraphs}</span>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_supporting_point(content, type_tag, paragraphs, is_legal=True, is_direct=True):
    tags = []
    if is_legal:
        tags.append('<span class="tag legal">Legal</span>')
    else:
        tags.append('<span class="tag factual">Factual</span>')
    if not is_direct:
        tags.append('<span class="tag indirect">Indirect</span>')
    
    html = f"""
    <div class="bg-{type_tag}-50 rounded-lg p-3 mb-2">
        <div class="flex items-center gap-2 mb-1">
            {''.join(tags)}
        </div>
        <p class="text-sm text-gray-700">{content}</p>
        <span class="text-xs text-gray-500 mt-1 block">¶{paragraphs}</span>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_exhibit_item(id, title, summary, citations):
    html = f"""
    <div class="bg-gray-50 rounded-lg p-3 mb-3">
        <div class="flex justify-between items-start">
            <div>
                <p class="text-sm font-medium">{id}: {title}</p>
                <p class="text-xs text-gray-600 mt-1">{summary}</p>
                <div class="mt-2">
                    <span class="text-xs text-gray-500">Cited in: </span>
                    {' '.join([f'<span class="text-xs bg-gray-200 rounded px-2 py-1 ml-1">¶{cite}</span>' for cite in citations])}
                </div>
            </div>
            <button class="h-6">🔗</button>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Main tabs
tabs = st.tabs(["⏱️ Timeline", "⚖️ Arguments", "📎 Evidence"])

with tabs[0]:  # Timeline tab
    st.title("Event Timeline")
    col1, col2 = st.columns([4, 1])
    with col2:
        st.button("Show Disputed Only", key="toggle_disputed")
        st.button("Export", key="export_timeline")
    
    # Timeline content cols
    timeline_col1, timeline_col2 = st.columns(2)
    with timeline_col1:
        st.markdown("### Appellant's Timeline")
        render_fact_item(
            "Agreement signed on February 19, 2025",
            is_disputed=False,
            paragraphs="15-16"
        )
        render_fact_item(
            "Notice of Appeal filed on March 1, 2025",
            is_disputed=True,
            source="Respondent",
            paragraphs="17-18"
        )
    
    with timeline_col2:
        st.markdown("### Respondent's Timeline")
        render_fact_item(
            "Authorization request filed on February 15, 2025",
            is_disputed=True,
            source="Appellant",
            paragraphs="22-23"
        )

with tabs[1]:  # Arguments tab
    render_argument_header()
    
    if st.session_state.view_type == 'detailed':
        st.markdown("### Sporting Succession")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Appellant's Position")
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                Assessment of sporting succession requires comprehensive analysis of multiple established criteria...
                """)
                render_supporting_point(
                    "Public perception as key factor in CAS jurisprudence",
                    "blue",
                    "15-17",
                    is_legal=True
                )
            
            with st.expander("Supporting Points", expanded=True):
                render_supporting_point(
                    "Consistent media recognition since 1950",
                    "green",
                    "18-19",
                    is_legal=False
                )
                render_supporting_point(
                    "Uninterrupted fan support and recognition",
                    "green",
                    "20-21",
                    is_legal=False,
                    is_direct=False
                )
            
            with st.expander("Evidence", expanded=True):
                render_exhibit_item(
                    "A-1",
                    "Historical Registration Documents",
                    "Official records showing continuous name usage since 1950",
                    ["20", "21", "24"]
                )
        
        with col2:
            st.markdown("#### Respondent's Position")
            # Similar structure for respondent's position...

with tabs[2]:  # Evidence tab
    st.title("Evidence Summary")
    evidence_col1, evidence_col2 = st.columns(2)
    
    with evidence_col1:
        st.markdown("### Appellant's Exhibits")
        render_exhibit_item(
            "A-1",
            "Historical Registration Documents",
            "Official records showing club name usage since 1950",
            ["20", "21", "24"]
        )
    
    with evidence_col2:
        st.markdown("### Respondent's Exhibits")
        render_exhibit_item(
            "R-1",
            "Historical Color Documentation",
            "Records showing changes in club colors",
            ["63", "64", "65"]
        )
