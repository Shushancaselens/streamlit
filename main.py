import streamlit as st
import pandas as pd
from datetime import datetime
import json
import base64
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.app_logo import add_logo
from streamlit_toggle import st_toggle_switch
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="Legal Analysis Interface",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match the original design
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding: 1rem;
        max-width: 1200px;
    }
    
    /* Card styling */
    .stCard {
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        padding: 1rem;
        background-color: white;
        margin-bottom: 1rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 14px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: transparent;
        border-bottom: 2px solid #4f8bf9;
        color: #4f8bf9;
    }
    
    /* Claimant/Respondent styling */
    .claimant-header {
        color: #2563eb; /* Blue */
        font-weight: 600;
        font-size: 1.2rem;
    }
    
    .respondent-header {
        color: #dc2626; /* Red */
        font-weight: 600;
        font-size: 1.2rem;
    }
    
    /* Status badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .disputed {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    
    .undisputed {
        background-color: #dcfce7;
        color: #15803d;
    }
    
    /* Argument section styling */
    .argument-section {
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .argument-header {
        display: flex;
        align-items: center;
        padding: 0.75rem 1rem;
        cursor: pointer;
        background-color: #f9fafb;
    }
    
    .argument-header:hover {
        background-color: #f3f4f6;
    }
    
    .argument-content {
        padding: 1rem;
        border-top: 1px solid #e5e7eb;
    }
    
    /* Exhibit and Timeline table styling */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 1rem;
    }
    
    .styled-table thead th {
        background-color: #f9fafb;
        padding: 0.75rem 1rem;
        text-align: left;
        font-size: 0.875rem;
        font-weight: 500;
        color: #6b7280;
        border-bottom: 1px solid #e5e7eb;
    }
    
    .styled-table tbody td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #e5e7eb;
        font-size: 0.875rem;
    }
    
    /* Header section styling */
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Filter section */
    .filter-section {
        display: flex;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Topic view sections */
    .topic-section {
        margin-bottom: 2rem;
    }
    
    .topic-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1f2937;
    }
    
    .topic-description {
        font-size: 0.875rem;
        color: #6b7280;
        margin-bottom: 1rem;
    }
    
    /* Overrides for Streamlit elements */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: row;
    }
    
    /* Custom badges */
    .party-badge {
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .appellant-badge {
        background-color: #dbeafe;
        color: #1e40af;
    }
    
    .respondent-badge {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    
    .type-badge {
        background-color: #f3f4f6;
        color: #374151;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
    }
    
    /* Override Streamlit's default padding on buttons */
    .stButton button {
        padding: 0.25rem 0.75rem;
        font-size: 0.875rem;
    }
    
    /* Custom expandable container for arguments */
    .expandable-container {
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .expandable-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem 1rem;
        cursor: pointer;
        border-bottom: 1px solid #e5e7eb;
        background-color: #f9fafb;
    }
    
    .expandable-content {
        padding: 1rem;
    }
    
    /* Point boxes styling */
    .point-box {
        border-radius: 0.5rem;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
    }
    
    .legal-point {
        background-color: #dbeafe;
    }
    
    .factual-point {
        background-color: #dcfce7;
    }
    
    .evidence-point {
        background-color: #f3f4f6;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for tracking expanded arguments
if 'expanded_args' not in st.session_state:
    st.session_state.expanded_args = {}

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Arguments"

if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "default"

# Helper function to toggle argument expansion
def toggle_argument(arg_id):
    if arg_id in st.session_state.expanded_args:
        st.session_state.expanded_args[arg_id] = not st.session_state.expanded_args[arg_id]
    else:
        st.session_state.expanded_args[arg_id] = True

# Helper functions for rendering argument components
def render_overview_points(points, paragraphs):
    st.markdown(f"""
    <div class="point-box" style="background-color: #f9fafb;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
            <span style="font-size: 0.75rem; background-color: #dbeafe; color: #1e40af; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">¶{paragraphs}</span>
        </div>
        <ul style="padding-left: 1.5rem;">
            {"".join([f'<li style="margin-bottom: 0.5rem; font-size: 0.875rem; color: #4b5563;">{point}</li>' for point in points])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

def render_legal_point(point, is_disputed, regulations, paragraphs):
    disputed_badge = f"""<span style="font-size: 0.75rem; background-color: #fee2e2; color: #b91c1c; padding: 0.25rem 0.5rem; border-radius: 0.25rem; margin-left: 0.5rem;">Disputed</span>""" if is_disputed else ""
    
    st.markdown(f"""
    <div class="point-box legal-point">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.75rem; background-color: #dbeafe; color: #1e40af; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">Legal</span>
            {disputed_badge}
        </div>
        <p style="font-size: 0.875rem; color: #4b5563; margin-bottom: 0.5rem;">{point}</p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
            {"".join([f'<span style="font-size: 0.75rem; background-color: #dbeafe; color: #1e40af; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">{reg}</span>' for reg in regulations])}
            <span style="font-size: 0.75rem; color: #6b7280; margin-left: 0.5rem;">¶{paragraphs}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_factual_point(point, date, is_disputed, source, paragraphs):
    disputed_text = f"""<span style="font-size: 0.75rem; background-color: #fee2e2; color: #b91c1c; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">Disputed by {source}</span>""" if is_disputed else ""
    
    st.markdown(f"""
    <div class="point-box factual-point">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.75rem; background-color: #dcfce7; color: #15803d; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">Factual</span>
            {disputed_text}
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-calendar"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <span style="font-size: 0.75rem; color: #6b7280;">{date}</span>
        </div>
        <p style="font-size: 0.875rem; color: #4b5563; margin-bottom: 0.5rem;">{point}</p>
        <span style="font-size: 0.75rem; color: #6b7280;">¶{paragraphs}</span>
    </div>
    """, unsafe_allow_html=True)

def render_evidence_reference(id, title, summary, citations):
    st.markdown(f"""
    <div class="point-box evidence-point">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <p style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.25rem;">{id}: {title}</p>
                <p style="font-size: 0.75rem; color: #6b7280; margin-bottom: 0.5rem;">{summary}</p>
                <div>
                    <span style="font-size: 0.75rem; color: #6b7280;">Cited in: </span>
                    {"".join([f'<span style="font-size: 0.75rem; background-color: #e5e7eb; padding: 0.25rem 0.5rem; border-radius: 0.25rem; margin-right: 0.25rem;">¶{cite}</span>' for cite in citations])}
                </div>
            </div>
            <button style="background: none; border: none; color: #6b7280; cursor: pointer;">
                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_case_law_reference(case_number, title, relevance, paragraphs, cited_paragraphs=None):
    cited_paras_html = ""
    if cited_paragraphs:
        cited_paras_html = f"""
        <div style="margin-top: 0.5rem;">
            <span style="font-size: 0.75rem; color: #6b7280;">Key Paragraphs: </span>
            {"".join([f'<span style="font-size: 0.75rem; background-color: #e5e7eb; padding: 0.25rem 0.5rem; border-radius: 0.25rem; margin-right: 0.25rem;">¶{para}</span>' for para in cited_paragraphs])}
        </div>
        """
    
    st.markdown(f"""
    <div class="point-box evidence-point">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
                    <p style="font-size: 0.875rem; font-weight: 500;">{case_number}</p>
                    <span style="font-size: 0.75rem; color: #6b7280;">¶{paragraphs}</span>
                </div>
                <p style="font-size: 0.75rem; color: #6b7280; margin-bottom: 0.5rem;">{title}</p>
                <p style="font-size: 0.875rem; color: #4b5563; margin-bottom: 0.25rem;">{relevance}</p>
                {cited_paras_html}
            </div>
            <button style="background: none; border: none; color: #6b7280; cursor: pointer;">
                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Define the argument section renderer
def render_argument_section(id, title, side, paragraphs=None, overview=None, legal_points=None, factual_points=None, evidence=None, case_law=None, level=0, children=None):
    base_color = "blue" if side == "claimant" else "red"
    bg_color = "#fff" if level == 0 else f"rgba({'59, 130, 246' if side == 'claimant' else '239, 68, 68'}, 0.1)"
    border_color = f"{'#2563eb' if side == 'claimant' else '#dc2626'}" if level == 0 else f"{'#93c5fd' if side == 'claimant' else '#fca5a5'}"
    
    # Check if this argument is expanded
    is_expanded = st.session_state.expanded_args.get(id, False)
    
    # Create a unique key for this argument
    key = f"{side}-{id}-{level}"
    
    # Argument header
    header_html = f"""
    <div class="expandable-header" style="background-color: {bg_color}; border: 1px solid {border_color}; border-radius: 0.5rem {"0.5rem 0 0" if is_expanded else ""};">
        <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span>{"▼" if is_expanded else "▶"}</span>
            <span style="font-weight: 500; font-size: 0.875rem; color: {'#2563eb' if side == 'claimant' else '#dc2626'};">
                {id}. {title}
            </span>
            {f'<span style="font-size: 0.75rem; background-color: rgba({"59, 130, 246" if side == "claimant" else "239, 68, 68"}, 0.2); color: {"#1e40af" if side == "claimant" else "#b91c1c"}; padding: 0.25rem 0.5rem; border-radius: 9999px;">{len(children) if children else 0} subarguments</span>' if children else f'<span style="font-size: 0.75rem; color: {"#2563eb" if side == "claimant" else "#dc2626"}; background-color: rgba({"59, 130, 246" if side == "claimant" else "239, 68, 68"}, 0.1); padding: 0.25rem 0.5rem; border-radius: 0.25rem;">¶{paragraphs}</span>'}
        </div>
    </div>
    """
    
    # Display the header with a button for toggling
    if st.markdown(header_html, unsafe_allow_html=True):
        toggle_argument(id)
    
    # If expanded, show the content
    if is_expanded:
        with st.container():
            st.markdown("""<div style="padding: 1rem; border: 1px solid #e5e7eb; border-top: none; border-radius: 0 0 0.5rem 0.5rem; background-color: white;">""", unsafe_allow_html=True)
            
            # Overview points
            if overview and overview.get('points'):
                render_overview_points(overview['points'], overview.get('paragraphs', ''))
            
            # Legal points
            if legal_points and len(legal_points) > 0:
                st.markdown("<h6 style='font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;'>Legal Points</h6>", unsafe_allow_html=True)
                for point in legal_points:
                    render_legal_point(
                        point['point'],
                        point.get('isDisputed', False),
                        point.get('regulations', []),
                        point.get('paragraphs', '')
                    )
            
            # Factual points
            if factual_points and len(factual_points) > 0:
                st.markdown("<h6 style='font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;'>Factual Points</h6>", unsafe_allow_html=True)
                for point in factual_points:
                    render_factual_point(
                        point['point'],
                        point.get('date', ''),
                        point.get('isDisputed', False),
                        point.get('source', ''),
                        point.get('paragraphs', '')
                    )
            
            # Evidence
            if evidence and len(evidence) > 0:
                st.markdown("<h6 style='font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;'>Evidence</h6>", unsafe_allow_html=True)
                for item in evidence:
                    render_evidence_reference(
                        item['id'],
                        item['title'],
                        item.get('summary', ''),
                        item.get('citations', [])
                    )
            
            # Case law
            if case_law and len(case_law) > 0:
                st.markdown("<h6 style='font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;'>Case Law</h6>", unsafe_allow_html=True)
                for item in case_law:
                    render_case_law_reference(
                        item['caseNumber'],
                        item['title'],
                        item.get('relevance', ''),
                        item.get('paragraphs', ''),
                        item.get('citedParagraphs', [])
                    )
            
            # Close the container
            st.markdown("</div>", unsafe_allow_html=True)
    
    # If there are children and the section is expanded, show them
    if is_expanded and children:
        for child in children:
            render_argument_section(**child, level=level+1)

# Define a function to render argument pairs side by side
def render_argument_pair(claimant_args, respondent_args, level=0, is_root=False):
    # Create two columns
    col1, col2 = st.columns(2)
    
    # Render the claimant argument in the first column
    with col1:
        render_argument_section(**claimant_args, side="claimant", level=level)
    
    # Render the respondent argument in the second column
    with col2:
        render_argument_section(**respondent_args, side="respondent", level=level)
    
    # If the parent is expanded and has children, render child pairs
    if (st.session_state.expanded_args.get(claimant_args['id'], False) and 
        'children' in claimant_args and claimant_args['children'] and
        'children' in respondent_args and respondent_args['children']):
        
        # Ensure the children arrays have the same length
        min_children = min(len(claimant_args['children']), len(respondent_args['children']))
        
        for i in range(min_children):
            render_argument_pair(
                claimant_args['children'][i],
                respondent_args['children'][i],
                level=level+1,
                is_root=False
            )

# Define the timeline view
def render_timeline_view():
    # Define timeline data
    timeline_data = [
        {
            'date': '2023-01-15',
            'appellant_version': 'Contract signed with Club',
            'respondent_version': '—',
            'status': 'Undisputed'
        },
        {
            'date': '2023-03-20',
            'appellant_version': 'Player received notification of exclusion from team',
            'respondent_version': '—',
            'status': 'Undisputed'
        },
        {
            'date': '2023-03-22',
            'appellant_version': 'Player requested explanation',
            'respondent_version': '—',
            'status': 'Undisputed'
        },
        {
            'date': '2023-04-01',
            'appellant_version': 'Player sent termination letter',
            'respondent_version': '—',
            'status': 'Undisputed'
        },
        {
            'date': '2023-04-05',
            'appellant_version': '—',
            'respondent_version': 'Club rejected termination as invalid',
            'status': 'Undisputed'
        },
        {
            'date': '2023-04-10',
            'appellant_version': 'Player was denied access to training facilities',
            'respondent_version': '—',
            'status': 'Disputed'
        },
        {
            'date': '2023-04-15',
            'appellant_version': '—',
            'respondent_version': 'Club issued warning letter',
            'status': 'Undisputed'
        },
        {
            'date': '2023-05-01',
            'appellant_version': 'Player filed claim with FIFA',
            'respondent_version': '—',
            'status': 'Undisputed'
        },
    ]
    
    # Convert to DataFrame for easier filtering
    df = pd.DataFrame(timeline_data)
    
    # Create action buttons
    col1, col2 = st.columns([4, 1])
    with col2:
        st.button("📋 Copy", key="timeline_copy")
        st.button("📥 Export Data", key="timeline_export")
    
    # Search and filter controls
    search_col, filter_col, checkbox_col = st.columns([2, 1, 2])
    
    with search_col:
        search_term = st.text_input("", placeholder="Search events...", key="timeline_search")
    
    with filter_col:
        st.button("🔍 Filter", key="timeline_filter")
    
    with checkbox_col:
        disputed_only = st.checkbox("Disputed events only", key="timeline_disputed")
    
    # Apply filters
    if search_term:
        df = df[
            df['appellant_version'].str.contains(search_term, case=False, na=False) |
            df['respondent_version'].str.contains(search_term, case=False, na=False)
        ]
    
    if disputed_only:
        df = df[df['status'] == 'Disputed']
    
    # Display the timeline table with custom HTML
    html_table = """
    <table class="styled-table">
        <thead>
            <tr>
                <th>DATE</th>
                <th>APPELLANT'S VERSION</th>
                <th>RESPONDENT'S VERSION</th>
                <th>STATUS</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        status_class = "disputed" if row['status'] == 'Disputed' else "undisputed"
        row_bg = 'style="background-color: #fee2e2;"' if row['status'] == 'Disputed' else ''
        
        html_table += f"""
        <tr {row_bg}>
            <td>{row['date']}</td>
            <td>{row['appellant_version']}</td>
            <td>{row['respondent_version']}</td>
            <td><span class="badge {status_class}">{row['status']}</span></td>
        </tr>
        """
    
    html_table += """
        </tbody>
    </table>
    """
    
    st.markdown(html_table, unsafe_allow_html=True)

# Define the exhibits view
def render_exhibits_view():
    # Define exhibits data
    exhibits_data = [
        {
            'id': 'C-1',
            'party': 'Appellant',
            'title': 'Employment Contract',
            'type': 'contract',
            'summary': 'Employment contract dated 15 January 2023 between Player and Club'
        },
        {
            'id': 'C-2',
            'party': 'Appellant',
            'title': 'Termination Letter',
            'type': 'letter',
            'summary': 'Player\'s termination letter sent on 1 April 2023'
        },
        {
            'id': 'C-3',
            'party': 'Appellant',
            'title': 'Email Correspondence',
            'type': 'communication',
            'summary': 'Email exchanges between Player and Club from 22-30 March 2023'
        },
        {
            'id': 'C-4',
            'party': 'Appellant',
            'title': 'Witness Statement',
            'type': 'statement',
            'summary': 'Statement from team captain confirming Player\'s exclusion'
        },
        {
            'id': 'R-1',
            'party': 'Respondent',
            'title': 'Club Regulations',
            'type': 'regulations',
            'summary': 'Internal regulations of the Club dated January 2022'
        },
        {
            'id': 'R-2',
            'party': 'Respondent',
            'title': 'Warning Letter',
            'type': 'letter',
            'summary': 'Warning letter issued to Player on 15 April 2023'
        },
        {
            'id': 'R-3',
            'party': 'Respondent',
            'title': 'Training Schedule',
            'type': 'schedule',
            'summary': 'Team training schedule for March-April 2023'
        }
    ]
    
    # Convert to DataFrame for easier filtering
    df = pd.DataFrame(exhibits_data)
    
    # Create action buttons
    col1, col2 = st.columns([4, 1])
    with col2:
        st.button("📋 Copy", key="exhibits_copy")
        st.button("📥 Export Data", key="exhibits_export")
    
    # Search and filter controls
    search_col, party_col, type_col = st.columns([2, 1, 1])
    
    with search_col:
        search_term = st.text_input("", placeholder="Search exhibits...", key="exhibits_search")
    
    with party_col:
        party_filter = st.selectbox("", ["All Parties", "Appellant", "Respondent"], key="party_filter")
    
    with type_col:
        all_types = ["All Types"] + list(df['type'].unique())
        type_filter = st.selectbox("", all_types, key="type_filter")
    
    # Apply filters
    if search_term:
        df = df[
            df['title'].str.contains(search_term, case=False) |
            df['summary'].str.contains(search_term, case=False) |
            df['id'].str.contains(search_term, case=False)
        ]
    
    if party_filter != "All Parties":
        df = df[df['party'] == party_filter]
    
    if type_filter != "All Types":
        df = df[df['type'] == type_filter]
    
    # Display the exhibits table with custom HTML
    html_table = """
    <table class="styled-table">
        <thead>
            <tr>
                <th>EXHIBIT ID</th>
                <th>PARTY</th>
                <th>TITLE</th>
                <th>TYPE</th>
                <th>SUMMARY</th>
                <th>ACTIONS</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        party_class = "appellant-badge" if row['party'] == 'Appellant' else "respondent-badge"
        
        html_table += f"""
        <tr>
            <td>{row['id']}</td>
            <td><span class="party-badge {party_class}">{row['party']}</span></td>
            <td>{row['title']}</td>
            <td><span class="type-badge">{row['type']}</span></td>
            <td>{row['summary']}</td>
            <td><a href="#" style="color: #2563eb; text-decoration: none;">View</a></td>
        </tr>
        """
    
    html_table += """
        </tbody>
    </table>
    """
    
    st.markdown(html_table, unsafe_allow_html=True)

# Define hierarchical view renderer
def render_hierarchical_view():
    # Define topic sections
    topic_sections = [
        {
            'id': 'topic-1',
            'title': 'Sporting Succession and Identity',
            'description': 'Questions of club identity, continuity, and succession rights',
            'claimant_args': {
                'id': '1',
                'title': 'Sporting Succession',
                'paragraphs': '15-18',
                'overview': {
                    'points': [
                        'Analysis of multiple established criteria',
                        'Focus on continuous use of identifying elements',
                        'Public recognition assessment'
                    ],
                    'paragraphs': '15-16'
                },
                'legal_points': [
                    {
                        'point': 'CAS jurisprudence establishes criteria for sporting succession',
                        'isDisputed': False,
                        'regulations': ['CAS 2016/A/4576'],
                        'paragraphs': '15-17'
                    }
                ],
                'factual_points': [
                    {
                        'point': 'Continuous operation under same name since 1950',
                        'date': '1950-present',
                        'isDisputed': False,
                        'paragraphs': '18-19'
                    }
                ],
                'evidence': [
                    {
                        'id': 'C-1',
                        'title': 'Historical Registration Documents',
                        'summary': 'Official records showing continuous name usage',
                        'citations': ['20', '21', '24']
                    }
                ],
                'case_law': [
                    {
                        'caseNumber': 'CAS 2016/A/4576',
                        'title': 'Criteria for sporting succession',
                        'relevance': 'Establishes key factors for succession',
                        'paragraphs': '45-48',
                        'citedParagraphs': ['45', '46', '47']
                    }
                ],
                'children': []
            },
            'respondent_args': {
                'id': '1',
                'title': 'Sporting Succession Rebuttal',
                'paragraphs': '200-218',
                'overview': {
                    'points': [
                        'Challenge to claimed continuity of operations',
                        'Analysis of discontinuities in club operations',
                        'Dispute over public recognition factors'
                    ],
                    'paragraphs': '200-202'
                },
                'legal_points': [
                    {
                        'point': 'CAS jurisprudence requires operational continuity not merely identification',
                        'isDisputed': False,
                        'regulations': ['CAS 2017/A/5465'],
                        'paragraphs': '203-205'
                    }
                ],
                'factual_points': [
                    {
                        'point': 'Operations ceased between 1975-1976',
                        'date': '1975-1976',
                        'isDisputed': True,
                        'source': 'Claimant',
                        'paragraphs': '206-207'
                    }
                ],
                'evidence': [
                    {
                        'id': 'R-1',
                        'title': 'Federation Records',
                        'summary': 'Records showing non-participation in 1975-1976 season',
                        'citations': ['208', '209', '210']
                    }
                ],
                'case_law': [
                    {
                        'caseNumber': 'CAS 2017/A/5465',
                        'title': 'Operational continuity requirement',
                        'relevance': 'Establishes primacy of operational continuity',
                        'paragraphs': '211-213',
                        'citedParagraphs': ['212']
                    }
                ],
                'children': []
            }
        },
        {
            'id': 'topic-2',
            'title': 'Doping Violation and Chain of Custody',
            'description': 'Issues related to doping test procedures and evidence handling',
            'claimant_args': {
                'id': '2',
                'title': 'Doping Violation Chain of Custody',
                'paragraphs': '70-125',
                'overview': {
                    'points': [
                        'Analysis of sample collection and handling procedures',
                        'Evaluation of laboratory testing protocols',
                        'Assessment of chain of custody documentation'
                    ],
                    'paragraphs': '70-72'
                },
                'legal_points': [
                    {
                        'point': 'WADA Code Article 5 establishes procedural requirements',
                        'isDisputed': False,
                        'regulations': ['WADA Code 2021', 'International Standard for Testing'],
                        'paragraphs': '73-75'
                    }
                ],
                'children': []
            },
            'respondent_args': {
                'id': '2',
                'title': 'Doping Chain of Custody Defense',
                'paragraphs': '250-290',
                'overview': {
                    'points': [
                        'Defense of sample collection procedures',
                        'Validation of laboratory testing protocols',
                        'Completeness of documentation'
                    ],
                    'paragraphs': '250-252'
                },
                'legal_points': [
                    {
                        'point': 'Minor procedural deviations do not invalidate results',
                        'isDisputed': False,
                        'regulations': ['CAS 2019/A/6148'],
                        'paragraphs': '253-255'
                    }
                ],
                'children': []
            }
        }
    ]
    
    for topic in topic_sections:
        st.markdown(f"""
        <div class="topic-section">
            <h2 class="topic-title">{topic['title']}</h2>
            <p class="topic-description">{topic['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Column headers
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h3 class="claimant-header">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
        with col2:
            st.markdown('<h3 class="respondent-header">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
        
        # Render argument pair
        render_argument_pair(topic['claimant_args'], topic['respondent_args'], is_root=True)

# Main interface with tabs
st.markdown("<h1 style='font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;'>Legal Arguments Analysis</h1>", unsafe_allow_html=True)

# Tabs for different views
tabs = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])

# Tab content
with tabs[0]:  # Arguments tab
    # View mode selector
    col1, col2 = st.columns([3, 1])
    with col2:
        view_mode = st.radio(
            "View Mode:",
            ["Standard View", "Topic View"],
            horizontal=True,
            label_visibility="collapsed",
            key="view_mode_selector",
            index=0 if st.session_state.view_mode == "default" else 1
        )
        st.session_state.view_mode = "default" if view_mode == "Standard View" else "hierarchical"
    
    # Display appropriate view
    if st.session_state.view_mode == "default":
        # Standard view with columns for claimant and respondent
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h2 class="claimant-header">Claimant\'s Arguments</h2>', unsafe_allow_html=True)
        with col2:
            st.markdown('<h2 class="respondent-header">Respondent\'s Arguments</h2>', unsafe_allow_html=True)
        
        # Sporting Succession argument pair
        claimant_args_1 = {
            'id': '1',
            'title': 'Sporting Succession',
            'paragraphs': '15-18',
            'overview': {
                'points': [
                    'Analysis of multiple established criteria',
                    'Focus on continuous use of identifying elements',
                    'Public recognition assessment'
                ],
                'paragraphs': '15-16'
            },
            'legal_points': [
                {
                    'point': 'CAS jurisprudence establishes criteria for sporting succession',
                    'isDisputed': False,
                    'regulations': ['CAS 2016/A/4576'],
                    'paragraphs': '15-17'
                }
            ],
            'factual_points': [
                {
                    'point': 'Continuous operation under same name since 1950',
                    'date': '1950-present',
                    'isDisputed': False,
                    'paragraphs': '18-19'
                }
            ],
            'evidence': [
                {
                    'id': 'C-1',
                    'title': 'Historical Registration Documents',
                    'summary': 'Official records showing continuous name usage',
                    'citations': ['20', '21', '24']
                }
            ],
            'case_law': [
                {
                    'caseNumber': 'CAS 2016/A/4576',
                    'title': 'Criteria for sporting succession',
                    'relevance': 'Establishes key factors for succession',
                    'paragraphs': '45-48',
                    'citedParagraphs': ['45', '46', '47']
                }
            ],
            'children': []
        }
        
        respondent_args_1 = {
            'id': '1',
            'title': 'Sporting Succession Rebuttal',
            'paragraphs': '200-218',
            'overview': {
                'points': [
                    'Challenge to claimed continuity of operations',
                    'Analysis of discontinuities in club operations',
                    'Dispute over public recognition factors'
                ],
                'paragraphs': '200-202'
            },
            'legal_points': [
                {
                    'point': 'CAS jurisprudence requires operational continuity not merely identification',
                    'isDisputed': False,
                    'regulations': ['CAS 2017/A/5465'],
                    'paragraphs': '203-205'
                }
            ],
            'factual_points': [
                {
                    'point': 'Operations ceased between 1975-1976',
                    'date': '1975-1976',
                    'isDisputed': True,
                    'source': 'Claimant',
                    'paragraphs': '206-207'
                }
            ],
            'evidence': [
                {
                    'id': 'R-1',
                    'title': 'Federation Records',
                    'summary': 'Records showing non-participation in 1975-1976 season',
                    'citations': ['208', '209', '210']
                }
            ],
            'case_law': [
                {
                    'caseNumber': 'CAS 2017/A/5465',
                    'title': 'Operational continuity requirement',
                    'relevance': 'Establishes primacy of operational continuity',
                    'paragraphs': '211-213',
                    'citedParagraphs': ['212']
                }
            ],
            'children': []
        }
        
        render_argument_pair(claimant_args_1, respondent_args_1, is_root=True)
        
        # Doping argument pair
        claimant_args_2 = {
            'id': '2',
            'title': 'Doping Violation Chain of Custody',
            'paragraphs': '70-125',
            'overview': {
                'points': [
                    'Analysis of sample collection and handling procedures',
                    'Evaluation of laboratory testing protocols',
                    'Assessment of chain of custody documentation'
                ],
                'paragraphs': '70-72'
            },
            'legal_points': [
                {
                    'point': 'WADA Code Article 5 establishes procedural requirements',
                    'isDisputed': False,
                    'regulations': ['WADA Code 2021', 'International Standard for Testing'],
                    'paragraphs': '73-75'
                }
            ],
            'children': []
        }
        
        respondent_args_2 = {
            'id': '2',
            'title': 'Doping Chain of Custody Defense',
            'paragraphs': '250-290',
            'overview': {
                'points': [
                    'Defense of sample collection procedures',
                    'Validation of laboratory testing protocols',
                    'Completeness of documentation'
                ],
                'paragraphs': '250-252'
            },
            'legal_points': [
                {
                    'point': 'Minor procedural deviations do not invalidate results',
                    'isDisputed': False,
                    'regulations': ['CAS 2019/A/6148'],
                    'paragraphs': '253-255'
                }
            ],
            'children': []
        }
        
        render_argument_pair(claimant_args_2, respondent_args_2, is_root=True)
    else:
        # Hierarchical/topic view
        render_hierarchical_view()

with tabs[1]:  # Timeline tab
    render_timeline_view()

with tabs[2]:  # Exhibits tab
    render_exhibits_view()

# Run the app
if __name__ == "__main__":
    st.sidebar.title("Legal Analysis Interface")
    st.sidebar.info("This is a Streamlit version of the Legal Analysis Interface.")
