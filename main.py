import streamlit as st
import pandas as pd
import datetime
import streamlit.components.v1 as components
import json

# Set page configuration
st.set_page_config(
    page_title="Legal Arguments Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling to match the React version
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Card styling */
    .stCard {
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        background-color: white;
        margin-bottom: 1rem;
        padding: 1rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        border-bottom: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        white-space: pre-wrap;
        border-radius: 0;
        border-bottom: 2px solid transparent;
        color: #6b7280;
        font-weight: 500;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        color: #3b82f6 !important;
        border-bottom-color: #3b82f6 !important;
    }
    
    /* Header styling */
    h1 {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    h2 {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }
    h3 {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 5px;
        border: 1px solid #e2e8f0;
        padding: 0.375rem 0.75rem;
        background-color: white;
        font-weight: 500;
        font-size: 0.875rem;
        color: #4b5563;
    }
    
    /* Toggle buttons */
    .toggle-button-group {
        display: flex;
        background-color: #f3f4f6;
        border-radius: 6px;
        padding: 2px;
        width: fit-content;
        margin-left: auto;
    }
    .toggle-button {
        padding: 0.25rem 0.75rem;
        border-radius: 4px;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s;
    }
    .toggle-button.active {
        background-color: white;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    /* Color badges */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.125rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    .badge-blue {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .badge-red {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .badge-green {
        background-color: #d1fae5;
        color: #065f46;
    }
    .badge-gray {
        background-color: #f3f4f6;
        color: #4b5563;
    }
    
    /* Table styling */
    .styled-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        overflow: hidden;
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
        font-size: 0.875rem;
        color: #374151;
        border-bottom: 1px solid #e5e7eb;
    }
    .styled-table tbody tr:last-child td {
        border-bottom: none;
    }
    
    /* Argument sections */
    .argument-section {
        margin-bottom: 1rem;
        border-radius: 8px;
        overflow: hidden;
    }
    .argument-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.75rem 1rem;
        cursor: pointer;
    }
    .claimant-header {
        background-color: #eff6ff;
        border: 1px solid #bfdbfe;
    }
    .respondent-header {
        background-color: #fee2e2;
        border: 1px solid #fecaca;
    }
    .argument-content {
        padding: 1rem;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-top: none;
    }
    
    /* Points */
    .points-card {
        background-color: #f9fafb;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .legal-point {
        background-color: #eff6ff;
        border-radius: 8px;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .factual-point {
        background-color: #d1fae5;
        border-radius: 8px;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    /* Disputed label */
    .disputed-label {
        background-color: #fee2e2;
        color: #b91c1c;
        padding: 0.125rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    /* Row styling for disputed events */
    .disputed-row {
        background-color: #fee2e2;
    }
    
    /* Two column grid */
    .two-column-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    
    /* Custom checkbox */
    .stCheckbox > div {
        display: flex;
        align-items: center;
    }
    .stCheckbox label {
        font-size: 0.875rem;
        color: #4b5563;
        font-weight: normal;
    }
</style>
""", unsafe_allow_html=True)

# Data for the application
def load_data():
    # Arguments data
    arguments_data = {
        "claimant": {
            "1": {
                "id": "1",
                "title": "Sporting Succession",
                "paragraphs": "15-18",
                "overview": {
                    "points": [
                        "Analysis of multiple established criteria",
                        "Focus on continuous use of identifying elements",
                        "Public recognition assessment"
                    ],
                    "paragraphs": "15-16"
                },
                "legal_points": [
                    {
                        "point": "CAS jurisprudence establishes criteria for sporting succession",
                        "is_disputed": False,
                        "regulations": ["CAS 2016/A/4576"],
                        "paragraphs": "15-17"
                    }
                ],
                "factual_points": [
                    {
                        "point": "Continuous operation under same name since 1950",
                        "date": "1950-present",
                        "is_disputed": False,
                        "paragraphs": "18-19"
                    }
                ],
                "evidence": [
                    {
                        "id": "C-1",
                        "title": "Historical Registration Documents",
                        "summary": "Official records showing continuous name usage",
                        "citations": ["20", "21", "24"]
                    }
                ],
                "case_law": [
                    {
                        "case_number": "CAS 2016/A/4576",
                        "title": "Criteria for sporting succession",
                        "relevance": "Establishes key factors for succession",
                        "paragraphs": "45-48",
                        "cited_paragraphs": ["45", "46", "47"]
                    }
                ],
                "children": {
                    "1.1": {
                        "id": "1.1",
                        "title": "Club Name Analysis",
                        "paragraphs": "20-45",
                        "overview": {
                            "points": [
                                "Historical continuity of name usage",
                                "Legal protection of naming rights",
                                "Public recognition of club name"
                            ],
                            "paragraphs": "20-21"
                        },
                        "legal_points": [
                            {
                                "point": "Name registration complies with regulations",
                                "is_disputed": False,
                                "regulations": ["Name Registration Act"],
                                "paragraphs": "22-24"
                            },
                            {
                                "point": "Trademark protection since 1960",
                                "is_disputed": False,
                                "regulations": ["Trademark Law"],
                                "paragraphs": "25-27"
                            }
                        ],
                        "children": {}  # Simplified for brevity
                    },
                    "1.2": {
                        "id": "1.2",
                        "title": "Club Colors Analysis",
                        "paragraphs": "46-65",
                        "overview": {
                            "points": [
                                "Consistent use of club colors",
                                "Minor variations analysis",
                                "Color trademark protection"
                            ],
                            "paragraphs": "46-47"
                        },
                        "legal_points": [
                            {
                                "point": "Color trademark registration valid since 1960",
                                "is_disputed": False,
                                "regulations": ["Trademark Act"],
                                "paragraphs": "48-50"
                            }
                        ],
                        "factual_points": [
                            {
                                "point": "Consistent use of blue and white since founding",
                                "date": "1950-present",
                                "is_disputed": True,
                                "source": "Respondent",
                                "paragraphs": "51-52"
                            }
                        ],
                        "children": {}  # Simplified for brevity
                    }
                }
            },
            "2": {
                "id": "2",
                "title": "Doping Violation Chain of Custody",
                "paragraphs": "70-125",
                "overview": {
                    "points": [
                        "Analysis of sample collection and handling procedures",
                        "Evaluation of laboratory testing protocols",
                        "Assessment of chain of custody documentation"
                    ],
                    "paragraphs": "70-72"
                },
                "legal_points": [
                    {
                        "point": "WADA Code Article 5 establishes procedural requirements",
                        "is_disputed": False,
                        "regulations": ["WADA Code 2021", "International Standard for Testing"],
                        "paragraphs": "73-75"
                    }
                ],
                "children": {}
            }
        },
        "respondent": {
            "1": {
                "id": "1",
                "title": "Sporting Succession Rebuttal",
                "paragraphs": "200-218",
                "overview": {
                    "points": [
                        "Challenge to claimed continuity of operations",
                        "Analysis of discontinuities in club operations",
                        "Dispute over public recognition factors"
                    ],
                    "paragraphs": "200-202"
                },
                "legal_points": [
                    {
                        "point": "CAS jurisprudence requires operational continuity not merely identification",
                        "is_disputed": False,
                        "regulations": ["CAS 2017/A/5465"],
                        "paragraphs": "203-205"
                    }
                ],
                "factual_points": [
                    {
                        "point": "Operations ceased between 1975-1976",
                        "date": "1975-1976",
                        "is_disputed": True,
                        "source": "Claimant",
                        "paragraphs": "206-207"
                    }
                ],
                "evidence": [
                    {
                        "id": "R-1",
                        "title": "Federation Records",
                        "summary": "Records showing non-participation in 1975-1976 season",
                        "citations": ["208", "209", "210"]
                    }
                ],
                "case_law": [
                    {
                        "case_number": "CAS 2017/A/5465",
                        "title": "Operational continuity requirement",
                        "relevance": "Establishes primacy of operational continuity",
                        "paragraphs": "211-213",
                        "cited_paragraphs": ["212"]
                    }
                ],
                "children": {
                    "1.1": {
                        "id": "1.1",
                        "title": "Club Name Analysis Rebuttal",
                        "paragraphs": "220-240",
                        "overview": {
                            "points": [
                                "Name registration discontinuities",
                                "Trademark ownership gaps",
                                "Analysis of public confusion"
                            ],
                            "paragraphs": "220-222"
                        },
                        "legal_points": [
                            {
                                "point": "Registration lapse voided legal continuity",
                                "is_disputed": True,
                                "regulations": ["Registration Act"],
                                "paragraphs": "223-225"
                            }
                        ],
                        "children": {}  # Simplified for brevity
                    },
                    "1.2": {
                        "id": "1.2",
                        "title": "Club Colors Analysis Rebuttal",
                        "paragraphs": "241-249",
                        "overview": {
                            "points": [
                                "Significant color variations",
                                "Trademark registration gaps",
                                "Multiple competing color claims"
                            ],
                            "paragraphs": "241-242"
                        },
                        "legal_points": [
                            {
                                "point": "Color trademark lapsed during 1975-1976",
                                "is_disputed": False,
                                "regulations": ["Trademark Act"],
                                "paragraphs": "243-244"
                            }
                        ],
                        "factual_points": [
                            {
                                "point": "Significant color scheme change in 1976",
                                "date": "1976",
                                "is_disputed": True,
                                "source": "Claimant",
                                "paragraphs": "245-246"
                            }
                        ],
                        "children": {}  # Simplified for brevity
                    }
                }
            },
            "2": {
                "id": "2",
                "title": "Doping Chain of Custody Defense",
                "paragraphs": "250-290",
                "overview": {
                    "points": [
                        "Defense of sample collection procedures",
                        "Validation of laboratory testing protocols",
                        "Completeness of documentation"
                    ],
                    "paragraphs": "250-252"
                },
                "legal_points": [
                    {
                        "point": "Minor procedural deviations do not invalidate results",
                        "is_disputed": False,
                        "regulations": ["CAS 2019/A/6148"],
                        "paragraphs": "253-255"
                    }
                ],
                "children": {}
            }
        }
    }
    
    # Timeline data
    timeline_data = pd.DataFrame([
        {
            "date": "2023-01-15",
            "appellant_version": "Contract signed with Club",
            "respondent_version": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-03-20",
            "appellant_version": "Player received notification of exclusion from team",
            "respondent_version": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-03-22",
            "appellant_version": "Player requested explanation",
            "respondent_version": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-01",
            "appellant_version": "Player sent termination letter",
            "respondent_version": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-05",
            "appellant_version": "—",
            "respondent_version": "Club rejected termination as invalid",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-10",
            "appellant_version": "Player was denied access to training facilities",
            "respondent_version": "—",
            "status": "Disputed"
        },
        {
            "date": "2023-04-15",
            "appellant_version": "—",
            "respondent_version": "Club issued warning letter",
            "status": "Undisputed"
        },
        {
            "date": "2023-05-01",
            "appellant_version": "Player filed claim with FIFA",
            "respondent_version": "—",
            "status": "Undisputed"
        }
    ])
    
    # Exhibits data
    exhibits_data = pd.DataFrame([
        {
            "id": "C-1",
            "party": "Appellant",
            "title": "Employment Contract",
            "type": "contract",
            "summary": "Employment contract dated 15 January 2023 between Player and Club"
        },
        {
            "id": "C-2",
            "party": "Appellant",
            "title": "Termination Letter",
            "type": "letter",
            "summary": "Player's termination letter sent on 1 April 2023"
        },
        {
            "id": "C-3",
            "party": "Appellant",
            "title": "Email Correspondence",
            "type": "communication",
            "summary": "Email exchanges between Player and Club from 22-30 March 2023"
        },
        {
            "id": "C-4",
            "party": "Appellant",
            "title": "Witness Statement",
            "type": "statement",
            "summary": "Statement from team captain confirming Player's exclusion"
        },
        {
            "id": "R-1",
            "party": "Respondent",
            "title": "Club Regulations",
            "type": "regulations",
            "summary": "Internal regulations of the Club dated January 2022"
        },
        {
            "id": "R-2",
            "party": "Respondent",
            "title": "Warning Letter",
            "type": "letter",
            "summary": "Warning letter issued to Player on 15 April 2023"
        },
        {
            "id": "R-3",
            "party": "Respondent",
            "title": "Training Schedule",
            "type": "schedule",
            "summary": "Team training schedule for March-April 2023"
        }
    ])
    
    # Topic sections data
    topic_sections = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argument_ids": ["1"]
        },
        {
            "id": "topic-2",
            "title": "Doping Violation and Chain of Custody",
            "description": "Issues related to doping test procedures and evidence handling",
            "argument_ids": ["2"]
        }
    ]
    
    return arguments_data, timeline_data, exhibits_data, topic_sections

arguments_data, timeline_data, exhibits_data, topic_sections = load_data()

# Initialize session state for expansion states
if 'expanded_states' not in st.session_state:
    st.session_state.expanded_states = {}

if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "default"

# Card container with title
st.markdown('<div class="stCard">', unsafe_allow_html=True)
st.markdown('<h1>Legal Arguments Analysis</h1>', unsafe_allow_html=True)

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])

# Helper function to render an overview points card
def render_overview_points(points, paragraphs):
    st.markdown(f"""
    <div class="points-card">
        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
            <h6 style="font-size: 0.875rem; font-weight: 500; margin: 0;">Key Points</h6>
            <span class="badge badge-blue">¶{paragraphs}</span>
        </div>
        <ul style="list-style-type: none; padding: 0; margin: 0; space-y: 0.5rem;">
            {"".join([f'<li style="display: flex; align-items: center; gap: 0.5rem; margin-top: 0.5rem;"><div style="width: 6px; height: 6px; border-radius: 50%; background-color: #3b82f6;"></div><span style="font-size: 0.875rem; color: #4b5563;">{point}</span></li>' for point in points])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Helper function to render a legal point
def render_legal_point(point, is_disputed, regulations, paragraphs):
    st.markdown(f"""
    <div class="legal-point">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
            <span class="badge badge-blue">Legal</span>
            {f'<span class="disputed-label">Disputed</span>' if is_disputed else ''}
        </div>
        <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{point}</p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem;">
            {"".join([f'<span class="badge badge-blue">{reg}</span>' for reg in regulations])}
            <span style="font-size: 0.75rem; color: #6b7280;">¶{paragraphs}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Helper function to render a factual point
def render_factual_point(point, date, is_disputed, source, paragraphs):
    st.markdown(f"""
    <div class="factual-point">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
            <span class="badge badge-green">Factual</span>
            {f'<span class="disputed-label">Disputed by {source}</span>' if is_disputed else ''}
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
            <span style="font-size: 0.75rem; color: #6b7280;">📅 {date}</span>
        </div>
        <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{point}</p>
        <span style="font-size: 0.75rem; color: #6b7280; display: block; margin-top: 0.5rem;">¶{paragraphs}</span>
    </div>
    """, unsafe_allow_html=True)

# Helper function to render evidence
def render_evidence(id, title, summary, citations):
    st.markdown(f"""
    <div class="points-card">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <p style="font-size: 0.875rem; font-weight: 500; margin: 0;">{id}: {title}</p>
                <p style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{summary}</p>
                <div style="margin-top: 0.5rem;">
                    <span style="font-size: 0.75rem; color: #6b7280;">Cited in: </span>
                    {"".join([f'<span class="badge badge-gray">¶{cite}</span>' for cite in citations])}
                </div>
            </div>
            <button class="stButton">🔗</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Helper function to render case law
def render_case_law(case_number, title, relevance, paragraphs, cited_paragraphs):
    st.markdown(f"""
    <div class="points-card">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <p style="font-size: 0.875rem; font-weight: 500; margin: 0;">{case_number}</p>
                    <span style="font-size: 0.75rem; color: #6b7280;">¶{paragraphs}</span>
                </div>
                <p style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{title}</p>
                <p style="font-size: 0.875rem; color: #4b5563; margin-top: 0.5rem;">{relevance}</p>
                {f'''
                <div style="margin-top: 0.5rem;">
                    <span style="font-size: 0.75rem; color: #6b7280;">Key Paragraphs: </span>
                    {"".join([f'<span class="badge badge-gray">¶{para}</span>' for para in cited_paragraphs])}
                </div>
                ''' if cited_paragraphs else ''}
            </div>
            <button class="stButton">🔗</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Function to render an argument section
def render_argument_section(arg_data, side, level=0):
    arg_id = arg_data["id"]
    
    # Check if this argument is expanded
    is_expanded = st.session_state.expanded_states.get(arg_id, False)
    
    # Create a unique key for the expander
    key = f"{side}-{arg_id}"
    
    # Determine styles based on side
    header_class = "claimant-header" if side == "claimant" else "respondent-header"
    text_color = "text-blue-600" if side == "claimant" else "text-red-600"
    
    # Render the argument header
    expander = st.expander(
        f"{arg_id}. {arg_data['title']} (¶{arg_data['paragraphs']})",
        expanded=is_expanded
    )
    
    # Update session state when expander is clicked
    if expander.expanded != is_expanded:
        st.session_state.expanded_states[arg_id] = expander.expanded
    
    # Render the argument content if expanded
    with expander:
        # Overview points
        if "overview" in arg_data and arg_data["overview"] and "points" in arg_data["overview"]:
            render_overview_points(
                arg_data["overview"]["points"],
                arg_data["overview"]["paragraphs"]
            )
        
        # Legal points
        if "legal_points" in arg_data and arg_data["legal_points"]:
            st.markdown("##### Legal Points", unsafe_allow_html=True)
            for point in arg_data["legal_points"]:
                render_legal_point(
                    point["point"],
                    point.get("is_disputed", False),
                    point.get("regulations", []),
                    point.get("paragraphs", "")
                )
        
        # Factual points
        if "factual_points" in arg_data and arg_data["factual_points"]:
            st.markdown("##### Factual Points", unsafe_allow_html=True)
            for point in arg_data["factual_points"]:
                render_factual_point(
                    point["point"],
                    point.get("date", ""),
                    point.get("is_disputed", False),
                    point.get("source", ""),
                    point.get("paragraphs", "")
                )
        
        # Evidence
        if "evidence" in arg_data and arg_data["evidence"]:
            st.markdown("##### Evidence", unsafe_allow_html=True)
            for item in arg_data["evidence"]:
                render_evidence(
                    item["id"],
                    item["title"],
                    item["summary"],
                    item.get("citations", [])
                )
        
        # Case Law
        if "case_law" in arg_data and arg_data["case_law"]:
            st.markdown("##### Case Law", unsafe_allow_html=True)
            for item in arg_data["case_law"]:
                render_case_law(
                    item["case_number"],
                    item["title"],
                    item["relevance"],
                    item.get("paragraphs", ""),
                    item.get("cited_paragraphs", [])
                )
        
        # Render child arguments if they exist
        if "children" in arg_data and arg_data["children"]:
            for child_id, child_data in arg_data["children"].items():
                render_argument_section(child_data, side, level + 1)

# Function to render a two-column argument display
def render_argument_pair(claimant_arg, respondent_arg):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"<h3 style='color: #3b82f6;'>Claimant's Arguments</h3>", unsafe_allow_html=True)
        render_argument_section(claimant_arg, "claimant")
    
    with col2:
        st.markdown(f"<h3 style='color: #ef4444;'>Respondent's Arguments</h3>", unsafe_allow_html=True)
        render_argument_section(respondent_arg, "respondent")

# Function to render topic view with arguments grouped by topic
def render_topic_view():
    for topic in topic_sections:
        st.markdown(f"<h2>{topic['title']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6b7280; margin-bottom: 1rem;'>{topic['description']}</p>", unsafe_allow_html=True)
        
        # For each argument ID in this topic, render the pair
        for arg_id in topic["argument_ids"]:
            if arg_id in arguments_data["claimant"] and arg_id in arguments_data["respondent"]:
                render_argument_pair(
                    arguments_data["claimant"][arg_id],
                    arguments_data["respondent"][arg_id]
                )

# Function to render the default view with all arguments
def render_default_view():
    # For each top-level argument, render the pair
    for arg_id in arguments_data["claimant"]:
        if arg_id in arguments_data["respondent"]:
            render_argument_pair(
                arguments_data["claimant"][arg_id],
                arguments_data["respondent"][arg_id]
            )

# Summary of Arguments Tab
with tab1:
    # View mode toggle
    cols = st.columns([3, 1])
    with cols[1]:
        st.markdown("""
        <div class="toggle-button-group">
            <div class="toggle-button default-view">Standard View</div>
            <div class="toggle-button topic-view">Topic View</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Create buttons for toggling view mode
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Standard View"):
                st.session_state.view_mode = "default"
                st.experimental_rerun()
        with col2:
            if st.button("Topic View"):
                st.session_state.view_mode = "topic"
                st.experimental_rerun()
    
    # Render the appropriate view based on view mode
    if st.session_state.view_mode == "default":
        render_default_view()
    else:
        render_topic_view()

# Timeline Tab
with tab2:
    # Action buttons
    cols = st.columns([3, 1])
    with cols[1]:
        col1, col2 = st.columns(2)
        with col1:
            st.button("Copy", key="copy_timeline")
        with col2:
            st.button("Export Data", key="export_timeline")
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("Search events...", key="timeline_search")
    with col2:
        disputed_only = st.checkbox("Disputed events only", key="disputed_only")
    
    # Filter data based on search and filter
    filtered_timeline = timeline_data
    if search:
        filtered_timeline = filtered_timeline[
            filtered_timeline["appellant_version"].str.contains(search, case=False, na=False) |
            filtered_timeline["respondent_version"].str.contains(search, case=False, na=False)
        ]
    if disputed_only:
        filtered_timeline = filtered_timeline[filtered_timeline["status"] == "Disputed"]
    
    # Display timeline data
    st.markdown("""
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
    """, unsafe_allow_html=True)
    
    for _, row in filtered_timeline.iterrows():
        status_color = "text-red-600" if row["status"] == "Disputed" else "text-green-600"
        row_class = "disputed-row" if row["status"] == "Disputed" else ""
        
        st.markdown(f"""
        <tr class="{row_class}">
            <td>{row["date"]}</td>
            <td>{row["appellant_version"]}</td>
            <td>{row["respondent_version"]}</td>
            <td class="{status_color}">{row["status"]}</td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("</tbody></table>", unsafe_allow_html=True)

# Exhibits Tab
with tab3:
    # Action buttons
    cols = st.columns([3, 1])
    with cols[1]:
        col1, col2 = st.columns(2)
        with col1:
            st.button("Copy", key="copy_exhibits")
        with col2:
            st.button("Export Data", key="export_exhibits")
    
    # Search and filters
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        search_exhibits = st.text_input("Search exhibits...", key="exhibits_search")
    with col2:
        party_filter = st.selectbox(
            "Party",
            ["All Parties", "Appellant", "Respondent"],
            key="party_filter"
        )
    with col3:
        type_filter = st.selectbox(
            "Type",
            ["All Types"] + sorted(exhibits_data["type"].unique().tolist()),
            key="type_filter"
        )
    
    # Filter data based on search and filters
    filtered_exhibits = exhibits_data
    if search_exhibits:
        filtered_exhibits = filtered_exhibits[
            filtered_exhibits["title"].str.contains(search_exhibits, case=False) |
            filtered_exhibits["summary"].str.contains(search_exhibits, case=False) |
            filtered_exhibits["id"].str.contains(search_exhibits, case=False)
        ]
    if party_filter != "All Parties":
        filtered_exhibits = filtered_exhibits[filtered_exhibits["party"] == party_filter]
    if type_filter != "All Types":
        filtered_exhibits = filtered_exhibits[filtered_exhibits["type"] == type_filter]
    
    # Display exhibits data
    st.markdown("""
    <table class="styled-table">
        <thead>
            <tr>
                <th>EXHIBIT ID</th>
                <th>PARTY</th>
                <th>TITLE</th>
                <th>TYPE</th>
                <th>SUMMARY</th>
                <th style="text-align: right;">ACTIONS</th>
            </tr>
        </thead>
        <tbody>
    """, unsafe_allow_html=True)
    
    for _, row in filtered_exhibits.iterrows():
        party_class = "badge-blue" if row["party"] == "Appellant" else "badge-red"
        
        st.markdown(f"""
        <tr>
            <td>{row["id"]}</td>
            <td><span class="badge {party_class}">{row["party"]}</span></td>
            <td>{row["title"]}</td>
            <td><span class="badge badge-gray">{row["type"]}</span></td>
            <td>{row["summary"]}</td>
            <td style="text-align: right;"><a href="#" class="text-blue-600">View</a></td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("</tbody></table>", unsafe_allow_html=True)

# Close the card container
st.markdown('</div>', unsafe_allow_html=True)

# Add JavaScript for interactions
components.html(
    """
    <script>
        // Wait for the DOM to be fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Toggle buttons for view mode
            const defaultViewBtn = document.querySelector('.default-view');
            const topicViewBtn = document.querySelector('.topic-view');
            
            if (defaultViewBtn && topicViewBtn) {
                defaultViewBtn.addEventListener('click', function() {
                    // Handle view toggle
                    defaultViewBtn.classList.add('active');
                    topicViewBtn.classList.remove('active');
                });
                
                topicViewBtn.addEventListener('click', function() {
                    // Handle view toggle
                    topicViewBtn.classList.add('active');
                    defaultViewBtn.classList.remove('active');
                });
            }
        });
    </script>
    """,
    height=0,
)
