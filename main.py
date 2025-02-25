import streamlit as st
import pandas as pd
from streamlit_elements import elements, mui, html
import streamlit.components.v1 as components
import json
from datetime import datetime

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Add custom CSS for styling
st.markdown("""
<style>
    /* General styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        margin-bottom: 1rem;
    }
    .stTabs [data-baseweb="tab"] {
        padding-bottom: 0.5rem;
        padding-top: 0.5rem;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        color: #1E6BE0;
        border-bottom-color: #1E6BE0;
    }
    
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        margin-bottom: 16px;
    }
    
    /* Argument section styling */
    .argument-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px;
        border-radius: 8px;
        cursor: pointer;
        margin-bottom: 8px;
    }
    .claimant-header {
        background-color: #EBF5FF;
        border: 1px solid #BEE3F8;
    }
    .respondent-header {
        background-color: #FFF5F5;
        border: 1px solid #FEB2B2;
    }
    .claimant-text {
        color: #3182CE;
    }
    .respondent-text {
        color: #E53E3E;
    }
    
    /* Points and evidence styling */
    .overview-points {
        background-color: #F7FAFC;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
    }
    .legal-point {
        background-color: #EBF8FF;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 8px;
    }
    .factual-point {
        background-color: #F0FFF4;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 8px;
    }
    .evidence-item {
        background-color: #F7FAFC;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 8px;
    }
    
    /* Badge and tag styling */
    .badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 4px;
    }
    .legal-badge {
        background-color: #BEE3F8;
        color: #2C5282;
    }
    .factual-badge {
        background-color: #C6F6D5;
        color: #276749;
    }
    .disputed-badge {
        background-color: #FED7D7;
        color: #C53030;
    }
    .paragraph-tag {
        background-color: #E2E8F0;
        color: #4A5568;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 11px;
    }
    
    /* Custom columns for arguments */
    .argument-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
    }
    
    /* Timeline table */
    .timeline-table {
        width: 100%;
        border-collapse: collapse;
    }
    .timeline-table th {
        background-color: #F7FAFC;
        text-align: left;
        padding: 12px;
        border-bottom: 1px solid #E2E8F0;
        color: #4A5568;
        font-size: 14px;
        font-weight: 500;
    }
    .timeline-table td {
        padding: 12px;
        border-bottom: 1px solid #E2E8F0;
        font-size: 14px;
    }
    .timeline-table tr.disputed {
        background-color: #FFF5F5;
    }
    .timeline-table .undisputed {
        color: #2F855A;
    }
    .timeline-table .disputed {
        color: #C53030;
    }
    
    /* Exhibits table */
    .exhibits-table {
        width: 100%;
        border-collapse: collapse;
    }
    .exhibits-table th {
        background-color: #F7FAFC;
        text-align: left;
        padding: 12px;
        border-bottom: 1px solid #E2E8F0;
        color: #4A5568;
        font-size: 14px;
        font-weight: 500;
    }
    .exhibits-table td {
        padding: 12px;
        border-bottom: 1px solid #E2E8F0;
        font-size: 14px;
    }
    .party-appellant {
        background-color: #EBF8FF;
        color: #2B6CB0;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    .party-respondent {
        background-color: #FFF5F5;
        color: #C53030;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    .type-badge {
        background-color: #EDF2F7;
        color: #4A5568;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    .view-link {
        color: #3182CE;
        text-decoration: none;
    }
    
    /* Topic headers */
    .topic-header {
        margin-bottom: 16px;
    }
    .topic-title {
        font-size: 18px;
        font-weight: 600;
        color: #2D3748;
        margin-bottom: 4px;
    }
    .topic-description {
        font-size: 14px;
        color: #718096;
    }
</style>
""", unsafe_allow_html=True)

