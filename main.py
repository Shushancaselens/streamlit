import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

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
                    "exhibits": ["C-1"],
                    "source_text": "The Club has maintained continuous operations under the same registered name 'Athletic Club United' since its original incorporation on January 12, 1950, without any interruption in its legal status or operational capacity.",
                    "page": "18",
                    "doc_name": "Statement of Appeal",
                    "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
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
                                    "exhibits": ["C-2"],
                                    "source_text": "The club was officially registered with the National Football Federation on January 12, 1950, under registration number NFF-1950-047.",
                                    "page": "25",
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30",
                                    "exhibits": ["C-2"],
                                    "source_text": "While administrative challenges arose during the 1975-1976 period due to financial restructuring, the club's core operations and identity remained intact throughout this transitional phase.",
                                    "page": "29",
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
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
                            "exhibits": ["C-4"],
                            "source_text": "The club has consistently utilized the blue and white color scheme as its primary identity markers since its founding in 1950, with only minor shade variations that do not affect the overall visual identity.",
                            "page": "51",
                            "doc_name": "Statement of Appeal",
                            "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
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
                                    "exhibits": ["C-5"],
                                    "source_text": "The minor variations in blue shade intensity during the 1970-1980 period were purely technical adjustments due to fabric manufacturing changes and do not constitute a break in visual identity continuity.",
                                    "page": "56",
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59",
                                    "exhibits": ["C-5"],
                                    "source_text": "A red accent color was temporarily incorporated into the uniform design between 1982-1988 for commemorative purposes, while maintaining the core blue and white identity elements.",
                                    "page": "58",
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
                                }
                            ],
                            "children": {}
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
                    "exhibits": ["R-1"],
                    "source_text": "Official federation records demonstrate a complete cessation of competitive activities during the 1975-1976 season, with no registered players, no match participation, and formal withdrawal from all competitions.",
                    "page": "206",
                    "doc_name": "Answer to Request for Provisional Measures",
                    "doc_summary": "Respondent's primary response document challenging the appellant's claims and presenting counter-evidence"
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
            "children": {}
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
                    'argTitle': arg['title'],
                    'source_text': point.get('source_text', ''),
                    'page': point.get('page', ''),
                    'doc_name': point.get('doc_name', ''),
                    'doc_summary': point.get('doc_summary', '')
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

