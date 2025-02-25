import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Add custom CSS for styling
st.markdown("""
<style>
    /* Reset some Streamlit defaults */
    .stApp {
        font-family: sans-serif;
    }
    
    /* Hide Streamlit elements we don't need */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 16px;
        overflow: hidden;
    }
    
    /* Argument section styling */
    .arg-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 16px;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .arg-header:hover {
        background-color: #F7FAFC;
    }
    .arg-title {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .arg-content {
        padding: 16px;
        border-top: 1px solid #EDF2F7;
    }
    
    /* Side-specific styling */
    .claimant-header {
        background-color: #EBF5FF;
        border: 1px solid #BEE3F8;
        border-radius: 8px;
    }
    .respondent-header {
        background-color: #FFF5F5;
        border: 1px solid #FED7D7;
        border-radius: 8px;
    }
    .claimant-text {
        color: #3182CE;
    }
    .respondent-text {
        color: #E53E3E;
    }
    .claimant-badge {
        background-color: #EBF8FF;
        color: #2B6CB0;
    }
    .respondent-badge {
        background-color: #FFF5F5; 
        color: #C53030;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    .para-badge {
        background-color: #EDF2F7;
        color: #4A5568;
        font-size: 11px;
        padding: 2px 6px;
        border-radius: 4px;
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
    
    /* Point containers */
    .overview-box {
        background-color: #F7FAFC;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
    }
    .point-box {
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 8px;
    }
    .legal-box {
        background-color: #EBF8FF;
    }
    .factual-box {
        background-color: #F0FFF4;
    }
    .evidence-box {
        background-color: #F7FAFC;
    }
    
    /* Custom bullet points */
    .bullet-list {
        list-style-type: none;
        padding-left: 0;
    }
    .bullet-list li {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
    }
    .bullet-point {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background-color: #3182CE;
        flex-shrink: 0;
    }
    
    /* Tab styling */
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
    
    /* Timeline and Exhibits table styling */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
    }
    .custom-table th {
        background-color: #F7FAFC;
        text-align: left;
        padding: 12px;
        border-bottom: 1px solid #E2E8F0;
        color: #4A5568;
        font-size: 14px;
        font-weight: 500;
    }
    .custom-table td {
        padding: 12px;
        border-bottom: 1px solid #E2E8F0;
        font-size: 14px;
    }
    .custom-table tr.disputed {
        background-color: #FFF5F5;
    }
    
    /* Topic view styling */
    .topic-header {
        margin-bottom: 16px;
    }
    .topic-title {
        font-size: 18px;
        font-weight: 600;
        color: #2D3748;
    }
    .topic-desc {
        font-size: 14px;
        color: #718096;
        margin-top: 4px;
    }
    
    /* Hide checkbox label but keep the checkbox */
    .toggle-arg .stCheckbox {
        position: absolute;
        opacity: 0;
    }
    .toggle-arg p {
        display: none;
    }
    
    /* Hide default Streamlit margins */
    .element-container {
        margin-bottom: 0 !important;
    }
    div[data-testid="stVerticalBlock"] > div.element-container {
        margin-bottom: 0 !important;
    }

    /* Vertically center align the elements */
    .flex-center {
        display: flex;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for custom components behavior
st.markdown("""
<script>
function toggleArgument(id) {
    const content = document.getElementById('content-' + id);
    const chevron = document.getElementById('chevron-' + id);
    
    if (content.style.display === 'none' || !content.style.display) {
        content.style.display = 'block';
        chevron.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
        </svg>`;
    } else {
        content.style.display = 'none';
        chevron.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
        </svg>`;
    }
}
</script>
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

# Initialize session state
if "expanded" not in st.session_state:
    st.session_state.expanded = {}
    
if "view_mode" not in st.session_state:
    st.session_state.view_mode = "default"

# Render HTML argument section - uses custom HTML/CSS instead of Streamlit components
def render_html_argument(arg, side):
    # Get the expanded state key for this argument
    key = f"{side}_{arg['id']}"
    is_expanded = st.session_state.expanded.get(key, False)
    
    # Get child count
    child_count = len(arg.get("children", {}))
    
    # Set styling based on side
    side_class = "claimant" if side == "claimant" else "respondent"
    
    # Render overview section if available
    overview_html = ""
    if "overview" in arg and "points" in arg["overview"]:
        points_html = ""
        for point in arg["overview"]["points"]:
            points_html += f"""
            <li>
                <div class="bullet-point"></div>
                <span>{point}</span>
            </li>
            """
        
        overview_html = f"""
        <div class="overview-box">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                <h6 style="font-size: 14px; font-weight: 500; margin: 0;">Key Points</h6>
                <span class="para-badge">¶{arg["overview"]["paragraphs"]}</span>
            </div>
            <ul class="bullet-list">
                {points_html}
            </ul>
        </div>
        """
    
    # Render legal points if available
    legal_points_html = ""
    if "legal_points" in arg and arg["legal_points"]:
        points_html = ""
        for point in arg["legal_points"]:
            disputed = ""
            if point.get("is_disputed", False):
                disputed = '<span class="badge disputed-badge">Disputed</span>'
            
            regulations_html = ""
            for reg in point.get("regulations", []):
                regulations_html += f'<span class="badge legal-badge">{reg}</span>'
            
            points_html += f"""
            <div class="point-box legal-box">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                    <span class="badge legal-badge">Legal</span>
                    {disputed}
                </div>
                <p style="font-size: 14px; margin: 0 0 8px 0;">{point["point"]}</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    {regulations_html}
                    <span class="para-badge">¶{point["paragraphs"]}</span>
                </div>
            </div>
            """
        
        legal_points_html = f"""
        <div style="margin-bottom: 16px;">
            <h6 style="font-size: 14px; font-weight: 500; margin: 0 0 8px 0;">Legal Points</h6>
            {points_html}
        </div>
        """
    
    # Render factual points if available
    factual_points_html = ""
    if "factual_points" in arg and arg["factual_points"]:
        points_html = ""
        for point in arg["factual_points"]:
            disputed = ""
            if point.get("is_disputed", False):
                disputed = f'<span class="badge disputed-badge">Disputed by {point.get("source", "")}</span>'
            
            points_html += f"""
            <div class="point-box factual-box">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                    <span class="badge factual-badge">Factual</span>
                    {disputed}
                </div>
                <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 6px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                    <span style="font-size: 12px; color: #4A5568;">{point.get("date", "")}</span>
                </div>
                <p style="font-size: 14px; margin: 0 0 8px 0;">{point["point"]}</p>
                <span class="para-badge">¶{point["paragraphs"]}</span>
            </div>
            """
        
        factual_points_html = f"""
        <div style="margin-bottom: 16px;">
            <h6 style="font-size: 14px; font-weight: 500; margin: 0 0 8px 0;">Factual Points</h6>
            {points_html}
        </div>
        """
    
    # Render evidence if available
    evidence_html = ""
    if "evidence" in arg and arg["evidence"]:
        items_html = ""
        for item in arg["evidence"]:
            citations_html = ""
            for citation in item.get("citations", []):
                citations_html += f'<span class="para-badge" style="margin-left: 4px;">¶{citation}</span>'
            
            items_html += f"""
            <div class="point-box evidence-box">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <p style="font-size: 14px; font-weight: 500; margin: 0 0 4px 0;">{item["id"]}: {item["title"]}</p>
                        <p style="font-size: 12px; color: #4A5568; margin: 0 0 8px 0;">{item["summary"]}</p>
                        <div>
                            <span style="font-size: 12px; color: #4A5568;">Cited in: </span>
                            {citations_html}
                        </div>
                    </div>
                    <button style="background: none; border: none; cursor: pointer; color: #3182CE; height: 24px; width: 24px; padding: 0; display: flex; align-items: center; justify-content: center;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                        </svg>
                    </button>
                </div>
            </div>
            """
        
        evidence_html = f"""
        <div style="margin-bottom: 16px;">
            <h6 style="font-size: 14px; font-weight: 500; margin: 0 0 8px 0;">Evidence</h6>
            {items_html}
        </div>
        """
    
    # Render case law if available
    case_law_html = ""
    if "case_law" in arg and arg["case_law"]:
        items_html = ""
        for case in arg["case_law"]:
            cited_paras_html = ""
            for para in case.get("cited_paragraphs", []):
                cited_paras_html += f'<span class="para-badge" style="margin-left: 4px;">¶{para}</span>'
            
            items_html += f"""
            <div class="point-box evidence-box">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                            <p style="font-size: 14px; font-weight: 500; margin: 0;">{case["case_number"]}</p>
                            <span class="para-badge">¶{case["paragraphs"]}</span>
                        </div>
                        <p style="font-size: 12px; color: #4A5568; margin: 0 0 8px 0;">{case["title"]}</p>
                        <p style="font-size: 14px; margin: 0 0 8px 0;">{case["relevance"]}</p>
                        <div>
                            <span style="font-size: 12px; color: #4A5568;">Key Paragraphs: </span>
                            {cited_paras_html}
                        </div>
                    </div>
                    <button style="background: none; border: none; cursor: pointer; color: #3182CE; height: 24px; width: 24px; padding: 0; display: flex; align-items: center; justify-content: center;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                        </svg>
                    </button>
                </div>
            </div>
            """
        
        case_law_html = f"""
        <div style="margin-bottom: 16px;">
            <h6 style="font-size: 14px; font-weight: 500; margin: 0 0 8px 0;">Case Law</h6>
            {items_html}
        </div>
        """
    
    # Combine all content
    content_html = overview_html + legal_points_html + factual_points_html + evidence_html + case_law_html
    
    # Check if we have child arguments
    has_children = len(arg.get("children", {})) > 0
    
    display_style = "block" if is_expanded else "none"
    chevron_html = """
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="9 18 15 12 9 6"></polyline>
    </svg>
    """ if not is_expanded else """
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="6 9 12 15 18 9"></polyline>
    </svg>
    """
    
    # Build the full HTML for the argument
    html = f"""
    <div class="card" id="arg-{side}-{arg['id']}">
        <div class="arg-header {side_class}-header" onclick="document.getElementById('checkbox-{key}').click();">
            <div class="arg-title">
                <span id="chevron-{key}">{chevron_html}</span>
                <h5 class="{side_class}-text" style="font-size: 14px; font-weight: 500; margin: 0;">
                    {arg['id']}. {arg['title']}
                </h5>
                {f'<span class="badge {side_class}-badge">{child_count} subarguments</span>' if child_count > 0 else f'<span class="para-badge">¶{arg["paragraphs"]}</span>'}
            </div>
        </div>
        <div class="arg-content" id="content-{key}" style="display: {display_style};">
            {content_html}
        </div>
    </div>
    """
    
    # Use a hidden checkbox to track state
    st.checkbox("", key=f"checkbox-{key}", value=is_expanded, label_visibility="collapsed")
    
    # Update session state when checkbox changes
    if f"checkbox-{key}" in st.session_state:
        st.session_state.expanded[key] = st.session_state[f"checkbox-{key}"]
    
    return html

# Render side-by-side arguments
def render_argument_pair(claimant_arg, respondent_arg):
    # Create columns for side-by-side display
    col1, col2 = st.columns(2)
    
    # Render claimant arguments
    with col1:
        components.html(
            render_html_argument(claimant_arg, "claimant"),
            height=400,  # Adjust based on content
            scrolling=True
        )
    
    # Render respondent arguments
    with col2:
        components.html(
            render_html_argument(respondent_arg, "respondent"),
            height=400,  # Adjust based on content
            scrolling=True
        )

# Function to render by topic
def render_topic_view(topics, claimant_args, respondent_args):
    for topic in topics:
        st.markdown(f"""
        <div class="topic-header">
            <h2 class="topic-title">{topic['title']}</h2>
            <p class="topic-desc">{topic['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Column headers
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<h3 class="claimant-text" style="font-size: 16px; font-weight: 600;">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<h3 class="respondent-text" style="font-size: 16px; font-weight: 600;">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
        
        # Render each argument pair for this topic
        for arg_id in topic.get("argument_ids", []):
            if arg_id in claimant_args and arg_id in respondent_args:
                render_argument_pair(claimant_args[arg_id], respondent_args[arg_id])
        
        st.markdown("---")

# Timeline view with HTML
def render_timeline_html(timeline_df, search="", disputed_only=False):
    # Apply filters
    filtered_df = timeline_df.copy()
    
    if search:
        mask = (
            filtered_df["appellant_version"].str.contains(search, case=False, na=False) |
            filtered_df["respondent_version"].str.contains(search, case=False, na=False)
        )
        filtered_df = filtered_df[mask]
    
    if disputed_only:
        filtered_df = filtered_df[filtered_df["status"] == "Disputed"]
    
    # Build HTML table
    rows_html = ""
    for _, row in filtered_df.iterrows():
        row_class = "disputed" if row["status"] == "Disputed" else ""
        status_color = "color: #C53030;" if row["status"] == "Disputed" else "color: #2F855A;"
        
        rows_html += f"""
        <tr class="{row_class}">
            <td>{row["date"]}</td>
            <td>{row["appellant_version"]}</td>
            <td>{row["respondent_version"]}</td>
            <td style="{status_color}">{row["status"]}</td>
        </tr>
        """
    
    html = f"""
    <div style="max-height: 500px; overflow-y: auto; border: 1px solid #E2E8F0; border-radius: 6px;">
        <table class="custom-table">
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
    </div>
    """
    
    return html

# Exhibits view with HTML
def render_exhibits_html(exhibits_df, search="", party_filter="All Parties", type_filter="All Types"):
    # Apply filters
    filtered_df = exhibits_df.copy()
    
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
    
    # Build HTML table
    rows_html = ""
    for _, row in filtered_df.iterrows():
        party_class = "claimant-badge" if row["party"] == "Appellant" else "respondent-badge"
        
        rows_html += f"""
        <tr>
            <td>{row["id"]}</td>
            <td><span class="badge {party_class}">{row["party"]}</span></td>
            <td>{row["title"]}</td>
            <td><span class="badge para-badge">{row["type"]}</span></td>
            <td>{row["summary"]}</td>
            <td><a href="#" style="color: #3182CE; text-decoration: none;">View</a></td>
        </tr>
        """
    
    html = f"""
    <div style="max-height: 500px; overflow-y: auto; border: 1px solid #E2E8F0; border-radius: 6px;">
        <table class="custom-table">
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
    </div>
    """
    
    return html

# Main app function
def main():
    # Set app title
    st.markdown('<h1 style="font-size: 1.8rem; margin-bottom: 1rem;">Legal Arguments Analysis</h1>', unsafe_allow_html=True)
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])
    
    # Get the data
    claimant_args, respondent_args, topics = get_argument_data()
    timeline_df = get_timeline_data()
    exhibits_df = get_exhibits_data()
    
    # Summary of Arguments tab
    with tab1:
        # View mode selection
        col1, col2 = st.columns([4, 1])
        with col2:
            view_mode = st.radio(
                "View Mode:",
                ["Standard View", "Topic View"],
                horizontal=True,
                index=0 if st.session_state.view_mode == "default" else 1,
                label_visibility="collapsed"
            )
            st.session_state.view_mode = "default" if view_mode == "Standard View" else "topic"
        
        # Display arguments based on view mode
        if st.session_state.view_mode == "default":
            # Column headers
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<h2 style="color: #3182CE; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem;">Claimant\'s Arguments</h2>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<h2 style="color: #E53E3E; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem;">Respondent\'s Arguments</h2>', unsafe_allow_html=True)
            
            # Display arguments in standard view
            for arg_id in claimant_args:
                if arg_id in respondent_args:
                    render_argument_pair(claimant_args[arg_id], respondent_args[arg_id])
        else:
            # Display arguments in topic view
            render_topic_view(topics, claimant_args, respondent_args)
    
    # Timeline tab
    with tab2:
        # Search and filter options
        col1, col2 = st.columns([3, 1])
        with col1:
            timeline_search = st.text_input("Search events...", key="timeline_search")
        with col2:
            disputed_only = st.checkbox("Disputed events only", key="disputed_filter")
        
        # Add copy and export buttons
        col1, col2 = st.columns([5, 1])
        with col2:
            st.markdown("""
            <div style="display: flex; justify-content: flex-end; gap: 8px; margin-bottom: 16px;">
                <button style="display: flex; align-items: center; gap: 4px; background-color: white; border: 1px solid #E2E8F0; padding: 6px 12px; border-radius: 6px; font-size: 14px; cursor: pointer;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                </button>
                <button style="display: flex; align-items: center; gap: 4px; background-color: white; border: 1px solid #E2E8F0; padding: 6px 12px; border-radius: 6px; font-size: 14px; cursor: pointer;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                    Export Data
                </button>
            </div>
            """, unsafe_allow_html=True)
        
        # Display timeline
        components.html(
            render_timeline_html(timeline_df, timeline_search, disputed_only),
            height=500,
            scrolling=False
        )
    
    # Exhibits tab
    with tab3:
        # Search and filter options
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            exhibits_search = st.text_input("Search exhibits...", key="exhibits_search")
        with col2:
            party_filter = st.selectbox(
                "Party", 
                ["All Parties", "Appellant", "Respondent"],
                key="party_filter"
            )
        with col3:
            type_options = ["All Types"] + sorted(exhibits_df["type"].unique().tolist())
            type_filter = st.selectbox(
                "Type",
                type_options,
                key="type_filter"
            )
        
        # Add copy and export buttons
        col1, col2 = st.columns([5, 1])
        with col2:
            st.markdown("""
            <div style="display: flex; justify-content: flex-end; gap: 8px; margin-bottom: 16px;">
                <button style="display: flex; align-items: center; gap: 4px; background-color: white; border: 1px solid #E2E8F0; padding: 6px 12px; border-radius: 6px; font-size: 14px; cursor: pointer;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                </button>
                <button style="display: flex; align-items: center; gap: 4px; background-color: white; border: 1px solid #E2E8F0; padding: 6px 12px; border-radius: 6px; font-size: 14px; cursor: pointer;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                    Export Data
                </button>
            </div>
            """, unsafe_allow_html=True)
            
        # Display exhibits
        components.html(
            render_exhibits_html(exhibits_df, exhibits_search, party_filter, type_filter),
            height=500,
            scrolling=False
        )

# Run the app
if __name__ == "__main__":
    main()
