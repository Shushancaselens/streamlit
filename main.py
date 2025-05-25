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
    # Create sample facts with the new required fields
    facts = [
        {
            'date': '1950-01-12',
            'end_date': '',
            'event': 'Club founded and officially registered in the Football Federation',
            'source_text': 'The club was established on January 12, 1950, with official registration documents filed with the National Football Federation showing continuous operation under the same name and colors.',
            'page': '18,19',
            'doc_name': 'Statement of Appeal',
            'doc_summary': 'Primary appeal document establishing the foundation and continuous operation of the sporting club since 1950.'
        },
        {
            'date': '1950-01-12',
            'end_date': 'present',
            'event': 'Continuous operation under same name since 1950',
            'source_text': 'Official records demonstrate uninterrupted name usage and operational continuity from the date of founding through the present day, establishing a clear line of sporting succession.',
            'page': '20,21,24',
            'doc_name': 'Historical Registration Documents',
            'doc_summary': 'Comprehensive collection documenting the club\'s continuous legal existence and operational history.'
        },
        {
            'date': '1955-05-20',
            'end_date': '',
            'event': 'First National Championship won',
            'source_text': 'The club achieved its first major sporting success by winning the National Championship, establishing its competitive credentials and public recognition.',
            'page': '45,46',
            'doc_name': 'Appeal Brief',
            'doc_summary': 'Supporting documentation detailing the club\'s sporting achievements and competitive history.'
        },
        {
            'date': '1956-03-10',
            'end_date': '',
            'event': 'Club colors established as blue and white',
            'source_text': 'Official adoption of blue and white as the club\'s identifying colors, documented in federation records and consistently maintained throughout the club\'s history.',
            'page': '51,52',
            'doc_name': 'Club Colors Analysis',
            'doc_summary': 'Analysis of the club\'s visual identity elements and their consistency over time.'
        },
        {
            'date': '1962-09-15',
            'end_date': '',
            'event': 'First international competition participation',
            'source_text': 'The club participated in its first international competition, marking its entry into continental sporting events and establishing international recognition.',
            'page': '78,79',
            'doc_name': 'International Competition Records',
            'doc_summary': 'Documentation of the club\'s participation in international sporting competitions.'
        },
        {
            'date': '1970-01-01',
            'end_date': '1980-12-31',
            'event': 'Minor variations in club color shades introduced',
            'source_text': 'During this period, minor variations in the specific shades of blue and white were observed, but the core color scheme remained consistent with the club\'s established identity.',
            'page': '56,57',
            'doc_name': 'Color Variations Analysis',
            'doc_summary': 'Detailed analysis of minor variations in club colors and their impact on continuity.'
        },
        {
            'date': '1975-04-30',
            'end_date': '',
            'event': 'Administrative operations halted due to financial difficulties',
            'source_text': 'The club faced significant financial challenges leading to a temporary halt in administrative operations, though the legal entity remained in existence.',
            'page': '206,207',
            'doc_name': 'Answer to Request for PM',
            'doc_summary': 'Respondent\'s documentation of the club\'s financial difficulties and operational challenges.'
        },
        {
            'date': '1975-05-15',
            'end_date': '1976-09-14',
            'event': 'Operations ceased between 1975-1976',
            'source_text': 'Federation records indicate a complete absence of the club from all levels of competition during the 1975-1976 season, with official withdrawal notification filed.',
            'page': '208,209,210',
            'doc_name': 'Federation Records',
            'doc_summary': 'Official competition records showing the club\'s absence from competitive activities during this period.'
        },
        {
            'date': '1976-09-15',
            'end_date': '',
            'event': 'New entity registered with similar name',
            'source_text': 'A new sporting entity was registered with a similar name and claimed succession rights, leading to the current dispute over sporting succession and identity.',
            'page': '212,213',
            'doc_name': 'Registration Gap Evidence',
            'doc_summary': 'Evidence documenting the registration of a new entity and claims to sporting succession.'
        },
        {
            'date': '1976-10-01',
            'end_date': '',
            'event': 'Significant color scheme change implemented',
            'source_text': 'The newly registered entity implemented changes to the traditional blue and white color scheme, raising questions about continuity of visual identity.',
            'page': '65,66',
            'doc_name': 'Brief on Admissibility',
            'doc_summary': 'Analysis of changes to the club\'s visual identity and their significance for succession claims.'
        },
        {
            'date': '1982-01-01',
            'end_date': '1988-12-31',
            'event': 'Third color temporarily added to uniform',
            'source_text': 'A third color was temporarily incorporated into the team uniform design, representing a period of experimentation with the club\'s visual identity.',
            'page': '58,59',
            'doc_name': 'Color Variations Analysis',
            'doc_summary': 'Documentation of temporary modifications to the club\'s color scheme during the 1980s.'
        },
        {
            'date': '1987-06-24',
            'end_date': '',
            'event': 'Club won Continental Cup with post-1976 team',
            'source_text': 'The club achieved significant success by winning the Continental Cup, demonstrating competitive continuity and sporting excellence under the post-1976 organization.',
            'page': '95,96',
            'doc_name': 'Statement of Appeal',
            'doc_summary': 'Evidence of the club\'s continued sporting success and competitive achievements.'
        },
        {
            'date': '1989-08-12',
            'end_date': '',
            'event': 'Return to original blue and white color scheme',
            'source_text': 'The club returned to its traditional blue and white colors, restoring the visual identity consistent with its historical appearance.',
            'page': '67,68',
            'doc_name': 'Club Colors Analysis',
            'doc_summary': 'Documentation of the restoration of the club\'s traditional color scheme.'
        },
        {
            'date': '1995-11-30',
            'end_date': '',
            'event': 'Trademark registration for club name and emblem',
            'source_text': 'The club secured legal protection for its name and emblem through trademark registration, establishing formal intellectual property rights.',
            'page': '125,126',
            'doc_name': 'Club Name Analysis',
            'doc_summary': 'Legal documentation of trademark protections for the club\'s identifying elements.'
        },
        {
            'date': '2010-05-18',
            'end_date': '',
            'event': 'Federation officially recognizes club history spanning pre and post 1976',
            'source_text': 'The National Football Federation issued an official recognition acknowledging the club\'s continuous history spanning both pre-1976 and post-1976 periods.',
            'page': '145,146,147',
            'doc_name': 'Reply to Objection to Admissibility',
            'doc_summary': 'Official federation recognition of the club\'s historical continuity and sporting succession.'
        }
    ]
    
    return facts