# Define data structures for arguments
def get_argument_data():
    # This would normally come from a database or API
    claimant_arguments = {
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
                    "children": {}  # Subarguments would go here
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
    }
    
    respondent_arguments = {
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
    
    return claimant_arguments, respondent_arguments

# Define timeline data
def get_timeline_data():
    return [
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

# Define exhibits data
def get_exhibits_data():
    return [
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

# Define the topic structure
def get_topic_data():
    return [
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

# Function to render argument overview points
def render_overview_points(overview):
    if not overview or "points" not in overview:
        return ""
    
    points_html = ""
    for point in overview["points"]:
        points_html += f'<li class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full" style="background-color:#3182CE;"></div><span class="text-sm text-gray-700">{point}</span></li>'
    
    return f"""
    <div class="overview-points">
        <div class="flex justify-between items-start mb-2">
            <h6 class="text-sm font-medium">Key Points</h6>
            <span class="paragraph-tag">¶{overview["paragraphs"]}</span>
        </div>
        <ul class="space-y-2">
            {points_html}
        </ul>
    </div>
    """

# Function to render legal points
def render_legal_points(legal_points):
    if not legal_points:
        return ""
    
    points_html = ""
    for point in legal_points:
        disputed = ""
        if point.get("isDisputed", False):
            disputed = '<span class="badge disputed-badge">Disputed</span>'
        
        regulations_html = ""
        for reg in point.get("regulations", []):
            regulations_html += f'<span class="badge legal-badge">{reg}</span>'
        
        points_html += f"""
        <div class="legal-point">
            <div class="flex items-center gap-2 mb-1">
                <span class="badge legal-badge">Legal</span>
                {disputed}
            </div>
            <p class="text-sm text-gray-700">{point["point"]}</p>
            <div class="mt-2 flex flex-wrap gap-2">
                {regulations_html}
                <span class="paragraph-tag">¶{point["paragraphs"]}</span>
            </div>
        </div>
        """
    
    return f"""
    <div class="mb-6">
        <h6 class="text-sm font-medium mb-2">Legal Points</h6>
        {points_html}
    </div>
    """

# Function to render factual points
def render_factual_points(factual_points):
    if not factual_points:
        return ""
    
    points_html = ""
    for point in factual_points:
        disputed = ""
        if point.get("isDisputed", False):
            disputed = f'<span class="badge disputed-badge">Disputed by {point.get("source", "")}</span>'
        
        points_html += f"""
        <div class="factual-point">
            <div class="flex items-center gap-2 mb-1">
                <span class="badge factual-badge">Factual</span>
                {disputed}
            </div>
            <div class="flex items-center gap-2 mb-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#A0AEC0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="16" y1="2" x2="16" y2="6"></line>
                    <line x1="8" y1="2" x2="8" y2="6"></line>
                    <line x1="3" y1="10" x2="21" y2="10"></line>
                </svg>
                <span class="text-xs text-gray-600">{point.get("date", "")}</span>
            </div>
            <p class="text-sm text-gray-700">{point["point"]}</p>
            <span class="paragraph-tag mt-2 inline-block">¶{point["paragraphs"]}</span>
        </div>
        """
    
    return f"""
    <div class="mb-6">
        <h6 class="text-sm font-medium mb-2">Factual Points</h6>
        {points_html}
    </div>
    """

# Function to render evidence
def render_evidence(evidence_items):
    if not evidence_items:
        return ""
    
    items_html = ""
    for evidence in evidence_items:
        citations_html = ""
        for citation in evidence.get("citations", []):
            citations_html += f'<span class="paragraph-tag ml-1">¶{citation}</span>'
        
        items_html += f"""
        <div class="evidence-item">
            <div class="flex justify-between items-start">
                <div>
                    <p class="text-sm font-medium">{evidence["id"]}: {evidence["title"]}</p>
                    <p class="text-xs text-gray-600 mt-1">{evidence["summary"]}</p>
                    <div class="mt-2">
                        <span class="text-xs text-gray-500">Cited in: </span>
                        {citations_html}
                    </div>
                </div>
                <button class="text-blue-600 h-6">
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                    </svg>
                </button>
            </div>
        </div>
        """
    
    return f"""
    <div class="mb-6">
        <h6 class="text-sm font-medium mb-2">Evidence</h6>
        {items_html}
    </div>
    """

# Function to render case law
def render_case_law(case_law_items):
    if not case_law_items:
        return ""
    
    items_html = ""
    for case in case_law_items:
        cited_paragraphs_html = ""
        for para in case.get("citedParagraphs", []):
            cited_paragraphs_html += f'<span class="paragraph-tag ml-1">¶{para}</span>'
        
        items_html += f"""
        <div class="evidence-item">
            <div class="flex justify-between items-start">
                <div>
                    <div class="flex items-center gap-2">
                        <p class="text-sm font-medium">{case["caseNumber"]}</p>
                        <span class="paragraph-tag">¶{case["paragraphs"]}</span>
                    </div>
                    <p class="text-xs text-gray-600 mt-1">{case["title"]}</p>
                    <p class="text-sm text-gray-700 mt-2">{case["relevance"]}</p>
                    <div class="mt-2">
                        <span class="text-xs text-gray-500">Key Paragraphs: </span>
                        {cited_paragraphs_html}
                    </div>
                </div>
                <button class="text-blue-600 h-6">
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                    </svg>
                </button>
            </div>
        </div>
        """
    
    return f"""
    <div class="mb-6">
        <h6 class="text-sm font-medium mb-2">Case Law</h6>
        {items_html}
    </div>
    """

# Function to render an argument section
def render_argument(argument, side, level=0):
    if not argument:
        return ""
    
    # Determine styling based on side
    side_class = "claimant" if side == "claimant" else "respondent"
    
    # Get child count
    child_count = len(argument.get("children", {}))
    
    # Create session state key for this argument
    state_key = f"{side}-{argument['id']}"
    if state_key not in st.session_state:
        st.session_state[state_key] = False  # Default collapsed
    
    # Argument header with toggle
    header_html = f"""
    <div class="argument-header {side_class}-header" onclick="toggleArgument('{state_key}')">
        <div class="flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="chevron" data-state-key="{state_key}">
                <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
            <h5 class="font-medium text-sm {side_class}-text">
                {argument["id"]}. {argument["title"]}
            </h5>
            {f'<span class="badge {side_class}-badge">{child_count} subarguments</span>' if child_count > 0 else f'<span class="paragraph-tag">¶{argument["paragraphs"]}</span>'}
        </div>
    </div>
    """
    
    # Content to show when expanded
    content_html = ""
    if "overview" in argument:
        content_html += render_overview_points(argument["overview"])
    if "legalPoints" in argument:
        content_html += render_legal_points(argument["legalPoints"])
    if "factualPoints" in argument:
        content_html += render_factual_points(argument["factualPoints"])
    if "evidence" in argument:
        content_html += render_evidence(argument["evidence"])
    if "caseLaw" in argument:
        content_html += render_case_law(argument["caseLaw"])
    
    # JavaScript for toggling arguments
    js = f"""
    <script>
    function toggleArgument(key) {{
        // Toggle the display of the content
        const content = document.getElementById(key + '-content');
        const isVisible = content.style.display !== 'none';
        content.style.display = isVisible ? 'none' : 'block';
        
        // Rotate the chevron icon
        const chevron = document.querySelector('.chevron[data-state-key="' + key + '"]');
        chevron.style.transform = isVisible ? 'rotate(0deg)' : 'rotate(90deg)';
        
        // If this is a parent argument, toggle visibility of children
        const children = document.querySelectorAll('[data-parent="' + key + '"]');
        children.forEach(child => {{
            child.style.display = isVisible ? 'none' : 'block';
        }});
    }}
    </script>
    """
    
    # Combine the HTML
    argument_html = f"""
    <div class="argument-section" id="{state_key}-wrapper">
        {header_html}
        <div id="{state_key}-content" style="display: none; padding: 16px; background-color: white; border-radius: 0 0 8px 8px;">
            {content_html}
        </div>
        {js}
    </div>
    """
    
    return argument_html

# Render arguments side by side
def render_argument_pair(claimant_arg, respondent_arg, level=0):
    claimant_html = render_argument(claimant_arg, "claimant", level)
    respondent_html = render_argument(respondent_arg, "respondent", level)
    
    return f"""
    <div class="argument-grid">
        <div>{claimant_html}</div>
        <div>{respondent_html}</div>
    </div>
    """

# Function to render the timeline view
def render_timeline(data, search_term="", show_disputed_only=False):
    # Filter the data based on search term and disputed checkbox
    filtered_data = data
    if search_term:
        filtered_data = [item for item in data if 
                         search_term.lower() in item["appellant_version"].lower() or 
                         search_term.lower() in item["respondent_version"].lower()]
    
    if show_disputed_only:
        filtered_data = [item for item in filtered_data if item["status"] == "Disputed"]
    
    # Create the table HTML
    rows_html = ""
    for item in filtered_data:
        row_class = "disputed" if item["status"] == "Disputed" else ""
        status_class = "disputed" if item["status"] == "Disputed" else "undisputed"
        
        rows_html += f"""
        <tr class="{row_class}">
            <td>{item["date"]}</td>
            <td>{item["appellant_version"]}</td>
            <td>{item["respondent_version"]}</td>
            <td class="{status_class}">{item["status"]}</td>
        </tr>
        """
    
    return f"""
    <table class="timeline-table">
        <thead>
            <tr>
                <th>DATE</th>
                <th>APPELLANT'S VERSION</th>
                <th>RESPONDENT'S VERSION</th>
                <th>STATUS</th>
            </tr>
        </thead>
        <tbody>
            {rows_html}
        </tbody>
    </table>
    """

# Function to render the exhibits view
def render_exhibits(data, search_term="", party_filter="All Parties", type_filter="All Types"):
    # Filter the data based on search term and dropdown filters
    filtered_data = data
    
    if search_term:
        filtered_data = [item for item in filtered_data if 
                         search_term.lower() in item["title"].lower() or 
                         search_term.lower() in item["summary"].lower() or
                         search_term.lower() in item["id"].lower()]
    
    if party_filter != "All Parties":
        filtered_data = [item for item in filtered_data if item["party"] == party_filter]
    
    if type_filter != "All Types":
        filtered_data = [item for item in filtered_data if item["type"] == type_filter]
    
    # Create the table HTML
    rows_html = ""
    for item in filtered_data:
        party_class = "party-appellant" if item["party"] == "Appellant" else "party-respondent"
        
        rows_html += f"""
        <tr>
            <td>{item["id"]}</td>
            <td><span class="{party_class}">{item["party"]}</span></td>
            <td>{item["title"]}</td>
            <td><span class="type-badge">{item["type"]}</span></td>
            <td>{item["summary"]}</td>
            <td><a href="#" class="view-link">View</a></td>
        </tr>
        """
    
    return f"""
    <table class="exhibits-table">
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
            {rows_html}
        </tbody>
    </table>
    """

# Function to render the topic view
def render_topic_view(topics, claimant_args, respondent_args):
    topics_html = ""
    
    for topic in topics:
        topic_html = f"""
        <div class="mb-8">
            <div class="topic-header">
                <h2 class="topic-title">{topic["title"]}</h2>
                <p class="topic-description">{topic["description"]}</p>
            </div>
            
            <div class="grid grid-cols-2 gap-6 mb-4 px-4">
                <div>
                    <h3 class="text-md font-semibold claimant-text">Claimant's Arguments</h3>
                </div>
                <div>
                    <h3 class="text-md font-semibold respondent-text">Respondent's Arguments</h3>
                </div>
            </div>
        """
        
        # Add argument pairs for this topic
        for arg_id in topic["argument_ids"]:
            claimant_arg = claimant_args.get(arg_id, {})
            respondent_arg = respondent_args.get(arg_id, {})
            
            if claimant_arg and respondent_arg:
                topic_html += render_argument_pair(claimant_arg, respondent_arg)
        
        topic_html += "</div>"
        topics_html += topic_html
    
    return topics_html

# Main app
def main():
    # Initialize session state for tab
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "arguments"
    
    if "view_mode" not in st.session_state:
        st.session_state.view_mode = "default"
    
    # Get data
    claimant_arguments, respondent_arguments = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    topic_data = get_topic_data()
    
    # Title
    st.title("Legal Arguments Analysis")
    
    # Tab navigation
    tab1, tab2, tab3 = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])
    
    with tab1:  # Arguments tab
        # View mode toggle
        col1, col2, col3 = st.columns([6, 2, 2])
        with col3:
            view_mode = st.radio(
                "View Mode:",
                ["Standard View", "Topic View"],
                horizontal=True,
                label_visibility="collapsed"
            )
            st.session_state.view_mode = "default" if view_mode == "Standard View" else "hierarchical"
        
        if st.session_state.view_mode == "default":
            # Headers for both columns
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<h3 style='color:#3182CE;'>Claimant's Arguments</h3>", unsafe_allow_html=True)
            with col2:
                st.markdown("<h3 style='color:#E53E3E;'>Respondent's Arguments</h3>", unsafe_allow_html=True)
            
            # Render argument pairs
            for arg_id in claimant_arguments:
                claimant_arg = claimant_arguments[arg_id]
                respondent_arg = respondent_arguments[arg_id]
                
                # Use custom component to render HTML
                components.html(
                    render_argument_pair(claimant_arg, respondent_arg),
                    height=350,  # Adjust as needed
                    scrolling=True
                )
        else:
            # Topic view
            components.html(
                render_topic_view(topic_data, claimant_arguments, respondent_arguments),
                height=700,  # Adjust as needed
                scrolling=True
            )
    
    with tab2:  # Timeline tab
        col1, col2 = st.columns([4, 1])
        with col1:
            search_term = st.text_input("Search events...", key="timeline_search")
        with col2:
            show_disputed_only = st.checkbox("Disputed events only", key="disputed_only")
        
        # Render timeline
        components.html(
            render_timeline(timeline_data, search_term, show_disputed_only),
            height=500,
            scrolling=True
        )
    
    with tab3:  # Exhibits tab
        col1, col2, col3 = st.columns([4, 1, 1])
        with col1:
            search_term = st.text_input("Search exhibits...", key="exhibits_search")
        with col2:
            party_filter = st.selectbox("Party", ["All Parties", "Appellant", "Respondent"], key="party_filter")
        with col3:
            # Get unique types
            types = ["All Types"] + list(set(item["type"] for item in exhibits_data))
            type_filter = st.selectbox("Type", types, key="type_filter")
        
        # Render exhibits
        components.html(
            render_exhibits(exhibits_data, search_term, party_filter, type_filter),
            height=500,
            scrolling=True
        )

if __name__ == "__main__":
    main()
