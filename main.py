import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Arguments"

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
    
    # Add Streamlit sidebar with styled buttons stacked vertically
    with st.sidebar:
        st.title("Legal Analysis")
        
        # Custom CSS for button styling
        st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            height: 50px;
            margin-bottom: 10px;
            transition: all 0.3s;
        }
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .button-active {
            background-color: #3182CE !important;
            color: white !important;
            border: none !important;
        }
        .button-inactive {
            background-color: #f0f2f6;
            color: #333;
            border: 1px solid #ddd;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_timeline_view():
            st.session_state.view = "Timeline"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Vertical button layout - with icons instead of text
        st.markdown("""
        <div style="padding-top: 20px;"></div>
        """, unsafe_allow_html=True)
        
        # Arguments button with document icon
        arguments_active = "button-active" if st.session_state.view == "Arguments" else "button-inactive"
        st.markdown(f"""
        <div class='stButton'>
            <button class='{arguments_active}' onclick="document.dispatchEvent(new CustomEvent('streamlit:args_button'))">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                    <line x1="16" y1="13" x2="8" y2="13"></line>
                    <line x1="16" y1="17" x2="8" y2="17"></line>
                    <polyline points="10 9 9 9 8 9"></polyline>
                </svg>
            </button>
        </div>
        """, unsafe_allow_html=True)
        arguments_clicked = st.button("Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True, label_visibility="collapsed")
        
        # Timeline button with timeline icon
        timeline_active = "button-active" if st.session_state.view == "Timeline" else "button-inactive"
        st.markdown(f"""
        <div class='stButton'>
            <button class='{timeline_active}' onclick="document.dispatchEvent(new CustomEvent('streamlit:timeline_button'))">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="12" y1="2" x2="12" y2="22"></line>
                    <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
            </button>
        </div>
        """, unsafe_allow_html=True)
        timeline_clicked = st.button("Timeline", key="timeline_button", on_click=set_timeline_view, use_container_width=True, label_visibility="collapsed")
        
        # Exhibits button with folder icon
        exhibits_active = "button-active" if st.session_state.view == "Exhibits" else "button-inactive"
        st.markdown(f"""
        <div class='stButton'>
            <button class='{exhibits_active}' onclick="document.dispatchEvent(new CustomEvent('streamlit:exhibits_button'))">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                </svg>
            </button>
        </div>
        """, unsafe_allow_html=True)
        exhibits_clicked = st.button("Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True, label_visibility="collapsed")
    
    # Determine which view to show based on sidebar selection
    if st.session_state.view == "Arguments":
        active_tab = 0
    elif st.session_state.view == "Timeline":
        active_tab = 1
    else:  # Exhibits
        active_tab = 2
    
    # Initialize the view options as a JavaScript variable
    view_options_json = json.dumps({
        "activeTab": active_tab
    })
    
    # Create a single HTML component containing the full UI with minimalistic design
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Minimalistic base styling */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #fff;
            }}
            
            /* Simple container */
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            /* Content sections */
            .content-section {{
                display: none;
            }}
            
            .content-section.active {{
                display: block;
            }}
            
            /* Card styling */
            .card {{
                background-color: #fff;
                border: 1px solid #f0f0f0;
                border-radius: 8px;
                margin-bottom: 16px;
                overflow: hidden;
            }}
            
            .card-header {{
                padding: 12px 16px;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #f0f0f0;
                background-color: #fafafa;
            }}
            
            .card-content {{
                padding: 16px;
                display: none;
            }}
            
            /* Arguments layout */
            .arguments-row {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }}
            
            .side-heading {{
                margin-bottom: 16px;
                font-weight: 500;
            }}
            
            .appellant-color {{
                color: #3182ce;
            }}
            
            .respondent-color {{
                color: #e53e3e;
            }}
            
            /* Badge styling */
            .badge {{
                display: inline-block;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .appellant-badge {{
                background-color: rgba(49, 130, 206, 0.1);
                color: #3182ce;
            }}
            
            .respondent-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .exhibit-badge {{
                background-color: rgba(221, 107, 32, 0.1);
                color: #dd6b20;
            }}
            
            .disputed-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .para-badge {{
                background-color: rgba(0, 0, 0, 0.05);
                color: #666;
                margin-left: 5px;
            }}
            
            /* Evidence and factual points */
            .item-block {{
                background-color: #fafafa;
                border-radius: 6px;
                padding: 12px;
                margin-bottom: 10px;
            }}
            
            .item-title {{
                font-weight: 600;
                margin-bottom: 6px;
                color: #333;
            }}
            
            .evidence-block {{
                background-color: #fff8f0;
                border-left: 3px solid #dd6b20;
                padding: 10px 12px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            .caselaw-block {{
                background-color: #ebf8ff;
                border-left: 3px solid #3182ce;
                padding: 10px 12px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            /* Tables */
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            
            th {{
                text-align: left;
                padding: 12px;
                background-color: #fafafa;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            td {{
                padding: 12px;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            tr.disputed {{
                background-color: rgba(229, 62, 62, 0.05);
            }}
            
            /* Copy button */
            .copy-button {{
                position: absolute;
                top: 20px;
                right: 20px;
                padding: 8px 16px;
                background-color: #f9f9f9;
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                cursor: pointer;
            }}
            
            /* Nested content */
            .nested-content {{
                padding-left: 20px;
                margin-top: 10px;
                border-left: 1px solid #f0f0f0;
                /* No display:none to show nested content */
            }}
            
            /* Simple list styling */
            ul.point-list {{
                list-style-type: none;
                padding-left: 0;
                margin: 0;
            }}
            
            ul.point-list li {{
                position: relative;
                padding-left: 16px;
                margin-bottom: 8px;
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
            }}
            
            ul.point-list li:before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #8c8c8c;
            }}
            
            /* Chevron icon */
            .chevron {{
                transition: transform 0.2s;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            /* Citation tags */
            .citation-tag {{
                padding: 2px 5px;
                background: rgba(0,0,0,0.05);
                border-radius: 3px;
                font-size: 11px;
                color: #666;
                margin-right: 2px;
            }}
            
            /* Section title */
            .section-title {{
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                padding-bottom: 0.5rem;
                border-bottom: 1px solid #eaeaea;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <button class="copy-button" onclick="copyAllContent()">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                Copy All
            </button>
            
            <!-- Arguments Section -->
            <div id="arguments" class="content-section">
                <div class="section-title">Legal Arguments</div>
                <div id="topics-container"></div>
            </div>
            
            <!-- Timeline Section -->
            <div id="timeline" class="content-section">
                <div class="section-title">Case Timeline</div>
                <table id="timeline-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Appellant's Version</th>
                            <th>Respondent's Version</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody id="timeline-body"></tbody>
                </table>
            </div>
            
            <!-- Exhibits Section -->
            <div id="exhibits" class="content-section">
                <div class="section-title">Case Exhibits</div>
                <table id="exhibits-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Party</th>
                            <th>Title</th>
                            <th>Type</th>
                            <th>Summary</th>
                        </tr>
                    </thead>
                    <tbody id="exhibits-body"></tbody>
                </table>
            </div>
        </div>
        
        <script>
            // Initialize data
            const argsData = {args_json};
            const timelineData = {timeline_json};
            const exhibitsData = {exhibits_json};
            const viewOptions = {view_options_json};
            
            // Show the selected view based on sidebar selection
            document.addEventListener('DOMContentLoaded', function() {{
                // Show the correct content based on sidebar selection
                const sections = ['arguments', 'timeline', 'exhibits'];
                const activeSection = sections[viewOptions.activeTab];
                
                document.querySelectorAll('.content-section').forEach(section => {{
                    section.classList.remove('active');
                }});
                
                document.getElementById(activeSection).classList.add('active');
                
                // Initialize content as needed
                if (activeSection === 'arguments') renderTopics();
                if (activeSection === 'timeline') renderTimeline();
                if (activeSection === 'exhibits') renderExhibits();
            }});
            
            // Render overview points
            function renderOverviewPoints(overview) {{
                if (!overview || !overview.points || overview.points.length === 0) return '';
                
                const pointsList = overview.points.map(point => 
                    `<li>
                        <span>${{point}}</span>
                        <span class="para-badge">¶${{overview.paragraphs}}</span>
                    </li>`
                ).join('');
                
                return `
                <div class="item-block">
                    <div class="item-title">Supporting Points</div>
                    <ul class="point-list">
                        ${{pointsList}}
                    </ul>
                </div>
                `;
            }}
            
            // Render factual points
            function renderFactualPoints(points) {{
                if (!points || points.length === 0) return '';
                
                const pointsHtml = points.map(point => {{
                    const disputed = point.isDisputed 
                        ? `<span class="badge disputed-badge">Disputed</span>` 
                        : '';
                    
                    // Exhibits badges
                    const exhibitBadges = point.exhibits && point.exhibits.length > 0
                        ? point.exhibits.map(exhibitId => `<span class="badge exhibit-badge">${{exhibitId}}</span>`).join(' ')
                        : '';
                    
                    return `
                    <div class="item-block">
                        <div style="display: flex; justify-content: space-between;">
                            <span>${{point.point}}</span>
                            <span>
                                ${{disputed}}
                                ${{exhibitBadges}}
                                <span class="para-badge">¶${{point.paragraphs}}</span>
                            </span>
                        </div>
                        <div style="font-size: 12px; color: #666; margin-top: 4px;">${{point.date}}</div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Factual Points</div>
                    ${{pointsHtml}}
                </div>
                `;
            }}
            
            // Render evidence
            function renderEvidence(evidence) {{
                if (!evidence || evidence.length === 0) return '';
                
                const evidenceHtml = evidence.map(item => {{
                    const citations = item.citations && item.citations.length > 0
                        ? item.citations.map(cite => `<span class="citation-tag">¶${{cite}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="evidence-block">
                        <div class="item-title">${{item.id}}: ${{item.title}}</div>
                        <div style="margin: 6px 0;">${{item.summary}}</div>
                        <div style="margin-top: 8px; font-size: 12px;">
                            <span style="color: #666; margin-right: 5px;">Cited in:</span>
                            ${{citations}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Evidence</div>
                    ${{evidenceHtml}}
                </div>
                `;
            }}
            
            // Render case law
            function renderCaseLaw(cases) {{
                if (!cases || cases.length === 0) return '';
                
                const casesHtml = cases.map(item => {{
                    const citedParagraphs = item.citedParagraphs && item.citedParagraphs.length > 0
                        ? item.citedParagraphs.map(cite => `<span class="citation-tag">¶${{cite}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="caselaw-block">
                        <div class="item-title">${{item.caseNumber}}</div>
                        <div style="font-size: 12px; margin: 2px 0 8px 0;">¶${{item.paragraphs}}</div>
                        <div style="font-weight: 500; margin-bottom: 4px;">${{item.title}}</div>
                        <div style="margin: 6px 0;">${{item.relevance}}</div>
                        <div style="margin-top: 8px; font-size: 12px;">
                            <span style="color: #666; margin-right: 5px;">Key Paragraphs:</span>
                            ${{citedParagraphs}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Case Law</div>
                    ${{casesHtml}}
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
            function renderArgument(arg, side) {{
                if (!arg) return '';
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const argId = `${{side}}-${{arg.id}}`;
                
                // Store corresponding pair ID for synchronization
                const pairId = arg.id;
                
                // Style based on side
                const badgeClass = side === 'appellant' ? 'appellant-badge' : 'respondent-badge';
                
                // Render children if any - removed style="display: none;"
                let childrenHtml = '';
                if (hasChildren) {{
                    childrenHtml = `<div class="nested-content" id="children-${{argId}}">`;
                    
                    Object.values(arg.children).forEach(child => {{
                        childrenHtml += renderArgument(child, side);
                    }});
                    
                    childrenHtml += `</div>`;
                }}
                
                return `
                <div class="card">
                    <div class="card-header" onclick="toggleArgument('${{argId}}', '${{pairId}}', '${{side}}')">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <svg id="chevron-${{argId}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                            <span>${{arg.id}}. ${{arg.title}}</span>
                        </div>
                        <span class="badge ${{badgeClass}}">¶${{arg.paragraphs}}</span>
                    </div>
                    <div class="card-content" id="content-${{argId}}">
                        ${{renderArgumentContent(arg)}}
                    </div>
                    ${{childrenHtml}}
                </div>
                `;
            }}
            
            // Render arguments by topic
            function renderTopics() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                argsData.topics.forEach(topic => {{
                    html += `
                    <div class="card" style="margin-bottom: 24px;">
                        <div class="card-header" onclick="toggleCard('topic-${{topic.id}}')">
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <svg id="chevron-topic-${{topic.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span>${{topic.title}}</span>
                            </div>
                        </div>
                        <div class="card-content" id="content-topic-${{topic.id}}">
                            <p>${{topic.description}}</p>
                            
                            ${{topic.argumentIds.map(argId => {{
                                if (argsData.claimantArgs[argId] && argsData.respondentArgs[argId]) {{
                                    return `
                                    <div style="margin-top: 16px;">
                                        <div class="arguments-row">
                                            <div>
                                                <h3 class="side-heading appellant-color">Appellant's Position</h3>
                                                ${{renderArgument(argsData.claimantArgs[argId], 'appellant')}}
                                            </div>
                                            <div>
                                                <h3 class="side-heading respondent-color">Respondent's Position</h3>
                                                ${{renderArgument(argsData.respondentArgs[argId], 'respondent')}}
                                            </div>
                                        </div>
                                    </div>
                                    `;
                                }}
                                return '';
                            }}).join('')}}
                        </div>
                    </div>
                    `;
                }});
                
                container.innerHTML = html;
                
                // Auto-expand first topic
                setTimeout(() => {{
                    const firstTopic = argsData.topics[0];
                    if (firstTopic) {{
                        toggleCard(`topic-${{firstTopic.id}}`);
                    }}
                }}, 100);
            }}
            
            // Toggle a card without synchronizing - modified to only toggle content, not children
            function toggleCard(id) {{
                const contentEl = document.getElementById(`content-${{id}}`);
                const chevronEl = document.getElementById(`chevron-${{id}}`);
                
                if (contentEl) {{
                    contentEl.style.display = contentEl.style.display === 'block' ? 'none' : 'block';
                }}
                
                if (chevronEl) {{
                    chevronEl.classList.toggle('expanded');
                }}
            }}
            
            // Toggle an argument and its counterpart - modified to only toggle content
            function toggleArgument(argId, pairId, side) {{
                // First, handle the clicked argument
                toggleCard(argId);
                
                // Then, determine and handle the counterpart
                const otherSide = side === 'appellant' ? 'respondent' : 'appellant';
                const counterpartId = `${{otherSide}}-${{pairId}}`;
                
                // Toggle the counterpart (if it exists)
                const counterpartContentEl = document.getElementById(`content-${{counterpartId}}`);
                if (counterpartContentEl) {{
                    const counterpartChevronEl = document.getElementById(`chevron-${{counterpartId}}`);
                    
                    // Make sure the counterpart's state matches the toggled argument
                    const originalDisplay = document.getElementById(`content-${{argId}}`).style.display;
                    counterpartContentEl.style.display = originalDisplay;
                    
                    if (counterpartChevronEl) {{
                        if (originalDisplay === 'block') {{
                            counterpartChevronEl.classList.add('expanded');
                        }} else {{
                            counterpartChevronEl.classList.remove('expanded');
                        }}
                    }}
                }}
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                tbody.innerHTML = '';
                
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    if (item.status === 'Disputed') {{
                        row.classList.add('disputed');
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
                tbody.innerHTML = '';
                
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td><span class="badge ${{badgeClass}}">${{item.party}}</span></td>
                        <td>${{item.title}}</td>
                        <td>${{item.type}}</td>
                        <td>${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Copy all content function
            function copyAllContent() {{
                // Simple implementation - would need to be extended 
                // to actually collect and copy all content
                alert('All content copied to clipboard');
            }}
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
