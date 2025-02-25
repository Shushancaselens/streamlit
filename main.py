import streamlit as st
import pandas as pd
import numpy as np

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
    
    /* Card with border */
    .card {
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: white;
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
    
    /* Button styling */
    .custom-button {
        background-color: transparent;
        border: 1px solid #e5e7eb;
        padding: 0.375rem 0.75rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
        margin-right: 0.5rem;
        cursor: pointer;
    }
    
    .custom-button:hover {
        background-color: #f3f4f6;
    }
    
    /* Radio buttons as toggle */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: row;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        padding: 0.375rem 0.75rem;
        border: 1px solid #e5e7eb;
        margin-right: 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
        cursor: pointer;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label:hover {
        background-color: #f3f4f6;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
        display: none;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label[aria-checked="true"] {
        background-color: #f3f4f6;
        border-color: #d1d5db;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state for tracking expanded arguments
if 'expanded_args' not in st.session_state:
    st.session_state.expanded_args = {}

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0

if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "default"

# Define manual HTML rendering function since we can't use external components
def render_html(html_content):
    st.markdown(html_content, unsafe_allow_html=True)

# Create a card container
def card(content_func):
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        content_func()
        st.markdown('</div>', unsafe_allow_html=True)

# Define Timeline View Data
def get_timeline_data():
    return [
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
        }
    ]

# Define Exhibits Data
def get_exhibits_data():
    return [
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

# Define Legal Argument Data
def get_claimant_args_1():
    return {
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
        ]
    }

def get_respondent_args_1():
    return {
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
        ]
    }

def get_claimant_args_2():
    return {
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
        'factual_points': [],
        'evidence': [],
        'case_law': []
    }

def get_respondent_args_2():
    return {
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
        'factual_points': [],
        'evidence': [],
        'case_law': []
    }

# Helper function to toggle argument expansion
def toggle_argument(arg_id):
    if arg_id in st.session_state.expanded_args:
        st.session_state.expanded_args[arg_id] = not st.session_state.expanded_args[arg_id]
    else:
        st.session_state.expanded_args[arg_id] = True

# Render an argument section
def render_argument_section(arg_data, side):
    arg_id = arg_data['id']
    title = arg_data['title']
    paragraphs = arg_data.get('paragraphs', '')
    
    # Get the expanded state
    is_expanded = st.session_state.expanded_args.get(arg_id, False)
    
    # Colors based on side
    bg_color = "#dbeafe" if side == "claimant" else "#fee2e2"
    text_color = "#1e40af" if side == "claimant" else "#b91c1c"
    border_color = "#93c5fd" if side == "claimant" else "#fca5a5"
    
    # Create the header with an expander
    header = st.expander(f"{arg_id}. {title}", expanded=is_expanded)
    
    # Update the session state when expanded/collapsed
    if header.expanded != is_expanded:
        st.session_state.expanded_args[arg_id] = header.expanded
    
    # If expanded, show the content
    if header.expanded:
        with header:
            # Overview points
            if 'overview' in arg_data and arg_data['overview'].get('points'):
                with st.container():
                    st.markdown("#### Key Points")
                    for point in arg_data['overview']['points']:
                        st.markdown(f"• {point}")
                    st.caption(f"Paragraphs: {arg_data['overview'].get('paragraphs', '')}")
                st.divider()
            
            # Legal points
            if 'legal_points' in arg_data and arg_data['legal_points']:
                st.markdown("#### Legal Points")
                for point in arg_data['legal_points']:
                    with st.container():
                        st.markdown(f"**{point['point']}**")
                        st.caption(f"Regulations: {', '.join(point.get('regulations', []))}")
                        if point.get('isDisputed'):
                            st.warning("Disputed")
                        st.caption(f"Paragraphs: {point.get('paragraphs', '')}")
                st.divider()
            
            # Factual points
            if 'factual_points' in arg_data and arg_data['factual_points']:
                st.markdown("#### Factual Points")
                for point in arg_data['factual_points']:
                    with st.container():
                        st.markdown(f"**{point['point']}**")
                        st.caption(f"Date: {point.get('date', '')}")
                        if point.get('isDisputed'):
                            st.warning(f"Disputed by {point.get('source', '')}")
                        st.caption(f"Paragraphs: {point.get('paragraphs', '')}")
                st.divider()
            
            # Evidence
            if 'evidence' in arg_data and arg_data['evidence']:
                st.markdown("#### Evidence")
                for item in arg_data['evidence']:
                    with st.container():
                        st.markdown(f"**{item['id']}: {item['title']}**")
                        st.markdown(f"{item.get('summary', '')}")
                        if 'citations' in item:
                            st.caption(f"Cited in paragraphs: {', '.join(item['citations'])}")
                st.divider()
            
            # Case law
            if 'case_law' in arg_data and arg_data['case_law']:
                st.markdown("#### Case Law")
                for item in arg_data['case_law']:
                    with st.container():
                        st.markdown(f"**{item['caseNumber']}**")
                        st.markdown(f"{item['title']}")
                        st.markdown(f"{item.get('relevance', '')}")
                        if 'citedParagraphs' in item:
                            st.caption(f"Key paragraphs: {', '.join(item['citedParagraphs'])}")
                        st.caption(f"Paragraphs: {item.get('paragraphs', '')}")

# Render the timeline view
def render_timeline_view():
    timeline_data = get_timeline_data()
    df = pd.DataFrame(timeline_data)
    
    # Create action buttons and filters
    col1, col2, col3 = st.columns([2, 1, 1])
    with col3:
        st.button("📋 Copy", key="timeline_copy")
        st.button("📥 Export Data", key="timeline_export")
    
    # Search and filter controls
    search_col, filter_col, checkbox_col = st.columns([3, 1, 2])
    
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
    
    # Apply styling to the dataframe
    def style_status(val):
        color = '#dcfce7' if val == 'Undisputed' else '#fee2e2'
        text_color = '#15803d' if val == 'Undisputed' else '#b91c1c'
        return f'background-color: {color}; color: {text_color}; border-radius: 9999px; padding: 0.2rem 0.5rem;'
    
    def highlight_disputed_rows(row):
        if row['status'] == 'Disputed':
            return ['background-color: #fef2f2'] * len(row)
        return [''] * len(row)
    
    # Display the styled dataframe
    st.dataframe(
        df.style
        .apply(highlight_disputed_rows, axis=1)
        .applymap(style_status, subset=['status']),
        use_container_width=True,
        hide_index=True
    )

# Render the exhibits view
def render_exhibits_view():
    exhibits_data = get_exhibits_data()
    df = pd.DataFrame(exhibits_data)
    
    # Create action buttons
    col1, col2, col3 = st.columns([2, 1, 1])
    with col3:
        st.button("📋 Copy", key="exhibits_copy")
        st.button("📥 Export Data", key="exhibits_export")
    
    # Search and filter controls
    search_col, party_col, type_col = st.columns([3, 1, 1])
    
    with search_col:
        search_term = st.text_input("", placeholder="Search exhibits...", key="exhibits_search")
    
    with party_col:
        party_options = ["All Parties"] + sorted(df['party'].unique().tolist())
        party_filter = st.selectbox("", party_options, key="party_filter")
    
    with type_col:
        type_options = ["All Types"] + sorted(df['type'].unique().tolist())
        type_filter = st.selectbox("", type_options, key="type_filter")
    
    # Apply filters
    filtered_df = df.copy()
    
    if search_term:
        filtered_df = filtered_df[
            filtered_df['id'].str.contains(search_term, case=False) |
            filtered_df['title'].str.contains(search_term, case=False) |
            filtered_df['summary'].str.contains(search_term, case=False)
        ]
    
    if party_filter != "All Parties":
        filtered_df = filtered_df[filtered_df['party'] == party_filter]
    
    if type_filter != "All Types":
        filtered_df = filtered_df[filtered_df['type'] == type_filter]
    
    # Add a view button column
    filtered_df['actions'] = "View"
    
    # Apply styling to specific columns
    def style_party(val):
        if val == 'Appellant':
            return 'background-color: #dbeafe; color: #1e40af; border-radius: 4px; padding: 0.2rem 0.5rem;'
        else:
            return 'background-color: #fee2e2; color: #b91c1c; border-radius: 4px; padding: 0.2rem 0.5rem;'
    
    def style_type(val):
        return 'background-color: #f3f4f6; color: #374151; border-radius: 4px; padding: 0.2rem 0.5rem;'
    
    def style_action(val):
        return 'color: #2563eb; text-decoration: none; cursor: pointer;'
    
    # Display the styled dataframe
    st.dataframe(
        filtered_df.style
        .applymap(style_party, subset=['party'])
        .applymap(style_type, subset=['type'])
        .applymap(style_action, subset=['actions']),
        use_container_width=True,
        hide_index=True,
        column_config={
            "actions": st.column_config.LinkColumn("ACTIONS")
        }
    )

# Render the hierarchical view
def render_hierarchical_view():
    topics = [
        {
            'title': 'Sporting Succession and Identity',
            'description': 'Questions of club identity, continuity, and succession rights',
            'claimant_args': get_claimant_args_1(),
            'respondent_args': get_respondent_args_1()
        },
        {
            'title': 'Doping Violation and Chain of Custody',
            'description': 'Issues related to doping test procedures and evidence handling',
            'claimant_args': get_claimant_args_2(),
            'respondent_args': get_respondent_args_2()
        }
    ]
    
    for topic in topics:
        st.markdown(f"## {topic['title']}")
        st.markdown(f"*{topic['description']}*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<h3 style="color: #2563eb;">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
            render_argument_section(topic['claimant_args'], "claimant")
        
        with col2:
            st.markdown('<h3 style="color: #dc2626;">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
            render_argument_section(topic['respondent_args'], "respondent")
        
        st.divider()

# Render the standard view
def render_standard_view():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h3 style="color: #2563eb;">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
        render_argument_section(get_claimant_args_1(), "claimant")
        render_argument_section(get_claimant_args_2(), "claimant")
    
    with col2:
        st.markdown('<h3 style="color: #dc2626;">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
        render_argument_section(get_respondent_args_1(), "respondent")
        render_argument_section(get_respondent_args_2(), "respondent")

# Main app
st.title("Legal Arguments Analysis")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])

# Arguments Tab
with tab1:
    view_col1, view_col2 = st.columns([3, 1])
    with view_col2:
        view_mode = st.radio(
            "View Mode:",
            options=["Standard View", "Topic View"],
            horizontal=True,
            index=0 if st.session_state.view_mode == "default" else 1,
            key="view_mode_selector"
        )
        st.session_state.view_mode = "default" if view_mode == "Standard View" else "hierarchical"
    
    if st.session_state.view_mode == "default":
        render_standard_view()
    else:
        render_hierarchical_view()

# Timeline Tab
with tab2:
    render_timeline_view()

# Exhibits Tab
with tab3:
    render_exhibits_view()

# Hide Streamlit branding in sidebar
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
