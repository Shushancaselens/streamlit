import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

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
        }
    }
    
    topics = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argumentIds": ["1"]
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

# Get all facts from the data
def get_all_facts():
    args_data = get_argument_data()
    facts = []
    
    # Helper function to extract facts from arguments
    def extract_facts(arg, party):
        if not arg:
            return
            
        if 'factualPoints' in arg and arg['factualPoints']:
            for point in arg['factualPoints']:
                fact = {
                    'point': point['point'],
                    'date': point['date'],
                    'isDisputed': point['isDisputed'],
                    'party': party,
                    'paragraphs': point.get('paragraphs', ''),
                    'exhibits': point.get('exhibits', []),
                    'argId': arg['id'],
                    'argTitle': arg['title']
                }
                facts.append(fact)
                
        # Process children
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    # Extract from claimant args
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Appellant')
        
    # Extract from respondent args
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
        
    return facts

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    facts_data = get_all_facts()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    facts_json = json.dumps(facts_data)
    
    # Initialize session state if not already done
    if 'view' not in st.session_state:
        st.session_state.view = "Arguments"
    
    # Add Streamlit sidebar with navigation buttons only
    with st.sidebar:
        # Add the logo and CaseLens text
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#whatsapp-mask)">
                <!-- Rounded square background -->
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <!-- WhatsApp phone icon -->
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
        
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
        </style>
        """, unsafe_allow_html=True)
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Create buttons with names
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Determine which view to show based on sidebar selection
    if st.session_state.view == "Arguments":
        active_tab = 0
    elif st.session_state.view == "Facts":
        active_tab = 1
    elif st.session_state.view == "Timeline":
        active_tab = 2
    else:  # Exhibits
        active_tab = 3
    
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
            
            /* Party view styles */
            .appellant-only .arguments-row > div:nth-child(2) {{
                display: none;
            }}
            .appellant-only .arguments-row > div:nth-child(1) {{
                grid-column: 1 / span 2;
            }}
            .appellant-only .respondent-color {{
                display: none;
            }}
            
            .respondent-only .arguments-row > div:nth-child(1) {{
                display: none;
            }}
            .respondent-only .arguments-row > div:nth-child(2) {{
                grid-column: 1 / span 2;
            }}
            .respondent-only .appellant-color {{
                display: none;
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
            
            /* Action buttons */
            .action-buttons {{
                position: absolute;
                top: 20px;
                right: 20px;
                display: flex;
                gap: 10px;
            }}
            
            .action-button {{
                padding: 8px 16px;
                background-color: #f9f9f9;
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                cursor: pointer;
            }}
            
            .action-button:hover {{
                background-color: #f1f1f1;
            }}
            
            .export-dropdown {{
                position: relative;
                display: inline-block;
            }}
            
            .export-dropdown-content {{
                display: none;
                position: absolute;
                right: 0;
                background-color: #f9f9f9;
                min-width: 160px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                border-radius: 4px;
            }}
            
            .export-dropdown-content a {{
                color: black;
                padding: 12px 16px;
                text-decoration: none;
                display: block;
                cursor: pointer;
            }}
            
            .export-dropdown-content a:hover {{
                background-color: #f1f1f1;
            }}
            
            .export-dropdown:hover .export-dropdown-content {{
                display: block;
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
            
            /* Table view */
            .table-view {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            
            .table-view th {{
                padding: 12px;
                text-align: left;
                background-color: #f8f9fa;
                border-bottom: 2px solid #dee2e6;
                position: sticky;
                top: 0;
                cursor: pointer;
            }}
            
            .table-view th:hover {{
                background-color: #e9ecef;
            }}
            
            .table-view td {{
                padding: 12px;
                border-bottom: 1px solid #dee2e6;
            }}
            
            .table-view tr:hover {{
                background-color: #f8f9fa;
            }}
            
            /* Facts styling */
            .facts-container {{
                margin-top: 20px;
            }}
            
            .facts-header {{
                display: flex;
                margin-bottom: 20px;
                border-bottom: 1px solid #dee2e6;
            }}
            
            .tab-button {{
                padding: 10px 20px;
                background: none;
                border: none;
                cursor: pointer;
            }}
            
            .tab-button.active {{
                border-bottom: 2px solid #4299e1;
                color: #4299e1;
                font-weight: 500;
            }}
            
            .facts-content {{
                margin-top: 20px;
            }}
            
            /* View toggle */
            .view-toggle {{
                display: flex;
                justify-content: flex-end;
                margin-bottom: 16px;
            }}
            
            .view-toggle button {{
                padding: 8px 16px;
                border: 1px solid #e2e8f0;
                background-color: #f7fafc;
                cursor: pointer;
            }}
            
            .view-toggle button.active {{
                background-color: #4299e1;
                color: white;
                border-color: #4299e1;
            }}
            
            .view-toggle button:first-child {{
                border-radius: 4px 0 0 4px;
            }}
            
            .view-toggle button:last-child {{
                border-radius: 0 4px 4px 0;
            }}
            
            /* Copy notification */
            .copy-notification {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #2d3748;
                color: white;
                padding: 10px 20px;
                border-radius: 4px;
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.3s;
            }}
            
            .copy-notification.show {{
                opacity: 1;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div id="copy-notification" class="copy-notification">Content copied to clipboard!</div>
            
            <div class="action-buttons">
                <button class="action-button" onclick="copyAllContent()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                </button>
                <div class="export-dropdown">
                    <button class="action-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                            <polyline points="7 10 12 15 17 10"></polyline>
                            <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                        Export
                    </button>
                    <div class="export-dropdown-content">
                        <a onclick="exportAsCsv()">CSV</a>
                        <a onclick="exportAsPdf()">PDF</a>
                        <a onclick="exportAsWord()">Word</a>
                    </div>
                </div>
            </div>
            
            <!-- Arguments Section -->
            <div id="arguments" class="content-section">
                <div class="section-title">Issues</div>
                
                <!-- Direct inline buttons for view toggling -->
                <div style="display: flex; justify-content: space-between; margin-bottom: 16px;">
                    <div id="party-buttons">
                        <button id="both-btn" onclick="changePartyView('both')" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #4299e1; color: white; cursor: pointer; margin-right: 5px;">Both Parties</button>
                        
                        <button id="app-btn" onclick="changePartyView('appellant')" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #f7fafc; color: black; cursor: pointer; margin-right: 5px;">Appellant Only</button>
                        
                        <button id="resp-btn" onclick="changePartyView('respondent')" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #f7fafc; color: black; cursor: pointer;">Respondent Only</button>
                    </div>
                    <div>
                        <button id="detailed-view-btn" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #4299e1; color: white; cursor: pointer; margin-right: 5px;" onclick="document.getElementById('detailed-view').style.display='block'; document.getElementById('table-view').style.display='none'; this.style.backgroundColor='#4299e1'; this.style.color='white'; document.getElementById('table-view-btn').style.backgroundColor='#f7fafc'; document.getElementById('table-view-btn').style.color='black';">Detailed View</button>
                        
                        <button id="table-view-btn" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #f7fafc; cursor: pointer;" onclick="document.getElementById('detailed-view').style.display='none'; document.getElementById('table-view').style.display='block'; this.style.backgroundColor='#4299e1'; this.style.color='white'; document.getElementById('detailed-view-btn').style.backgroundColor='#f7fafc'; document.getElementById('detailed-view-btn').style.color='black';">Table View</button>
                    </div>
                </div>
                
                <!-- Detailed view content -->
                <div id="detailed-view" class="view-content active">
                    <div id="topics-container"></div>
                </div>
                
                <!-- Table view content -->
                <div id="table-view" class="view-content" style="display: none;">
                    <table class="table-view">
                        <thead>
                            <tr>
                                <th onclick="sortTable('table-view-body', 0)">ID</th>
                                <th onclick="sortTable('table-view-body', 1)">Argument</th>
                                <th onclick="sortTable('table-view-body', 2)">Party</th>
                                <th onclick="sortTable('table-view-body', 3)">Status</th>
                                <th onclick="sortTable('table-view-body', 4)">Evidence</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="table-view-body"></tbody>
                    </table>
                </div>
            </div>
            
            <!-- Facts Section -->
            <div id="facts" class="content-section">
                <div class="section-title">Case Facts</div>
                
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <div class="facts-content">
                    <table class="table-view">
                        <thead>
                            <tr>
                                <th onclick="sortTable('facts-table-body', 0)">Date</th>
                                <th onclick="sortTable('facts-table-body', 1)">Event</th>
                                <th onclick="sortTable('facts-table-body', 2)">Party</th>
                                <th onclick="sortTable('facts-table-body', 3)">Status</th>
                                <th onclick="sortTable('facts-table-body', 4)">Related Argument</th>
                                <th onclick="sortTable('facts-table-body', 5)">Evidence</th>
                            </tr>
                        </thead>
                        <tbody id="facts-table-body"></tbody>
                    </table>
                </div>
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
            const factsData = {facts_json};
            const viewOptions = {view_options_json};
            
            // Function to change party view
            function changePartyView(view) {{
                console.log("Changing party view to:", view);
                
                // Get the container
                const container = document.getElementById('topics-container');
                
                // Update button styling
                const bothBtn = document.getElementById('both-btn');
                const appBtn = document.getElementById('app-btn');
                const respBtn = document.getElementById('resp-btn');
                
                // Reset button styles
                bothBtn.style.backgroundColor = '#f7fafc';
                bothBtn.style.color = 'black';
                appBtn.style.backgroundColor = '#f7fafc';
                appBtn.style.color = 'black';
                respBtn.style.backgroundColor = '#f7fafc';
                respBtn.style.color = 'black';
                
                // Apply class to container based on view
                container.className = '';
                
                if (view === 'both') {{
                    bothBtn.style.backgroundColor = '#4299e1';
                    bothBtn.style.color = 'white';
                    // Default view - no special class needed
                }} else if (view === 'appellant') {{
                    appBtn.style.backgroundColor = '#4299e1';
                    appBtn.style.color = 'white';
                    container.className = 'appellant-only';
                }} else if (view === 'respondent') {{
                    respBtn.style.backgroundColor = '#4299e1';
                    respBtn.style.color = 'white';
                    container.className = 'respondent-only';
                }}
            }}
            
            // Show the selected view based on sidebar selection
            document.addEventListener('DOMContentLoaded', function() {{
                // Show the correct section based on sidebar selection
                const sections = ['arguments', 'facts', 'timeline', 'exhibits'];
                const activeSection = sections[viewOptions.activeTab];
                
                document.querySelectorAll('.content-section').forEach(section => {{
                    section.classList.remove('active');
                }});
                
                document.getElementById(activeSection).classList.add('active');
                
                // Initialize content as needed
                if (activeSection === 'arguments') {{
                    renderTopics();
                    renderArgumentsTable();
                }}
                if (activeSection === 'timeline') renderTimeline();
                if (activeSection === 'exhibits') renderExhibits();
                if (activeSection === 'facts') renderFacts();
            }});
            
            // Switch view between detailed and table
            function switchView(viewType) {{
                const detailedBtn = document.getElementById('detailed-view-btn');
                const tableBtn = document.getElementById('table-view-btn');
                const detailedView = document.getElementById('detailed-view');
                const tableView = document.getElementById('table-view');
                
                if (viewType === 'detailed') {{
                    detailedBtn.classList.add('active');
                    tableBtn.classList.remove('active');
                    detailedView.style.display = 'block';
                    tableView.style.display = 'none';
                }} else {{
                    detailedBtn.classList.remove('active');
                    tableBtn.classList.add('active');
                    detailedView.style.display = 'none';
                    tableView.style.display = 'block';
                }}
            }}
            
            // Switch facts tab
            function switchFactsTab(tabType) {{
                const allBtn = document.getElementById('all-facts-btn');
                const disputedBtn = document.getElementById('disputed-facts-btn');
                const undisputedBtn = document.getElementById('undisputed-facts-btn');
                
                // Remove active class from all
                allBtn.classList.remove('active');
                disputedBtn.classList.remove('active');
                undisputedBtn.classList.remove('active');
                
                // Add active to selected
                if (tabType === 'all') {{
                    allBtn.classList.add('active');
                    renderFacts('all');
                }} else if (tabType === 'disputed') {{
                    disputedBtn.classList.add('active');
                    renderFacts('disputed');
                }} else {{
                    undisputedBtn.classList.add('active');
                    renderFacts('undisputed');
                }}
            }}
            
            // Sort table function
            function sortTable(tableId, columnIndex) {{
                const table = document.getElementById(tableId);
                const rows = Array.from(table.rows);
                let dir = 1; // 1 for ascending, -1 for descending
                
                // Check if already sorted in this direction
                if (table.getAttribute('data-sort-column') === String(columnIndex) &&
                    table.getAttribute('data-sort-dir') === '1') {{
                    dir = -1;
                }}
                
                // Sort the rows
                rows.sort((a, b) => {{
                    const cellA = a.cells[columnIndex].textContent.trim();
                    const cellB = b.cells[columnIndex].textContent.trim();
                    
                    // Handle date sorting
                    if (columnIndex === 0 && tableId === 'facts-table-body') {{
                        // Attempt to parse as dates
                        const dateA = new Date(cellA);
                        const dateB = new Date(cellB);
                        
                        if (!isNaN(dateA) && !isNaN(dateB)) {{
                            return dir * (dateA - dateB);
                        }}
                    }}
                    
                    return dir * cellA.localeCompare(cellB);
                }});
                
                // Remove existing rows and append in new order
                rows.forEach(row => table.appendChild(row));
                
                // Store current sort direction and column
                table.setAttribute('data-sort-column', columnIndex);
                table.setAttribute('data-sort-dir', dir);
            }}
            
            // Copy all content function
            function copyAllContent() {{
                const activeSection = document.querySelector('.content-section.active');
                if (!activeSection) return;
                
                let contentToCopy = '';
                
                // Extract content based on section
                if (activeSection.id === 'arguments') {{
                    if (document.getElementById('detailed-view').style.display !== 'none') {{
                        contentToCopy = extractArgumentsDetailedText();
                    }} else {{
                        contentToCopy = extractArgumentsTableText();
                    }}
                }} else if (activeSection.id === 'timeline') {{
                    contentToCopy = extractTimelineText();
                }} else if (activeSection.id === 'exhibits') {{
                    contentToCopy = extractExhibitsText();
                }} else if (activeSection.id === 'facts') {{
                    contentToCopy = extractFactsText();
                }}
                
                // Create a temporary textarea to copy the content
                const textarea = document.createElement('textarea');
                textarea.value = contentToCopy;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);
                
                // Show notification
                const notification = document.getElementById('copy-notification');
                notification.classList.add('show');
                
                setTimeout(() => {{
                    notification.classList.remove('show');
                }}, 2000);
            }}
            
            // Export functions
            function exportAsCsv() {{
                const activeSection = document.querySelector('.content-section.active');
                if (!activeSection) return;
                
                let contentToCsv = '';
                
                // Extract content based on section
                if (activeSection.id === 'arguments') {{
                    if (document.getElementById('detailed-view').style.display !== 'none') {{
                        contentToCsv = extractArgumentsDetailedText();
                    }} else {{
                        contentToCsv = extractArgumentsTableText();
                    }}
                }} else if (activeSection.id === 'timeline') {{
                    contentToCsv = extractTimelineText();
                }} else if (activeSection.id === 'exhibits') {{
                    contentToCsv = extractExhibitsText();
                }} else if (activeSection.id === 'facts') {{
                    contentToCsv = extractFactsText();
                }}
                
                // Create link for CSV download
                const csvContent = "data:text/csv;charset=utf-8," + encodeURIComponent(contentToCsv);
                const encodedUri = csvContent;
                const link = document.createElement("a");
                link.setAttribute("href", encodedUri);
                link.setAttribute("download", activeSection.id + ".csv");
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }}
            
            function exportAsPdf() {{
                alert("PDF export functionality would be implemented here");
            }}
            
            function exportAsWord() {{
                alert("Word export functionality would be implemented here");
            }}
            
            // Extract text from arguments detailed view
            function extractArgumentsDetailedText() {{
                const container = document.getElementById('topics-container');
                return container.innerText;
            }}
            
            // Extract text from arguments table
            function extractArgumentsTableText() {{
                const table = document.querySelector('#table-view table');
                let text = '';
                
                // Get headers
                const headers = Array.from(table.querySelectorAll('th'))
                    .map(th => th.textContent.trim())
                    .filter(header => header !== 'Actions')
                    .join('\\t');
                
                text += headers + '\\n';
                
                // Get rows
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(row => {{
                    const rowText = Array.from(row.querySelectorAll('td'))
                        .filter((td, index) => index !== row.cells.length - 1) // Exclude Actions column
                        .map(td => td.textContent.trim())
                        .join('\\t');
                    
                    text += rowText + '\\n';
                }});
                
                return text;
            }}
            
            // Extract text from timeline
            function extractTimelineText() {{
                const table = document.getElementById('timeline-table');
                let text = '';
                
                // Get headers
                const headers = Array.from(table.querySelectorAll('th'))
                    .map(th => th.textContent.trim())
                    .join('\\t');
                
                text += headers + '\\n';
                
                // Get rows
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(row => {{
                    const rowText = Array.from(row.querySelectorAll('td'))
                        .map(td => td.textContent.trim())
                        .join('\\t');
                    
                    text += rowText + '\\n';
                }});
                
                return text;
            }}
            
            // Extract text from exhibits
            function extractExhibitsText() {{
                const table = document.getElementById('exhibits-table');
                let text = '';
                
                // Get headers
                const headers = Array.from(table.querySelectorAll('th'))
                    .map(th => th.textContent.trim())
                    .join('\\t');
                
                text += headers + '\\n';
                
                // Get rows
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(row => {{
                    const rowText = Array.from(row.querySelectorAll('td'))
                        .map(td => td.textContent.trim())
                        .join('\\t');
                    
                    text += rowText + '\\n';
                }});
                
                return text;
            }}
            
            // Extract text from facts
            function extractFactsText() {{
                const table = document.querySelector('.facts-content table');
                let text = '';
                
                // Get headers
                const headers = Array.from(table.querySelectorAll('th'))
                    .map(th => th.textContent.trim())
                    .join('\\t');
                
                text += headers + '\\n';
                
                // Get rows
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(row => {{
                    const rowText = Array.from(row.querySelectorAll('td'))
                        .map(td => td.textContent.trim())
                        .join('\\t');
                    
                    text += rowText + '\\n';
                }});
                
                return text;
            }}
            
            // Render arguments in table format
            function renderArgumentsTable() {{
                const tableBody = document.getElementById('table-view-body');
                tableBody.innerHTML = '';
                
                // Helper function to flatten arguments
                function flattenArguments(args, party) {{
                    let result = [];
                    
                    Object.values(args).forEach(arg => {{
                        // Track if argument has disputed facts
                        const hasDisputedFacts = arg.factualPoints && 
                            arg.factualPoints.some(point => point.isDisputed);
                        
                        // Count pieces of evidence
                        const evidenceCount = arg.evidence ? arg.evidence.length : 0;
                        
                        // Add this argument
                        result.push({{
                            id: arg.id,
                            title: arg.title,
                            party: party,
                            hasDisputedFacts: hasDisputedFacts,
                            evidenceCount: evidenceCount,
                            paragraphs: arg.paragraphs
                        }});
                        
                        // Process children recursively
                        if (arg.children) {{
                            Object.values(arg.children).forEach(child => {{
                                result = result.concat(flattenArguments({{[child.id]: child}}, party));
                            }});
                        }}
                    }});
                    
                    return result;
                }}
                
                // Get flattened arguments
                const appellantArgs = flattenArguments(argsData.claimantArgs, "Appellant");
                const respondentArgs = flattenArguments(argsData.respondentArgs, "Respondent");
                const allArgs = [...appellantArgs, ...respondentArgs];
                
                // Render rows
                allArgs.forEach(arg => {{
                    const row = document.createElement('tr');
                    
                    // ID column
                    const idCell = document.createElement('td');
                    idCell.textContent = arg.id;
                    row.appendChild(idCell);
                    
                    // Title column
                    const titleCell = document.createElement('td');
                    titleCell.textContent = arg.title;
                    row.appendChild(titleCell);
                    
                    // Party column
                    const partyCell = document.createElement('td');
                    const partyBadge = document.createElement('span');
                    partyBadge.className = `badge ${{arg.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                    partyBadge.textContent = arg.party;
                    partyCell.appendChild(partyBadge);
                    row.appendChild(partyCell);
                    
                    // Status column
                    const statusCell = document.createElement('td');
                    if (arg.hasDisputedFacts) {{
                        const disputedBadge = document.createElement('span');
                        disputedBadge.className = 'badge disputed-badge';
                        disputedBadge.textContent = 'Disputed';
                        statusCell.appendChild(disputedBadge);
                    }} else {{
                        statusCell.textContent = 'Undisputed';
                    }}
                    row.appendChild(statusCell);
                    
                    // Evidence column
                    const evidenceCell = document.createElement('td');
                    evidenceCell.textContent = arg.evidenceCount > 0 ? `${{arg.evidenceCount}} items` : 'None';
                    row.appendChild(evidenceCell);
                    
                    // Actions column
                    const actionsCell = document.createElement('td');
                    const viewBtn = document.createElement('button');
                    viewBtn.textContent = 'View';
                    viewBtn.style.padding = '4px 8px';
                    viewBtn.style.marginRight = '8px';
                    viewBtn.style.border = '1px solid #e2e8f0';
                    viewBtn.style.borderRadius = '4px';
                    viewBtn.style.backgroundColor = '#f7fafc';
                    viewBtn.style.cursor = 'pointer';
                    viewBtn.onclick = function() {{
                        // Switch to detailed view and expand this argument
                        switchView('detailed');
                        // Logic to find and expand the argument would go here
                    }};
                    actionsCell.appendChild(viewBtn);
                    row.appendChild(actionsCell);
                    
                    tableBody.appendChild(row);
                }});
            }}
            
            // Render facts table
            function renderFacts(type = 'all') {{
                const tableBody = document.getElementById('facts-table-body');
                tableBody.innerHTML = '';
                
                // Filter by type
                let filteredFacts = factsData;
                
                if (type === 'disputed') {{
                    filteredFacts = factsData.filter(fact => fact.isDisputed);
                }} else if (type === 'undisputed') {{
                    filteredFacts = factsData.filter(fact => !fact.isDisputed);
                }}
                
                // Sort by date
                filteredFacts.sort((a, b) => {{
                    // Handle date ranges like "1950-present"
                    const dateA = a.date.split('-')[0];
                    const dateB = b.date.split('-')[0];
                    return new Date(dateA) - new Date(dateB);
                }});
                
                // Render rows
                filteredFacts.forEach(fact => {{
                    const row = document.createElement('tr');
                    
                    // Date column
                    const dateCell = document.createElement('td');
                    dateCell.textContent = fact.date;
                    row.appendChild(dateCell);
                    
                    // Event column
                    const eventCell = document.createElement('td');
                    eventCell.textContent = fact.point;
                    row.appendChild(eventCell);
                    
                    // Party column
                    const partyCell = document.createElement('td');
                    const partyBadge = document.createElement('span');
                    partyBadge.className = `badge ${{fact.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                    partyBadge.textContent = fact.party;
                    partyCell.appendChild(partyBadge);
                    row.appendChild(partyCell);
                    
                    // Status column
                    const statusCell = document.createElement('td');
                    if (fact.isDisputed) {{
                        const disputedBadge = document.createElement('span');
                        disputedBadge.className = 'badge disputed-badge';
                        disputedBadge.textContent = 'Disputed';
                        statusCell.appendChild(disputedBadge);
                    }} else {{
                        statusCell.textContent = 'Undisputed';
                    }}
                    row.appendChild(statusCell);
                    
                    // Related argument
                    const argCell = document.createElement('td');
                    argCell.textContent = `${{fact.argId}}. ${{fact.argTitle}}`;
                    row.appendChild(argCell);
                    
                    // Evidence column
                    const evidenceCell = document.createElement('td');
                    if (fact.exhibits && fact.exhibits.length > 0) {{
                        fact.exhibits.forEach(exhibitId => {{
                            const exhibitBadge = document.createElement('span');
                            exhibitBadge.className = 'badge exhibit-badge';
                            exhibitBadge.textContent = exhibitId;
                            exhibitBadge.style.marginRight = '4px';
                            evidenceCell.appendChild(exhibitBadge);
                        }});
                    }} else {{
                        evidenceCell.textContent = 'None';
                    }}
                    row.appendChild(evidenceCell);
                    
                    tableBody.appendChild(row);
                }});
            }}
            
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
            
            // Render factual points (now called Events)
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
                            </span>
                        </div>
                        <div style="font-size: 12px; color: #666; margin-top: 4px;">${{point.date}}</div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Events</div>
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
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Summary of arguments")
    components.html(html_content, height=950, scrolling=True)

if __name__ == "__main__":
    main()

