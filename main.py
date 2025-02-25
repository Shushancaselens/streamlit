import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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
        height: 50px;
        white-space: pre-wrap;
        padding-top: 10px;
    }
    .stTabs [aria-selected="true"] {
        color: #3182CE;
        border-bottom: 2px solid #3182CE;
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
    
    /* Expander custom styling */
    .streamlit-expanderHeader {
        font-size: 1rem;
        font-weight: 500;
    }
    .claimant-expander .streamlit-expanderHeader {
        background-color: #EBF5FF;
        color: #3182CE;
        border: 1px solid #BEE3F8;
        border-radius: 8px;
    }
    .respondent-expander .streamlit-expanderHeader {
        background-color: #FFF5F5;
        color: #E53E3E;
        border: 1px solid #FEB2B2;
        border-radius: 8px;
    }
    
    /* Hide checkbox elements but keep functionality */
    .toggle-checkbox-container {
        position: absolute;
        opacity: 0;
        width: 0;
        height: 0;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 4px;
        font-weight: 500;
    }
    .claimant-badge {
        background-color: #EBF8FF;
        color: #2B6CB0;
    }
    .respondent-badge {
        background-color: #FFF5F5;
        color: #C53030;
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
    .paragraph-badge {
        background-color: #E2E8F0;
        color: #4A5568;
        font-size: 11px;
    }
    
    /* Point styling */
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
    
    /* No margin for list items in arguments */
    .argument-content ul {
        list-style-type: none;
        padding-left: 0;
    }
    .argument-content ul li {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
    }
    .argument-content ul li:before {
        content: "";
        display: block;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background-color: #3182CE;
    }
    
    /* Child arguments indentation */
    .child-argument {
        margin-left: 1.5rem;
        position: relative;
    }
    .child-argument:before {
        content: "";
        position: absolute;
        left: -1rem;
        top: 0;
        height: 100%;
        width: 2px;
        background-color: #E2E8F0;
    }
    .claimant-child:before {
        background-color: rgba(66, 153, 225, 0.5);
    }
    .respondent-child:before {
        background-color: rgba(245, 101, 101, 0.5);
    }
    
    /* Custom connector lines */
    .argument-connector {
        position: relative;
    }
    .connector-line {
        position: absolute;
        left: -0.5rem;
        top: 1.25rem;
        width: 0.5rem;
        height: 1px;
        background-color: #CBD5E0;
    }
    .claimant-connector .connector-line {
        background-color: rgba(66, 153, 225, 0.5);
    }
    .respondent-connector .connector-line {
        background-color: rgba(245, 101, 101, 0.5);
    }
    
    /* Timeline table styling */
    .timeline-table th {
        background-color: #F7FAFC;
        text-align: left;
        font-weight: 500;
    }
    .timeline-table td {
        border-top: 1px solid #E2E8F0;
    }
    .disputed-row {
        background-color: #FFF5F5 !important;
    }
    .status-undisputed {
        color: #2F855A;
    }
    .status-disputed {
        color: #C53030;
    }
    
    /* Topic view styling */
    .topic-header {
        margin-bottom: 1rem;
    }
    .topic-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.25rem;
    }
    .topic-description {
        color: #718096;
        font-size: 0.875rem;
    }

    /* Checkbox to button styling */
    div[data-testid="stCheckbox"] {
        display: none;
    }
    
    /* Fix for expandable elements */
    .streamlit-expanderContent {
        overflow: visible !important;
    }
    
    /* Action buttons */
    .action-buttons {
        display: flex;
        justify-content: flex-end;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    .action-button {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background-color: white;
        border: 1px solid #E2E8F0;
        padding: 0.5rem 0.75rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        cursor: pointer;
        transition: all 0.2s;
    }
    .action-button:hover {
        background-color: #F7FAFC;
    }
    
    /* Custom button styling */
    .custom-button {
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 14px;
        cursor: pointer;
        border: 1px solid #E2E8F0;
        background-color: white;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .custom-button:hover {
        background-color: #F7FAFC;
    }
    
    /* View toggle */
    .view-toggle {
        display: flex;
        background-color: #F7FAFC;
        border-radius: 6px;
        padding: 4px;
        margin-bottom: 16px;
    }
    .view-toggle-button {
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
        border: none;
        background: none;
    }
    .view-toggle-button.active {
        background-color: white;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Function to get argument data
def get_argument_data():
    # Claimant arguments
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
                            "children": {
                                "1.1.1.1": {
                                    "id": "1.1.1.1",
                                    "title": "Registration Gap Analysis",
                                    "paragraphs": "31-35",
                                    "overview": {
                                        "points": [
                                            "Detailed analysis of 1975-1976 gap",
                                            "Legal force majeure considerations",
                                            "Public usage during gap period"
                                        ],
                                        "paragraphs": "31"
                                    },
                                    "legal_points": [
                                        {
                                            "point": "Administrative gap explained by force majeure",
                                            "is_disputed": False,
                                            "regulations": ["Administrative Law"],
                                            "paragraphs": "32-33"
                                        }
                                    ],
                                    "factual_points": [
                                        {
                                            "point": "Club activities continued during gap period",
                                            "date": "1975-1976",
                                            "is_disputed": False,
                                            "paragraphs": "33-34"
                                        },
                                        {
                                            "point": "Media coverage continued using same name",
                                            "date": "1975-1976",
                                            "is_disputed": False,
                                            "paragraphs": "34-35"
                                        }
                                    ],
                                    "children": {}
                                }
                            }
                        },
                        "1.1.2": {
                            "id": "1.1.2",
                            "title": "Public Recognition",
                            "paragraphs": "36-42",
                            "legal_points": [
                                {
                                    "point": "Public perception as legal factor in CAS jurisprudence",
                                    "is_disputed": False,
                                    "regulations": ["CAS 2016/A/4576 ¶24"],
                                    "paragraphs": "36-37"
                                }
                            ],
                            "factual_points": [
                                {
                                    "point": "Continuous media recognition since 1950",
                                    "date": "1950-present",
                                    "is_disputed": False,
                                    "paragraphs": "38-39"
                                },
                                {
                                    "point": "Fan support remained consistent",
                                    "date": "1950-present",
                                    "is_disputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "40-41"
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-3",
                                    "title": "Media Archive Collection",
                                    "summary": "Press coverage demonstrating continuous recognition",
                                    "citations": ["38", "39", "40"]
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
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Variations Analysis",
                            "paragraphs": "56-60",
                            "factual_points": [
                                {
                                    "point": "Minor shade variations do not affect continuity",
                                    "date": "1970-1980",
                                    "is_disputed": False,
                                    "paragraphs": "56-57"
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "is_disputed": False,
                                    "paragraphs": "58-59"
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
                            "children": {
                                "1.1.1.1": {
                                    "id": "1.1.1.1",
                                    "title": "Legal Entity Discontinuity",
                                    "paragraphs": "231-235",
                                    "legal_points": [
                                        {
                                            "point": "New registration created distinct legal entity",
                                            "is_disputed": True,
                                            "regulations": ["Company Law §15"],
                                            "paragraphs": "231-232"
                                        }
                                    ],
                                    "factual_points": [
                                        {
                                            "point": "Different ownership structure post-1976",
                                            "date": "1976",
                                            "is_disputed": False,
                                            "paragraphs": "233-234"
                                        }
                                    ],
                                    "case_law": [
                                        {
                                            "case_number": "CAS 2018/A/5618",
                                            "title": "Legal entity identity case",
                                            "relevance": "Registration gap creating new legal entity",
                                            "paragraphs": "235",
                                            "cited_paragraphs": ["235"]
                                        }
                                    ],
                                    "children": {}
                                }
                            }
                        },
                        "1.1.2": {
                            "id": "1.1.2",
                            "title": "Public Recognition Rebuttal",
                            "paragraphs": "236-240",
                            "legal_points": [
                                {
                                    "point": "Public perception secondary to operational continuity",
                                    "is_disputed": True,
                                    "regulations": ["CAS 2017/A/5465 ¶45"],
                                    "paragraphs": "236-237"
                                }
                            ],
                            "factual_points": [
                                {
                                    "point": "Media referred to 'new club' in 1976",
                                    "date": "1976",
                                    "is_disputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "238-239"
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-3",
                                    "title": "Newspaper Articles 1976",
                                    "summary": "Media reports referring to new club formation",
                                    "citations": ["238", "239"]
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
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Symbolism Analysis",
                            "paragraphs": "247-249",
                            "factual_points": [
                                {
                                    "point": "Pre-1976 colors represented original city district",
                                    "date": "1950-1975",
                                    "is_disputed": False,
                                    "paragraphs": "247"
                                },
                                {
                                    "point": "Post-1976 colors represented new ownership region",
                                    "date": "1976-present",
                                    "is_disputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "248-249"
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
    
    # Topic structure
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
    
    return claimant_arguments, respondent_arguments, topics

# Get timeline data
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

# Get exhibits data
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
def init_session_state():
    if "expanded" not in st.session_state:
        st.session_state.expanded = {}
    if "view_mode" not in st.session_state:
        st.session_state.view_mode = "default"
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = 0
    if "timeline_search" not in st.session_state:
        st.session_state.timeline_search = ""
    if "disputed_only" not in st.session_state:
        st.session_state.disputed_only = False
    if "exhibits_search" not in st.session_state:
        st.session_state.exhibits_search = ""
    if "party_filter" not in st.session_state:
        st.session_state.party_filter = "All Parties"
    if "type_filter" not in st.session_state:
        st.session_state.type_filter = "All Types"

# Function to render overview points
def render_overview_points(overview):
    if not overview or "points" not in overview:
        return ""
    
    points_html = ""
    for point in overview["points"]:
        points_html += f'<li>{point}</li>'
    
    return f"""
    <div class="overview-points">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <h6 style="font-size: 0.9rem; font-weight: 500; margin: 0;">Key Points</h6>
            <span class="badge paragraph-badge">¶{overview["paragraphs"]}</span>
        </div>
        <ul class="argument-content">
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
        if point.get("is_disputed", False):
            disputed = '<span class="badge disputed-badge">Disputed</span>'
        
        regulations_html = ""
        for reg in point.get("regulations", []):
            regulations_html += f'<span class="badge legal-badge">{reg}</span>'
        
        points_html += f"""
        <div class="legal-point">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                <span class="badge legal-badge">Legal</span>
                {disputed}
            </div>
            <p style="font-size: 0.9rem; margin-bottom: 8px;">{point["point"]}</p>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {regulations_html}
                <span class="badge paragraph-badge">¶{point["paragraphs"]}</span>
            </div>
        </div>
        """
    
    return f"""
    <div style="margin-bottom: 16px;">
        <h6 style="font-size: 0.9rem; font-weight: 500; margin-bottom: 8px;">Legal Points</h6>
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
        if point.get("is_disputed", False):
            disputed = f'<span class="badge disputed-badge">Disputed by {point.get("source", "")}</span>'
        
        points_html += f"""
        <div class="factual-point">
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
                <span style="font-size: 0.8rem; color: #4A5568;">{point.get("date", "")}</span>
            </div>
            <p style="font-size: 0.9rem; margin-bottom: 8px;">{point["point"]}</p>
            <span class="badge paragraph-badge">¶{point["paragraphs"]}</span>
        </div>
        """
    
    return f"""
    <div style="margin-bottom: 16px;">
        <h6 style="font-size: 0.9rem; font-weight: 500; margin-bottom: 8px;">Factual Points</h6>
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
            citations_html += f'<span class="badge paragraph-badge">¶{citation}</span>'
        
        items_html += f"""
        <div class="evidence-item">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <p style="font-size: 0.9rem; font-weight: 500; margin-bottom: 4px;">{evidence["id"]}: {evidence["title"]}</p>
                    <p style="font-size: 0.8rem; color: #4A5568; margin-bottom: 8px;">{evidence["summary"]}</p>
                    <div>
                        <span style="font-size: 0.8rem; color: #4A5568;">Cited in: </span>
                        {citations_html}
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
        """
    
    return f"""
    <div style="margin-bottom: 16px;">
        <h6 style="font-size: 0.9rem; font-weight: 500; margin-bottom: 8px;">Evidence</h6>
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
        for para in case.get("cited_paragraphs", []):
            cited_paragraphs_html += f'<span class="badge paragraph-badge">¶{para}</span>'
        
        items_html += f"""
        <div class="evidence-item">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                        <p style="font-size: 0.9rem; font-weight: 500; margin: 0;">{case["case_number"]}</p>
                        <span class="badge paragraph-badge">¶{case["paragraphs"]}</span>
                    </div>
                    <p style="font-size: 0.8rem; color: #4A5568; margin-bottom: 8px;">{case["title"]}</p>
                    <p style="font-size: 0.9rem; margin-bottom: 8px;">{case["relevance"]}</p>
                    <div>
                        <span style="font-size: 0.8rem; color: #4A5568;">Key Paragraphs: </span>
                        {cited_paragraphs_html}
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
        """
    
    return f"""
    <div style="margin-bottom: 16px;">
        <h6 style="font-size: 0.9rem; font-weight: 500; margin-bottom: 8px;">Case Law</h6>
        {items_html}
    </div>
    """

# Create a custom HTML component for an argument
def argument_component(argument, side, level=0, show_connector=False):
    if not argument:
        return ""
    
    # Get expanded state key
    key = f"{side}_{argument['id']}"
    is_expanded = st.session_state.expanded.get(key, False)
    
    # Child arguments count
    child_count = len(argument.get("children", {}))
    
    # Styling based on side
    side_class = "claimant" if side == "claimant" else "respondent"
    badge_class = "claimant-badge" if side == "claimant" else "respondent-badge"
    
    # Chevron icon based on expanded state
    chevron = "down" if is_expanded else "right"
    
    # Generate content sections
    content = ""
    if is_expanded:
        if "overview" in argument:
            content += render_overview_points(argument["overview"])
        if "legal_points" in argument:
            content += render_legal_points(argument["legal_points"])
        if "factual_points" in argument:
            content += render_factual_points(argument["factual_points"])
        if "evidence" in argument:
            content += render_evidence(argument["evidence"])
        if "case_law" in argument:
            content += render_case_law(argument["case_law"])
    
    # Create HTML for argument header
    header = f"""
    <div class="argument-header {side_class}-header" id="{key}-header" onclick="toggleArgument('{key}')">
        <div style="display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" id="{key}-chevron" style="transform: rotate({0 if chevron == 'right' else 90}deg); transition: transform 0.2s;">
                <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
            <span style="font-size: 0.9rem; font-weight: 500; color: {("#3182CE" if side == "claimant" else "#E53E3E")}">
                {argument["id"]}. {argument["title"]}
            </span>
            {f'<span class="badge {badge_class}" style="margin-left: 6px;">{child_count} subarguments</span>' if child_count > 0 else f'<span class="badge paragraph-badge" style="margin-left: 6px;">¶{argument["paragraphs"]}</span>'}
        </div>
    </div>
    """
    
    # Create expandable content section
    content_section = f"""
    <div id="{key}-content" style="display: {'block' if is_expanded else 'none'}; padding: 16px; background-color: white; border-radius: 0 0 8px 8px; border: 1px solid #E2E8F0; border-top: none; margin-bottom: 12px;">
        {content}
    </div>
    """
    
    # Child arguments
    children_html = ""
    if is_expanded and child_count > 0:
        for child_id, child in argument.get("children", {}).items():
            child_class = f"{side_class}-child"
            connector_class = f"{side_class}-connector"
            
            children_html += f"""
            <div class="child-argument {child_class}">
                <div class="argument-connector {connector_class}">
                    <div class="connector-line"></div>
                    {argument_component(child, side, level + 1, True)}
                </div>
            </div>
            """
    
    # JavaScript for toggling arguments
    toggle_script = f"""
    <script>
    function toggleArgument(key) {{
        // Toggle content visibility
        const content = document.getElementById(key + '-content');
        const isVisible = content.style.display === 'block';
        content.style.display = isVisible ? 'none' : 'block';
        
        // Rotate chevron icon
        const chevron = document.getElementById(key + '-chevron');
        chevron.style.transform = isVisible ? 'rotate(0deg)' : 'rotate(90deg)';
        
        // Update session state via a fetch request
        fetch('/_stcore/component_communication', {{
            method: 'POST',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{ 
                name: 'toggle_argument', 
                args: [key.split('_')[1], key.split('_')[0]],
                key: Date.now().toString()
            }})
        }});
    }}
    </script>
    """
    
    # Combine everything
    return f"""
    <div class="argument-wrapper" id="{key}-wrapper" data-level="{level}">
        {header}
        {content_section}
        {children_html}
    </div>
    {toggle_script}
    """

# Function to render an argument pair
def render_argument_pair(claimant_arg, respondent_arg):
    # Create HTML
    html = f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
        <div>
            {argument_component(claimant_arg, "claimant", 0)}
        </div>
        <div>
            {argument_component(respondent_arg, "respondent", 0)}
        </div>
    </div>
    """
    
    # Use st.components to render custom HTML
    components.html(html, height=600, scrolling=True)

# Function to render arguments by topic
def render_topic_arguments(topics, claimant_args, respondent_args):
    for topic in topics:
        st.markdown(f"""
        <div class="topic-header">
            <h2 class="topic-title">{topic['title']}</h2>
            <p class="topic-description">{topic['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Render column headers for this topic
        st.markdown("""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 8px; padding: 0 16px;">
            <div>
                <h3 style="font-size: 1rem; font-weight: 500; color: #3182CE;">Claimant's Arguments</h3>
            </div>
            <div>
                <h3 style="font-size: 1rem; font-weight: 500; color: #E53E3E;">Respondent's Arguments</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Render argument pairs for this topic
        for arg_id in topic.get("argument_ids", []):
            if arg_id in claimant_args and arg_id in respondent_args:
                render_argument_pair(claimant_args[arg_id], respondent_args[arg_id])
        
        st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

# Function to create the Timeline view
def render_timeline(data, search_term="", show_disputed_only=False):
    # Filter data
    filtered_data = data.copy()
    
    if search_term:
        filtered_data = filtered_data[
            filtered_data["appellant_version"].str.contains(search_term, case=False, na=False) | 
            filtered_data["respondent_version"].str.contains(search_term, case=False, na=False)
        ]
    
    if show_disputed_only:
        filtered_data = filtered_data[filtered_data["status"] == "Disputed"]
    
    # Create HTML table
    rows = ""
    for _, row in filtered_data.iterrows():
        status_class = "status-disputed" if row["status"] == "Disputed" else "status-undisputed"
        row_class = "disputed-row" if row["status"] == "Disputed" else ""
        
        rows += f"""
        <tr class="{row_class}">
            <td>{row["date"]}</td>
            <td>{row["appellant_version"]}</td>
            <td>{row["respondent_version"]}</td>
            <td class="{status_class}">{row["status"]}</td>
        </tr>
        """
    
    html = f"""
    <table class="timeline-table" style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="padding: 12px; text-align: left; border-bottom: 1px solid #E2E8F0;">DATE</th>
                <th style="padding: 12px; text-align: left; border-bottom: 1px solid #E2E8F0;">APPELLANT'S VERSION</th>
                <th style="padding: 12px; text-align: left; border-bottom: 1px solid #E2E8F0;">RESPONDENT'S VERSION</th>
                <th style="padding: 12px; text-align: left; border-bottom: 1px solid #E2E8F0;">STATUS</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """
    
    components.html(html, height=400, scrolling=True)

# Function to create the Exhibits view
def render_exhibits(data, search_term="", party_filter="All Parties", type_filter="All Types"):
    # Filter data
    filtered_data = data.copy()
    
    if search_term:
        filtered_data = filtered_data[
            filtered_data["id"].str.contains(search_term, case=False, na=False) | 
            filtered_data["title"].str.contains(search_term, case=False, na=False) |
            filtered_data["summary"].str.contains(search_term, case=False, na=False)
        ]
    
    if party_filter != "All Parties":
        filtered_data = filtered_data[filtered_data["party"] == party_filter]
    
    if type_filter != "All Types":
        filtered_data = filtered_data[filtered_data["type"] == type_filter]
    
    # Create HTML table
    rows = ""
    for _, row in filtered_data.iterrows():
        party_class = "claimant-badge" if row["party"] == "Appellant" else "respondent-badge"
        
        rows += f"""
        <tr>
            <td>{row["id"]}</td>
            <td><span class="badge {party_class}">{row["party"]}</span></td>
            <td>{row["title"]}</td>
            <td><span class="badge paragraph-badge">{row["type"]}</span></td>
            <td>{row["summary"]}</td>
            <td><a href="#" style="color: #3182CE; text-decoration: none;">View</a></td>
        </tr>
        """
    
    html = f"""
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="padding: 12px; text-align: left; background-color: #F7FAFC; border-bottom: 1px solid #E2E8F0;">EXHIBIT ID</th>
                <th style="padding: 12px; text-align: left; background-color: #F7FAFC; border-bottom: 1px solid #E2E8F0;">PARTY</th>
                <th style="padding: 12px; text-align: left; background-color: #F7FAFC; border-bottom: 1px solid #E2E8F0;">TITLE</th>
                <th style="padding: 12px; text-align: left; background-color: #F7FAFC; border-bottom: 1px solid #E2E8F0;">TYPE</th>
                <th style="padding: 12px; text-align: left; background-color: #F7FAFC; border-bottom: 1px solid #E2E8F0;">SUMMARY</th>
                <th style="padding: 12px; text-align: left; background-color: #F7FAFC; border-bottom: 1px solid #E2E8F0;">ACTIONS</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """
    
    components.html(html, height=400, scrolling=True)

# Function to handle argument toggle
def toggle_argument(arg_id, side):
    key = f"{side}_{arg_id}"
    if key in st.session_state.expanded:
        st.session_state.expanded[key] = not st.session_state.expanded[key]
    else:
        st.session_state.expanded[key] = True

# Main app
def main():
    # Initialize session state
    init_session_state()
    
    # Register argument toggle handler
    components.declare_component("toggle_argument", toggle_argument)
    
    # Set app title
    st.title("Legal Arguments Analysis")
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])
    
    # Get data
    claimant_args, respondent_args, topics = get_argument_data()
    timeline_df = get_timeline_data()
    exhibits_df = get_exhibits_data()
    
    # Tab 1: Arguments
    with tab1:
        # View toggle buttons
        st.markdown("""
        <div class="view-toggle">
            <button id="standard-view" class="view-toggle-button active" onclick="setViewMode('default')">Standard View</button>
            <button id="topic-view" class="view-toggle-button" onclick="setViewMode('topic')">Topic View</button>
        </div>
        
        <script>
        function setViewMode(mode) {
            // Update button styles
            document.getElementById('standard-view').classList.toggle('active', mode === 'default');
            document.getElementById('topic-view').classList.toggle('active', mode === 'topic');
            
            // Update session state via fetch
            fetch('/_stcore/component_communication', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    name: 'set_view_mode', 
                    args: [mode],
                    key: Date.now().toString()
                })
            }).then(() => {
                // Reload the page to reflect the changes
                window.location.reload();
            });
        }
        </script>
        """, unsafe_allow_html=True)
        
        # Render arguments based on view mode
        if st.session_state.view_mode == "default":
            # Standard view - show side by side arguments
            for arg_id in claimant_args:
                if arg_id in respondent_args:
                    render_argument_pair(claimant_args[arg_id], respondent_args[arg_id])
        else:
            # Topic view - group by topic
            render_topic_arguments(topics, claimant_args, respondent_args)
    
    # Tab 2: Timeline
    with tab2:
        # Action buttons
        st.markdown("""
        <div class="action-buttons">
            <button class="action-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                Copy
            </button>
            <button class="action-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
                Export Data
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        # Search and filter controls
        col1, col2 = st.columns([4, 1])
        with col1:
            search_term = st.text_input("Search events...", key="timeline_search", value=st.session_state.timeline_search)
            st.session_state.timeline_search = search_term
        with col2:
            disputed_only = st.checkbox("Disputed events only", key="disputed_filter", value=st.session_state.disputed_only)
            st.session_state.disputed_only = disputed_only
        
        # Render timeline
        render_timeline(timeline_df, search_term, disputed_only)
    
    # Tab 3: Exhibits
    with tab3:
        # Action buttons
        st.markdown("""
        <div class="action-buttons">
            <button class="action-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                Copy
            </button>
            <button class="action-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
                Export Data
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        # Search and filter controls
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            search_term = st.text_input("Search exhibits...", key="exhibits_search", value=st.session_state.exhibits_search)
            st.session_state.exhibits_search = search_term
        with col2:
            party_filter = st.selectbox("Party", ["All Parties", "Appellant", "Respondent"], key="party_filter", index=["All Parties", "Appellant", "Respondent"].index(st.session_state.party_filter))
            st.session_state.party_filter = party_filter
        with col3:
            types = ["All Types"] + sorted(list(exhibits_df["type"].unique()))
            type_filter = st.selectbox("Type", types, key="type_filter", index=types.index(st.session_state.type_filter) if st.session_state.type_filter in types else 0)
            st.session_state.type_filter = type_filter
        
        # Render exhibits
        render_exhibits(exhibits_df, search_term, party_filter, type_filter)

if __name__ == "__main__":
    main()
