import streamlit as st
import streamlit.components.v1 as components
import json

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view and current view type
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"
if 'current_tab_type' not in st.session_state:
    st.session_state.current_tab_type = "all"

# Create data structures (same as original)
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
                    "exhibits": ["C-1", "C-2", "C-4", "R-1"],
                    "source_text": "The club has maintained continuous operation under the same name 'Athletic Club United' since its official registration in 1950, as evidenced by uninterrupted participation in national competitions and consistent use of the same corporate identity throughout this period.",
                    "page": 23,
                    "doc_name": "Statement of Appeal",
                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Historical Registration Documents",
                    "summary": "Official records showing continuous name usage from 1950 to present day. Includes original registration certificate dated January 12, 1950, and all subsequent renewal documentation without interruption.",
                    "citations": ["20", "21", "24"]
                },
                {
                    "id": "C-2", 
                    "title": "Competition Participation Records",
                    "summary": "Complete records of the club's participation in national and regional competitions from 1950 to present, demonstrating uninterrupted competitive activity under the same name and organizational structure.",
                    "citations": ["25", "26", "28"]
                },
                {
                    "id": "C-4",
                    "title": "Media Coverage Archive", 
                    "summary": "Comprehensive collection of newspaper clippings, sports magazines, and media reports spanning 1950-2024 consistently referring to the club by the same name and recognizing its continuous identity.",
                    "citations": ["53", "54", "55"]
                }
            ],
            "children": {
                "1.1": {
                    "id": "1.1",
                    "title": "Club Name Analysis",
                    "paragraphs": "20-45",
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
                                    "source_text": "The club was initially registered with the National Football Federation on January 12, 1950, under registration number NFF-1950-0047, establishing its legal existence as a sporting entity.",
                                    "page": 31,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30",
                                    "exhibits": ["C-2"],
                                    "source_text": "While there was a temporary administrative restructuring during 1975-1976 due to financial difficulties, the club's core operations and identity remained intact throughout this period, with no cessation of sporting activities.",
                                    "page": 35,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
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
                    "factualPoints": [
                        {
                            "point": "Consistent use of blue and white since founding",
                            "date": "1950-present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "51-52",
                            "exhibits": ["C-4"],
                            "source_text": "The club has consistently utilized blue and white as its primary colors since its founding in 1950, with these colors being integral to the club's visual identity and fan recognition throughout its history.",
                            "page": 58,
                            "doc_name": "Statement of Appeal",
                            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
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
                                    "source_text": "Minor variations in the specific shades of blue and white used in uniforms and club materials during the 1970s were purely aesthetic choices that did not alter the fundamental color identity of the club.",
                                    "page": 63,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59",
                                    "exhibits": ["C-5"],
                                    "source_text": "Between 1982 and 1988, the club temporarily incorporated a third accent color (gold) in its uniform design for special occasions, while maintaining blue and white as the primary colors.",
                                    "page": 65,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                }
                            ]
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
                    "source_text": "The club's operations completely ceased during the 1975-1976 season, with no participation in any competitive events and complete absence from all official federation records during this period.",
                    "page": 89,
                    "doc_name": "Answer to Request for Provisional Measures",
                    "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity."
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "Federation Records",
                    "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season. Includes official withdrawal notification dated May 15, 1975.",
                    "citations": ["208", "209", "210"]
                },
                {
                    "id": "R-2",
                    "title": "Financial Audit Reports",
                    "summary": "Independent auditor reports from 1975-1976 documenting the complete cessation of club operations, closure of all bank accounts, and termination of all contractual obligations, establishing a clear operational break.",
                    "citations": ["211", "212", "213"]
                }
            ]
        }
    }
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args
    }

def get_document_sets():
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
            "id": "provisional_measures",
            "name": "provisional measures",
            "party": "Respondent",
            "category": "provisional measures",
            "isGroup": True,
            "documents": [
                {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "category": "provisional measures"},
                {"id": "4", "name": "4. Answer to PM", "party": "Respondent", "category": "provisional measures"}
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

# Get the data
args_data = get_argument_data()
document_sets = get_document_sets()

# Add Streamlit sidebar with navigation buttons (EXACTLY like original)
with st.sidebar:
    # Add the logo and CaseLens text (EXACTLY like original)
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
    
    # Custom CSS for button styling (EXACTLY like original)
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
    
    # Define button click handlers (EXACTLY like original)
    def set_arguments_view():
        st.session_state.view = "Arguments"
        
    def set_facts_view():
        st.session_state.view = "Facts"
        
    def set_exhibits_view():
        st.session_state.view = "Exhibits"
    
    # Create buttons with names (EXACTLY like original)
    st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
    st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
    st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)