# Get enhanced timeline data with additional events
def get_timeline_data():
    # Create a richer set of timeline events
    timeline_events = [
        {
            "point": "Club founded and officially registered in the Football Federation",
            "date": "1950-01-12",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-1"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Statement of Appeal",
            "source_text": "Athletic Club United was officially incorporated and registered with the National Football Federation on January 12, 1950, marking the beginning of its formal competitive existence.",
            "page": "15",
            "doc_name": "Statement of Appeal",
            "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
        },
        {
            "point": "First National Championship won",
            "date": "1955-05-20",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-3"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Appeal Brief",
            "source_text": "Athletic Club United achieved its first major sporting success by winning the National Championship on May 20, 1955, establishing its competitive credentials and public recognition.",
            "page": "22",
            "doc_name": "Appeal Brief",
            "doc_summary": "Comprehensive legal brief supporting the appellant's arguments with detailed evidence and case law analysis"
        },
        {
            "point": "Club colors established as blue and white",
            "date": "1956-03-10",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-4"],
            "argId": "1.2",
            "argTitle": "Club Colors Analysis",
            "source": "Appeal - Statement of Appeal",
            "source_text": "The official club colors of blue and white were formally registered and established as the club's visual identity on March 10, 1956, following the successful championship season.",
            "page": "46",
            "doc_name": "Statement of Appeal",
            "doc_summary": "Primary appeal document outlining the appellant's case for sporting succession and continuous club identity"
        },
        {
            "point": "First international competition participation",
            "date": "1962-09-15",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-6"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Appeal Brief"
        },
        {
            "point": "Minor variations in club color shades introduced",
            "date": "1970-1980",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-5"],
            "argId": "1.2.1",
            "argTitle": "Color Variations Analysis",
            "source": "Appeal - Statement of Appeal"
        },
        {
            "point": "Administrative operations halted due to financial difficulties",
            "date": "1975-04-30",
            "isDisputed": False,
            "party": "Respondent",
            "exhibits": ["R-2"],
            "argId": "1.1.1",
            "argTitle": "Registration Gap Evidence",
            "source": "provisional messier - Answer to Request for PM",
            "source_text": "Due to severe financial constraints, the club was forced to suspend administrative operations on April 30, 1975, leading to temporary cessation of competitive activities.",
            "page": "145",
            "doc_name": "Answer to Request for Provisional Measures",
            "doc_summary": "Respondent's primary response document challenging the appellant's claims and presenting counter-evidence"
        },
        {
            "point": "Operations ceased between 1975-1976",
            "date": "1975-1976",
            "isDisputed": True,
            "party": "Respondent",
            "exhibits": ["R-1"],
            "argId": "1",
            "argTitle": "Sporting Succession Rebuttal",
            "source": "provisional messier - Answer to PM",
            "source_text": "Official federation records demonstrate a complete cessation of competitive activities during the 1975-1976 season, with no registered players, no match participation, and formal withdrawal from all competitions.",
            "page": "206",
            "doc_name": "Answer to Request for Provisional Measures",
            "doc_summary": "Respondent's primary response document challenging the appellant's claims and presenting counter-evidence"
        },
        {
            "point": "Club registration formally terminated",
            "date": "1975-04-30",
            "isDisputed": False,
            "party": "Respondent",
            "exhibits": ["R-2"],
            "argId": "1.1.1",
            "argTitle": "Registration Gap Evidence",
            "source": "provisional messier - Answer to Request for PM"
        },
        {
            "point": "New entity registered with similar name",
            "date": "1976-09-15",
            "isDisputed": False,
            "party": "Respondent",
            "exhibits": ["R-2"],
            "argId": "1.1.1",
            "argTitle": "Registration Gap Evidence",
            "source": "provisional messier - Answer to Request for PM"
        },
        {
            "point": "Significant color scheme change implemented",
            "date": "1976-10-01",
            "isDisputed": True,
            "party": "Respondent",
            "exhibits": ["R-4"],
            "argId": "1.2",
            "argTitle": "Club Colors Analysis Rebuttal",
            "source": "admissibility - Brief on Admissibility"
        },
        {
            "point": "Third color temporarily added to uniform",
            "date": "1982-1988",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-5"],
            "argId": "1.2.1",
            "argTitle": "Color Variations Analysis",
            "source": "Appeal - Appeal Brief"
        },
        {
            "point": "Club won Continental Cup with post-1976 team",
            "date": "1987-06-24",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-7"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Statement of Appeal"
        },
        {
            "point": "Return to original blue and white color scheme",
            "date": "1989-08-12",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-8"],
            "argId": "1.2",
            "argTitle": "Club Colors Analysis",
            "source": "Appeal - Appeal Brief"
        },
        {
            "point": "Trademark registration for club name and emblem",
            "date": "1995-11-30",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-9"],
            "argId": "1.1",
            "argTitle": "Club Name Analysis",
            "source": "Appeal - Statement of Appeal"
        },
        {
            "point": "Federation officially recognizes club history spanning pre and post 1976",
            "date": "2010-05-18",
            "isDisputed": True,
            "party": "Appellant",
            "exhibits": ["C-10"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "admissibility - Reply to Objection to Admissibility",
            "source_text": "The National Football Federation issued Official Recognition Letter NFF-2010-REG-047 acknowledging the continuous sporting succession and historical continuity of Athletic Club United spanning both pre-1976 and post-1976 periods.",
            "page": "89",
            "doc_name": "Reply to Objection to Admissibility",
            "doc_summary": "Appellant's response to respondent's admissibility objections, providing additional supporting evidence and legal arguments"
        }
    ]
    
    # Sort events chronologically
    timeline_events.sort(key=lambda x: x['date'])
    
    return timeline_events

# Sample document sets for demonstrating the document set view
def get_document_sets():
    # Return grouped document sets with individual document subfolders
    return [
        {
            "id": "appeal",
            "name": "Appeal",
            "party": "Mixed",
            "category": "Appeal",
            "isGroup": True,
            "documents": [
                {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant", "category": "Appeal"},
                {"id": "2", "name": "2. Request for a Stay", "party": "Appellant", "category": "Appeal"},
                {"id": "5", "name": "5. Appeal Brief", "party": "Appellant", "category": "Appeal"},
                {"id": "10", "name": "Jurisprudence", "party": "Shared", "category": "Appeal"}
            ]
        },
        {
            "id": "provisional_messier",
            "name": "provisional messier",
            "party": "Respondent",
            "category": "provisional messier",
            "isGroup": True,
            "documents": [
                {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "category": "provisional messier"},
                {"id": "4", "name": "4. Answer to PM", "party": "Respondent", "category": "provisional messier"}
            ]
        },
        {
            "id": "admissibility",
            "name": "admissibility",
            "party": "Mixed",
            "category": "admissibility",
            "isGroup": True,
            "documents": [
                {"id": "6", "name": "6. Brief on Admissibility", "party": "Respondent", "category": "admissibility"},
                {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant", "category": "admissibility"},
                {"id": "11", "name": "Objection to Admissibility", "party": "Respondent", "category": "admissibility"}
            ]
        },
        {
            "id": "challenge",
            "name": "challenge",
            "party": "Mixed",
            "category": "challenge",
            "isGroup": True,
            "documents": [
                {"id": "8", "name": "8. Challenge", "party": "Appellant", "category": "challenge"},
                {"id": "9", "name": "ChatGPT", "party": "Shared", "category": "challenge"},
                {"id": "12", "name": "Swiss Court", "party": "Shared", "category": "challenge"}
            ]
        }
    ]

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
    facts_data = get_all_facts()
    document_sets = get_document_sets()
    timeline_data = get_timeline_data()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    document_sets_json = json.dumps(document_sets)
    timeline_json = json.dumps(timeline_data)
    
    # Initialize session state if not already done
    if 'view' not in st.session_state:
        st.session_state.view = "Facts"
    
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
    
    # Create the facts HTML component
    if st.session_state.view == "Facts":
        # Create a single HTML component containing the Facts UI
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
                
                .shared-badge {{
                    background-color: rgba(128, 128, 128, 0.1);
                    color: #666;
                }}
                
                .exhibit-badge {{
                    background-color: rgba(221, 107, 32, 0.1);
                    color: #dd6b20;
                }}
                
                .disputed-badge {{
                    background-color: rgba(229, 62, 62, 0.1);
                    color: #e53e3e;
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
                
                .view-toggle button:not(:first-child):not(:last-child) {{
                    border-radius: 0;
                    border-left: none;
                    border-right: none;
                }}
                
                .view-toggle button:last-child {{
                    border-radius: 0 4px 4px 0;
                }}
                
                /* Document sets */
                .docset-header {{
                    display: flex;
                    align-items: center;
                    padding: 10px 15px;
                    background-color: #f8f9fa;
                    border: 1px solid #e9ecef;
                    border-radius: 4px;
                    margin-bottom: 10px;
                    cursor: pointer;
                }}
                
                .docset-header:hover {{
                    background-color: #e9ecef;
                }}
                
                .docset-icon {{
                    margin-right: 10px;
                    color: #4299e1;
                }}
                
                .docset-content {{
                    display: block; /* Changed from 'none' to 'block' to be open by default */
                    padding: 0 0 20px 0;
                }}
                
                .docset-content.show {{
                    display: block;
                }}
                
                .folder-icon {{
                    color: #4299e1;
                    margin-right: 8px;
                }}
                
                .chevron {{
                    transition: transform 0.2s;
                    margin-right: 8px;
                    transform: rotate(90deg); /* Start expanded by default */
                }}
                
                .chevron.expanded {{
                    transform: rotate(90deg);
                }}
                
                /* Enhanced Timeline styling */
                .timeline-container {{
                    display: flex;
                    flex-direction: column;
                    margin-top: 20px;
                    position: relative;
                    max-width: 1000px;
                    margin: 0 auto;
                }}
                
                .timeline-wrapper {{
                    position: relative;
                    margin-left: 20px;
                }}
                
                .timeline-line {{
                    position: absolute;
                    left: 0;
                    top: 0;
                    bottom: 0;
                    width: 4px;
                    background: linear-gradient(to bottom, #4299e1, #7f9cf5);
                    border-radius: 4px;
                }}
                
                .timeline-item {{
                    display: flex;
                    margin-bottom: 32px;
                    position: relative;
                }}
                
                .timeline-point {{
                    position: absolute;
                    left: -12px;
                    top: 18px;
                    width: 24px;
                    height: 24px;
                    border-radius: 50%;
                    background-color: #4299e1;
                    border: 4px solid white;
                    box-shadow: 0 0 0 2px rgba(66, 153, 225, 0.3);
                    z-index: 10;
                }}
                
                .timeline-point.disputed {{
                    background-color: #e53e3e;
                    box-shadow: 0 0 0 2px rgba(229, 62, 62, 0.3);
                }}
                
                .timeline-content {{
                    margin-left: 32px;
                    flex-grow: 1;
                    background-color: white;
                    border-radius: 8px;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
                    overflow: hidden;
                    transition: all 0.2s;
                }}
                
                .timeline-content:hover {{
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06);
                    transform: translateY(-2px);
                }}
                
                .timeline-header {{
                    padding: 12px 16px;
                    border-bottom: 1px solid #e2e8f0;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    background-color: #f8fafc;
                }}
                
                .timeline-header-disputed {{
                    background-color: rgba(229, 62, 62, 0.05);
                }}
                
                .timeline-date {{
                    font-weight: 600;
                    color: #1a202c;
                }}
                
                .timeline-badges {{
                    display: flex;
                    gap: 6px;
                }}
                
                .timeline-body {{
                    padding: 16px;
                }}
                
                .timeline-fact {{
                    margin-bottom: 12px;
                    font-size: 15px;
                    color: #2d3748;
                }}
                
                .timeline-footer {{
                    padding: 12px 16px;
                    background-color: #f8fafc;
                    display: flex;
                    flex-wrap: wrap;
                    gap: 6px;
                    border-top: 1px solid #e2e8f0;
                }}
                
                .timeline-meta {{
                    font-size: 13px;
                    color: #718096;
                    margin-top: 8px;
                }}
                
                .timeline-meta span {{
                    display: inline-block;
                    margin-right: 12px;
                }}
                
                .timeline-year-marker {{
                    display: flex;
                    align-items: center;
                    margin: 24px 0;
                    position: relative;
                }}
                
                .timeline-year {{
                    background-color: #4299e1;
                    color: white;
                    padding: 4px 12px;
                    border-radius: 16px;
                    font-weight: 600;
                    position: relative;
                    z-index: 10;
                    margin-left: 32px;
                }}
                
                .timeline-year-line {{
                    flex-grow: 1;
                    height: 2px;
                    background-color: #e2e8f0;
                    margin-left: 12px;
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
                
                <!-- Facts Section -->
                <div id="facts" class="content-section active">
                    <div class="section-title">Case Facts</div>
                    
                    <div class="view-toggle">
                        <button id="table-view-btn" class="active" onclick="switchView('table')">Table View</button>
                        <button id="docset-view-btn" onclick="switchView('docset')">Document Categories</button>
                        <button id="timeline-view-btn" onclick="switchView('timeline')">Timeline View</button>
                    </div>
                    
                    <div class="facts-header">
                        <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                        <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                        <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                    </div>
                    
                    <!-- Table View -->
                    <div id="table-view-content" class="facts-content">
                        <table class="table-view">
                            <thead>
                                <tr>
                                    <th onclick="sortTable('facts-table-body', 0)">Date</th>
                                    <th onclick="sortTable('facts-table-body', 1)">Event</th>
                                    <th onclick="sortTable('facts-table-body', 2)">Source Text</th>
                                    <th onclick="sortTable('facts-table-body', 3)">Page</th>
                                    <th onclick="sortTable('facts-table-body', 4)">Document</th>
                                    <th onclick="sortTable('facts-table-body', 5)">Party</th>
                                    <th onclick="sortTable('facts-table-body', 6)">Status</th>
                                    <th onclick="sortTable('facts-table-body', 7)">Evidence</th>
                                </tr>
                            </thead>
                            <tbody id="facts-table-body"></tbody>
                        </table>
                    </div>
                    
                    <!-- Timeline View -->
                    <div id="timeline-view-content" class="facts-content" style="display: none;">
                        <div class="timeline-container">
                            <div class="timeline-wrapper">
                                <div class="timeline-line"></div>
                                <div id="timeline-events"></div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Document Sets View -->
                    <div id="docset-view-content" class="facts-content" style="display: none;">
                        <div id="document-sets-container"></div>
                    </div>
                </div>
            </div>
            
            <script>
                // Initialize data
                const factsData = {facts_json};
                const documentSets = {document_sets_json};
                const timelineData = {timeline_json};
                
                // Switch view between table, timeline, and document sets
                function switchView(viewType) {{
                    const tableBtn = document.getElementById('table-view-btn');
                    const timelineBtn = document.getElementById('timeline-view-btn');
                    const docsetBtn = document.getElementById('docset-view-btn');
                    
                    const tableContent = document.getElementById('table-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    // Remove active class from all buttons
                    tableBtn.classList.remove('active');
                    timelineBtn.classList.remove('active');
                    docsetBtn.classList.remove('active');
                    
                    // Hide all content
                    tableContent.style.display = 'none';
                    timelineContent.style.display = 'none';
                    docsetContent.style.display = 'none';
                    
                    // Activate the selected view
                    if (viewType === 'table') {{
                        tableBtn.classList.add('active');
                        tableContent.style.display = 'block';
                    }} else if (viewType === 'timeline') {{
                        timelineBtn.classList.add('active');
                        timelineContent.style.display = 'block';
                        renderTimeline();
                    }} else if (viewType === 'docset') {{
                        docsetBtn.classList.add('active');
                        docsetContent.style.display = 'block';
                        renderDocumentSets();
                    }}
                }}
                
                // Copy all content function
                function copyAllContent() {{
                    let contentToCopy = '';
                    
                    // Determine which view is active
                    const tableContent = document.getElementById('table-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    
                    if (tableContent.style.display !== 'none') {{
                        // Copy table data
                        const table = document.querySelector('.table-view');
                        const headers = Array.from(table.querySelectorAll('th'))
                            .map(th => th.textContent.trim())
                            .join('\\t');
                        
                        contentToCopy += 'Case Facts\\n\\n';
                        contentToCopy += headers + '\\n';
                        
                        // Get rows
                        const rows = table.querySelectorAll('tbody tr');
                        rows.forEach(row => {{
                            const rowText = Array.from(row.querySelectorAll('td'))
                                .map(td => td.textContent.trim())
                                .join('\\t');
                            
                            contentToCopy += rowText + '\\n';
                        }});
                    }} else if (timelineContent.style.display !== 'none') {{
                        // Copy timeline data
                        contentToCopy += 'Case Timeline\\n\\n';
                        
                        const timelineItems = document.querySelectorAll('.timeline-item');
                        timelineItems.forEach(item => {{
                            const dateEl = item.querySelector('.timeline-date');
                            const factEl = item.querySelector('.timeline-fact');
                            const partyEl = item.querySelector('.badge');
                            
                            if (dateEl && factEl) {{
                                const date = dateEl.textContent.trim();
                                const fact = factEl.textContent.trim();
                                const party = partyEl ? partyEl.textContent.trim() : '';
                                
                                contentToCopy += `${{date}} - ${{fact}} (${{party}})\\n\\n`;
                            }}
                        }});
                    }} else {{
                        // Copy document sets data (just a basic representation)
                        contentToCopy += 'Case Facts by Document\\n\\n';
                        
                        // This is a simplified version since the full structure would be complex
                        const docsetContainers = document.querySelectorAll('.docset-container');
                        docsetContainers.forEach(container => {{
                            const header = container.querySelector('.docset-header');
                            const title = header.querySelector('span').textContent;
                            contentToCopy += `=== ${{title}} ===\\n`;
                            
                            // Get facts from this document
                            const tableFacts = container.querySelectorAll('tbody tr');
                            tableFacts.forEach(fact => {{
                                const cells = Array.from(fact.querySelectorAll('td'));
                                contentToCopy += `- ${{cells[0].textContent}} | ${{cells[1].textContent}}\\n`;
                            }});
                            
                            contentToCopy += '\\n';
                        }});
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
                    let contentToCsv = '';
                    
                    // Determine which view is active
                    const tableContent = document.getElementById('table-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    
                    if (tableContent.style.display !== 'none') {{
                        // Export table data
                        const table = document.querySelector('.table-view');
                        const headers = Array.from(table.querySelectorAll('th'))
                            .map(th => th.textContent.trim())
                            .join(',');
                        
                        contentToCsv += headers + '\\n';
                        
                        // Get rows
                        const rows = table.querySelectorAll('tbody tr');
                        rows.forEach(row => {{
                            const rowText = Array.from(row.querySelectorAll('td'))
                                .map(td => '\"' + td.textContent.trim() + '\"')
                                .join(',');
                            
                            contentToCsv += rowText + '\\n';
                        }});
                        
                        // Create link for CSV download
                        const csvContent = "data:text/csv;charset=utf-8," + encodeURIComponent(contentToCsv);
                        const encodedUri = csvContent;
                        const link = document.createElement("a");
                        link.setAttribute("href", encodedUri);
                        link.setAttribute("download", "facts.csv");
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);
                    }} else if (timelineContent.style.display !== 'none') {{
                        // Export timeline data
                        let headers = "Date,Event,Source Text,Page,Document,Document Summary,Party,Status,Evidence,Argument\\n";
                        let rows = '';
                        
                        timelineData.forEach(item => {{
                            const exhibits = item.exhibits ? item.exhibits.join(', ') : '';
                            const sourceText = (item.source_text || '').replace(/"/g, '""');
                            const docSummary = (item.doc_summary || '').replace(/"/g, '""');
                            rows += `"${{item.date}}","${{item.point}}","${{sourceText}}","${{item.page || 'N/A'}}","${{item.doc_name || 'N/A'}}","${{docSummary}}","${{item.party}}","${{item.isDisputed ? 'Disputed' : 'Undisputed'}}","${{exhibits}}","${{item.argId}}. ${{item.argTitle}}"\\n`;
                        }});
                        
                        const csvContent = headers + rows;
                        const encodedUri = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
                        const link = document.createElement("a");
                        link.setAttribute("href", encodedUri);
                        link.setAttribute("download", "timeline.csv");
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);
                    }} else {{
                        alert("CSV export for document sets view is not implemented yet.");
                    }}
                }}
                
                function exportAsPdf() {{
                    alert("PDF export functionality would be implemented here");
                }}
                
                function exportAsWord() {{
                    alert("Word export functionality would be implemented here");
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
                    
                    // Update active view
                    const tableContent = document.getElementById('table-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    if (tableContent.style.display !== 'none') {{
                        renderFacts(tabType);
                    }} else if (timelineContent.style.display !== 'none') {{
                        renderTimeline(tabType);
                    }} else if (docsetContent.style.display !== 'none') {{
                        renderDocumentSets(tabType);
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
                        if (columnIndex === 0) {{
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
                
                // Toggle document set visibility
                function toggleDocSet(docsetId) {{
                    const content = document.getElementById(`docset-content-${{docsetId}}`);
                    const chevron = document.getElementById(`chevron-${{docsetId}}`);
                    
                    if (content.style.display === 'none') {{
                        content.style.display = 'block';
                        chevron.style.transform = 'rotate(90deg)';
                    }} else {{
                        content.style.display = 'none';
                        chevron.style.transform = 'rotate(0deg)';
                    }}
                }}
                
                // Format date for display
                function formatDate(dateString) {{
                    // If it's a range, just return it as is
                    if (dateString.includes('-')) {{
                        return dateString;
                    }}
                    
                    // Try to parse as a date
                    const date = new Date(dateString);
                    if (isNaN(date)) {{
                        return dateString;
                    }}
                    
                    // Format the date
                    const options = {{ year: 'numeric', month: 'short', day: 'numeric' }};
                    return date.toLocaleDateString(undefined, options);
                }}
                
                // Helper to extract year from date
                function getYear(dateString) {{
                    if (dateString.includes('-')) {{
                        return dateString.split('-')[0];
                    }}
                    
                    const date = new Date(dateString);
                    if (isNaN(date)) {{
                        return '';
                    }}
                    
                    return date.getFullYear().toString();
                }}
                
                // Render enhanced timeline view
                function renderTimeline(tabType = 'all') {{
                    const container = document.getElementById('timeline-events');
                    container.innerHTML = '';
                    
                    // Filter timeline data based on tab type
                    let filteredData = timelineData;
                    if (tabType === 'disputed') {{
                        filteredData = timelineData.filter(item => item.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredData = timelineData.filter(item => !item.isDisputed);
                    }}
                    
                    // Sort by date
                    filteredData.sort((a, b) => {{
                        // Handle date ranges like "1950-present"
                        const dateA = a.date.split('-')[0];
                        const dateB = b.date.split('-')[0];
                        return new Date(dateA) - new Date(dateB);
                    }});
                    
                    // Track years for year markers
                    let currentYear = '';
                    let prevYear = '';
                    
                    // Create timeline items
                    filteredData.forEach(fact => {{
                        // Get the year and check if we need a year marker
                        currentYear = getYear(fact.date);
                        if (currentYear && currentYear !== prevYear) {{
                            // Add year marker
                            const yearMarker = document.createElement('div');
                            yearMarker.className = 'timeline-year-marker';
                            yearMarker.innerHTML = `
                                <div class="timeline-year">${{currentYear}}</div>
                                <div class="timeline-year-line"></div>
                            `;
                            container.appendChild(yearMarker);
                            prevYear = currentYear;
                        }}
                    
                        // Create timeline item
                        const timelineItem = document.createElement('div');
                        timelineItem.className = 'timeline-item';
                        
                        // Create timeline point
                        const timelinePoint = document.createElement('div');
                        timelinePoint.className = `timeline-point${{fact.isDisputed ? ' disputed' : ''}}`;
                        timelineItem.appendChild(timelinePoint);
                        
                        // Create timeline content
                        const contentEl = document.createElement('div');
                        contentEl.className = 'timeline-content';
                        
                        // Create timeline header
                        const headerEl = document.createElement('div');
                        headerEl.className = `timeline-header${{fact.isDisputed ? ' timeline-header-disputed' : ''}}`;
                        
                        // Date
                        const dateEl = document.createElement('div');
                        dateEl.className = 'timeline-date';
                        dateEl.textContent = formatDate(fact.date);
                        headerEl.appendChild(dateEl);
                        
                        // Badges
                        const badgesEl = document.createElement('div');
                        badgesEl.className = 'timeline-badges';
                        
                        // Party badge
                        const partyBadge = document.createElement('span');
                        partyBadge.className = `badge ${{fact.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                        partyBadge.textContent = fact.party;
                        badgesEl.appendChild(partyBadge);
                        
                        // Disputed badge
                        if (fact.isDisputed) {{
                            const disputedBadge = document.createElement('span');
                            disputedBadge.className = 'badge disputed-badge';
                            disputedBadge.textContent = 'Disputed';
                            badgesEl.appendChild(disputedBadge);
                        }}
                        
                        headerEl.appendChild(badgesEl);
                        contentEl.appendChild(headerEl);
                        
                        // Create timeline body
                        const bodyEl = document.createElement('div');
                        bodyEl.className = 'timeline-body';
                        
                        // Fact content
                        const factContent = document.createElement('div');
                        factContent.className = 'timeline-fact';
                        factContent.textContent = fact.point;
                        bodyEl.appendChild(factContent);
                        
                        // Source text
                        if (fact.source_text) {{
                            const sourceTextEl = document.createElement('div');
                            sourceTextEl.className = 'timeline-source-text';
                            sourceTextEl.style.fontSize = '14px';
                            sourceTextEl.style.color = '#4a5568';
                            sourceTextEl.style.fontStyle = 'italic';
                            sourceTextEl.style.marginTop = '8px';
                            sourceTextEl.style.padding = '8px';
                            sourceTextEl.style.backgroundColor = '#f7fafc';
                            sourceTextEl.style.borderRadius = '4px';
                            sourceTextEl.textContent = `"${{fact.source_text}}"`;
                            bodyEl.appendChild(sourceTextEl);
                        }}
                        
                        // Related argument and source
                        const metaEl = document.createElement('div');
                        metaEl.className = 'timeline-meta';
                        metaEl.innerHTML = `
                            <span><strong>Document:</strong> ${{fact.doc_name || 'N/A'}}</span>
                            <span><strong>Page:</strong> ${{fact.page || 'N/A'}}</span>
                            <span><strong>Argument:</strong> ${{fact.argId}}. ${{fact.argTitle}}</span>
                            ${{fact.paragraphs ? '<span><strong>Paragraphs:</strong> ' + fact.paragraphs + '</span>' : ''}}
                            <span><strong>Source:</strong> ${{fact.source}}</span>
                        `;
                        bodyEl.appendChild(metaEl);
                        
                        contentEl.appendChild(bodyEl);
                        
                        // Add footer if there are exhibits
                        if (fact.exhibits && fact.exhibits.length > 0) {{
                            const footerEl = document.createElement('div');
                            footerEl.className = 'timeline-footer';
                            
                            // Add exhibit badges
                            fact.exhibits.forEach(exhibitId => {{
                                const exhibitBadge = document.createElement('span');
                                exhibitBadge.className = 'badge exhibit-badge';
                                exhibitBadge.textContent = exhibitId;
                                footerEl.appendChild(exhibitBadge);
                            }});
                            
                            contentEl.appendChild(footerEl);
                        }}
                        
                        timelineItem.appendChild(contentEl);
                        container.appendChild(timelineItem);
                    }});
                    
                    // If no events found
                    if (filteredData.length === 0) {{
                        container.innerHTML = '<p>No timeline events found matching the selected criteria.</p>';
                    }}
                }}
                
                // Render document sets view
                function renderDocumentSets(tabType = 'all') {{
                    const container = document.getElementById('document-sets-container');
                    container.innerHTML = '';
                    
                    // Filter facts based on tab type
                    let filteredFacts = factsData;
                    if (tabType === 'disputed') {{
                        filteredFacts = factsData.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = factsData.filter(fact => !fact.isDisputed);
                    }}
                    
                    // Initialize docsWithFacts for all groups
                    const docsWithFacts = {{}};
                    
                    // Initialize all groups
                    documentSets.forEach(ds => {{
                        if (ds.isGroup) {{
                            docsWithFacts[ds.id] = {{
                                docset: ds,
                                facts: []
                            }};
                        }}
                    }});
                    
                    // Distribute facts to categories based on document
                    filteredFacts.forEach((fact, index) => {{
                        // Find which document this fact belongs to based on source
                        let factAssigned = false;
                        
                        documentSets.forEach(ds => {{
                            if (ds.isGroup) {{
                                ds.documents.forEach(doc => {{
                                    // Check if the fact's source contains the document number
                                    if (fact.source && fact.source.includes(doc.id + '.')) {{
                                        docsWithFacts[ds.id].facts.push({{ 
                                            ...fact, 
                                            documentName: doc.name
                                        }});
                                        factAssigned = true;
                                    }}
                                }});
                            }}
                        }});
                        
                        // If not assigned by source, assign by party matching
                        if (!factAssigned) {{
                            documentSets.forEach(ds => {{
                                if (ds.isGroup) {{
                                    ds.documents.forEach(doc => {{
                                        if (doc.party === 'Mixed' || 
                                            (fact.party === 'Appellant' && doc.party === 'Appellant') ||
                                            (fact.party === 'Respondent' && doc.party === 'Respondent')) {{
                                            docsWithFacts[ds.id].facts.push({{ 
                                                ...fact, 
                                                documentName: doc.name
                                            }});
                                            factAssigned = true;
                                            return;
                                        }}
                                    }});
                                    if (factAssigned) return;
                                }}
                            }});
                        }}
                    }});
                    
                    // Create document sets UI with direct table display
                    Object.values(docsWithFacts).forEach(docWithFacts => {{
                        const docset = docWithFacts.docset;
                        const facts = docWithFacts.facts;
                        
                        // Create document set container
                        const docsetEl = document.createElement('div');
                        docsetEl.className = 'docset-container';
                        
                        // Create folder header
                        const headerHtml = `
                            <div class="docset-header" onclick="toggleDocSet('${{docset.id}}')">
                                <svg id="chevron-${{docset.id}}" class="chevron expanded" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <svg class="folder-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                                </svg>
                                <span><strong>${{docset.name}}</strong></span>
                                <span style="margin-left: auto;">
                                    <span class="badge ${{docset.party === 'Appellant' ? 'appellant-badge' : (docset.party === 'Respondent' ? 'respondent-badge' : 'shared-badge')}}">
                                        ${{docset.party}}
                                    </span>
                                    <span class="badge">${{facts.length}} facts</span>
                                </span>
                            </div>
                            <div id="docset-content-${{docset.id}}" class="docset-content">
                        `;
                        
                        let contentHtml = '';
                        
                        if (facts.length > 0) {{
                            // Create a single table for all facts in this category
                            contentHtml += `
                                <table class="table-view">
                                    <thead>
                                        <tr>
                                            <th>Date</th>
                                            <th>Event</th>
                                            <th>Source Text</th>
                                            <th>Page</th>
                                            <th>Document</th>
                                            <th>Party</th>
                                            <th>Status</th>
                                            <th>Evidence</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${{facts.map(fact => `
                                            <tr ${{fact.isDisputed ? 'class="disputed"' : ''}}>
                                                <td>${{fact.date}}</td>
                                                <td>${{fact.point}}</td>
                                                <td style="max-width: 300px; overflow: hidden; text-overflow: ellipsis;" title="${{fact.source_text || 'N/A'}}">${{(fact.source_text || 'N/A').substring(0, 100)}}${{(fact.source_text || '').length > 100 ? '...' : ''}}</td>
                                                <td>${{fact.page || 'N/A'}}</td>
                                                <td><strong>${{fact.doc_name || 'N/A'}}</strong></td>
                                                <td>
                                                    <span class="badge ${{fact.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">
                                                        ${{fact.party}}
                                                    </span>
                                                </td>
                                                <td>${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : 'Undisputed'}}</td>
                                                <td>${{fact.exhibits && fact.exhibits.length > 0 
                                                    ? fact.exhibits.map(ex => `<span class="badge exhibit-badge">${{ex}}</span>`).join(' ') 
                                                    : 'None'}}</td>
                                            </tr>
                                        `).join('')}}
                                    </tbody>
                                </table>
                            `;
                        }} else {{
                            contentHtml += '<p style="padding: 12px;">No facts found</p>';
                        }}
                        
                        contentHtml += '</div>';
                        docsetEl.innerHTML = headerHtml + contentHtml;
                        
                        container.appendChild(docsetEl);
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
                        if (fact.isDisputed) {{
                            row.classList.add('disputed');
                        }}
                        
                        // Date column
                        const dateCell = document.createElement('td');
                        dateCell.textContent = fact.date;
                        row.appendChild(dateCell);
                        
                        // Event column
                        const eventCell = document.createElement('td');
                        eventCell.textContent = fact.point;
                        row.appendChild(eventCell);
                        
                        // Source Text column
                        const sourceTextCell = document.createElement('td');
                        sourceTextCell.textContent = fact.source_text || 'N/A';
                        sourceTextCell.style.maxWidth = '300px';
                        sourceTextCell.style.overflow = 'hidden';
                        sourceTextCell.style.textOverflow = 'ellipsis';
                        sourceTextCell.title = fact.source_text || 'N/A';
                        row.appendChild(sourceTextCell);
                        
                        // Page column
                        const pageCell = document.createElement('td');
                        pageCell.textContent = fact.page || 'N/A';
                        row.appendChild(pageCell);
                        
                        // Document column
                        const docCell = document.createElement('td');
                        docCell.innerHTML = `<strong>${fact.doc_name || 'N/A'}</strong>`;
                        docCell.title = fact.doc_summary || 'N/A';
                        row.appendChild(docCell);
                        
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
                
                // Initialize facts on page load
                document.addEventListener('DOMContentLoaded', function() {{
                    renderFacts('all');
                }});
                
                // Initialize facts immediately
                renderFacts('all');
            </script>
        </body>
        </html>
        """
        
        # Render the HTML component
        st.title("Case Facts")
        components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
