import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.card import card
import streamlit.components.v1 as components
import json
from datetime import datetime
import re

# Set page configuration
st.set_page_config(
    page_title="Legal Arguments Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match the React design
st.markdown("""
<style>
    /* General styling */
    .main {
        background-color: #f9fafb;
        padding: 1rem;
    }
    .card {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .tab-nav {
        display: flex;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
    }
    .tab {
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        font-size: 0.875rem;
        cursor: pointer;
    }
    .tab-active {
        color: #2563eb;
        border-bottom: 2px solid #2563eb;
    }
    .tab-inactive {
        color: #6b7280;
    }
    .tab-inactive:hover {
        color: #374151;
    }
    
    /* Arguments styling */
    .argument-header {
        display: flex;
        align-items: center;
        padding: 0.75rem;
        cursor: pointer;
        border-radius: 0.5rem;
    }
    .claimant-header {
        background-color: rgba(219, 234, 254, 0.4);
        border: 1px solid #bfdbfe;
    }
    .respondent-header {
        background-color: rgba(254, 226, 226, 0.4);
        border: 1px solid #fecaca;
    }
    .argument-title {
        font-weight: 500;
        font-size: 0.875rem;
        margin-left: 0.5rem;
    }
    .claimant-title {
        color: #2563eb;
    }
    .respondent-title {
        color: #dc2626;
    }
    .badge {
        font-size: 0.75rem;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        margin-left: 0.5rem;
    }
    .badge-blue {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .badge-red {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .badge-gray {
        background-color: #f3f4f6;
        color: #4b5563;
    }
    
    /* Points and evidence styling */
    .points-section {
        background-color: #f9fafb;
        border-radius: 0.375rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .legal-point {
        background-color: #dbeafe;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .factual-point {
        background-color: #d1fae5;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .evidence-item {
        background-color: #f3f4f6;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .case-law-item {
        background-color: #f3f4f6;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .disputed-tag {
        background-color: #fee2e2;
        color: #b91c1c;
        font-size: 0.75rem;
        padding: 0.125rem 0.5rem;
        border-radius: 0.25rem;
        margin-left: 0.5rem;
    }
    .regulation-tag {
        background-color: #dbeafe;
        font-size: 0.75rem;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        margin-right: 0.25rem;
        display: inline-block;
    }
    .paragraph-ref {
        color: #6b7280;
        font-size: 0.75rem;
    }
    
    /* Topic view specific styling */
    .topic-section {
        margin-bottom: 2rem;
    }
    .topic-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #111827;
        margin-bottom: 0.25rem;
    }
    .topic-description {
        font-size: 0.875rem;
        color: #6b7280;
        margin-bottom: 1rem;
    }
    
    /* Hide Streamlit elements we don't need */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Connector lines for nested arguments */
    .connector-line {
        border-left: 1px solid rgba(59, 130, 246, 0.5);
        margin-left: 1rem;
        padding-left: 1rem;
    }
    .connector-line-respondent {
        border-left: 1px solid rgba(239, 68, 68, 0.5);
    }
    
    /* Custom toggle button styling */
    .view-toggle {
        display: flex;
        background-color: #f3f4f6;
        border-radius: 0.375rem;
        padding: 0.25rem;
        width: fit-content;
        margin-left: auto;
        margin-bottom: 1rem;
    }
    .toggle-btn {
        padding: 0.5rem 0.75rem;
        font-size: 0.875rem;
        font-weight: 500;
        border-radius: 0.25rem;
        cursor: pointer;
    }
    .toggle-btn-active {
        background-color: white;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    .toggle-btn-inactive {
        color: #6b7280;
    }
    .toggle-btn-inactive:hover {
        color: #374151;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for expanded arguments and active tab
if 'expanded_args' not in st.session_state:
    st.session_state.expanded_args = {}
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "arguments"
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "default"

# Function to toggle argument expansion
def toggle_expand(arg_id):
    if arg_id in st.session_state.expanded_args:
        st.session_state.expanded_args[arg_id] = not st.session_state.expanded_args[arg_id]
    else:
        st.session_state.expanded_args[arg_id] = True
    st.experimental_rerun()

# Function to render overview points
def render_overview_points(points, paragraphs):
    with st.container():
        st.markdown(f"""
        <div class="points-section">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                <span class="badge badge-blue">¶{paragraphs}</span>
            </div>
            <ul style="list-style-type: none; padding-left: 0; margin-top: 0.5rem;">
                {"".join([f'<li style="display: flex; align-items: center; margin-bottom: 0.5rem;"><div style="width: 6px; height: 6px; border-radius: 50%; background-color: #3b82f6; margin-right: 0.5rem;"></div><span style="font-size: 0.875rem; color: #4b5563;">{point}</span></li>' for point in points])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Function to render legal points
def render_legal_points(points):
    for point in points:
        st.markdown(f"""
        <div class="legal-point">
            <div style="display: flex; align-items: center; margin-bottom: 0.25rem;">
                <span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: #dbeafe; color: #1e40af; border-radius: 0.25rem;">Legal</span>
                {f'<span class="disputed-tag">Disputed</span>' if point.get('isDisputed') else ''}
            </div>
            <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{point['point']}</p>
            <div style="margin-top: 0.5rem;">
                {"".join([f'<span class="regulation-tag">{reg}</span>' for reg in point.get('regulations', [])])}
                <span class="paragraph-ref">¶{point['paragraphs']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Function to render factual points
def render_factual_points(points):
    for point in points:
        st.markdown(f"""
        <div class="factual-point">
            <div style="display: flex; align-items: center; margin-bottom: 0.25rem;">
                <span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: #d1fae5; color: #065f46; border-radius: 0.25rem;">Factual</span>
                {f'<span class="disputed-tag">Disputed by {point["source"]}</span>' if point.get('isDisputed') else ''}
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.25rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                <span style="font-size: 0.75rem; color: #6b7280; margin-left: 0.5rem;">{point['date']}</span>
            </div>
            <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{point['point']}</p>
            <span class="paragraph-ref">¶{point['paragraphs']}</span>
        </div>
        """, unsafe_allow_html=True)

# Function to render evidence references
def render_evidence(items):
    for item in items:
        st.markdown(f"""
        <div class="evidence-item">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <p style="font-size: 0.875rem; font-weight: 500; margin: 0;">{item['id']}: {item['title']}</p>
                    <p style="font-size: 0.75rem; color: #6b7280; margin: 0.25rem 0;">{item['summary']}</p>
                    <div style="margin-top: 0.5rem;">
                        <span style="font-size: 0.75rem; color: #6b7280;">Cited in: </span>
                        {"".join([f'<span style="font-size: 0.75rem; background-color: #e5e7eb; border-radius: 0.25rem; padding: 0.25rem 0.5rem; margin-left: 0.25rem;">¶{cite}</span>' for cite in item['citations']])}
                    </div>
                </div>
                <button style="background: none; border: none; color: #6b7280; padding: 0.25rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Function to render case law references
def render_case_law(items):
    for item in items:
        st.markdown(f"""
        <div class="case-law-item">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <div style="display: flex; align-items: center;">
                        <p style="font-size: 0.875rem; font-weight: 500; margin: 0;">{item['caseNumber']}</p>
                        <span style="font-size: 0.75rem; color: #6b7280; margin-left: 0.5rem;">¶{item['paragraphs']}</span>
                    </div>
                    <p style="font-size: 0.75rem; color: #6b7280; margin: 0.25rem 0;">{item['title']}</p>
                    <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{item['relevance']}</p>
                    {f'''
                    <div style="margin-top: 0.5rem;">
                        <span style="font-size: 0.75rem; color: #6b7280;">Key Paragraphs: </span>
                        {"".join([f'<span style="font-size: 0.75rem; background-color: #e5e7eb; border-radius: 0.25rem; padding: 0.25rem 0.5rem; margin-left: 0.25rem;">¶{para}</span>' for para in item.get('citedParagraphs', [])])}
                    </div>
                    ''' if item.get('citedParagraphs') else ''}
                </div>
                <button style="background: none; border: none; color: #6b7280; padding: 0.25rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Function to render an argument section
def render_argument_section(arg_id, title, paragraphs, side, level=0, overview=None, 
                           legal_points=None, factual_points=None, evidence=None, 
                           case_law=None, children=None, is_aligned=False, connector=False):
    
    base_color = "blue" if side == "claimant" else "red"
    header_class = "claimant-header" if side == "claimant" else "respondent-header"
    title_class = "claimant-title" if side == "claimant" else "respondent-title"
    
    # Check if this argument is expanded
    is_expanded = st.session_state.expanded_args.get(arg_id, False)
    
    # Create the clickable header
    header = f"""
    <div class="argument-header {header_class}" onclick="handleArgClick('{arg_id}')" id="arg-header-{arg_id}">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" 
             stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            {'<polyline points="6 9 12 15 18 9"></polyline>' if is_expanded else '<polyline points="9 18 15 12 9 6"></polyline>'}
        </svg>
        <span class="argument-title {title_class}">{arg_id}. {title}</span>
        {f'<span class="badge badge-{base_color}">{len(children) if children else 0} subarguments</span>' if children else f'<span class="badge badge-gray">¶{paragraphs}</span>'}
    </div>
    """
    
    # Create a container for the argument
    with st.container():
        st.markdown(header, unsafe_allow_html=True)
        
        # If expanded, show the content
        if is_expanded:
            with st.container():
                st.markdown('<div style="padding: 1rem; border: 1px solid #e5e7eb; border-top: none; border-radius: 0 0 0.5rem 0.5rem;">', unsafe_allow_html=True)
                
                # Overview points
                if overview and 'points' in overview:
                    render_overview_points(overview['points'], overview['paragraphs'])
                
                # Legal points
                if legal_points and len(legal_points) > 0:
                    st.markdown('<h6 style="font-size: 0.875rem; font-weight: 500; margin: 1rem 0 0.5rem 0;">Legal Points</h6>', unsafe_allow_html=True)
                    render_legal_points(legal_points)
                
                # Factual points
                if factual_points and len(factual_points) > 0:
                    st.markdown('<h6 style="font-size: 0.875rem; font-weight: 500; margin: 1rem 0 0.5rem 0;">Factual Points</h6>', unsafe_allow_html=True)
                    render_factual_points(factual_points)
                
                # Evidence
                if evidence and len(evidence) > 0:
                    st.markdown('<h6 style="font-size: 0.875rem; font-weight: 500; margin: 1rem 0 0.5rem 0;">Evidence</h6>', unsafe_allow_html=True)
                    render_evidence(evidence)
                
                # Case law
                if case_law and len(case_law) > 0:
                    st.markdown('<h6 style="font-size: 0.875rem; font-weight: 500; margin: 1rem 0 0.5rem 0;">Case Law</h6>', unsafe_allow_html=True)
                    render_case_law(case_law)
                
                st.markdown('</div>', unsafe_allow_html=True)
        
        # Add JavaScript to handle click events
        st.markdown(f"""
        <script>
        function handleArgClick(id) {{
            // Use Streamlit's messaging to send the ID back to Python
            window.parent.postMessage({{
                type: "streamlit:setComponentValue",
                value: id,
                dataType: "json"
            }}, "*");
        }}
        </script>
        """, unsafe_allow_html=True)

# Function to render an argument pair
def render_argument_pair(claimant_data, respondent_data, level=0, is_root=True):
    col1, col2 = st.columns(2)
    
    with col1:
        render_argument_section(
            arg_id=claimant_data['id'],
            title=claimant_data['title'],
            paragraphs=claimant_data['paragraphs'],
            side="claimant",
            level=level,
            overview=claimant_data.get('overview'),
            legal_points=claimant_data.get('legalPoints'),
            factual_points=claimant_data.get('factualPoints'),
            evidence=claimant_data.get('evidence'),
            case_law=claimant_data.get('caseLaw'),
            children=claimant_data.get('children'),
            is_aligned=True
        )
    
    with col2:
        render_argument_section(
            arg_id=respondent_data['id'],
            title=respondent_data['title'],
            paragraphs=respondent_data['paragraphs'],
            side="respondent",
            level=level,
            overview=respondent_data.get('overview'),
            legal_points=respondent_data.get('legalPoints'),
            factual_points=respondent_data.get('factualPoints'),
            evidence=respondent_data.get('evidence'),
            case_law=respondent_data.get('caseLaw'),
            children=respondent_data.get('children'),
            is_aligned=True
        )

# Sample data for arguments (same structure as in the React version)
def get_arguments_data():
    return [
        {
            'id': '1',
            'claimant': {
                'id': '1',
                'title': 'Sporting Succession',
                'paragraphs': '15-18',
                'overview': {
                    'points': [
                        "Analysis of multiple established criteria",
                        "Focus on continuous use of identifying elements",
                        "Public recognition assessment"
                    ],
                    'paragraphs': '15-16'
                },
                'legalPoints': [
                    {
                        'point': 'CAS jurisprudence establishes criteria for sporting succession',
                        'isDisputed': False,
                        'regulations': ['CAS 2016/A/4576'],
                        'paragraphs': '15-17'
                    }
                ],
                'factualPoints': [
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
                'caseLaw': [
                    {
                        'caseNumber': 'CAS 2016/A/4576',
                        'title': 'Criteria for sporting succession',
                        'relevance': 'Establishes key factors for succession',
                        'paragraphs': '45-48',
                        'citedParagraphs': ['45', '46', '47']
                    }
                ],
                'children': [
                    # Nested argument sections would go here
                ]
            },
            'respondent': {
                'id': '1',
                'title': 'Sporting Succession Rebuttal',
                'paragraphs': '200-218',
                'overview': {
                    'points': [
                        "Challenge to claimed continuity of operations",
                        "Analysis of discontinuities in club operations",
                        "Dispute over public recognition factors"
                    ],
                    'paragraphs': '200-202'
                },
                'legalPoints': [
                    {
                        'point': 'CAS jurisprudence requires operational continuity not merely identification',
                        'isDisputed': False,
                        'regulations': ['CAS 2017/A/5465'],
                        'paragraphs': '203-205'
                    }
                ],
                'factualPoints': [
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
                'caseLaw': [
                    {
                        'caseNumber': 'CAS 2017/A/5465',
                        'title': 'Operational continuity requirement',
                        'relevance': 'Establishes primacy of operational continuity',
                        'paragraphs': '211-213',
                        'citedParagraphs': ['212']
                    }
                ],
                'children': [
                    # Nested argument sections would go here
                ]
            }
        },
        {
            'id': '2',
            'claimant': {
                'id': '2',
                'title': 'Doping Violation Chain of Custody',
                'paragraphs': '70-125',
                'overview': {
                    'points': [
                        "Analysis of sample collection and handling procedures",
                        "Evaluation of laboratory testing protocols",
                        "Assessment of chain of custody documentation"
                    ],
                    'paragraphs': '70-72'
                },
                'legalPoints': [
                    {
                        'point': 'WADA Code Article 5 establishes procedural requirements',
                        'isDisputed': False,
                        'regulations': ['WADA Code 2021', 'International Standard for Testing'],
                        'paragraphs': '73-75'
                    }
                ]
            },
            'respondent': {
                'id': '2',
                'title': 'Doping Chain of Custody Defense',
                'paragraphs': '250-290',
                'overview': {
                    'points': [
                        "Defense of sample collection procedures",
                        "Validation of laboratory testing protocols",
                        "Completeness of documentation"
                    ],
                    'paragraphs': '250-252'
                },
                'legalPoints': [
                    {
                        'point': 'Minor procedural deviations do not invalidate results',
                        'isDisputed': False,
                        'regulations': ['CAS 2019/A/6148'],
                        'paragraphs': '253-255'
                    }
                ]
            }
        }
    ]

# Timeline data
def get_timeline_data():
    return [
        { 
            'date': '2023-01-15', 
            'appellantVersion': 'Contract signed with Club', 
            'respondentVersion': '—', 
            'status': 'Undisputed' 
        },
        { 
            'date': '2023-03-20', 
            'appellantVersion': 'Player received notification of exclusion from team', 
            'respondentVersion': '—', 
            'status': 'Undisputed' 
        },
        { 
            'date': '2023-03-22', 
            'appellantVersion': 'Player requested explanation', 
            'respondentVersion': '—', 
            'status': 'Undisputed' 
        },
        { 
            'date': '2023-04-01', 
            'appellantVersion': 'Player sent termination letter', 
            'respondentVersion': '—', 
            'status': 'Undisputed' 
        },
        { 
            'date': '2023-04-05', 
            'appellantVersion': '—', 
            'respondentVersion': 'Club rejected termination as invalid', 
            'status': 'Undisputed' 
        },
        { 
            'date': '2023-04-10', 
            'appellantVersion': 'Player was denied access to training facilities', 
            'respondentVersion': '—', 
            'status': 'Disputed' 
        },
        { 
            'date': '2023-04-15', 
            'appellantVersion': '—', 
            'respondentVersion': 'Club issued warning letter', 
            'status': 'Undisputed' 
        },
        { 
            'date': '2023-05-01', 
            'appellantVersion': 'Player filed claim with FIFA', 
            'respondentVersion': '—', 
            'status': 'Undisputed' 
        },
    ]

# Exhibits data
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

# Topic data for hierarchical view
def get_topic_data():
    return [
        {
            'id': 'topic-1',
            'title': 'Sporting Succession and Identity',
            'description': 'Questions of club identity, continuity, and succession rights',
            'arguments': [
                {
                    'claimant': {
                        'id': '1',
                        'title': 'Sporting Succession',
                        'paragraphs': '15-18',
                        'overview': {
                            'points': [
                                "Analysis of multiple established criteria",
                                "Focus on continuous use of identifying elements",
                                "Public recognition assessment"
                            ],
                            'paragraphs': '15-16'
                        },
                        'legalPoints': [
                            {
                                'point': 'CAS jurisprudence establishes criteria for sporting succession',
                                'isDisputed': False,
                                'regulations': ['CAS 2016/A/4576'],
                                'paragraphs': '15-17'
                            }
                        ],
                        'factualPoints': [
                            {
                                'point': 'Continuous operation under same name since 1950',
                                'date': '1950-present',
                                'isDisputed': False,
                                'paragraphs': '18-19'
                            }
                        ]
                    },
                    'respondent': {
                        'id': '1',
                        'title': 'Sporting Succession Rebuttal',
                        'paragraphs': '200-218',
                        'overview': {
                            'points': [
                                "Challenge to claimed continuity of operations",
                                "Analysis of discontinuities in club operations",
                                "Dispute over public recognition factors"
                            ],
                            'paragraphs': '200-202'
                        },
                        'legalPoints': [
                            {
                                'point': 'CAS jurisprudence requires operational continuity not merely identification',
                                'isDisputed': False,
                                'regulations': ['CAS 2017/A/5465'],
                                'paragraphs': '203-205'
                            }
                        ],
                        'factualPoints': [
                            {
                                'point': 'Operations ceased between 1975-1976',
                                'date': '1975-1976',
                                'isDisputed': True,
                                'source': 'Claimant',
                                'paragraphs': '206-207'
                            }
                        ]
                    }
                }
            ]
        },
        {
            'id': 'topic-2',
            'title': 'Doping Violation and Chain of Custody',
            'description': 'Issues related to doping test procedures and evidence handling',
            'arguments': [
                {
                    'claimant': {
                        'id': '2',
                        'title': 'Doping Violation Chain of Custody',
                        'paragraphs': '70-125',
                        'overview': {
                            'points': [
                                "Analysis of sample collection and handling procedures",
                                "Evaluation of laboratory testing protocols",
                                "Assessment of chain of custody documentation"
                            ],
                            'paragraphs': '70-72'
                        },
                        'legalPoints': [
                            {
                                'point': 'WADA Code Article 5 establishes procedural requirements',
                                'isDisputed': False,
                                'regulations': ['WADA Code 2021', 'International Standard for Testing'],
                                'paragraphs': '73-75'
                            }
                        ]
                    },
                    'respondent': {
                        'id': '2',
                        'title': 'Doping Chain of Custody Defense',
                        'paragraphs': '250-290',
                        'overview': {
                            'points': [
                                "Defense of sample collection procedures",
                                "Validation of laboratory testing protocols",
                                "Completeness of documentation"
                            ],
                            'paragraphs': '250-252'
                        },
                        'legalPoints': [
                            {
                                'point': 'Minor procedural deviations do not invalidate results',
                                'isDisputed': False,
                                'regulations': ['CAS 2019/A/6148'],
                                'paragraphs': '253-255'
                            }
                        ]
                    }
                }
            ]
        }
    ]

# Timeline view component
def render_timeline_view():
    data = get_timeline_data()
    
    search = st.text_input("", placeholder="Search events...", key="timeline_search")
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.button("Filter", key="timeline_filter")
    
    with col2:
        show_disputed = st.checkbox("Disputed events only", key="timeline_disputed")
    
    # Filter data based on search and checkbox
    filtered_data = data
    if search:
        filtered_data = [item for item in data if search.lower() in item['appellantVersion'].lower() or search.lower() in item['respondentVersion'].lower()]
    
    if show_disputed:
        filtered_data = [item for item in filtered_data if item['status'] == 'Disputed']
    
    # Create DataFrame for display
    df = pd.DataFrame(filtered_data)
    
    # Apply styling
    def highlight_disputed(val):
        return 'background-color: rgba(254, 226, 226, 0.5)' if val == 'Disputed' else ''
    
    def color_status(val):
        return f'color: {"#dc2626" if val == "Disputed" else "#16a34a"}'
    
    styled_df = df.style.applymap(highlight_disputed, subset=['status'])
    styled_df = styled_df.applymap(color_status, subset=['status'])
    
    st.dataframe(
        styled_df,
        column_config={
            "date": "DATE",
            "appellantVersion": "APPELLANT'S VERSION",
            "respondentVersion": "RESPONDENT'S VERSION",
            "status": "STATUS"
        },
        hide_index=True
    )

# Exhibits view component
def render_exhibits_view():
    data = get_exhibits_data()
    
    search = st.text_input("", placeholder="Search exhibits...", key="exhibits_search")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        party_filter = st.selectbox("", ["All Parties", "Appellant", "Respondent"], key="exhibits_party")
    
    with col2:
        types = ["All Types"] + list(set([item['type'] for item in data]))
        type_filter = st.selectbox("", types, key="exhibits_type")
    
    # Filter data
    filtered_data = data
    if search:
        filtered_data = [item for item in data if search.lower() in item['id'].lower() or search.lower() in item['title'].lower() or search.lower() in item['summary'].lower()]
    
    if party_filter != "All Parties":
        filtered_data = [item for item in filtered_data if item['party'] == party_filter]
    
    if type_filter != "All Types":
        filtered_data = [item for item in filtered_data if item['type'] == type_filter]
    
    # Create DataFrame
    df = pd.DataFrame(filtered_data)
    
    # Apply styling for party badges
    def format_party(val):
        color = "blue" if val == "Appellant" else "red"
        return f'<span style="background-color: {color}15; color: {color}; padding: 2px 6px; border-radius: 4px; font-size: 0.8em;">{val}</span>'
    
    def format_type(val):
        return f'<span style="background-color: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 0.8em;">{val}</span>'
    
    def add_view_button(val):
        return f'<a href="#" style="color: #2563eb; text-decoration: none;">View</a>'
    
    st.markdown(
        """
        <div style="height: 600px; overflow-y: auto;">
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: #f9fafb; border-bottom: 1px solid #e5e7eb;">
                    <th style="padding: 12px 16px; text-align: left; font-size: 0.8em; color: #6b7280;">EXHIBIT ID</th>
                    <th style="padding: 12px 16px; text-align: left; font-size: 0.8em; color: #6b7280;">PARTY</th>
                    <th style="padding: 12px 16px; text-align: left; font-size: 0.8em; color: #6b7280;">TITLE</th>
                    <th style="padding: 12px 16px; text-align: left; font-size: 0.8em; color: #6b7280;">TYPE</th>
                    <th style="padding: 12px 16px; text-align: left; font-size: 0.8em; color: #6b7280;">SUMMARY</th>
                    <th style="padding: 12px 16px; text-align: right; font-size: 0.8em; color: #6b7280;">ACTIONS</th>
                </tr>
            </thead>
            <tbody>
                {"".join([f'''
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 12px 16px; font-size: 0.9em;">{item['id']}</td>
                    <td style="padding: 12px 16px;">
                        <span style="background-color: {'rgba(219, 234, 254, 0.7)' if item['party'] == 'Appellant' else 'rgba(254, 226, 226, 0.7)'}; 
                               color: {'#1e40af' if item['party'] == 'Appellant' else '#b91c1c'}; 
                               padding: 4px 8px; border-radius: 4px; font-size: 0.8em;">
                            {item['party']}
                        </span>
                    </td>
                    <td style="padding: 12px 16px; font-size: 0.9em;">{item['title']}</td>
                    <td style="padding: 12px 16px;">
                        <span style="background-color: #f3f4f6; padding: 4px 8px; border-radius: 4px; font-size: 0.8em;">
                            {item['type']}
                        </span>
                    </td>
                    <td style="padding: 12px 16px; font-size: 0.9em;">{item['summary']}</td>
                    <td style="padding: 12px 16px; text-align: right;">
                        <a href="#" style="color: #2563eb; text-decoration: none; font-size: 0.9em;">View</a>
                    </td>
                </tr>
                ''' for item in filtered_data])}
            </tbody>
        </table>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Hierarchical topic view
def render_topic_view():
    topics = get_topic_data()
    
    for topic in topics:
        st.markdown(f"""
        <div class="topic-section">
            <h2 class="topic-title">{topic['title']}</h2>
            <p class="topic-description">{topic['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Column headers
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h3 style="font-size: 1rem; font-weight: 600; color: #2563eb; margin-bottom: 1rem;">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
        with col2:
            st.markdown('<h3 style="font-size: 1rem; font-weight: 600; color: #dc2626; margin-bottom: 1rem;">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
        
        # Argument pairs
        for arg_pair in topic['arguments']:
            render_argument_pair(arg_pair['claimant'], arg_pair['respondent'])

# Main UI
st.markdown('<h1 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Legal Arguments Analysis</h1>', unsafe_allow_html=True)

# Tab navigation
tab_html = f"""
<div class="tab-nav">
    <div class="tab {'tab-active' if st.session_state.active_tab == 'arguments' else 'tab-inactive'}" 
         onclick="handleTabClick('arguments')">Summary of Arguments</div>
    <div class="tab {'tab-active' if st.session_state.active_tab == 'timeline' else 'tab-inactive'}" 
         onclick="handleTabClick('timeline')">Timeline</div>
    <div class="tab {'tab-active' if st.session_state.active_tab == 'exhibits' else 'tab-inactive'}" 
         onclick="handleTabClick('exhibits')">Exhibits</div>
</div>
<script>
function handleTabClick(tab) {{
    window.parent.postMessage({{
        type: "streamlit:setComponentValue",
        value: {{"tab": tab}},
        dataType: "json"
    }}, "*");
}}
</script>
"""
components.html(tab_html, height=50)

# Handle the component's output
component_value = st.experimental_get_query_params()
if component_value:
    if 'tab' in component_value:
        st.session_state.active_tab = component_value['tab'][0]
    if 'arg_id' in component_value:
        toggle_expand(component_value['arg_id'][0])

# Actions bar for Timeline and Exhibits views
if st.session_state.active_tab in ['timeline', 'exhibits']:
    col1, col2 = st.columns([5, 1])
    with col2:
        st.download_button("Export Data", "exported_data.csv", "Export")
        st.button("Copy")

# Arguments View Mode Toggle
if st.session_state.active_tab == 'arguments':
    toggle_html = f"""
    <div class="view-toggle">
        <div class="toggle-btn {'toggle-btn-active' if st.session_state.view_mode == 'default' else 'toggle-btn-inactive'}" 
             onclick="handleViewToggle('default')">Standard View</div>
        <div class="toggle-btn {'toggle-btn-active' if st.session_state.view_mode == 'hierarchical' else 'toggle-btn-inactive'}" 
             onclick="handleViewToggle('hierarchical')">Topic View</div>
    </div>
    <script>
    function handleViewToggle(mode) {{
        window.parent.postMessage({{
            type: "streamlit:setComponentValue",
            value: {{"view_mode": mode}},
            dataType: "json"
        }}, "*");
    }}
    </script>
    """
    components.html(toggle_html, height=50)
    
    if st.session_state.view_mode == 'default':
        # Standard view with all arguments
        arguments_data = get_arguments_data()
        for arg_pair in arguments_data:
            render_argument_pair(arg_pair['claimant'], arg_pair['respondent'])
    else:
        # Topic view
        render_topic_view()

# Timeline view
elif st.session_state.active_tab == 'timeline':
    render_timeline_view()

# Exhibits view
elif st.session_state.active_tab == 'exhibits':
    render_exhibits_view()

# JavaScript to handle component communication
st.markdown("""
<script>
// Listen for messages from components
window.addEventListener('message', function(e) {
    if (e.data.type === 'streamlit:componentOutput') {
        const data = e.data.value;
        if (data) {
            // Update URL parameters
            const searchParams = new URLSearchParams(window.location.search);
            
            if (data.tab) {
                searchParams.set('tab', data.tab);
            }
            
            if (data.view_mode) {
                searchParams.set('view_mode', data.view_mode);
            }
            
            if (typeof data === 'string') {
                searchParams.set('arg_id', data);
            }
            
            // Replace URL
            const newUrl = window.location.pathname + '?' + searchParams.toString();
            window.history.replaceState({}, '', newUrl);
            
            // Reload to apply changes
            window.location.reload();
        }
    }
});
</script>
""", unsafe_allow_html=True)
