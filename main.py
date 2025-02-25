import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Add custom CSS for styling
st.markdown("""
<style>
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        margin-bottom: 16px;
    }
    
    /* Claimant and Respondent specific colors */
    .claimant-color { color: #3182CE; }
    .respondent-color { color: #E53E3E; }
    .claimant-bg { background-color: #EBF8FF; }
    .respondent-bg { background-color: #FFF5F5; }
    .claimant-border { border: 1px solid #BEE3F8; }
    .respondent-border { border: 1px solid #FEB2B2; }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 4px;
    }
    .legal-badge {
        background-color: #EBF8FF;
        color: #2C5282;
    }
    .factual-badge {
        background-color: #F0FFF4;
        color: #276749;
    }
    .disputed-badge {
        background-color: #FED7D7;
        color: #C53030;
    }
    
    /* Timeline table */
    .timeline-table th {
        background-color: #F7FAFC;
        padding: 8px 12px;
        text-align: left;
        font-weight: 500;
    }
    .timeline-table td {
        padding: 8px 12px;
        border-top: 1px solid #E2E8F0;
    }
    .timeline-table tr:nth-child(even) {
        background-color: #F7FAFC;
    }
    .timeline-table .disputed {
        background-color: #FFF5F5;
    }
    
    /* Exhibits table */
    .stDataFrame {
        font-size: 14px;
    }
    
    /* Custom header styling */
    .header-container {
        display: flex; 
        justify-content: space-between; 
        align-items: center;
        margin-bottom: 1rem;
    }
    
    /* No margin on generated paragraphs */
    .argument-container p {
        margin-bottom: 0 !important;
    }
    
    /* Override Streamlit defaults */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        padding-top: 10px;
    }
    .stTabs [data-baseweb="tab-border"] {
        display: none;
    }
    .stTabs [aria-selected="true"] {
        color: #3182CE;
        border-bottom: 2px solid #3182CE;
    }
    
    /* Point styling */
    .point-container {
        background-color: #F7FAFC;
        border-radius: 6px;
        padding: 12px;
        margin: 8px 0;
    }
    
    /* Custom expander styling */
    .custom-expander {
        border: 1px solid #E2E8F0;
        border-radius: 6px;
        margin-bottom: 8px;
    }
    .custom-expander-header {
        padding: 8px 12px;
        background-color: #F7FAFC;
        border-radius: 6px 6px 0 0;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .custom-expander-content {
        padding: 12px;
        border-top: 1px solid #E2E8F0;
        border-radius: 0 0 6px 6px;
    }
</style>
""", unsafe_allow_html=True)