# Only show Facts view content (since that's what we're implementing)
if st.session_state.view == "Facts":
    # Main content area will be handled by React component
    
    # Create a simple header with view toggle using Streamlit components (like original)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Card View", use_container_width=True, 
                    type="primary" if st.session_state.current_view_type == "card" else "secondary"):
            st.session_state.current_view_type = "card"
            st.rerun()
    
    with col2:
        if st.button("📅 Timeline View", use_container_width=True,
                    type="primary" if st.session_state.current_view_type == "timeline" else "secondary"):
            st.session_state.current_view_type = "timeline"
            st.rerun()
    
    with col3:
        if st.button("📁 Document Categories", use_container_width=True,
                    type="primary" if st.session_state.current_view_type == "docset" else "secondary"):
            st.session_state.current_view_type = "docset"
            st.rerun()
    
    st.divider()
    
    # Facts filter using selectbox (like original)
    filter_option = st.selectbox(
        "Filter Facts:",
        ["All Facts", "Disputed Facts", "Undisputed Facts"],
        index=0
    )
    
    # Set current tab type based on selection
    if filter_option == "All Facts":
        st.session_state.current_tab_type = "all"
    elif filter_option == "Disputed Facts":
        st.session_state.current_tab_type = "disputed"
    else:
        st.session_state.current_tab_type = "undisputed"
    
    st.divider()
    
    # Now render the React component for the main content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CaseLens Facts View</title>
        <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
        <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <style>
            body {{
                margin: 0;
                font-family: "Source Sans Pro", sans-serif;
                background-color: #ffffff;
                color: #262730;
            }}
            
            .main-content {{
                padding: 0;
            }}
            
            .title {{
                font-size: 2rem;
                font-weight: 600;
                margin-bottom: 2rem;
                color: #262730;
            }}
            
            .fact-card {{
                border: 1px solid #e6e6e6;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
                overflow: hidden;
                background-color: white;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            
            .fact-header {{
                padding: 1rem;
                background-color: #f8f9fa;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #e6e6e6;
                transition: background-color 0.2s;
            }}
            
            .fact-header:hover {{
                background-color: #e9ecef;
            }}
            
            .fact-title {{
                font-weight: 600;
                color: #262730;
            }}
            
            .dispute-indicator {{
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background-color: #dc3545;
            }}
            
            .dispute-indicator.undisputed {{
                background-color: #28a745;
            }}
            
            .fact-content {{
                padding: 1.5rem;
                display: none;
            }}
            
            .fact-content.expanded {{
                display: block;
            }}
            
            .section-header {{
                font-size: 1.1rem;
                font-weight: 600;
                margin: 1.5rem 0 0.75rem 0;
                color: #262730;
            }}
            
            .evidence-item {{
                margin-bottom: 1rem;
                padding: 1rem;
                background-color: #f8f9fa;
                border-radius: 0.5rem;
                border: 1px solid #e6e6e6;
            }}
            
            .evidence-title {{
                font-weight: 600;
                margin-bottom: 0.5rem;
                color: #262730;
            }}
            
            .submission-section {{
                margin: 1rem 0;
            }}
            
            .submission-header {{
                font-weight: 600;
                margin-bottom: 0.5rem;
            }}
            
            .submission-content {{
                padding: 1rem;
                border-radius: 0.5rem;
                font-style: italic;
                border-left: 4px solid;
            }}
            
            .claimant-submission {{
                background-color: #cce5ff;
                border-left-color: #0066cc;
                color: #003d7a;
            }}
            
            .respondent-submission {{
                background-color: #ffe6e6;
                border-left-color: #cc0000;
                color: #7a0000;
            }}
            
            .status-section {{
                display: flex;
                gap: 2rem;
                margin-top: 1rem;
                padding-top: 1rem;
                border-top: 1px solid #e6e6e6;
            }}
            
            .status-item {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            
            .copy-button {{
                padding: 0.25rem 0.5rem;
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.8rem;
                transition: background-color 0.2s;
            }}
            
            .copy-button:hover {{
                background-color: #5a6268;
            }}
            
            .no-facts {{
                text-align: center;
                padding: 3rem;
                color: #6c757d;
                font-style: italic;
            }}
            
            .timeline-year {{
                font-size: 1.5rem;
                font-weight: 600;
                margin: 2rem 0 1rem 0;
                color: #262730;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            
            .timeline-event {{
                margin-bottom: 2rem;
                padding: 1rem;
                border-left: 4px solid #ff6900;
                background-color: #f8f9fa;
                border-radius: 0 0.5rem 0.5rem 0;
            }}
            
            .timeline-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }}
            
            .timeline-date {{
                font-weight: 600;
                color: #ff6900;
            }}
            
            .timeline-title {{
                font-weight: 600;
                flex: 1;
                margin: 0 1rem;
            }}
            
            .docset-container {{
                margin-bottom: 1rem;
            }}
            
            .docset-header {{
                padding: 1rem;
                background-color: #f8f9fa;
                cursor: pointer;
                border: 1px solid #e6e6e6;
                border-radius: 0.5rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: background-color 0.2s;
            }}
            
            .docset-header:hover {{
                background-color: #e9ecef;
            }}
            
            .docset-content {{
                display: none;
                border: 1px solid #e6e6e6;
                border-top: none;
                border-radius: 0 0 0.5rem 0.5rem;
                padding: 1rem;
                background-color: white;
            }}
            
            .docset-content.expanded {{
                display: block;
            }}
            
            .divider {{
                height: 1px;
                background-color: #e6e6e6;
                margin: 1rem 0;
            }}
        </style>
    </head>
    <body>
        <div id="root"></div>

        <script type="text/babel">
            const {{ useState }} = React;

            // Data
            const argumentData = {json.dumps(args_data)};
            const documentSets = {json.dumps(document_sets)};
            const currentViewType = "{st.session_state.current_view_type}";
            const currentTabType = "{st.session_state.current_tab_type}";

            // Utility functions
            const extractFacts = (args, party) => {{
                const facts = [];
                
                const processArg = (arg) => {{
                    if (arg.factualPoints) {{
                        arg.factualPoints.forEach(point => {{
                            facts.push({{
                                event: point.point,
                                date: point.date,
                                isDisputed: point.isDisputed,
                                party: party,
                                paragraphs: point.paragraphs || '',
                                exhibits: point.exhibits || [],
                                argId: arg.id,
                                argTitle: arg.title,
                                source_text: point.source_text || '',
                                page: point.page || '',
                                doc_name: point.doc_name || '',
                                doc_summary: point.doc_summary || ''
                            }});
                        }});
                    }}
                    
                    if (arg.children) {{
                        Object.values(arg.children).forEach(processArg);
                    }}
                }};
                
                Object.values(args).forEach(processArg);
                return facts;
            }};

            const getAllFacts = () => {{
                const claimantFacts = extractFacts(argumentData.claimantArgs, 'Appellant');
                const respondentFacts = extractFacts(argumentData.respondentArgs, 'Respondent');
                
                const allFacts = [...claimantFacts, ...respondentFacts];
                const factGroups = {{}};
                
                allFacts.forEach(fact => {{
                    const key = `${{fact.date}}_${{fact.event.substring(0, 50)}}`;
                    if (!factGroups[key]) {{
                        factGroups[key] = {{
                            event: fact.event,
                            date: fact.date,
                            isDisputed: fact.isDisputed,
                            claimant_submission: '',
                            respondent_submission: '',
                            source_text: fact.source_text,
                            page: fact.page,
                            doc_name: fact.doc_name,
                            doc_summary: fact.doc_summary,
                            exhibits: fact.exhibits,
                            paragraphs: fact.paragraphs,
                            argId: fact.argId,
                            argTitle: fact.argTitle,
                            parties_involved: []
                        }};
                    }}
                    
                    if (fact.party === 'Appellant') {{
                        factGroups[key].claimant_submission = fact.source_text;
                    }} else {{
                        factGroups[key].respondent_submission = fact.source_text;
                    }}
                    
                    factGroups[key].parties_involved.push(fact.party);
                    
                    if (fact.isDisputed) {{
                        factGroups[key].isDisputed = true;
                    }}
                }});
                
                return Object.values(factGroups).map(group => ({{
                    ...group,
                    claimant_submission: group.claimant_submission || 'No specific submission recorded',
                    respondent_submission: group.respondent_submission || 'No specific submission recorded',
                    parties_involved: [...new Set(group.parties_involved)]
                }}));
            }};

            const getEvidenceContent = (fact) => {{
                if (!fact.exhibits || fact.exhibits.length === 0) {{
                    return [];
                }}
                
                const evidenceContent = [];
                
                const findEvidence = (args) => {{
                    for (const argKey in args) {{
                        const arg = args[argKey];
                        if (arg.evidence) {{
                            const evidence = arg.evidence.find(e => fact.exhibits.includes(e.id));
                            if (evidence) {{
                                evidenceContent.push({{
                                    id: evidence.id,
                                    title: evidence.title,
                                    summary: evidence.summary
                                }});
                            }}
                        }}
                        if (arg.children) {{
                            findEvidence(arg.children);
                        }}
                    }}
                }};
                
                findEvidence(argumentData.claimantArgs);
                findEvidence(argumentData.respondentArgs);
                
                fact.exhibits.forEach(exhibitId => {{
                    if (!evidenceContent.find(e => e.id === exhibitId)) {{
                        evidenceContent.push({{
                            id: exhibitId,
                            title: exhibitId,
                            summary: 'Evidence details not available'
                        }});
                    }}
                }});
                
                return evidenceContent;
            }};

            // Components
            const FactCard = ({{ fact, index }}) => {{
                const [expanded, setExpanded] = useState(false);
                const evidenceContent = getEvidenceContent(fact);
                
                return (
                    <div className="fact-card">
                        <div className="fact-header" onClick={{() => setExpanded(!expanded)}}>
                            <div className="fact-title">
                                <strong>{{fact.date}}</strong> - {{fact.event}}
                            </div>
                            <div className={{`dispute-indicator ${{!fact.isDisputed ? 'undisputed' : ''}}`}}></div>
                        </div>
                        <div className={{`fact-content ${{expanded ? 'expanded' : ''}}`}}>
                            <div className="section-header">📁 Evidence & Source References</div>
                            {{evidenceContent.length > 0 ? (
                                evidenceContent.map((evidence, idx) => (
                                    <div key={{idx}} className="evidence-item">
                                        <div className="evidence-title">
                                            <strong>{{evidence.id}}</strong> - {{evidence.title}}
                                        </div>
                                        {{fact.doc_summary && (
                                            <div style={{{{ margin: '0.5rem 0', padding: '0.5rem', backgroundColor: '#cce5ff', borderRadius: '4px', border: '1px solid #b3d9ff' }}}}>
                                                <strong>Document Summary:</strong> {{fact.doc_summary}}
                                            </div>
                                        )}}
                                        {{fact.source_text && (
                                            <div style={{{{ margin: '0.5rem 0', fontStyle: 'italic' }}}}>
                                                <strong>Source Text:</strong> {{fact.source_text}}
                                            </div>
                                        )}}
                                        <div style={{{{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '0.5rem' }}}}>
                                            <div>
                                                <strong>Exhibit:</strong> {{evidence.id}}
                                                {{fact.page && <span> | <strong>Page:</strong> {{fact.page}}</span>}}
                                                {{fact.paragraphs && <span> | <strong>Paragraphs:</strong> {{fact.paragraphs}}</span>}}
                                            </div>
                                            <button className="copy-button" onClick={{() => {{
                                                const refText = `Exhibit: ${{evidence.id}}${{fact.page ? `, Page: ${{fact.page}}` : ''}}${{fact.paragraphs ? `, Paragraphs: ${{fact.paragraphs}}` : ''}}`;
                                                navigator.clipboard.writeText(refText);
                                            }}}}>
                                                📋 Copy Ref
                                            </button>
                                        </div>
                                        {{idx < evidenceContent.length - 1 && <div className="divider"></div>}}
                                    </div>
                                ))
                            ) : (
                                <div style={{{{ fontStyle: 'italic', color: '#6c757d' }}}}>
                                    No evidence references available for this fact
                                </div>
                            )}}
                            
                            <div className="section-header">⚖️ Party Submissions</div>
                            <div className="submission-section">
                                <div className="submission-header">🔵 Claimant Submission</div>
                                <div className="submission-content claimant-submission">
                                    {{fact.claimant_submission === 'No specific submission recorded' ? 
                                        <em>No submission provided</em> : 
                                        fact.claimant_submission
                                    }}
                                </div>
                            </div>
                            <div className="submission-section">
                                <div className="submission-header">🔴 Respondent Submission</div>
                                <div className="submission-content respondent-submission">
                                    {{fact.respondent_submission === 'No specific submission recorded' ? 
                                        <em>No submission provided</em> : 
                                        fact.respondent_submission
                                    }}
                                </div>
                            </div>
                            
                            <div className="section-header">📊 Status</div>
                            <div className="status-section">
                                <div className="status-item">
                                    <strong>Status:</strong> 
                                    <span style={{{{ color: fact.isDisputed ? '#dc3545' : '#28a745', marginLeft: '0.5rem' }}}}>
                                        {{fact.isDisputed ? 'Disputed' : 'Undisputed'}}
                                    </span>
                                </div>
                                {{fact.parties_involved && (
                                    <div className="status-item">
                                        <strong>Parties:</strong> {{fact.parties_involved.join(', ')}}
                                    </div>
                                )}}
                            </div>
                        </div>
                    </div>
                );
            }};

            // Timeline View Component
            const TimelineView = ({{ facts }}) => {{
                const sortedFacts = [...facts].sort((a, b) => {{
                    const dateA = a.date.split('-')[0];
                    const dateB = b.date.split('-')[0];
                    return dateA.localeCompare(dateB);
                }});
                
                // Group by year
                const eventsByYear = {{}};
                sortedFacts.forEach(fact => {{
                    const year = fact.date.split('-')[0];
                    if (!eventsByYear[year]) {{
                        eventsByYear[year] = [];
                    }}
                    eventsByYear[year].push(fact);
                }});
                
                return (
                    <div>
                        {{Object.entries(eventsByYear).map(([year, events]) => (
                            <div key={{year}}>
                                <div className="timeline-year">📅 {{year}}</div>
                                <div className="divider"></div>
                                {{events.map((fact, index) => {{
                                    const evidenceContent = getEvidenceContent(fact);
                                    return (
                                        <div key={{index}} className="timeline-event">
                                            <div className="timeline-header">
                                                <div className="timeline-date">📆 {{fact.date}}</div>
                                                <div className="timeline-title">{{fact.event}}</div>
                                                <div className={{`dispute-indicator ${{!fact.isDisputed ? 'undisputed' : ''}}`}}></div>
                                            </div>
                                            
                                            <div style={{{{ marginTop: '1rem' }}}}>
                                                <div className="section-header">📁 Evidence & Source References</div>
                                                {{evidenceContent.length > 0 ? (
                                                    evidenceContent.map((evidence, idx) => (
                                                        <div key={{idx}} style={{{{ marginBottom: '1rem' }}}}>
                                                            <div>• <strong>{{evidence.id}}</strong> - {{evidence.title}}</div>
                                                            {{fact.doc_summary && (
                                                                <div style={{{{ margin: '0.5rem 0', padding: '0.5rem', backgroundColor: '#cce5ff', borderRadius: '4px', border: '1px solid #b3d9ff' }}}}>
                                                                    <strong>Document Summary:</strong> {{fact.doc_summary}}
                                                                </div>
                                                            )}}
                                                            {{fact.source_text && (
                                                                <div style={{{{ margin: '0.5rem 0', fontStyle: 'italic' }}}}>
                                                                    <strong>Source Text:</strong> {{fact.source_text}}
                                                                </div>
                                                            )}}
                                                        </div>
                                                    ))
                                                ) : (
                                                    <div style={{{{ fontStyle: 'italic', color: '#6c757d' }}}}>
                                                        No evidence references available
                                                    </div>
                                                )}}
                                                
                                                <div className="section-header">⚖️ Party Submissions</div>
                                                <div className="submission-section">
                                                    <div className="submission-header">🔵 Claimant Submission</div>
                                                    <div className="submission-content claimant-submission">
                                                        {{fact.claimant_submission === 'No specific submission recorded' ? 
                                                            <em>No submission provided</em> : 
                                                            fact.claimant_submission
                                                        }}
                                                    </div>
                                                </div>
                                                <div className="submission-section">
                                                    <div className="submission-header">🔴 Respondent Submission</div>
                                                    <div className="submission-content respondent-submission">
                                                        {{fact.respondent_submission === 'No specific submission recorded' ? 
                                                            <em>No submission provided</em> : 
                                                            fact.respondent_submission
                                                        }}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    );
                                }})}}
                            </div>
                        ))}}
                    </div>
                );
            }};

            // Document Categories View Component
            const DocumentCategoriesView = ({{ facts }}) => {{
                const [expandedDocsets, setExpandedDocsets] = useState({{}});
                
                // Group facts by document categories
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
                
                // Distribute facts to categories
                facts.forEach(fact => {{
                    let factAssigned = false;
                    
                    // Try to assign based on source matching
                    for (const ds of documentSets) {{
                        if (ds.isGroup) {{
                            for (const doc of ds.documents) {{
                                if (fact.source && fact.source.includes(doc.id + '.')) {{
                                    docsWithFacts[ds.id].facts.push({{
                                        ...fact,
                                        documentName: doc.name
                                    }});
                                    factAssigned = true;
                                    break;
                                }}
                            }}
                            if (factAssigned) break;
                        }}
                    }}
                    
                    // If not assigned by source, assign by party matching
                    if (!factAssigned) {{
                        for (const ds of documentSets) {{
                            if (ds.isGroup) {{
                                for (const doc of ds.documents) {{
                                    const parties = fact.parties_involved || [];
                                    if (doc.party === 'Mixed' || 
                                        (doc.party === 'Appellant' && parties.includes('Appellant')) ||
                                        (doc.party === 'Respondent' && parties.includes('Respondent'))) {{
                                        docsWithFacts[ds.id].facts.push({{
                                            ...fact,
                                            documentName: doc.name
                                        }});
                                        factAssigned = true;
                                        break;
                                    }}
                                }}
                                if (factAssigned) break;
                            }}
                        }}
                    }}
                }});
                
                const toggleDocset = (docsetId) => {{
                    setExpandedDocsets(prev => ({{
                        ...prev,
                        [docsetId]: !prev[docsetId]
                    }}));
                }};
                
                return (
                    <div>
                        {{Object.entries(docsWithFacts).map(([docsetId, docWithFacts]) => {{
                            const docset = docWithFacts.docset;
                            const docsetFacts = docWithFacts.facts;
                            
                            const partyColor = docset.party === 'Appellant' ? '🔵' : 
                                             docset.party === 'Respondent' ? '🔴' : '⚪';
                            
                            return (
                                <div key={{docsetId}} className="docset-container">
                                    <div className="docset-header" onClick={{() => toggleDocset(docsetId)}}>
                                        <div>📁 {{partyColor}} <strong>{{docset.name}}</strong> ({{docsetFacts.length}} facts)</div>
                                        <div>{{expandedDocsets[docsetId] ? '▼' : '▶'}}</div>
                                    </div>
                                    <div className={{`docset-content ${{expandedDocsets[docsetId] ? 'expanded' : ''}}`}}>
                                        {{docsetFacts.length > 0 ? (
                                            docsetFacts.map((fact, index) => {{
                                                const evidenceContent = getEvidenceContent(fact);
                                                return (
                                                    <div key={{index}} style={{{{ marginBottom: '2rem', paddingBottom: '1rem', borderBottom: index < docsetFacts.length - 1 ? '1px solid #e6e6e6' : 'none' }}}}>
                                                        <div style={{{{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}}}>
                                                            <div><strong>{{fact.date}}</strong></div>
                                                            <div style={{{{ flex: 1, margin: '0 1rem' }}}}><strong>{{fact.event}}</strong></div>
                                                            <div className={{`dispute-indicator ${{!fact.isDisputed ? 'undisputed' : ''}}`}}></div>
                                                        </div>
                                                        
                                                        <div className="section-header">📁 Evidence & Source References</div>
                                                        {{evidenceContent.length > 0 ? (
                                                            evidenceContent.map((evidence, idx) => (
                                                                <div key={{idx}} style={{{{ marginBottom: '1rem' }}}}>
                                                                    <div>• <strong>{{evidence.id}}</strong> - {{evidence.title}}</div>
                                                                    {{fact.doc_summary && (
                                                                        <div style={{{{ margin: '0.5rem 0', padding: '0.5rem', backgroundColor: '#cce5ff', borderRadius: '4px', border: '1px solid #b3d9ff' }}}}>
                                                                            <strong>Document Summary:</strong> {{fact.doc_summary}}
                                                                        </div>
                                                                    )}}
                                                                    {{fact.source_text && (
                                                                        <div style={{{{ margin: '0.5rem 0', fontStyle: 'italic' }}}}>
                                                                            <strong>Source Text:</strong> {{fact.source_text}}
                                                                        </div>
                                                                    )}}
                                                                </div>
                                                            ))
                                                        ) : (
                                                            <div style={{{{ fontStyle: 'italic', color: '#6c757d' }}}}>
                                                                No evidence references available
                                                            </div>
                                                        )}}
                                                        
                                                        <div className="section-header">⚖️ Party Submissions</div>
                                                        <div className="submission-section">
                                                            <div className="submission-header">🔵 Claimant Submission</div>
                                                            <div className="submission-content claimant-submission">
                                                                {{fact.claimant_submission === 'No specific submission recorded' ? 
                                                                    <em>No submission provided</em> : 
                                                                    fact.claimant_submission
                                                                }}
                                                            </div>
                                                        </div>
                                                        <div className="submission-section">
                                                            <div className="submission-header">🔴 Respondent Submission</div>
                                                            <div className="submission-content respondent-submission">
                                                                {{fact.respondent_submission === 'No specific submission recorded' ? 
                                                                    <em>No submission provided</em> : 
                                                                    fact.respondent_submission
                                                                }}
                                                            </div>
                                                        </div>
                                                    </div>
                                                );
                                            }})
                                        ) : (
                                            <div className="no-facts">No facts found in this document category.</div>
                                        )}}
                                    </div>
                                </div>
                            );
                        }})}}
                    </div>
                );
            }};

            // Main App Component
            const FactsMainContent = () => {{
                const allFacts = getAllFacts();
                
                const getFilteredFacts = () => {{
                    switch (currentTabType) {{
                        case 'disputed':
                            return allFacts.filter(fact => fact.isDisputed);
                        case 'undisputed':
                            return allFacts.filter(fact => !fact.isDisputed);
                        default:
                            return allFacts;
                    }}
                }};
                
                const filteredFacts = getFilteredFacts();
                
                const renderContent = () => {{
                    switch (currentViewType) {{
                        case 'timeline':
                            return <TimelineView facts={{filteredFacts}} />;
                        case 'docset':
                            return <DocumentCategoriesView facts={{filteredFacts}} />;
                        default:
                            return (
                                <div>
                                    {{filteredFacts.length > 0 ? (
                                        filteredFacts.map((fact, index) => (
                                            <FactCard key={{index}} fact={{fact}} index={{index}} />
                                        ))
                                    ) : (
                                        <div className="no-facts">No facts found matching the selected criteria.</div>
                                    )}}
                                </div>
                            );
                    }}
                }};
                
                return (
                    <div className="main-content">
                        {{renderContent()}}
                    </div>
                );
            }};

            ReactDOM.render(<FactsMainContent />, document.getElementById('root'));
        </script>
    </body>
    </html>
    """
    
    # Render the React component
    components.html(html_content, height=700, scrolling=True)

else:
    # Show placeholder for other views
    st.title(f"{st.session_state.view}")
    st.info(f"{st.session_state.view} view is not implemented in this demo. Only the Facts view with React components is available.")
    st.markdown("---")
    st.markdown("### Available Features in Facts View:")
    st.markdown("""
    - **Card View**: Expandable fact cards with detailed evidence and submissions
    - **Timeline View**: Chronological display of case events grouped by year
    - **Document Categories**: Facts organized by document categories with party indicators
    - **Filtering**: Filter by All Facts, Disputed Facts, or Undisputed Facts
    - **Evidence Tracking**: Links to specific exhibits and source documents
    - **Copy References**: Easy copying of citation references
    """)
