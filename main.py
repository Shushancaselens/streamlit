import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import json

# Set page config
st.set_page_config(
    page_title="Legal Arguments Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS for styling
st.markdown("""
<style>
    /* Card styling */
    .stApp {
        background-color: #f9fafb;
    }
    .card {
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .card-header {
        padding-bottom: 1rem;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
    }
    
    /* Tab styling */
    .tab-active {
        border-bottom: 2px solid #3b82f6;
        color: #3b82f6;
        font-weight: 500;
        padding-bottom: 0.5rem;
    }
    .tab-inactive {
        color: #6b7280;
        padding-bottom: 0.5rem;
    }
    .tab-container {
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
    }
    
    /* Argument styling */
    .argument-claimant {
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 0.375rem;
        margin-bottom: 1rem;
    }
    .argument-respondent {
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 0.375rem;
        margin-bottom: 1rem;
    }
    .argument-header-claimant {
        background-color: rgba(239, 246, 255, 0.7);
        padding: 0.75rem;
        border-radius: 0.375rem 0.375rem 0 0;
        cursor: pointer;
    }
    .argument-header-respondent {
        background-color: rgba(254, 242, 242, 0.7);
        padding: 0.75rem;
        border-radius: 0.375rem 0.375rem 0 0;
        cursor: pointer;
    }
    .argument-content {
        padding: 1rem;
    }
    
    /* Badge styling */
    .badge {
        font-size: 0.75rem;
        padding: 0.125rem 0.5rem;
        border-radius: 9999px;
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
    
    /* Points styling */
    .points-container {
        background-color: #f9fafb;
        border-radius: 0.375rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .point-item {
        display: flex;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    .point-bullet {
        width: 6px;
        height: 6px;
        background-color: #3b82f6;
        border-radius: 50%;
        margin-right: 0.5rem;
    }
    
    /* Toggle button */
    .view-toggle {
        display: inline-flex;
        background-color: #f3f4f6;
        border-radius: 0.375rem;
        padding: 0.25rem;
    }
    .view-button {
        padding: 0.375rem 0.75rem;
        font-size: 0.875rem;
        border-radius: 0.25rem;
    }
    .view-button-active {
        background-color: white;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    
    /* Evidence reference styling */
    .evidence-container {
        background-color: #f9fafb;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    /* Connector line styling */
    .connector-vertical {
        position: relative;
    }
    .connector-vertical:before {
        content: "";
        position: absolute;
        left: 10px;
        top: 0;
        height: 100%;
        width: 1px;
        background-color: #d1d5db;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for expanded arguments
if 'expanded_args' not in st.session_state:
    st.session_state.expanded_args = {}

# Initialize session state for active tab
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "arguments"

# Initialize session state for view mode
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "default"

# Data for arguments
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
            "legalPoints": [
                {
                    "point": "CAS jurisprudence establishes criteria for sporting succession",
                    "isDisputed": False,
                    "regulations": ["CAS 2016/A/4576"],
                    "paragraphs": "15-17"
                }
            ],
            "factualPoints": [
                {
                    "point": "Continuous operation under same name since 1950",
                    "date": "1950-present",
                    "isDisputed": False,
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
            "caseLaw": [
                {
                    "caseNumber": "CAS 2016/A/4576",
                    "title": "Criteria for sporting succession",
                    "relevance": "Establishes key factors for succession",
                    "paragraphs": "45-48",
                    "citedParagraphs": ["45", "46", "47"]
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
                    "legalPoints": [
                        {
                            "point": "Name registration complies with regulations",
                            "isDisputed": False,
                            "regulations": ["Name Registration Act"],
                            "paragraphs": "22-24"
                        },
                        {
                            "point": "Trademark protection since 1960",
                            "isDisputed": False,
                            "regulations": ["Trademark Law"],
                            "paragraphs": "25-27"
                        }
                    ],
                    "children": {}
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
                    "legalPoints": [
                        {
                            "point": "Color trademark registration valid since 1960",
                            "isDisputed": False,
                            "regulations": ["Trademark Act"],
                            "paragraphs": "48-50"
                        }
                    ],
                    "factualPoints": [
                        {
                            "point": "Consistent use of blue and white since founding",
                            "date": "1950-present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "51-52"
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-4",
                            "title": "Historical Photographs",
                            "summary": "Visual evidence of consistent color usage",
                            "citations": ["53", "54", "55"]
                        }
                    ],
                    "children": {}
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
            "legalPoints": [
                {
                    "point": "WADA Code Article 5 establishes procedural requirements",
                    "isDisputed": False,
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
            "legalPoints": [
                {
                    "point": "CAS jurisprudence requires operational continuity not merely identification",
                    "isDisputed": False,
                    "regulations": ["CAS 2017/A/5465"],
                    "paragraphs": "203-205"
                }
            ],
            "factualPoints": [
                {
                    "point": "Operations ceased between 1975-1976",
                    "date": "1975-1976",
                    "isDisputed": True,
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
            "caseLaw": [
                {
                    "caseNumber": "CAS 2017/A/5465",
                    "title": "Operational continuity requirement",
                    "relevance": "Establishes primacy of operational continuity",
                    "paragraphs": "211-213",
                    "citedParagraphs": ["212"]
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
                    "legalPoints": [
                        {
                            "point": "Registration lapse voided legal continuity",
                            "isDisputed": True,
                            "regulations": ["Registration Act"],
                            "paragraphs": "223-225"
                        }
                    ],
                    "children": {}
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
                    "legalPoints": [
                        {
                            "point": "Color trademark lapsed during 1975-1976",
                            "isDisputed": False,
                            "regulations": ["Trademark Act"],
                            "paragraphs": "243-244"
                        }
                    ],
                    "factualPoints": [
                        {
                            "point": "Significant color scheme change in 1976",
                            "date": "1976",
                            "isDisputed": True,
                            "source": "Claimant",
                            "paragraphs": "245-246"
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-4",
                            "title": "Historical Photographs Comparison",
                            "summary": "Visual evidence of color scheme changes",
                            "citations": ["245", "246", "247"]
                        }
                    ],
                    "children": {}
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
            "legalPoints": [
                {
                    "point": "Minor procedural deviations do not invalidate results",
                    "isDisputed": False,
                    "regulations": ["CAS 2019/A/6148"],
                    "paragraphs": "253-255"
                }
            ],
            "children": {}
        }
    }
}

# Topics for hierarchical view
topics_data = [
    {
        "id": "topic-1",
        "title": "Sporting Succession and Identity",
        "description": "Questions of club identity, continuity, and succession rights",
        "argumentIds": ["1"]
    },
    {
        "id": "topic-2",
        "title": "Doping Violation and Chain of Custody",
        "description": "Issues related to doping test procedures and evidence handling",
        "argumentIds": ["2"]
    }
]

# Data for timeline
timeline_data = [
    {"date": "2023-01-15", "appellantVersion": "Contract signed with Club", "respondentVersion": "—", "status": "Undisputed"},
    {"date": "2023-03-20", "appellantVersion": "Player received notification of exclusion from team", "respondentVersion": "—", "status": "Undisputed"},
    {"date": "2023-03-22", "appellantVersion": "Player requested explanation", "respondentVersion": "—", "status": "Undisputed"},
    {"date": "2023-04-01", "appellantVersion": "Player sent termination letter", "respondentVersion": "—", "status": "Undisputed"},
    {"date": "2023-04-05", "appellantVersion": "—", "respondentVersion": "Club rejected termination as invalid", "status": "Undisputed"},
    {"date": "2023-04-10", "appellantVersion": "Player was denied access to training facilities", "respondentVersion": "—", "status": "Disputed"},
    {"date": "2023-04-15", "appellantVersion": "—", "respondentVersion": "Club issued warning letter", "status": "Undisputed"},
    {"date": "2023-05-01", "appellantVersion": "Player filed claim with FIFA", "respondentVersion": "—", "status": "Undisputed"}
]

# Data for exhibits
exhibits_data = [
    {"id": "C-1", "party": "Appellant", "title": "Employment Contract", "type": "contract", "summary": "Employment contract dated 15 January 2023 between Player and Club"},
    {"id": "C-2", "party": "Appellant", "title": "Termination Letter", "type": "letter", "summary": "Player's termination letter sent on 1 April 2023"},
    {"id": "C-3", "party": "Appellant", "title": "Email Correspondence", "type": "communication", "summary": "Email exchanges between Player and Club from 22-30 March 2023"},
    {"id": "C-4", "party": "Appellant", "title": "Witness Statement", "type": "statement", "summary": "Statement from team captain confirming Player's exclusion"},
    {"id": "R-1", "party": "Respondent", "title": "Club Regulations", "type": "regulations", "summary": "Internal regulations of the Club dated January 2022"},
    {"id": "R-2", "party": "Respondent", "title": "Warning Letter", "type": "letter", "summary": "Warning letter issued to Player on 15 April 2023"},
    {"id": "R-3", "party": "Respondent", "title": "Training Schedule", "type": "schedule", "summary": "Team training schedule for March-April 2023"}
]

# Custom components
def render_point_bullet():
    return """
    <div style="display: inline-block; width: 6px; height: 6px; background-color: #3b82f6; border-radius: 50%; margin-right: 8px;"></div>
    """

def render_chevron(is_expanded):
    if is_expanded:
        # Down chevron
        return """
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="m6 9 6 6 6-6"/>
        </svg>
        """
    else:
        # Right chevron
        return """
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="m9 18 6-6-6-6"/>
        </svg>
        """

def render_calendar_icon():
    return """
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect width="18" height="18" x="3" y="4" rx="2" ry="2"/>
        <line x1="16" x2="16" y1="2" y2="6"/>
        <line x1="8" x2="8" y1="2" y2="6"/>
        <line x1="3" x2="21" y1="10" y2="10"/>
    </svg>
    """

def render_link_icon():
    return """
    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
    </svg>
    """

# Helper function to toggle argument expansion state
def toggle_arg_expansion(arg_id):
    if arg_id in st.session_state.expanded_args:
        st.session_state.expanded_args[arg_id] = not st.session_state.expanded_args[arg_id]
    else:
        st.session_state.expanded_args[arg_id] = True

# Render Overview Points
def render_overview_points(overview):
    if not overview or 'points' not in overview:
        return
    
    html = f"""
    <div class="points-container">
        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <h6 style="font-size: 0.875rem; font-weight: 500;">Key Points</h6>
            <span class="badge badge-blue">¶{overview['paragraphs']}</span>
        </div>
        <ul style="list-style-type: none; padding-left: 0; margin-top: 0.5rem;">
    """
    
    for point in overview['points']:
        html += f"""
        <li class="point-item">
            <div class="point-bullet"></div>
            <span style="font-size: 0.875rem; color: #4b5563;">{point}</span>
        </li>
        """
    
    html += """
        </ul>
    </div>
    """
    
    return html

# Render Legal Points
def render_legal_points(legal_points):
    if not legal_points:
        return
    
    html = """
    <div style="margin-bottom: 1.5rem;">
        <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Legal Points</h6>
    """
    
    for point in legal_points:
        html += f"""
        <div style="background-color: #dbeafe; border-radius: 0.375rem; padding: 0.75rem; margin-bottom: 0.5rem;">
            <div style="display: flex; gap: 0.5rem; margin-bottom: 0.25rem;">
                <span class="badge badge-blue">Legal</span>
                {f'<span class="badge badge-red">Disputed</span>' if point.get('isDisputed', False) else ''}
            </div>
            <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{point['point']}</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem;">
        """
        
        for reg in point.get('regulations', []):
            html += f'<span class="badge badge-blue">{reg}</span>'
        
        html += f"""
                <span style="font-size: 0.75rem; color: #6b7280;">¶{point.get('paragraphs', '')}</span>
            </div>
        </div>
        """
    
    html += "</div>"
    return html

# Render Factual Points
def render_factual_points(factual_points):
    if not factual_points:
        return
    
    html = """
    <div style="margin-bottom: 1.5rem;">
        <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Factual Points</h6>
    """
    
    for point in factual_points:
        html += f"""
        <div style="background-color: #d1fae5; border-radius: 0.375rem; padding: 0.75rem; margin-bottom: 0.5rem;">
            <div style="display: flex; gap: 0.5rem; margin-bottom: 0.25rem;">
                <span class="badge badge-green">Factual</span>
                {f'<span class="badge badge-red">Disputed by {point.get("source", "")}</span>' if point.get('isDisputed', False) else ''}
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
                {render_calendar_icon()}
                <span style="font-size: 0.75rem; color: #6b7280;">{point.get('date', '')}</span>
            </div>
            <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{point['point']}</p>
            <span style="font-size: 0.75rem; color: #6b7280; display: block; margin-top: 0.5rem;">¶{point.get('paragraphs', '')}</span>
        </div>
        """
    
    html += "</div>"
    return html

# Render Evidence
def render_evidence(evidence_items):
    if not evidence_items:
        return
    
    html = """
    <div style="margin-bottom: 1.5rem;">
        <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Evidence</h6>
    """
    
    for item in evidence_items:
        html += f"""
        <div class="evidence-container">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <p style="font-size: 0.875rem; font-weight: 500; margin: 0;">{item['id']}: {item['title']}</p>
                    <p style="font-size: 0.75rem; color: #6b7280; margin: 0.25rem 0;">{item['summary']}</p>
                    <div style="margin-top: 0.5rem;">
                        <span style="font-size: 0.75rem; color: #6b7280;">Cited in: </span>
        """
        
        for cite in item.get('citations', []):
            html += f'<span style="font-size: 0.75rem; background-color: #e5e7eb; border-radius: 0.25rem; padding: 0.25rem 0.5rem; margin-left: 0.25rem;">¶{cite}</span>'
        
        html += f"""
                    </div>
                </div>
                <button style="background: none; border: none; color: #4b5563; padding: 0.25rem; height: 1.5rem; cursor: pointer;">
                    {render_link_icon()}
                </button>
            </div>
        </div>
        """
    
    html += "</div>"
    return html

# Render Case Law
def render_case_law(case_law_items):
    if not case_law_items:
        return
    
    html = """
    <div style="margin-bottom: 1.5rem;">
        <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Case Law</h6>
    """
    
    for item in case_law_items:
        html += f"""
        <div class="evidence-container">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <p style="font-size: 0.875rem; font-weight: 500; margin: 0;">{item['caseNumber']}</p>
                        <span style="font-size: 0.75rem; color: #6b7280;">¶{item.get('paragraphs', '')}</span>
                    </div>
                    <p style="font-size: 0.75rem; color: #6b7280; margin: 0.25rem 0;">{item['title']}</p>
                    <p style="font-size: 0.875rem; color: #4b5563; margin: 0.5rem 0;">{item['relevance']}</p>
        """
        
        if 'citedParagraphs' in item and item['citedParagraphs']:
            html += """
                    <div style="margin-top: 0.5rem;">
                        <span style="font-size: 0.75rem; color: #6b7280;">Key Paragraphs: </span>
            """
            
            for para in item['citedParagraphs']:
                html += f'<span style="font-size: 0.75rem; background-color: #e5e7eb; border-radius: 0.25rem; padding: 0.25rem 0.5rem; margin-left: 0.25rem;">¶{para}</span>'
            
            html += """
                    </div>
            """
        
        html += f"""
                </div>
                <button style="background: none; border: none; color: #4b5563; padding: 0.25rem; height: 1.5rem; cursor: pointer;">
                    {render_link_icon()}
                </button>
            </div>
        </div>
        """
    
    html += "</div>"
    return html

# Render Argument Content
def render_argument_content(arg, side):
    html = ""
    
    # Overview Points
    if 'overview' in arg:
        html += render_overview_points(arg['overview']) or ""
    
    # Legal Points
    if 'legalPoints' in arg and arg['legalPoints']:
        html += render_legal_points(arg['legalPoints']) or ""
    
    # Factual Points
    if 'factualPoints' in arg and arg['factualPoints']:
        html += render_factual_points(arg['factualPoints']) or ""
    
    # Evidence
    if 'evidence' in arg and arg['evidence']:
        html += render_evidence(arg['evidence']) or ""
    
    # Case Law
    if 'caseLaw' in arg and arg['caseLaw']:
        html += render_case_law(arg['caseLaw']) or ""
    
    return html

# Render Argument Section
def render_argument_section(arg, side, level=0):
    arg_id = arg['id']
    is_expanded = st.session_state.expanded_args.get(arg_id, False)
    
    # Colors based on side
    if side == "claimant":
        base_color = "blue"
        header_class = "argument-header-claimant"
        container_class = "argument-claimant"
    else:
        base_color = "red"
        header_class = "argument-header-respondent"
        container_class = "argument-respondent"
    
    # Count subarguments
    has_children = 'children' in arg and arg['children']
    child_count = len(arg['children']) if has_children else 0
    
    # Create a key for the button
    button_key = f"{side}-{arg_id}-button"
    
    st.markdown(f"""
    <div class="{container_class}">
        <div class="{header_class}" id="{button_key}">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                {render_chevron(is_expanded)}
                <h5 style="font-size: 0.875rem; font-weight: 500; margin: 0;">
                    {arg_id}. {arg['title']}
                </h5>
                {f'<span class="badge badge-{base_color}">{child_count} subarguments</span>' if child_count > 0 else f'<span style="font-size: 0.75rem; color: #6b7280;">¶{arg.get("paragraphs", "")}</span>'}
            </div>
        </div>
        
        {f'<div class="argument-content" style="display: {"block" if is_expanded else "none"};">{render_argument_content(arg, side)}</div>' if is_expanded else ''}
    </div>
    """, unsafe_allow_html=True)
    
    # JavaScript for handling click
    components.html(f"""
    <script>
        document.getElementById('{button_key}').addEventListener('click', function() {{
            window.parent.postMessage({{
                type: 'streamlit:component',
                action: 'toggleArgExpansion',
                args: '{arg_id}'
            }}, '*');
        }});
    </script>
    """, height=0)
    
    # If expanded and has children, render them
    if is_expanded and has_children:
        for child_id, child_arg in arg['children'].items():
            render_argument_section(child_arg, side, level + 1)

# Create custom component for argument expansion toggle
def handle_click_messages():
    components.html("""
    <script>
        window.addEventListener('message', function(event) {
            const data = event.data;
            if (data.type === 'streamlit:component' && data.action === 'toggleArgExpansion') {
                const argId = data.args;
                
                // Create a button click event on the hidden button with the corresponding key
                const button = document.getElementById('toggle-' + argId);
                if (button) {
                    button.click();
                }
            }
        });
    </script>
    """, height=0)

# Handle Argument Pair
def argument_pair(claimant_arg, respondent_arg, level=0, is_root=True):
    cols = st.columns(2)
    
    with cols[0]:
        render_argument_section(claimant_arg, "claimant", level)
        
        # Create a hidden button for toggle functionality
        if st.button(f"Toggle {claimant_arg['id']}", key=f"toggle-{claimant_arg['id']}", help="Toggle argument expansion", visible=False):
            toggle_arg_expansion(claimant_arg['id'])
            st.experimental_rerun()
    
    with cols[1]:
        render_argument_section(respondent_arg, "respondent", level)
        
        # Create a hidden button for toggle functionality
        if st.button(f"Toggle {respondent_arg['id']}", key=f"toggle-{respondent_arg['id']}", help="Toggle argument expansion", visible=False):
            toggle_arg_expansion(respondent_arg['id'])
            st.experimental_rerun()
    
    # Render child argument pairs if both exist and parent is expanded
    if ('children' in claimant_arg and 'children' in respondent_arg and 
        claimant_arg['children'] and respondent_arg['children'] and
        st.session_state.expanded_args.get(claimant_arg['id'], False)):
        
        # Match child arguments by their IDs
        for child_id in claimant_arg['children']:
            if child_id in respondent_arg['children']:
                argument_pair(
                    claimant_arg['children'][child_id],
                    respondent_arg['children'][child_id],
                    level + 1,
                    False
                )

# Render Arguments View
def render_arguments_view():
    # Add view toggle buttons
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown("""
        <div style="display: flex; justify-content: flex-end;">
            <div class="view-toggle">
                <button class="view-button view-button-active" id="default-view-btn">Standard View</button>
                <button class="view-button" id="hierarchical-view-btn">Topic View</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # JavaScript for handling view toggle
        components.html("""
        <script>
            document.getElementById('default-view-btn').addEventListener('click', function() {
                this.classList.add('view-button-active');
                document.getElementById('hierarchical-view-btn').classList.remove('view-button-active');
                window.parent.postMessage({
                    type: 'streamlit:setViewMode',
                    mode: 'default'
                }, '*');
            });
            
            document.getElementById('hierarchical-view-btn').addEventListener('click', function() {
                this.classList.add('view-button-active');
                document.getElementById('default-view-btn').classList.remove('view-button-active');
                window.parent.postMessage({
                    type: 'streamlit:setViewMode',
                    mode: 'hierarchical'
                }, '*');
            });
        </script>
        """, height=0)
    
    # Check if we should show default or hierarchical view
    if st.session_state.view_mode == "default":
        # Headers for both columns
        cols = st.columns(2)
        with cols[0]:
            st.markdown('<h2 style="font-size: 1.125rem; font-weight: 600; color: #3b82f6;">Claimant\'s Arguments</h2>', unsafe_allow_html=True)
        with cols[1]:
            st.markdown('<h2 style="font-size: 1.125rem; font-weight: 600; color: #ef4444;">Respondent\'s Arguments</h2>', unsafe_allow_html=True)
        
        # Render argument pairs
        for arg_id in arguments_data['claimant']:
            claimant_arg = arguments_data['claimant'][arg_id]
            respondent_arg = arguments_data['respondent'][arg_id]
            argument_pair(claimant_arg, respondent_arg)
    else:
        # Hierarchical view
        for topic in topics_data:
            st.markdown(f'<h2 style="font-size: 1.25rem; font-weight: 600; color: #1f2937; margin-bottom: 0.5rem;">{topic["title"]}</h2>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size: 0.875rem; color: #6b7280; margin-bottom: 1rem;">{topic["description"]}</p>', unsafe_allow_html=True)
            
            # Column headers
            cols = st.columns(2)
            with cols[0]:
                st.markdown('<h3 style="font-size: 1rem; font-weight: 600; color: #3b82f6; margin-bottom: 1rem;">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
            with cols[1]:
                st.markdown('<h3 style="font-size: 1rem; font-weight: 600; color: #ef4444; margin-bottom: 1rem;">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
            
            # Render argument pairs for this topic
            for arg_id in topic['argumentIds']:
                if arg_id in arguments_data['claimant'] and arg_id in arguments_data['respondent']:
                    argument_pair(arguments_data['claimant'][arg_id], arguments_data['respondent'][arg_id])
            
            st.markdown('<hr style="margin: 2rem 0;">', unsafe_allow_html=True)

# Render Timeline View
def render_timeline_view():
    # Action buttons
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown("""
        <div style="display: flex; justify-content: flex-end; gap: 0.5rem;">
            <button class="view-button" style="border: 1px solid #e5e7eb;">
                <span style="display: flex; align-items: center; gap: 0.25rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect width="14" height="14" x="8" y="8" rx="2" ry="2"/>
                        <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>
                    </svg>
                    Copy
                </span>
            </button>
            <button class="view-button" style="border: 1px solid #e5e7eb;">
                <span style="display: flex; align-items: center; gap: 0.25rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="7 10 12 15 17 10"/>
                        <line x1="12" x2="12" y1="15" y2="3"/>
                    </svg>
                    Export Data
                </span>
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search = st.text_input("", placeholder="Search events...", label_visibility="collapsed")
    
    with col2:
        disputed_only = st.checkbox("Disputed events only")
    
    # Filter data
    filtered_timeline = timeline_data
    if search:
        filtered_timeline = [item for item in filtered_timeline if 
                             search.lower() in item['appellantVersion'].lower() or 
                             search.lower() in item['respondentVersion'].lower()]
    
    if disputed_only:
        filtered_timeline = [item for item in filtered_timeline if item['status'] == 'Disputed']
    
    # Create DataFrame for display
    df = pd.DataFrame(filtered_timeline)
    
    # Add styling
    def style_status(val):
        color = '#16a34a' if val == 'Undisputed' else '#dc2626'
        return f'color: {color}'
    
    def style_row(row):
        if row['status'] == 'Disputed':
            return ['background-color: #fee2e2'] * len(row)
        return [''] * len(row)
    
    styled_df = df.style.applymap(style_status, subset=['status']).apply(style_row, axis=1)
    
    # Display the table
    st.dataframe(styled_df, hide_index=True, use_container_width=True)

# Render Exhibits View
def render_exhibits_view():
    # Action buttons
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown("""
        <div style="display: flex; justify-content: flex-end; gap: 0.5rem;">
            <button class="view-button" style="border: 1px solid #e5e7eb;">
                <span style="display: flex; align-items: center; gap: 0.25rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect width="14" height="14" x="8" y="8" rx="2" ry="2"/>
                        <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>
                    </svg>
                    Copy
                </span>
            </button>
            <button class="view-button" style="border: 1px solid #e5e7eb;">
                <span style="display: flex; align-items: center; gap: 0.25rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="7 10 12 15 17 10"/>
                        <line x1="12" x2="12" y1="15" y2="3"/>
                    </svg>
                    Export Data
                </span>
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search = st.text_input("", placeholder="Search exhibits...", label_visibility="collapsed")
    
    with col2:
        party_filter = st.selectbox("", ["All Parties", "Appellant", "Respondent"], label_visibility="collapsed")
    
    with col3:
        type_options = ["All Types"] + list(set(item["type"] for item in exhibits_data))
        type_filter = st.selectbox("", type_options, label_visibility="collapsed")
    
    # Filter data
    filtered_exhibits = exhibits_data
    if search:
        filtered_exhibits = [item for item in filtered_exhibits if 
                             search.lower() in item['id'].lower() or 
                             search.lower() in item['title'].lower() or
                             search.lower() in item['summary'].lower()]
    
    if party_filter != "All Parties":
        filtered_exhibits = [item for item in filtered_exhibits if item['party'] == party_filter]
    
    if type_filter != "All Types":
        filtered_exhibits = [item for item in filtered_exhibits if item['type'] == type_filter]
    
    # Display exhibits as a dataframe with styling
    if filtered_exhibits:
        # Create a DataFrame
        exhibits_df = pd.DataFrame(filtered_exhibits)
        
        # Create HTML table for better styling
        html_table = """
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: #f9fafb; border-bottom: 1px solid #e5e7eb;">
                    <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #6b7280;">EXHIBIT ID</th>
                    <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #6b7280;">PARTY</th>
                    <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #6b7280;">TITLE</th>
                    <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #6b7280;">TYPE</th>
                    <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #6b7280;">SUMMARY</th>
                    <th style="padding: 0.75rem 1rem; text-align: right; font-size: 0.875rem; font-weight: 500; color: #6b7280;">ACTIONS</th>
                </tr>
            </thead>
            <tbody>
        """
        
        for item in filtered_exhibits:
            party_badge_color = "blue" if item['party'] == "Appellant" else "red"
            
            html_table += f"""
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">{item['id']}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">
                    <span class="badge badge-{party_badge_color}">{item['party']}</span>
                </td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">{item['title']}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">
                    <span class="badge badge-gray">{item['type']}</span>
                </td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">{item['summary']}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem; text-align: right;">
                    <a href="#" style="color: #3b82f6; text-decoration: none; font-size: 0.875rem;">View</a>
                </td>
            </tr>
            """
        
        html_table += """
            </tbody>
        </table>
        """
        
        st.markdown(html_table, unsafe_allow_html=True)
    else:
        st.info("No exhibits match your search criteria.")

# Main application
def main():
    # App container with card styling
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Card header
    st.markdown('<div class="card-header"><h1 class="card-title">Legal Arguments Analysis</h1></div>', unsafe_allow_html=True)
    
    # Tabs
    tab_labels = ["Summary of Arguments", "Timeline", "Exhibits"]
    
    st.markdown(
        f"""
        <div class="tab-container">
            <button class={'tab-active' if st.session_state.active_tab == 'arguments' else 'tab-inactive'} id="tab-arguments">Summary of Arguments</button>
            <button class={'tab-active' if st.session_state.active_tab == 'timeline' else 'tab-inactive'} id="tab-timeline">Timeline</button>
            <button class={'tab-active' if st.session_state.active_tab == 'exhibits' else 'tab-inactive'} id="tab-exhibits">Exhibits</button>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # JavaScript for tab switching
    components.html("""
    <script>
        document.getElementById('tab-arguments').addEventListener('click', function() {
            window.parent.postMessage({
                type: 'streamlit:setActiveTab',
                tab: 'arguments'
            }, '*');
        });
        
        document.getElementById('tab-timeline').addEventListener('click', function() {
            window.parent.postMessage({
                type: 'streamlit:setActiveTab',
                tab: 'timeline'
            }, '*');
        });
        
        document.getElementById('tab-exhibits').addEventListener('click', function() {
            window.parent.postMessage({
                type: 'streamlit:setActiveTab',
                tab: 'exhibits'
            }, '*');
        });
        
        window.addEventListener('message', function(event) {
            const data = event.data;
            if (data.type === 'streamlit:setActiveTab') {
                window.parent.postMessage({
                    type: 'streamlit:component',
                    action: 'changeTab',
                    args: data.tab
                }, '*');
            }
            else if (data.type === 'streamlit:setViewMode') {
                window.parent.postMessage({
                    type: 'streamlit:component',
                    action: 'changeViewMode',
                    args: data.mode
                }, '*');
            }
        });
    </script>
    """, height=0)
    
    # Handle click events for argument expansion
    handle_click_messages()
    
    # Content based on active tab
    if st.session_state.active_tab == 'arguments':
        render_arguments_view()
    elif st.session_state.active_tab == 'timeline':
        render_timeline_view()
    elif st.session_state.active_tab == 'exhibits':
        render_exhibits_view()
    
    # Hidden buttons for handling tab and view mode changes
    if st.button("Change Tab", key="change-tab-button", help="Change active tab", visible=False):
        pass
    
    if st.button("Change View Mode", key="change-view-mode-button", help="Change view mode", visible=False):
        pass
    
    # Close the card container
    st.markdown('</div>', unsafe_allow_html=True)

    # Listen for streamlit component messages
    components.html("""
    <script>
        window.addEventListener('message', function(event) {
            const data = event.data;
            
            if (data.type === 'streamlit:component') {
                if (data.action === 'changeTab') {
                    const tabButton = document.querySelector('button[data-testid="baseButton-secondary"]:has(div[key="change-tab-button"])');
                    if (tabButton) {
                        const stateElement = document.createElement('div');
                        stateElement.setAttribute('data-new-tab', data.args);
                        document.body.appendChild(stateElement);
                        tabButton.click();
                    }
                }
                else if (data.action === 'changeViewMode') {
                    const viewModeButton = document.querySelector('button[data-testid="baseButton-secondary"]:has(div[key="change-view-mode-button"])');
                    if (viewModeButton) {
                        const stateElement = document.createElement('div');
                        stateElement.setAttribute('data-new-view-mode', data.args);
                        document.body.appendChild(stateElement);
                        viewModeButton.click();
                    }
                }
            }
        });
    </script>
    """, height=0)

# Check if tab or view mode need to be changed
if st.session_state.widget_was_triggered(trigger_value="change-tab-button"):
    # Get the new tab from the HTML element
    new_tab = components.html("""
    <script>
        const stateElement = document.querySelector('[data-new-tab]');
        if (stateElement) {
            const newTab = stateElement.getAttribute('data-new-tab');
            stateElement.remove();
            window.parent.postMessage({
                type: 'streamlit:fromComponent',
                value: newTab
            }, '*');
        }
    </script>
    """, height=0, return_value=True)
    
    if new_tab:
        st.session_state.active_tab = new_tab
        st.experimental_rerun()

if st.session_state.widget_was_triggered(trigger_value="change-view-mode-button"):
    # Get the new view mode from the HTML element
    new_view_mode = components.html("""
    <script>
        const stateElement = document.querySelector('[data-new-view-mode]');
        if (stateElement) {
            const newViewMode = stateElement.getAttribute('data-new-view-mode');
            stateElement.remove();
            window.parent.postMessage({
                type: 'streamlit:fromComponent',
                value: newViewMode
            }, '*');
        }
    </script>
    """, height=0, return_value=True)
    
    if new_view_mode:
        st.session_state.view_mode = new_view_mode
        st.experimental_rerun()

if __name__ == "__main__":
    main()
