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
                padding: 20px;
                background-color: #fff;
            }}
            
            /* Tab navigation */
            .tabs {{
                display: flex;
                border-bottom: 1px solid #e2e8f0;
                margin-bottom: 24px;
            }}
            
            .tab {{
                padding: 12px 24px;
                font-weight: 500;
                color: #64748b;
                cursor: pointer;
                position: relative;
            }}
            
            .tab:hover {{
                color: #334155;
            }}
            
            .tab.active {{
                color: #4361EE;
                border-bottom: 2px solid #4361EE;
            }}
            
            /* Tab content */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Main container */
            .main-container {{
                display: flex;
                flex-direction: column;
            }}
            
            /* Columns layout */
            .columns {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 24px;
            }}
            
            /* Argument headings */
            .column-heading {{
                font-size: 18px;
                font-weight: 600;
                margin-bottom: 16px;
            }}
            
            .claimant-color {{
                color: #4361EE;
            }}
            
            .respondent-color {{
                color: #E63946;
            }}
            
            /* Argument sections */
            .argument {{
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                margin-bottom: 16px;
                overflow: hidden;
            }}
            
            .argument-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 16px;
                cursor: pointer;
            }}
            
            .argument-title {{
                display: flex;
                align-items: center;
                gap: 8px;
                font-weight: 500;
            }}
            
            .chevron {{
                transition: transform 0.2s;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            .subarg-badge {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 16px;
                font-size: 12px;
                font-weight: normal;
                background-color: #EFF6FF;
                color: #4361EE;
            }}
            
            .resp-subarg-badge {{
                background-color: #FEF2F2;
                color: #E63946;
            }}
            
            .argument-content {{
                padding: 16px;
                border-top: 1px solid #e2e8f0;
                display: none;
            }}
            
            /* Section styles */
            .section-title {{
                font-size: 16px;
                font-weight: 500;
                margin-bottom: 12px;
            }}
            
            /* Points list */
            .points-list {{
                list-style-type: none;
                padding-left: 0;
                margin-bottom: 24px;
            }}
            
            .point-item {{
                display: flex;
                margin-bottom: 8px;
                align-items: flex-start;
            }}
            
            .point-marker {{
                color: #4361EE;
                margin-right: 8px;
                flex-shrink: 0;
            }}
            
            .resp-point-marker {{
                color: #E63946;
            }}
            
            /* Paragraph references */
            .para-ref {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 12px;
                background-color: #EFF6FF;
                color: #4361EE;
                margin-left: 8px;
            }}
            
            .resp-para-ref {{
                background-color: #FEF2F2;
                color: #E63946;
            }}
            
            /* Legal points */
            .legal-tag {{
                display: inline-block;
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 4px;
                background-color: #F3F4F6;
                color: #6B7280;
                margin-bottom: 8px;
            }}
            
            .legal-content {{
                background-color: #F9FAFB;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 24px;
            }}
            
            .legal-text {{
                font-size: 15px;
                margin-bottom: 8px;
            }}
            
            .case-number {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-size: 14px;
                color: #6B7280;
            }}
            
            /* Factual points */
            .factual-tag {{
                display: inline-block;
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 4px;
                background-color: #ECFDF5;
                color: #059669;
                margin-bottom: 8px;
            }}
            
            .date-tag {{
                display: inline-flex;
                align-items: center;
                font-size: 12px;
                color: #6B7280;
                margin-bottom: 8px;
            }}
            
            .calendar-icon {{
                margin-right: 4px;
            }}
            
            .factual-content {{
                background-color: #F0FDF4;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 24px;
            }}
            
            .disputed-tag {{
                display: inline-block;
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 4px;
                background-color: #FEE2E2;
                color: #B91C1C;
                margin-left: 8px;
            }}
            
            /* Evidence */
            .evidence-section {{
                margin-bottom: 24px;
            }}
            
            .evidence-item {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 16px;
            }}
            
            .evidence-title {{
                display: flex;
                align-items: center;
                gap: 8px;
                font-weight: 500;
            }}
            
            .evidence-description {{
                font-size: 14px;
                color: #6B7280;
                margin-top: 4px;
            }}
            
            .citation-list {{
                display: flex;
                gap: 4px;
                margin-top: 8px;
                flex-wrap: wrap;
            }}
            
            .citation {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 12px;
                background-color: #F3F4F6;
                color: #6B7280;
            }}
        </style>
    </head>
    <body>
        <!-- Tab Navigation -->
        <div class="tabs">
            <div class="tab active" data-tab="arguments">Summary of Arguments</div>
            <div class="tab" data-tab="timeline">Timeline</div>
            <div class="tab" data-tab="exhibits">Exhibits</div>
        </div>
        
        <!-- Arguments Tab -->
        <div id="arguments" class="tab-content active">
            <div class="main-container">
                <div class="columns">
                    <div>
                        <h2 class="column-heading claimant-color">Claimant's Arguments</h2>
                    </div>
                    <div>
                        <h2 class="column-heading respondent-color">Respondent's Arguments</h2>
                    </div>
                </div>
                
                <div class="columns">
                    <!-- Claimant Arguments -->
                    <div>
                        <div class="argument">
                            <div class="argument-header" onclick="toggleArgument('claimant-1')">
                                <div class="argument-title">
                                    <svg class="chevron" id="chevron-claimant-1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    <span>1. Sporting Succession</span>
                                </div>
                                <span class="subarg-badge">2 subarguments</span>
                            </div>
                            <div id="content-claimant-1" class="argument-content">
                                <div class="section">
                                    <h3 class="section-title">Key Points</h3>
                                    <ul class="points-list">
                                        <li class="point-item">
                                            <span class="point-marker">•</span>
                                            <span>Analysis of multiple established criteria <span class="para-ref">¶15-16</span></span>
                                        </li>
                                        <li class="point-item">
                                            <span class="point-marker">•</span>
                                            <span>Focus on continuous use of identifying elements</span>
                                        </li>
                                        <li class="point-item">
                                            <span class="point-marker">•</span>
                                            <span>Public recognition assessment</span>
                                        </li>
                                    </ul>
                                </div>
                                
                                <div class="section">
                                    <h3 class="section-title">Legal Points</h3>
                                    <div>
                                        <span class="legal-tag">Legal</span>
                                        <div class="legal-content">
                                            <p class="legal-text">CAS jurisprudence establishes criteria for sporting succession</p>
                                            <div class="case-number">
                                                <span>CAS 2016/A/4576</span>
                                                <span class="para-ref">¶15-17</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="section">
                                    <h3 class="section-title">Factual Points</h3>
                                    <div>
                                        <span class="factual-tag">Factual</span>
                                        <span class="date-tag">
                                            <svg class="calendar-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                                <line x1="3" y1="10" x2="21" y2="10"></line>
                                            </svg>
                                            1950-present
                                        </span>
                                        <div class="factual-content">
                                            <p>Continuous operation under same name since 1950</p>
                                            <span class="para-ref">¶18-19</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="section evidence-section">
                                    <h3 class="section-title">Evidence</h3>
                                    <div class="evidence-item">
                                        <div>
                                            <div class="evidence-title">
                                                <span>C-1: Historical Registration Documents</span>
                                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                                </svg>
                                            </div>
                                            <p class="evidence-description">Official records showing continuous name usage</p>
                                            <div class="citation-list">
                                                <span>Cited in:</span>
                                                <span class="citation">¶20</span>
                                                <span class="citation">¶21</span>
                                                <span class="citation">¶24</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Respondent Arguments -->
                    <div>
                        <div class="argument">
                            <div class="argument-header" onclick="toggleArgument('respondent-1')">
                                <div class="argument-title">
                                    <svg class="chevron" id="chevron-respondent-1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    <span>1. Sporting Succession Rebuttal</span>
                                </div>
                                <span class="subarg-badge resp-subarg-badge">2 subarguments</span>
                            </div>
                            <div id="content-respondent-1" class="argument-content">
                                <div class="section">
                                    <h3 class="section-title">Key Points</h3>
                                    <ul class="points-list">
                                        <li class="point-item">
                                            <span class="point-marker resp-point-marker">•</span>
                                            <span>Challenge to claimed continuity of operations <span class="para-ref resp-para-ref">¶200-202</span></span>
                                        </li>
                                        <li class="point-item">
                                            <span class="point-marker resp-point-marker">•</span>
                                            <span>Analysis of discontinuities in club operations</span>
                                        </li>
                                        <li class="point-item">
                                            <span class="point-marker resp-point-marker">•</span>
                                            <span>Dispute over public recognition factors</span>
                                        </li>
                                    </ul>
                                </div>
                                
                                <div class="section">
                                    <h3 class="section-title">Legal Points</h3>
                                    <div>
                                        <span class="legal-tag">Legal</span>
                                        <div class="legal-content">
                                            <p class="legal-text">CAS jurisprudence requires operational continuity not merely identification</p>
                                            <div class="case-number">
                                                <span>CAS 2017/A/5465</span>
                                                <span class="para-ref resp-para-ref">¶203-205</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="section">
                                    <h3 class="section-title">Factual Points</h3>
                                    <div>
                                        <span class="factual-tag">Factual</span>
                                        <span class="date-tag">
                                            <svg class="calendar-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                                <line x1="3" y1="10" x2="21" y2="10"></line>
                                            </svg>
                                            1975-1976
                                        </span>
                                        <span class="disputed-tag">Disputed by Claimant</span>
                                        <div class="factual-content">
                                            <p>Operations ceased between 1975-1976</p>
                                            <span class="para-ref resp-para-ref">¶206-207</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="section evidence-section">
                                    <h3 class="section-title">Evidence</h3>
                                    <div class="evidence-item">
                                        <div>
                                            <div class="evidence-title">
                                                <span>R-1: Federation Records</span>
                                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                                </svg>
                                            </div>
                                            <p class="evidence-description">Records showing non-participation in 1975-1976 season</p>
                                            <div class="citation-list">
                                                <span>Cited in:</span>
                                                <span class="citation">¶208</span>
                                                <span class="citation">¶209</span>
                                                <span class="citation">¶210</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
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
                        <th>ACTIONS</th>
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
            
            // Toggle argument expansion
            function toggleArgument(id) {{
                const contentEl = document.getElementById(`content-${{id}}`);
                const chevronEl = document.getElementById(`chevron-${{id}}`);
                
                if (contentEl.style.display === 'block') {{
                    contentEl.style.display = 'none';
                    chevronEl.classList.remove('expanded');
                }} else {{
                    contentEl.style.display = 'block';
                    chevronEl.classList.add('expanded');
                }}
                
                // If this is a claimant/respondent pair, toggle the other side too
                const isClaimant = id.startsWith('claimant');
                const argNum = id.split('-')[1];
                const pairedId = isClaimant ? `respondent-${{argNum}}` : `claimant-${{argNum}}`;
                
                const pairedContentEl = document.getElementById(`content-${{pairedId}}`);
                const pairedChevronEl = document.getElementById(`chevron-${{pairedId}}`);
                
                if (pairedContentEl) {{
                    pairedContentEl.style.display = contentEl.style.display;
                    
                    if (contentEl.style.display === 'block') {{
                        pairedChevronEl.classList.add('expanded');
                    }} else {{
                        pairedChevronEl.classList.remove('expanded');
                    }}
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
                        <td>${{item.status}}</td>
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
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td>${{item.party}}</td>
                        <td>${{item.title}}</td>
                        <td>${{item.type}}</td>
                        <td>${{item.summary}}</td>
                        <td><a href="#">View</a></td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
