import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
def get_argument_data():
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
            "factualPoints": [
                {
                    "point": "Continuous operation under same name since 1950",
                    "date": "1950-present",
                    "isDisputed": False,
                    "paragraphs": "18-19",
                    "exhibits": ["C-1"]
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Historical Registration Documents",
                    "summary": "Official records showing continuous name usage from 1950 to present day. Includes original registration certificate dated January 12, 1950, and all subsequent renewal documentation without interruption.",
                    "citations": ["20", "21", "24"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2016/A/4576",
                    "title": "Criteria for sporting succession",
                    "relevance": "Establishes key factors for succession including: (1) continuous use of identifying elements, (2) public recognition of the entity's identity, (3) preservation of sporting records and achievements, and (4) consistent participation in competitions under the same identity.",
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration History",
                            "paragraphs": "25-30",
                            "factualPoints": [
                                {
                                    "point": "Initial registration in 1950",
                                    "date": "1950",
                                    "isDisputed": False,
                                    "paragraphs": "25-26",
                                    "exhibits": ["C-2"]
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30",
                                    "exhibits": ["C-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-2",
                                    "title": "Registration Records",
                                    "summary": "Comprehensive collection of official documentation showing the full registration history of the club from its founding to present day. Includes original application forms, government certificates, and renewal documentation.",
                                    "citations": ["25", "26", "28"]
                                }
                            ]
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
                    "factualPoints": [
                        {
                            "point": "Consistent use of blue and white since founding",
                            "date": "1950-present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "51-52",
                            "exhibits": ["C-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-4",
                            "title": "Historical Photographs",
                            "summary": "Collection of 73 photographs spanning from 1950 to present day showing the team's uniforms, promotional materials, and stadium decorations. Images are chronologically arranged and authenticated by sports historians.",
                            "citations": ["53", "54", "55"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Variations Analysis",
                            "paragraphs": "56-60",
                            "factualPoints": [
                                {
                                    "point": "Minor shade variations do not affect continuity",
                                    "date": "1970-1980",
                                    "isDisputed": False,
                                    "paragraphs": "56-57",
                                    "exhibits": ["C-5"]
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59",
                                    "exhibits": ["C-5"]
                                }
                            ],
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Historical Color Documentation",
                                    "paragraphs": "61-65",
                                    "evidence": [
                                        {
                                            "id": "C-5",
                                            "title": "Color Archives",
                                            "summary": "Detailed color specification documents from club archives, including official style guides, manufacturer specifications, and board meeting minutes about uniform decisions from 1950 to present day.",
                                            "citations": ["61", "62", "63"]
                                        }
                                    ]
                                }
                            }
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
            }
        }
    }
    
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
            "factualPoints": [
                {
                    "point": "Operations ceased between 1975-1976",
                    "date": "1975-1976",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "206-207",
                    "exhibits": ["R-1"]
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "Federation Records",
                    "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season. Includes official withdrawal notification dated May 15, 1975.",
                    "citations": ["208", "209", "210"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2017/A/5465",
                    "title": "Operational continuity requirement",
                    "relevance": "Establishes that actual operational continuity (specifically participation in competitions) is the primary determinant of sporting succession, outweighing factors such as name, colors, or stadium usage when they conflict. The panel specifically ruled that a gap in competitive activity creates a presumption against continuity that must be overcome with substantial evidence.",
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration Gap Evidence",
                            "paragraphs": "226-230",
                            "factualPoints": [
                                {
                                    "point": "Registration formally terminated on April 30, 1975",
                                    "date": "April 30, 1975",
                                    "isDisputed": False,
                                    "paragraphs": "226-227",
                                    "exhibits": ["R-2"]
                                },
                                {
                                    "point": "New entity registered on September 15, 1976",
                                    "date": "September 15, 1976",
                                    "isDisputed": False,
                                    "paragraphs": "228-229",
                                    "exhibits": ["R-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-2",
                                    "title": "Termination Certificate",
                                    "summary": "Official government certificate of termination for the original club entity, stamped and notarized on April 30, 1975, along with completely new registration documents for a separate legal entity filed on September 15, 1976, with different founding members and bylaws.",
                                    "citations": ["226", "227"]
                                }
                            ]
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
                    "factualPoints": [
                        {
                            "point": "Significant color scheme change in 1976",
                            "date": "1976",
                            "isDisputed": True,
                            "source": "Claimant",
                            "paragraphs": "245-246",
                            "exhibits": ["R-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-4",
                            "title": "Historical Photographs Comparison",
                            "summary": "Side-by-side comparison of team uniforms from 1974 (pre-dissolution) and 1976 (post-new registration), showing significant differences in shade, pattern, and design elements. Includes expert color analysis report from textile historian confirming different dye formulations were used.",
                            "citations": ["245", "246", "247"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Changes Analysis",
                            "paragraphs": "247-249",
                            "factualPoints": [
                                {
                                    "point": "Pre-1976 colors represented original city district",
                                    "date": "1950-1975",
                                    "isDisputed": False,
                                    "paragraphs": "247",
                                    "exhibits": ["R-5"]
                                },
                                {
                                    "point": "Post-1976 colors represented new ownership region",
                                    "date": "1976-present",
                                    "isDisputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "248-249",
                                    "exhibits": ["R-5"]
                                }
                            ],
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Color Identity Documentation",
                                    "paragraphs": "250-255",
                                    "evidence": [
                                        {
                                            "id": "R-5",
                                            "title": "Marketing Materials",
                                            "summary": "Collection of promotional materials, merchandise, and internal design documents from both pre-1975 and post-1976 periods, showing the deliberate change in color symbolism used in marketing campaigns and communications with fans.",
                                            "citations": ["250", "251", "252"]
                                        }
                                    ]
                                }
                            }
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
            }
        }
    }
    
    topics = [
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
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args,
        "topics": topics
    }

def get_timeline_data():
    return [
        {
            "date": "2023-01-15",
            "appellantVersion": "Contract signed with Club",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-03-20",
            "appellantVersion": "Player received notification of exclusion from team",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-03-22",
            "appellantVersion": "Player requested explanation",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-01",
            "appellantVersion": "Player sent termination letter",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-05",
            "appellantVersion": "—",
            "respondentVersion": "Club rejected termination as invalid",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-10",
            "appellantVersion": "Player was denied access to training facilities",
            "respondentVersion": "—",
            "status": "Disputed"
        },
        {
            "date": "2023-04-15",
            "appellantVersion": "—",
            "respondentVersion": "Club issued warning letter",
            "status": "Undisputed"
        },
        {
            "date": "2023-05-01",
            "appellantVersion": "Player filed claim with FIFA",
            "respondentVersion": "—",
            "status": "Undisputed"
        }
    ]

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

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    
    # Hide default Streamlit elements
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Create a single HTML component containing the full UI
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Base styling */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #fff;
            }}
            
            /* Search bar */
            .search-container {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 16px;
                margin-bottom: 20px;
            }}
            
            .search-bar {{
                display: flex;
                align-items: center;
                width: 100%;
                max-width: 1200px;
                border: 1px solid #e2e8f0;
                border-radius: 30px;
                padding: 0 16px;
                background-color: white;
            }}
            
            .search-input {{
                flex: 1;
                padding: 12px 8px;
                border: none;
                outline: none;
                font-size: 14px;
            }}
            
            .copy-button {{
                display: flex;
                align-items: center;
                padding: 8px 16px;
                margin-left: 16px;
                background-color: #f0f4ff;
                border: none;
                border-radius: 8px;
                color: #4f46e5;
                font-weight: 500;
                cursor: pointer;
            }}
            
            .copy-icon {{
                margin-right: 8px;
            }}
            
            /* Tab navigation */
            .tabs {{
                display: flex;
                border-bottom: 1px solid #e2e8f0;
                margin-bottom: 1.5rem;
            }}
            
            .tab {{
                padding: 1rem 1.5rem;
                font-weight: 500;
                color: #718096;
                cursor: pointer;
                position: relative;
            }}
            
            .tab:hover {{
                color: #4a5568;
            }}
            
            .tab.active {{
                color: #4f46e5;
                border-bottom: 2px solid #4f46e5;
            }}
            
            /* Tab content sections */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Section container */
            .section-container {{
                margin-bottom: 16px;
                border: 1px solid #f0f0f0;
                border-radius: 8px;
                overflow: hidden;
            }}
            
            .section-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 16px;
                background-color: #fff;
                border-bottom: 1px solid #f0f0f0;
                cursor: pointer;
            }}
            
            .section-title {{
                font-size: 18px;
                font-weight: 600;
                margin: 0;
            }}
            
            .section-tag {{
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 12px;
                background-color: #f7f7f7;
                color: #555;
            }}
            
            /* Positions container */
            .positions-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 32px;
                padding: 16px;
                background-color: white;
            }}
            
            .position-title {{
                font-size: 16px;
                margin-bottom: 16px;
            }}
            
            .appellant-color {{
                color: #4f46e5;
            }}
            
            .respondent-color {{
                color: #e11d48;
            }}
            
            .position-box {{
                background-color: #f9fafc;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 20px;
            }}
            
            /* Standard arguments view */
            .arguments-header {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
                margin-bottom: 1rem;
            }}
            
            .argument-pair {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
                margin-bottom: 1rem;
                position: relative;
            }}
            
            .argument-side {{
                position: relative;
            }}
            
            /* Argument card and details */
            .argument {{
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                overflow: hidden;
                margin-bottom: 1rem;
                box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            }}
            
            .argument-header {{
                padding: 0.75rem 1rem;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            
            .argument-header-left {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            
            .argument-content {{
                padding: 1rem;
                border-top: 1px solid #e2e8f0;
                display: none;
                background-color: white;
            }}
            
            .claimant-header {{
                background-color: #eff6ff;
                border-color: #bfdbfe;
            }}
            
            .respondent-header {{
                background-color: #fff1f2;
                border-color: #fecdd3;
            }}
            
            /* Child arguments container */
            .argument-children {{
                padding-left: 1.5rem;
                display: none;
                position: relative;
            }}
            
            /* Connector lines for tree structure */
            .connector-vertical {{
                position: absolute;
                left: 0.75rem;
                top: 0;
                width: 1px;
                height: 100%;
                background-color: #e2e8f0;
            }}
            
            .connector-horizontal {{
                position: absolute;
                left: 0.75rem;
                top: 1.25rem;
                width: 0.75rem;
                height: 1px;
                background-color: #e2e8f0;
            }}
            
            .claimant-connector {{
                background-color: rgba(79, 70, 229, 0.5);
            }}
            
            .respondent-connector {{
                background-color: rgba(225, 29, 72, 0.5);
            }}
            
            /* Badge styling */
            .badge {{
                display: inline-block;
                padding: 0.25rem 0.5rem;
                border-radius: 0.25rem;
                font-size: 0.75rem;
            }}
            
            .claimant-badge {{
                background-color: #eff6ff;
                color: #4f46e5;
            }}
            
            .respondent-badge {{
                background-color: #fff1f2;
                color: #e11d48;
            }}
            
            .exhibit-badge {{
                background-color: #fef3c7;
                color: #d97706;
                margin-right: 0.25rem;
            }}
            
            .disputed-badge {{
                background-color: #fee2e2;
                color: #b91c1c;
            }}
            
            .type-badge {{
                background-color: #f1f5f9;
                color: #64748b;
            }}
            
            /* Timeline & Exhibits tables */
            .data-table {{
                width: 100%;
                border-collapse: collapse;
                background-color: white;
                border-radius: 8px;
                overflow: hidden;
                border: 1px solid #e2e8f0;
                box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            }}
            
            .data-table th {{
                text-align: left;
                padding: 12px 16px;
                background-color: #f8fafc;
                font-weight: 500;
                color: #64748b;
                border-bottom: 1px solid #e2e8f0;
            }}
            
            .data-table td {{
                padding: 12px 16px;
                border-bottom: 1px solid #e2e8f0;
                font-size: 14px;
            }}
            
            .data-table tr:last-child td {{
                border-bottom: none;
            }}
            
            .undisputed {{
                color: #10b981;
            }}
            
            .disputed {{
                color: #ef4444;
            }}
            
            /* Support points list */
            .support-points-list {{
                list-style-type: none;
                padding-left: 0;
                margin-bottom: 20px;
            }}
            
            .support-point-item {{
                display: flex;
                margin-bottom: 8px;
                align-items: flex-start;
            }}
            
            .support-point-bullet {{
                margin-right: 12px;
                color: #a0aec0;
                flex-shrink: 0;
            }}
            
            /* Evidence section */
            .evidence-section {{
                margin-top: 16px;
            }}
            
            .evidence-item {{
                display: flex;
                align-items: center;
                margin-bottom: 8px;
            }}
            
            /* Case law section */
            .case-law-section {{
                margin-top: 16px;
            }}
            
            .case-law-item {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 8px;
            }}
            
            .copy-icon-small {{
                cursor: pointer;
                color: #a0aec0;
            }}
        </style>
    </head>
    <body>
        <!-- Search and Copy Bar -->
        <div class="search-container">
            <div class="search-bar">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" id="global-search" class="search-input" placeholder="Search issues, arguments, or evidence...">
            </div>
            <button class="copy-button">
                <div class="copy-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                </div>
                Copy All
            </button>
        </div>
        
        <!-- Tab Navigation -->
        <div class="tabs">
            <div class="tab active" data-tab="arguments">Summary of Arguments</div>
            <div class="tab" data-tab="timeline">Timeline</div>
            <div class="tab" data-tab="exhibits">Exhibits</div>
        </div>
        
        <!-- Arguments Tab -->
        <div id="arguments" class="tab-content active">
            <!-- CAS Jurisdiction Section -->
            <div class="section-container">
                <div class="section-header" onclick="toggleSection('jurisdiction')">
                    <h2 class="section-title">CAS Jurisdiction</h2>
                    <div class="section-tag">jurisdiction</div>
                </div>
                <div id="jurisdiction-content" class="positions-container">
                    <!-- Appellant's Position -->
                    <div>
                        <h3 class="position-title appellant-color">Appellant's Position</h3>
                        <div class="position-box">
                            <h4 style="margin-top: 0; font-size: 16px; margin-bottom: 16px;">CAS Has Authority to Hear This Case</h4>
                            
                            <div>
                                <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Supporting Points</h5>
                                <ul class="support-points-list">
                                    <li class="support-point-item">
                                        <span class="support-point-bullet">•</span>
                                        <span>The Federation's Anti-Doping Rules explicitly allow CAS to hear appeals</span>
                                    </li>
                                    <li class="support-point-item">
                                        <span class="support-point-bullet">•</span>
                                        <span>Athlete has completed all required internal appeal procedures first</span>
                                    </li>
                                    <li class="support-point-item">
                                        <span class="support-point-bullet">•</span>
                                        <span>Athlete signed agreement allowing CAS to handle disputes</span>
                                    </li>
                                </ul>
                            </div>
                            
                            <div class="evidence-section">
                                <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Evidence</h5>
                                <div class="evidence-item">
                                    <span class="badge claimant-badge" style="margin-right: 8px;">C1</span>
                                    <span>Federation Rules, Art. 60</span>
                                </div>
                                <div class="evidence-item">
                                    <span class="badge claimant-badge" style="margin-right: 8px;">C2</span>
                                    <span>Athlete's license containing arbitration agreement</span>
                                </div>
                                <div class="evidence-item">
                                    <span class="badge claimant-badge" style="margin-right: 8px;">C3</span>
                                    <span>Appeal submission documents</span>
                                </div>
                            </div>
                            
                            <div class="case-law-section">
                                <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Case Law</h5>
                                <div class="case-law-item">
                                    <span>CAS 2019/A/XYZ</span>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="copy-icon-small">
                                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Respondent's Position -->
                    <div>
                        <h3 class="position-title respondent-color">Respondent's Position</h3>
                        <div class="position-box">
                            <h4 style="margin-top: 0; font-size: 16px; margin-bottom: 16px;">CAS Cannot Hear This Case Yet</h4>
                            
                            <div>
                                <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Supporting Points</h5>
                                <ul class="support-points-list">
                                    <li class="support-point-item">
                                        <span class="support-point-bullet">•</span>
                                        <span>Athlete skipped required steps in federation's appeal process</span>
                                    </li>
                                    <li class="support-point-item">
                                        <span class="support-point-bullet">•</span>
                                        <span>Athlete missed important appeal deadlines within federation</span>
                                    </li>
                                    <li class="support-point-item">
                                        <span class="support-point-bullet">•</span>
                                        <span>Must follow proper appeal steps before going to CAS</span>
                                    </li>
                                </ul>
                            </div>
                            
                            <div class="evidence-section">
                                <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Evidence</h5>
                                <div class="evidence-item">
                                    <span class="badge respondent-badge" style="margin-right: 8px;">R1</span>
                                    <span>Federation internal appeals process documentation</span>
                                </div>
                                <div class="evidence-item">
                                    <span class="badge respondent-badge" style="margin-right: 8px;">R2</span>
                                    <span>Timeline of appeals process</span>
                                </div>
                                <div class="evidence-item">
                                    <span class="badge respondent-badge" style="margin-right: 8px;">R3</span>
                                    <span>Federation handbook on procedures</span>
                                </div>
                            </div>
                            
                            <div class="case-law-section">
                                <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Case Law</h5>
                                <div class="case-law-item">
                                    <span>CAS 2019/A/123</span>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="copy-icon-small">
                                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                    </svg>
                                </div>
                                <div class="case-law-item">
                                    <span>CAS 2018/A/456</span>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="copy-icon-small">
                                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Original Arguments Content -->
            <div class="arguments-header">
                <h3 class="appellant-color">Claimant's Arguments</h3>
                <h3 class="respondent-color">Respondent's Arguments</h3>
            </div>
            <div id="standard-arguments-container"></div>
        </div>
        
        <!-- Timeline Tab -->
        <div id="timeline" class="tab-content">
            <table id="timeline-table" class="data-table">
                <thead>
                    <tr>
                        <th>DATE</th>
                        <th>APPELLANT'S VERSION</th>
                        <th>RESPONDENT'S VERSION</th>
                        <th>STATUS</th>
                    </tr>
                </thead>
                <tbody id="timeline-body"></tbody>
            </table>
        </div>
        
        <!-- Exhibits Tab -->
        <div id="exhibits" class="tab-content">
            <table id="exhibits-table" class="data-table">
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
                <tbody id="exhibits-body"></tbody>
            </table>
        </div>
        
        <script>
            // Initialize data
            const argsData = {args_json};
            const timelineData = {timeline_json};
            const exhibitsData = {exhibits_json};
            
            // Keep track of expanded states - we'll use an object to track the state of each argument by its full path ID
            const expandedStates = {{}};
            
            // Toggle section
            function toggleSection(sectionId) {{
                const contentEl = document.getElementById(`${{sectionId}}-content`);
                const isExpanded = contentEl.style.display !== 'none';
                
                contentEl.style.display = isExpanded ? 'none' : 'grid';
            }}
            
            // Tab switching
            document.querySelectorAll('.tab').forEach(tab => {{
                tab.addEventListener('click', function() {{
                    // Update tabs
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Update content
                    const tabId = this.getAttribute('data-tab');
                    document.querySelectorAll('.tab-content').forEach(content => {{
                        content.style.display = 'none';
                    }});
                    document.getElementById(tabId).style.display = 'block';
                    
                    // Initialize content if needed
                    if (tabId === 'timeline') renderTimeline();
                    if (tabId === 'exhibits') renderExhibits();
                }});
            }});
            
            // Render overview points
            function renderOverviewPoints(overview) {{
                if (!overview || !overview.points || overview.points.length === 0) return '';
                
                const pointsHtml = overview.points.map(point => 
                    `<div class="support-point-item">
                        <span class="support-point-bullet">•</span>
                        <div>
                            <span>${{point}}</span>
                            <span class="badge claimant-badge">¶${{overview.paragraphs}}</span>
                        </div>
                    </div>`
                ).join('');
                
                return `
                <div>
                    <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Supporting Points</h5>
                    <div class="support-points-list">
                        ${{pointsHtml}}
                    </div>
                </div>
                `;
            }}
            
            // Render factual points
            function renderFactualPoints(points) {{
                if (!points || points.length === 0) return '';
                
                const pointsHtml = points.map(point => {{
                    const disputed = point.isDisputed 
                        ? `<span class="badge disputed-badge">Disputed by ${{point.source || ''}}</span>` 
                        : '';
                    
                    // Exhibits badges
                    const exhibitBadges = point.exhibits && point.exhibits.length > 0
                        ? point.exhibits.map(exhibitId => `<span class="badge exhibit-badge">${{exhibitId}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="support-point-item">
                        <span class="support-point-bullet">•</span>
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                                <span class="badge">Factual</span>
                                ${{disputed}}
                            </div>
                            <div style="font-size: 12px; color: #718096; margin-bottom: 4px;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: inline-block; vertical-align: middle; margin-right: 4px;">
                                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                    <line x1="16" y1="2" x2="16" y2="6"></line>
                                    <line x1="8" y1="2" x2="8" y2="6"></line>
                                    <line x1="3" y1="10" x2="21" y2="10"></line>
                                </svg>
                                ${{point.date}}
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                                <p style="margin: 0; font-size: 14px;">${{point.point}}</p>
                                <div style="margin-left: 8px; display: flex; gap: 4px;">
                                    ${{exhibitBadges}}
                                </div>
                            </div>
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Factual Points</h5>
                    <div class="support-points-list">
                        ${{pointsHtml}}
                    </div>
                </div>
                `;
            }}
            
            // Render evidence
            function renderEvidence(evidence) {{
                if (!evidence || evidence.length === 0) return '';
                
                const itemsHtml = evidence.map(item => {{
                    const citations = item.citations 
                        ? item.citations.map(cite => `<span class="badge" style="background-color: #f1f5f9; color: #64748b; margin-right: 4px;">¶${{cite}}</span>`).join('') 
                        : '';
                    
                    return `
                    <div class="evidence-item" style="margin-bottom: 12px;">
                        <span class="badge" style="background-color: #fef3c7; color: #d97706; margin-right: 8px;">${{item.id}}</span>
                        <div>
                            <div style="font-weight: 500;">${{item.title}}</div>
                            <p style="margin: 4px 0; font-size: 13px; color: #64748b;">${{item.summary}}</p>
                            <div>
                                <span style="font-size: 12px; color: #94a3b8;">Cited in:</span>
                                ${{citations}}
                            </div>
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Evidence</h5>
                    ${{itemsHtml}}
                </div>
                `;
            }}
            
            // Render case law
            function renderCaseLaw(cases) {{
                if (!cases || cases.length === 0) return '';
                
                const itemsHtml = cases.map(item => {{
                    const citedParagraphs = item.citedParagraphs 
                        ? item.citedParagraphs.map(para => `<span class="badge" style="background-color: #f1f5f9; color: #64748b; margin-right: 4px;">¶${{para}}</span>`).join('') 
                        : '';
                    
                    return `
                    <div class="case-law-item" style="margin-bottom: 12px;">
                        <div style="flex: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div style="font-weight: 500;">${{item.caseNumber}}</div>
                                <span style="font-size: 12px; color: #94a3b8;">¶${{item.paragraphs}}</span>
                            </div>
                            <p style="margin: 4px 0; font-size: 13px; font-weight: 500;">${{item.title}}</p>
                            <p style="margin: 4px 0; font-size: 13px; color: #4a5568;">${{item.relevance}}</p>
                            <div>
                                <span style="font-size: 12px; color: #94a3b8;">Key Paragraphs:</span>
                                ${{citedParagraphs}}
                            </div>
                        </div>
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="copy-icon-small">
                                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                            </svg>
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <h5 style="margin: 0 0 12px 0; font-size: 14px; font-weight: 500; color: #555;">Case Law</h5>
                    ${{itemsHtml}}
                </div>
                `;
            }}
            
            // Render argument content
            function renderArgumentContent(arg) {{
                let content = '';
                
                // Overview points
                if (arg.overview) {{
                    content += renderOverviewPoints(arg.overview);
                }}
                
                // Factual points
                if (arg.factualPoints) {{
                    content += renderFactualPoints(arg.factualPoints);
                }}
                
                // Evidence
                if (arg.evidence) {{
                    content += renderEvidence(arg.evidence);
                }}
                
                // Case law
                if (arg.caseLaw) {{
                    content += renderCaseLaw(arg.caseLaw);
                }}
                
                return content;
            }}
            
            // Render a single argument including its children
            function renderArgument(arg, side, path = '', level = 0) {{
                if (!arg) return '';
                
                const argId = path ? `${{path}}-${{arg.id}}` : arg.id;
                const fullId = `${{side}}-${{argId}}`;
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const childCount = hasChildren ? Object.keys(arg.children).length : 0;
                
                // Style based on side
                const baseColor = side === 'claimant' ? '#4f46e5' : '#e11d48';
                const headerClass = side === 'claimant' ? 'claimant-header' : 'respondent-header';
                const badgeClass = side === 'claimant' ? 'claimant-badge' : 'respondent-badge';
                const connectorClass = side === 'claimant' ? 'claimant-connector' : 'respondent-connector';
                
                // Header content
                const headerHtml = `
                <div class="argument-header-left">
                    <svg id="chevron-${{fullId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s ease;">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                    <h5 style="font-size: 0.875rem; font-weight: 500; color: ${{baseColor}}; margin: 0;">
                        ${{arg.id}}. ${{arg.title}}
                    </h5>
                </div>
                <div>
                    ${{hasChildren 
                        ? `<span class="badge ${{badgeClass}}" style="border-radius: 9999px;">${{childCount}} subarguments</span>` 
                        : `<span class="badge ${{badgeClass}}">¶${{arg.paragraphs}}</span>`
                    }}
                </div>
                `;
                
                // Detailed content
                const contentHtml = renderArgumentContent(arg);
                
                // Child arguments
                let childrenHtml = '';
                if (hasChildren) {{
                    const childrenArgs = Object.entries(arg.children).map(([childId, child]) => {{
                        // Pass the full path for this argument's children
                        return renderArgument(child, side, argId, level + 1);
                    }}).join('');
                    
                    childrenHtml = `
                    <div id="children-${{fullId}}" class="argument-children">
                        <div class="connector-vertical ${{connectorClass}}"></div>
                        ${{childrenArgs}}
                    </div>
                    `;
                }}
                
                // Complete argument HTML
                return `
                <div class="argument ${{headerClass}}" style="${{level > 0 ? 'position: relative;' : ''}}">
                    ${{level > 0 ? `<div class="connector-horizontal ${{connectorClass}}"></div>` : ''}}
                    <div class="argument-header" onclick="toggleArgument('${{fullId}}', '${{argId}}')">
                        ${{headerHtml}}
                    </div>
                    <div id="content-${{fullId}}" class="argument-content">
                        ${{contentHtml}}
                    </div>
                    ${{childrenHtml}}
                </div>
                `;
            }}
            
            // Render a pair of arguments (claimant and respondent)
            function renderArgumentPair(claimantArg, respondentArg, topLevel = true) {{
                return `
                <div class="argument-pair">
                    <div class="argument-side">
                        ${{renderArgument(claimantArg, 'claimant')}}
                    </div>
                    <div class="argument-side">
                        ${{renderArgument(respondentArg, 'respondent')}}
                    </div>
                </div>
                `;
            }}
            
            // Render the standard arguments view
            function renderStandardArguments() {{
                const container = document.getElementById('standard-arguments-container');
                let html = '';
                
                // For each top-level argument
                Object.keys(argsData.claimantArgs).forEach(argId => {{
                    if (argsData.respondentArgs[argId]) {{
                        const claimantArg = argsData.claimantArgs[argId];
                        const respondentArg = argsData.respondentArgs[argId];
                        
                        html += renderArgumentPair(claimantArg, respondentArg);
                    }}
                }});
                
                container.innerHTML = html;
            }}
            
            // Toggle argument expansion - updated to handle nested paths
            function toggleArgument(fullId, argPath) {{
                // Determine the side (claimant or respondent)
                const [side, ...rest] = fullId.split('-');
                
                // Toggle this argument
                const contentEl = document.getElementById(`content-${{fullId}}`);
                const childrenEl = document.getElementById(`children-${{fullId}}`);
                const chevronEl = document.getElementById(`chevron-${{fullId}}`);
                
                const isExpanded = contentEl.style.display === 'block';
                contentEl.style.display = isExpanded ? 'none' : 'block';
                if (chevronEl) {{
                    chevronEl.style.transform = isExpanded ? '' : 'rotate(90deg)';
                }}
                if (childrenEl) {{
                    childrenEl.style.display = isExpanded ? 'none' : 'block';
                }}
                
                // Save expanded state
                expandedStates[fullId] = !isExpanded;
                
                // Find and toggle the paired argument based on the path
                const otherSide = side === 'claimant' ? 'respondent' : 'claimant';
                const pairedId = `${{otherSide}}-${{argPath}}`;
                
                const pairedContentEl = document.getElementById(`content-${{pairedId}}`);
                const pairedChildrenEl = document.getElementById(`children-${{pairedId}}`);
                const pairedChevronEl = document.getElementById(`chevron-${{pairedId}}`);
                
                if (pairedContentEl) {{
                    pairedContentEl.style.display = contentEl.style.display;
                    expandedStates[pairedId] = expandedStates[fullId];
                }}
                
                if (pairedChevronEl) {{
                    pairedChevronEl.style.transform = chevronEl.style.transform;
                }}
                
                if (pairedChildrenEl) {{
                    pairedChildrenEl.style.display = isExpanded ? 'none' : 'block';
                }}
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                
                // Clear existing content
                tbody.innerHTML = '';
                
                // Render rows
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    
                    if (item.status === 'Disputed') {{
                        row.classList.add('disputed-row');
                    }}
                    
                    row.innerHTML = `
                        <td>${{item.date}}</td>
                        <td>${{item.appellantVersion}}</td>
                        <td>${{item.respondentVersion}}</td>
                        <td class="${{item.status.toLowerCase()}}">${{item.status}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Render exhibits
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                
                // Clear existing content
                tbody.innerHTML = '';
                
                // Render rows
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Appellant' ? 'claimant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td><span class="badge ${{badgeClass}}">${{item.id}}</span></td>
                        <td>${{item.party}}</td>
                        <td>${{item.title}}</td>
                        <td><span class="badge type-badge">${{item.type}}</span></td>
                        <td>${{item.summary}}</td>
                        <td style="text-align: right;"><a href="#" style="color: #4f46e5; text-decoration: none;">View</a></td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the page
            document.addEventListener('DOMContentLoaded', function() {{
                // Set up search functionality
                document.getElementById('global-search').addEventListener('input', function(e) {{
                    const searchTerm = e.target.value.toLowerCase();
                    // Implement search highlighting or filtering here
                }});
                
                // Initialize arguments
                renderStandardArguments();
                
                // Initialize tables
                renderTimeline();
                renderExhibits();
            }});
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