# Define data structures for the app
def get_argument_data():
    # Claimant arguments
    claimant_args = {
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration History",
                            "paragraphs": "25-30",
                            "factual_points": [
                                {
                                    "point": "Initial registration in 1950",
                                    "date": "1950",
                                    "is_disputed": False,
                                    "paragraphs": "25-26"
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "is_disputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30"
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-2",
                                    "title": "Registration Records",
                                    "summary": "Official documentation of registration history",
                                    "citations": ["25", "26", "28"]
                                }
                            ],
                            "children": {}
                        }
                    }
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
    }
    
    # Respondent arguments
    respondent_args = {
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration Gap Evidence",
                            "paragraphs": "226-230",
                            "factual_points": [
                                {
                                    "point": "Registration formally terminated on April 30, 1975",
                                    "date": "April 30, 1975",
                                    "is_disputed": False,
                                    "paragraphs": "226-227"
                                },
                                {
                                    "point": "New entity registered on September 15, 1976",
                                    "date": "September 15, 1976",
                                    "is_disputed": False,
                                    "paragraphs": "228-229"
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-2",
                                    "title": "Termination Certificate",
                                    "summary": "Official documentation of registration termination",
                                    "citations": ["226", "227"]
                                }
                            ],
                            "children": {}
                        }
                    }
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
    
    # Topic groupings
    topics = [
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
    
    return claimant_args, respondent_args, topics

def get_timeline_data():
    data = [
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
    ]
    return pd.DataFrame(data)

def get_exhibits_data():
    data = [
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
    ]
    return pd.DataFrame(data)

# Initialize session state for expanded arguments
def init_session_state():
    if "expanded" not in st.session_state:
        st.session_state.expanded = {}
    if "view_mode" not in st.session_state:
        st.session_state.view_mode = "default"
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = 0

# Function to toggle expanded state
def toggle_argument(arg_id, side):
    key = f"{side}_{arg_id}"
    if key in st.session_state.expanded:
        st.session_state.expanded[key] = not st.session_state.expanded[key]
    else:
        st.session_state.expanded[key] = True

# Function to check if argument is expanded
def is_expanded(arg_id, side):
    key = f"{side}_{arg_id}"
    if key in st.session_state.expanded:
        return st.session_state.expanded[key]
    return False

# Function to render a legal point
def render_legal_point(point):
    st.markdown(f"""
    <div class="point-container" style="background-color: #EBF8FF; border: 1px solid #BEE3F8;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
            <span class="badge legal-badge">Legal</span>
            {f'<span class="badge disputed-badge">Disputed</span>' if point.get('is_disputed', False) else ''}
        </div>
        <p style="font-size: 0.9rem;">{point.get('point', '')}</p>
        <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px;">
            {''.join([f'<span class="badge legal-badge">{reg}</span>' for reg in point.get('regulations', [])])}
            <span style="font-size: 0.8rem; color: #4A5568;">¶{point.get('paragraphs', '')}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Function to render a factual point
def render_factual_point(point):
    st.markdown(f"""
    <div class="point-container" style="background-color: #F0FFF4; border: 1px solid #C6F6D5;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
            <span class="badge factual-badge">Factual</span>
            {f'<span class="badge disputed-badge">Disputed by {point.get("source", "")}</span>' if point.get("is_disputed", False) else ''}
        </div>
        <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 6px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
            </svg>
            <span style="font-size: 0.8rem; color: #4A5568;">{point.get('date', '')}</span>
        </div>
        <p style="font-size: 0.9rem;">{point.get('point', '')}</p>
        <span style="font-size: 0.8rem; color: #4A5568; display: inline-block; margin-top: 8px;">¶{point.get('paragraphs', '')}</span>
    </div>
    """, unsafe_allow_html=True)

# Function to render evidence
def render_evidence(evidence):
    st.markdown(f"""
    <div class="point-container">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <p style="font-size: 0.9rem; font-weight: 500; margin-bottom: 4px;">{evidence.get('id', '')}: {evidence.get('title', '')}</p>
                <p style="font-size: 0.8rem; color: #4A5568; margin-bottom: 8px;">{evidence.get('summary', '')}</p>
                <div>
                    <span style="font-size: 0.8rem; color: #4A5568;">Cited in: </span>
                    {''.join([f'<span style="background-color: #E2E8F0; color: #4A5568; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; margin-left: 4px;">¶{cite}</span>' for cite in evidence.get('citations', [])])}
                </div>
            </div>
            <button style="background: none; border: none; color: #3182CE; cursor: pointer; height: 24px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                </svg>
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Function to render case law
def render_case_law(case):
    st.markdown(f"""
    <div class="point-container">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                    <p style="font-size: 0.9rem; font-weight: 500;">{case.get('case_number', '')}</p>
                    <span style="font-size: 0.8rem; color: #4A5568;">¶{case.get('paragraphs', '')}</span>
                </div>
                <p style="font-size: 0.8rem; color: #4A5568; margin-bottom: 8px;">{case.get('title', '')}</p>
                <p style="font-size: 0.9rem; margin-bottom: 8px;">{case.get('relevance', '')}</p>
                <div>
                    <span style="font-size: 0.8rem; color: #4A5568;">Key Paragraphs: </span>
                    {''.join([f'<span style="background-color: #E2E8F0; color: #4A5568; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; margin-left: 4px;">¶{para}</span>' for para in case.get('cited_paragraphs', [])])}
                </div>
            </div>
            <button style="background: none; border: none; color: #3182CE; cursor: pointer; height: 24px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                </svg>
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Function to render an argument
def render_argument(arg, side, level=0):
    # Check if this argument has children
    has_children = arg.get("children", {})
    child_count = len(has_children)
    
    # Create a unique key for the expander
    arg_key = f"{side}_{arg['id']}"
    
    # Style based on side
    bg_color = "#EBF8FF" if side == "claimant" else "#FFF5F5"
    text_color = "#3182CE" if side == "claimant" else "#E53E3E"
    
    # Expander for the argument
    expanded = st.checkbox(
        f"{arg['id']}. {arg['title']}",
        key=arg_key,
        value=is_expanded(arg['id'], side),
        help=arg.get('paragraphs', '')
    )
    
    # Store expanded state
    st.session_state.expanded[arg_key] = expanded
    
    if expanded:
        with st.container():
            # Overview points
            if "overview" in arg and "points" in arg["overview"]:
                st.markdown("#### Key Points")
                with st.container():
                    for point in arg["overview"]["points"]:
                        st.markdown(f"• {point}")
                st.markdown(f"Paragraphs: {arg['overview']['paragraphs']}")
                st.markdown("---")
            
            # Legal points
            if "legal_points" in arg and arg["legal_points"]:
                st.markdown("#### Legal Points")
                for point in arg["legal_points"]:
                    render_legal_point(point)
                st.markdown("---")
            
            # Factual points
            if "factual_points" in arg and arg["factual_points"]:
                st.markdown("#### Factual Points")
                for point in arg["factual_points"]:
                    render_factual_point(point)
                st.markdown("---")
            
            # Evidence
            if "evidence" in arg and arg["evidence"]:
                st.markdown("#### Evidence")
                for item in arg["evidence"]:
                    render_evidence(item)
                st.markdown("---")
            
            # Case law
            if "case_law" in arg and arg["case_law"]:
                st.markdown("#### Case Law")
                for case in arg["case_law"]:
                    render_case_law(case)
                st.markdown("---")
            
            # Render children
            if child_count > 0:
                for child_id, child in arg.get("children", {}).items():
                    st.markdown(f"### Sub-argument {child_id}")
                    render_argument(child, side, level + 1)

# Function to render argument pair side by side
def render_argument_pair(claimant_arg, respondent_arg):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"<h3 style='color: #3182CE;'>Claimant</h3>", unsafe_allow_html=True)
        render_argument(claimant_arg, "claimant")
    
    with col2:
        st.markdown(f"<h3 style='color: #E53E3E;'>Respondent</h3>", unsafe_allow_html=True)
        render_argument(respondent_arg, "respondent")

# Function to render by topic
def render_topic_view(topics, claimant_args, respondent_args):
    for topic in topics:
        st.markdown(f"## {topic['title']}")
        st.markdown(f"*{topic['description']}*")
        st.markdown("---")
        
        for arg_id in topic.get("argument_ids", []):
            if arg_id in claimant_args and arg_id in respondent_args:
                render_argument_pair(claimant_args[arg_id], respondent_args[arg_id])

# Main app function
def main():
    # Initialize app state
    init_session_state()
    
    # Set app title
    st.title("Legal Arguments Analysis")
    
    # Create tabs
    tabs = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])
    
    # Get the data
    claimant_args, respondent_args, topics = get_argument_data()
    
    # Arguments tab
    with tabs[0]:
        # View mode selection
        view_mode = st.radio(
            "View Mode",
            ["Standard View", "Topic View"],
            horizontal=True,
            index=0 if st.session_state.view_mode == "default" else 1,
            label_visibility="collapsed",
        )
        st.session_state.view_mode = "default" if view_mode == "Standard View" else "topic"
        
        # Display arguments based on view mode
        if st.session_state.view_mode == "default":
            # Display arguments in standard view
            for arg_id in claimant_args:
                if arg_id in respondent_args:
                    render_argument_pair(claimant_args[arg_id], respondent_args[arg_id])
        else:
            # Display arguments in topic view
            render_topic_view(topics, claimant_args, respondent_args)
    
    # Timeline tab
    with tabs[1]:
        # Get timeline data
        timeline_df = get_timeline_data()
        
        # Search and filter
        col1, col2 = st.columns([3, 1])
        with col1:
            search = st.text_input("Search events...", key="timeline_search")
        with col2:
            disputed_only = st.checkbox("Disputed events only", key="disputed_filter")
        
        # Apply filters
        filtered_df = timeline_df
        if search:
            mask = (
                filtered_df["appellant_version"].str.contains(search, case=False, na=False) |
                filtered_df["respondent_version"].str.contains(search, case=False, na=False)
            )
            filtered_df = filtered_df[mask]
        
        if disputed_only:
            filtered_df = filtered_df[filtered_df["status"] == "Disputed"]
        
        # Style the timeline table
        def highlight_disputed(row):
            if row["status"] == "Disputed":
                return ["background-color: #FFF5F5"] * len(row)
            return [""] * len(row)
        
        # Display timeline
        st.dataframe(
            filtered_df.style.apply(highlight_disputed, axis=1),
            use_container_width=True,
            hide_index=True,
        )
    
    # Exhibits tab
    with tabs[2]:
        # Get exhibits data
        exhibits_df = get_exhibits_data()
        
        # Search and filters
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            search = st.text_input("Search exhibits...", key="exhibits_search")
        with col2:
            party_filter = st.selectbox(
                "Party",
                ["All Parties", "Appellant", "Respondent"],
                key="party_filter"
            )
        with col3:
            type_options = ["All Types"] + list(exhibits_df["type"].unique())
            type_filter = st.selectbox("Type", type_options, key="type_filter")
        
        # Apply filters
        filtered_df = exhibits_df
        if search:
            mask = (
                filtered_df["id"].str.contains(search, case=False, na=False) |
                filtered_df["title"].str.contains(search, case=False, na=False) |
                filtered_df["summary"].str.contains(search, case=False, na=False)
            )
            filtered_df = filtered_df[mask]
        
        if party_filter != "All Parties":
            filtered_df = filtered_df[filtered_df["party"] == party_filter]
        
        if type_filter != "All Types":
            filtered_df = filtered_df[filtered_df["type"] == type_filter]
        
        # Style the exhibits table
        def color_party(val):
            if val == "Appellant":
                return "background-color: #EBF8FF; color: #2B6CB0;"
            elif val == "Respondent":
                return "background-color: #FFF5F5; color: #C53030;"
            return ""
        
        # Add a view column
        filtered_df["actions"] = "View"
        
        # Display exhibits
        st.dataframe(
            filtered_df.style.applymap(color_party, subset=["party"]),
            use_container_width=True,
            hide_index=True,
            column_config={
                "actions": st.column_config.LinkColumn("Actions")
            }
        )

# Run the app
if __name__ == "__main__":
    main()