# Get enhanced timeline data with additional events
def get_timeline_data():
    # Use the same data as facts for consistency
    return get_all_facts()

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
                    max-width: 300px;
                    word-wrap: break-word;
                }}
                
                .table-view td.text-column {{
                    max-width: 250px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;
                }}
                
                .table-view td.summary-column {{
                    max-width: 200px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;
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
                    </div>
                    
                    <!-- Table View -->
                    <div id="table-view-content" class="facts-content">
                        <table class="table-view">
                            <thead>
                                <tr>
                                    <th onclick="sortTable('facts-table-body', 0)">Date</th>
                                    <th onclick="sortTable('facts-table-body', 1)">End Date</th>
                                    <th onclick="sortTable('facts-table-body', 2)">Event</th>
                                    <th onclick="sortTable('facts-table-body', 3)">Source Text</th>
                                    <th onclick="sortTable('facts-table-body', 4)">Page</th>
                                    <th onclick="sortTable('facts-table-body', 5)">Document Name</th>
                                    <th onclick="sortTable('facts-table-body', 6)">Document Summary</th>
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
                            
                            if (dateEl && factEl) {{
                                const date = dateEl.textContent.trim();
                                const fact = factEl.textContent.trim();
                                
                                contentToCopy += `${{date}} - ${{fact}}\\n\\n`;
                            }}
                        }});
                    }} else {{
                        // Copy document sets data
                        contentToCopy += 'Case Facts by Document\\n\\n';
                        
                        const docsetContainers = document.querySelectorAll('.docset-container');
                        docsetContainers.forEach(container => {{
                            const header = container.querySelector('.docset-header');
                            const title = header.querySelector('span').textContent;
                            contentToCopy += `=== ${{title}} ===\\n`;
                            
                            // Get facts from this document
                            const tableFacts = container.querySelectorAll('tbody tr');
                            tableFacts.forEach(fact => {{
                                const cells = Array.from(fact.querySelectorAll('td'));
                                if (cells.length >= 3) {{
                                    contentToCopy += `- ${{cells[0].textContent}} | ${{cells[2].textContent}}\\n`;
                                }}
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
                        let headers = "Date,End Date,Event,Source Text,Page,Document Name,Document Summary\\n";
                        let rows = '';
                        
                        timelineData.forEach(item => {{
                            rows += `"${{item.date}}","${{item.end_date || ''}}","${{item.event}}","${{item.source_text}}","${{item.page}}","${{item.doc_name}}","${{item.doc_summary}}"\\n`;
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
                        // Export document sets data
                        let headers = "Document Name,Date,End Date,Event,Source Text,Page\\n";
                        let rows = '';
                        
                        factsData.forEach(item => {{
                            rows += `"${{item.doc_name}}","${{item.date}}","${{item.end_date || ''}}","${{item.event}}","${{item.source_text}}","${{item.page}}"\\n`;
                        }});
                        
                        const csvContent = headers + rows;
                        const encodedUri = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
                        const link = document.createElement("a");
                        link.setAttribute("href", encodedUri);
                        link.setAttribute("download", "document_facts.csv");
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);
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
                    
                    // Remove active class from all
                    allBtn.classList.remove('active');
                    
                    // Add active to selected (only 'all' now)
                    allBtn.classList.add('active');
                    renderFacts('all');
                    
                    // Update active view
                    const tableContent = document.getElementById('table-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    if (tableContent.style.display !== 'none') {{
                        renderFacts('all');
                    }} else if (timelineContent.style.display !== 'none') {{
                        renderTimeline('all');
                    }} else if (docsetContent.style.display !== 'none') {{
                        renderDocumentSets('all');
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
                    
                    // Use all timeline data (no filtering by disputed status since new structure doesn't have it)
                    let filteredData = timelineData;
                    
                    // Sort by date
                    filteredData.sort((a, b) => {{
                        return new Date(a.date) - new Date(b.date);
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
                        timelinePoint.className = 'timeline-point';
                        timelineItem.appendChild(timelinePoint);
                        
                        // Create timeline content
                        const contentEl = document.createElement('div');
                        contentEl.className = 'timeline-content';
                        
                        // Create timeline header
                        const headerEl = document.createElement('div');
                        headerEl.className = 'timeline-header';
                        
                        // Date
                        const dateEl = document.createElement('div');
                        dateEl.className = 'timeline-date';
                        dateEl.textContent = formatDate(fact.date) + (fact.end_date ? ' - ' + formatDate(fact.end_date) : '');
                        headerEl.appendChild(dateEl);
                        
                        // Page badge
                        const badgesEl = document.createElement('div');
                        badgesEl.className = 'timeline-badges';
                        
                        const pageBadge = document.createElement('span');
                        pageBadge.className = 'badge exhibit-badge';
                        pageBadge.textContent = 'Page ' + fact.page;
                        badgesEl.appendChild(pageBadge);
                        
                        headerEl.appendChild(badgesEl);
                        contentEl.appendChild(headerEl);
                        
                        // Create timeline body
                        const bodyEl = document.createElement('div');
                        bodyEl.className = 'timeline-body';
                        
                        // Event content
                        const eventContent = document.createElement('div');
                        eventContent.className = 'timeline-fact';
                        eventContent.innerHTML = `<strong>${{fact.event}}</strong>`;
                        bodyEl.appendChild(eventContent);
                        
                        // Source text
                        const sourceContent = document.createElement('div');
                        sourceContent.style.marginTop = '8px';
                        sourceContent.style.fontSize = '14px';
                        sourceContent.style.color = '#666';
                        sourceContent.textContent = fact.source_text;
                        bodyEl.appendChild(sourceContent);
                        
                        // Document info
                        const metaEl = document.createElement('div');
                        metaEl.className = 'timeline-meta';
                        metaEl.innerHTML = `
                            <span><strong>Document:</strong> ${{fact.doc_name}}</span>
                            <span><strong>Page:</strong> ${{fact.page}}</span>
                        `;
                        bodyEl.appendChild(metaEl);
                        
                        contentEl.appendChild(bodyEl);
                        
                        // Add footer with document summary
                        const footerEl = document.createElement('div');
                        footerEl.className = 'timeline-footer';
                        footerEl.style.fontSize = '13px';
                        footerEl.style.fontStyle = 'italic';
                        footerEl.textContent = fact.doc_summary;
                        contentEl.appendChild(footerEl);
                        
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
                    
                    // Group facts by document name
                    const docGroups = {{}};
                    
                    factsData.forEach(fact => {{
                        if (!docGroups[fact.doc_name]) {{
                            docGroups[fact.doc_name] = {{
                                name: fact.doc_name,
                                summary: fact.doc_summary,
                                facts: []
                            }};
                        }}
                        docGroups[fact.doc_name].facts.push(fact);
                    }});
                    
                    // Create document sets UI
                    Object.values(docGroups).forEach(docGroup => {{
                        // Create document set container
                        const docsetEl = document.createElement('div');
                        docsetEl.className = 'docset-container';
                        
                        // Create folder header
                        const headerHtml = `
                            <div class="docset-header" onclick="toggleDocSet('${{docGroup.name.replace(/\s+/g, '_')}}')">
                                <svg id="chevron-${{docGroup.name.replace(/\s+/g, '_')}}" class="chevron expanded" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <svg class="folder-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                                </svg>
                                <span><strong>${{docGroup.name}}</strong></span>
                                <span style="margin-left: auto;">
                                    <span class="badge">${{docGroup.facts.length}} facts</span>
                                </span>
                            </div>
                            <div id="docset-content-${{docGroup.name.replace(/\s+/g, '_')}}" class="docset-content">
                                <div style="padding: 12px; background: #f8f9fa; font-style: italic; border-bottom: 1px solid #dee2e6;">
                                    ${{docGroup.summary}}
                                </div>
                        `;
                        
                        let contentHtml = '';
                        
                        if (docGroup.facts.length > 0) {{
                            // Create a table for facts in this document
                            contentHtml += `
                                <table class="table-view">
                                    <thead>
                                        <tr>
                                            <th>Date</th>
                                            <th>End Date</th>
                                            <th>Event</th>
                                            <th>Source Text</th>
                                            <th>Page</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${{docGroup.facts.map(fact => `
                                            <tr>
                                                <td>${{fact.date}}</td>
                                                <td>${{fact.end_date || '-'}}</td>
                                                <td><strong>${{fact.event}}</strong></td>
                                                <td style="max-width: 400px; overflow: hidden; text-overflow: ellipsis;">${{fact.source_text}}</td>
                                                <td>${{fact.page}}</td>
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
                    
                    // Filter by type - for now showing all since we don't have disputed info in new structure
                    let filteredFacts = factsData;
                    
                    // Sort by date
                    filteredFacts.sort((a, b) => {{
                        return new Date(a.date) - new Date(b.date);
                    }});
                    
                    // Render rows
                    filteredFacts.forEach(fact => {{
                        const row = document.createElement('tr');
                        
                        // Date column
                        const dateCell = document.createElement('td');
                        dateCell.textContent = fact.date;
                        row.appendChild(dateCell);
                        
                        // End Date column
                        const endDateCell = document.createElement('td');
                        endDateCell.textContent = fact.end_date || '-';
                        row.appendChild(endDateCell);
                        
                        // Event column
                        const eventCell = document.createElement('td');
                        eventCell.textContent = fact.event;
                        row.appendChild(eventCell);
                        
                        // Source Text column
                        const sourceTextCell = document.createElement('td');
                        sourceTextCell.className = 'text-column';
                        sourceTextCell.textContent = fact.source_text;
                        sourceTextCell.title = fact.source_text; // Show full text on hover
                        row.appendChild(sourceTextCell);
                        
                        // Page column
                        const pageCell = document.createElement('td');
                        pageCell.textContent = fact.page;
                        row.appendChild(pageCell);
                        
                        // Document Name column
                        const docNameCell = document.createElement('td');
                        docNameCell.textContent = fact.doc_name;
                        row.appendChild(docNameCell);
                        
                        // Document Summary column
                        const docSummaryCell = document.createElement('td');
                        docSummaryCell.className = 'summary-column';
                        docSummaryCell.textContent = fact.doc_summary;
                        docSummaryCell.title = fact.doc_summary; // Show full text on hover
                        row.appendChild(docSummaryCell);
                        
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
