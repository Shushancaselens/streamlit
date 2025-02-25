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
    .card {
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: white;
    }
    
    /* Headers */
    .claimant-header {
        color: #2563eb; /* Blue */
        font-weight: 600;
    }
    
    .respondent-header {
        color: #dc2626; /* Red */
        font-weight: 600;
    }
    
    /* Argument header */
    .argument-header {
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        margin-bottom: 0.5rem;
        background-color: #f9fafb;
        cursor: pointer;
    }
    
    .claimant-argument-header {
        border-color: #93c5fd;
    }
    
    .respondent-argument-header {
        border-color: #fca5a5;
    }
    
    /* Argument content */
    .argument-content {
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: white;
    }
    
    /* Make the streamlit checkbox styling better */
    .stCheckbox label {
        font-weight: 500;
    }
    
    /* Status indicators */
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .status-disputed {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    
    .status-undisputed {
        background-color: #dcfce7;
        color: #15803d;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Button styling */
    .stButton button {
        font-size: 0.875rem;
    }
</style>
""", unsafe_allow_html=True)

# Define data for timeline view
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

# Define data for exhibits view
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

# Argument data
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
        ]
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
        ]
    }

# Topic data for hierarchical view
def get_topic_data():
    return [
        {
            'title': 'Sporting Succession and Identity',
            'description': 'Questions of club identity, continuity, and succession rights',
            'claimant_arg': get_claimant_args_1(),
            'respondent_arg': get_respondent_args_1()
        },
        {
            'title': 'Doping Violation and Chain of Custody',
            'description': 'Issues related to doping test procedures and evidence handling',
            'claimant_arg': get_claimant_args_2(),
            'respondent_arg': get_respondent_args_2()
        }
    ]

# Render argument section
def render_argument(arg_data, side, key_prefix=""):
    arg_id = arg_data['id']
    title = arg_data['title']
    paragraphs = arg_data.get('paragraphs', '')
    
    # Create a unique key for this argument
    arg_key = f"{key_prefix}{side}-{arg_id}"
    
    # Header styling based on side
    header_class = "claimant-argument-header" if side == "claimant" else "respondent-argument-header"
    
    # Draw the header with a checkbox to control expansion
    st.markdown(f"""
        <div class="argument-header {header_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span>{arg_id}. {title}</span>
                    <span style="font-size: 0.8rem; margin-left: 0.5rem; color: #6b7280;">¶{paragraphs}</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Use a checkbox to control visibility of the content
    expanded = st.checkbox(f"Show details for {arg_id}", key=arg_key, value=False, label_visibility="collapsed")
    
    # If expanded, show the content
    if expanded:
        with st.container():
            # Overview points
            if 'overview' in arg_data and arg_data['overview'].get('points'):
                st.markdown("#### Key Points")
                overview_points = arg_data['overview']['points']
                for point in overview_points:
                    st.markdown(f"- {point}")
                st.caption(f"Paragraphs: {arg_data['overview'].get('paragraphs', '')}")
                st.divider()
            
            # Legal points
            if 'legal_points' in arg_data and arg_data['legal_points']:
                st.markdown("#### Legal Points")
                for point in arg_data['legal_points']:
                    st.markdown(f"**{point['point']}**")
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.caption(f"Regulations: {', '.join(point.get('regulations', []))}")
                    with col2:
                        if point.get('isDisputed'):
                            st.warning("Disputed")
                    st.caption(f"Paragraphs: {point.get('paragraphs', '')}")
                    st.markdown("---")
            
            # Factual points
            if 'factual_points' in arg_data and arg_data['factual_points']:
                st.markdown("#### Factual Points")
                for point in arg_data['factual_points']:
                    st.markdown(f"**{point['point']}**")
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.caption(f"Date: {point.get('date', '')}")
                    with col2:
                        if point.get('isDisputed'):
                            st.warning(f"Disputed by {point.get('source', '')}")
                    st.caption(f"Paragraphs: {point.get('paragraphs', '')}")
                    st.markdown("---")
            
            # Evidence
            if 'evidence' in arg_data and arg_data['evidence']:
                st.markdown("#### Evidence")
                for item in arg_data['evidence']:
                    st.markdown(f"**{item['id']}: {item['title']}**")
                    st.markdown(f"{item.get('summary', '')}")
                    st.caption(f"Citations: {', '.join(item.get('citations', []))}")
                    st.markdown("---")
            
            # Case law
            if 'case_law' in arg_data and arg_data['case_law']:
                st.markdown("#### Case Law")
                for item in arg_data['case_law']:
                    st.markdown(f"**{item['caseNumber']}**")
                    st.markdown(f"{item['title']}")
                    st.markdown(f"{item.get('relevance', '')}")
                    if 'citedParagraphs' in item:
                        st.caption(f"Key paragraphs: {', '.join(item['citedParagraphs'])}")
                    st.caption(f"Paragraphs: {item.get('paragraphs', '')}")
                    st.markdown("---")

# Render standard view (side-by-side arguments)
def render_standard_view():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 class='claimant-header'>Claimant's Arguments</h3>", unsafe_allow_html=True)
        render_argument(get_claimant_args_1(), "claimant", "std-")
        render_argument(get_claimant_args_2(), "claimant", "std-")
    
    with col2:
        st.markdown("<h3 class='respondent-header'>Respondent's Arguments</h3>", unsafe_allow_html=True)
        render_argument(get_respondent_args_1(), "respondent", "std-")
        render_argument(get_respondent_args_2(), "respondent", "std-")

# Render hierarchical view (topics with claimant-respondent pairs)
def render_hierarchical_view():
    topics = get_topic_data()
    
    for i, topic in enumerate(topics):
        st.markdown(f"## {topic['title']}")
        st.markdown(f"*{topic['description']}*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4 class='claimant-header'>Claimant's Arguments</h4>", unsafe_allow_html=True)
            render_argument(topic['claimant_arg'], "claimant", f"hier-topic{i}-")
        
        with col2:
            st.markdown("<h4 class='respondent-header'>Respondent's Arguments</h4>", unsafe_allow_html=True)
            render_argument(topic['respondent_arg'], "respondent", f"hier-topic{i}-")
        
        st.divider()

# Render timeline view
def render_timeline_view():
    # Get timeline data
    timeline_data = get_timeline_data()
    
    # Add action buttons
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col3:
        st.button("📋 Copy", key="timeline_copy")
        st.button("📥 Export Data", key="timeline_export")
    
    # Add search and filter controls
    col1, col2, col3 = st.columns([3, 1, 2])
    
    with col1:
        search_term = st.text_input("", placeholder="Search events...", key="timeline_search")
    
    with col2:
        st.button("🔍 Filter", key="timeline_filter")
    
    with col3:
        disputed_only = st.checkbox("Disputed events only", key="timeline_disputed")
    
    # Convert to dataframe for easier filtering
    df = pd.DataFrame(timeline_data)
    
    # Apply filters
    if search_term:
        df = df[
            df['appellant_version'].str.contains(search_term, case=False, na=False) |
            df['respondent_version'].str.contains(search_term, case=False, na=False)
        ]
    
    if disputed_only:
        df = df[df['status'] == 'Disputed']
    
    # Create a table
    col_headers = ["DATE", "APPELLANT'S VERSION", "RESPONDENT'S VERSION", "STATUS"]
    
    # Create a basic table using streamlit's native table
    st.write("")  # Add a little spacing
    
    # Display header
    cols = st.columns([1, 2, 2, 1])
    for i, header in enumerate(col_headers):
        cols[i].markdown(f"**{header}**")
    
    # Display rows
    for _, row in df.iterrows():
        # Apply background color based on status
        row_bg = "#fef2f2" if row['status'] == 'Disputed' else "white"
        status_class = "status-disputed" if row['status'] == 'Disputed' else "status-undisputed"
        
        st.markdown(f"""
        <div style="display: flex; width: 100%; background-color: {row_bg}; padding: 0.5rem; margin-bottom: 0.25rem; border-radius: 0.25rem;">
            <div style="flex: 1;">{row['date']}</div>
            <div style="flex: 2;">{row['appellant_version']}</div>
            <div style="flex: 2;">{row['respondent_version']}</div>
            <div style="flex: 1;"><span class="status-badge {status_class}">{row['status']}</span></div>
        </div>
        """, unsafe_allow_html=True)

# Render exhibits view
def render_exhibits_view():
    # Get exhibits data
    exhibits_data = get_exhibits_data()
    
    # Add action buttons
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col3:
        st.button("📋 Copy", key="exhibits_copy")
        st.button("📥 Export Data", key="exhibits_export")
    
    # Add search and filter controls
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        search_term = st.text_input("", placeholder="Search exhibits...", key="exhibits_search")
    
    with col2:
        parties = ["All Parties", "Appellant", "Respondent"]
        party_filter = st.selectbox("", parties, key="party_filter")
    
    with col3:
        # Get unique types from data
        types = ["All Types"] + list(set([ex['type'] for ex in exhibits_data]))
        type_filter = st.selectbox("", types, key="type_filter")
    
    # Convert to dataframe for easier filtering
    df = pd.DataFrame(exhibits_data)
    
    # Apply filters
    if search_term:
        df = df[
            df['id'].str.contains(search_term, case=False) |
            df['title'].str.contains(search_term, case=False) |
            df['summary'].str.contains(search_term, case=False)
        ]
    
    if party_filter != "All Parties":
        df = df[df['party'] == party_filter]
    
    if type_filter != "All Types":
        df = df[df['type'] == type_filter]
    
    # Display table header
    st.write("")  # Add spacing
    
    cols = st.columns([1, 1, 2, 1, 4, 1])
    headers = ["EXHIBIT ID", "PARTY", "TITLE", "TYPE", "SUMMARY", "ACTIONS"]
    
    for i, header in enumerate(headers):
        cols[i].markdown(f"**{header}**")
    
    # Display rows
    for _, row in df.iterrows():
        # Style badge based on party
        party_style = "background-color: #dbeafe; color: #1e40af;" if row['party'] == "Appellant" else "background-color: #fee2e2; color: #b91c1c;"
        
        st.markdown(f"""
        <div style="display: flex; width: 100%; background-color: white; padding: 0.5rem; margin-bottom: 0.25rem; border-bottom: 1px solid #e5e7eb;">
            <div style="flex: 1;">{row['id']}</div>
            <div style="flex: 1;"><span style="padding: 0.25rem 0.5rem; border-radius: 0.25rem; {party_style}">{row['party']}</span></div>
            <div style="flex: 2;">{row['title']}</div>
            <div style="flex: 1;"><span style="padding: 0.25rem 0.5rem; border-radius: 0.25rem; background-color: #f3f4f6; color: #374151;">{row['type']}</span></div>
            <div style="flex: 4;">{row['summary']}</div>
            <div style="flex: 1;"><a href="#" style="color: #2563eb; text-decoration: none;">View</a></div>
        </div>
        """, unsafe_allow_html=True)

# Initialize session state for view mode
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "standard"

# Main application layout
st.title("Legal Arguments Analysis")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])

# Tab 1: Summary of Arguments
with tab1:
    # View mode selection
    view_col1, view_col2 = st.columns([3, 1])
    with view_col2:
        view_options = ["Standard View", "Topic View"]
        view_index = 0 if st.session_state.view_mode == "standard" else 1
        
        # Use radio buttons for view mode selection
        view_mode = st.radio(
            "View Mode:",
            options=view_options,
            index=view_index,
            horizontal=True,
            key="view_mode_radio"
        )
        
        # Update session state
        st.session_state.view_mode = "standard" if view_mode == "Standard View" else "hierarchical"
    
    # Render appropriate view
    if st.session_state.view_mode == "standard":
        render_standard_view()
    else:
        render_hierarchical_view()

# Tab 2: Timeline
with tab2:
    render_timeline_view()

# Tab 3: Exhibits
with tab3:
    render_exhibits_view()

# Hide Streamlit branding
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
