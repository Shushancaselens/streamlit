import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config with better styling
st.set_page_config(
    page_title="CaseLens - Legal Arguments Analysis", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "CaseLens - Advanced Legal Case Analysis Platform"
    }
)

# Enhanced CSS styling
st.markdown("""
<style>
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2D3748 0%, #1A202C 100%);
    }
    
    /* Button improvements */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 55px;
        margin-bottom: 12px;
        transition: all 0.3s ease;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Primary button styling */
    .stButton > button[data-baseweb="button"][kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Secondary button styling */
    .stButton > button[data-baseweb="button"][kind="secondary"] {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 10px;
        border: 1px solid #dee2e6;
        font-weight: 600;
    }
    
    /* Info boxes */
    .stInfo {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 5px solid #28a745;
        border-radius: 8px;
    }
    
    /* Warning boxes */
    .stWarning {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        border-left: 5px solid #ffc107;
        border-radius: 8px;
    }
    
    /* Error boxes */
    .stError {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        border-left: 5px solid #dc3545;
        border-radius: 8px;
    }
    
    /* Success boxes */
    .stSuccess {
        background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
        border-left: 5px solid #17a2b8;
        border-radius: 8px;
    }
    
    /* Custom card styling */
    .fact-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        border-left: 5px solid;
        transition: all 0.3s ease;
    }
    
    .fact-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .disputed-card {
        border-left-color: #dc3545;
    }
    
    .undisputed-card {
        border-left-color: #28a745;
    }
    
    /* Typography improvements */
    h1 {
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        color: #34495e;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #5a6c7d;
        font-weight: 500;
    }
    
    /* Metric styling */
    .metric-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Timeline styling */
    .timeline-event {
        border-left: 3px solid #667eea;
        padding-left: 20px;
        margin-bottom: 25px;
        position: relative;
    }
    
    .timeline-event::before {
        content: '';
        width: 12px;
        height: 12px;
        background: #667eea;
        border-radius: 50%;
        position: absolute;
        left: -7.5px;
        top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state to track selected view and current view type
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"

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

# Get all facts from the data with enhanced submissions structure
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
                    'event': point['point'],  # Renamed from 'point' to 'event'
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
                    'doc_summary': point.get('doc_summary', ''),
                    'claimant_submission': '',
                    'respondent_submission': ''
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
    
    # Now enhance facts with both parties' submissions
    enhanced_facts = []
    fact_groups = {}
    
    # Group facts by date and similar events
    for fact in facts:
        key = f"{fact['date']}_{fact['event'][:50]}"  # Group by date and first 50 chars of event
        if key not in fact_groups:
            fact_groups[key] = {
                'event': fact['event'],
                'date': fact['date'],
                'isDisputed': fact['isDisputed'],
                'claimant_submission': '',
                'respondent_submission': '',
                'source_text': fact['source_text'],
                'page': fact['page'],
                'doc_name': fact['doc_name'],
                'doc_summary': fact['doc_summary'],
                'exhibits': fact['exhibits'],
                'paragraphs': fact['paragraphs'],
                'argId': fact['argId'],
                'argTitle': fact['argTitle'],
                'parties_involved': []
            }
        
        # Add party-specific information
        if fact['party'] == 'Appellant':
            fact_groups[key]['claimant_submission'] = fact['source_text']
        else:
            fact_groups[key]['respondent_submission'] = fact['source_text']
        
        fact_groups[key]['parties_involved'].append(fact['party'])
        
        # Update disputed status if either party contests it
        if fact['isDisputed']:
            fact_groups[key]['isDisputed'] = True
    
    # Create enhanced facts with proper submissions structure
    for key, group in fact_groups.items():
        enhanced_fact = {
            'event': group['event'],
            'date': group['date'],
            'isDisputed': group['isDisputed'],
            'source_text': group['source_text'],
            'page': group['page'],
            'doc_name': group['doc_name'],
            'doc_summary': group['doc_summary'],
            'exhibits': group['exhibits'],
            'paragraphs': group['paragraphs'],
            'argId': group['argId'],
            'argTitle': group['argTitle'],
            'claimant_submission': group['claimant_submission'] or 'No specific submission recorded',
            'respondent_submission': group['respondent_submission'] or 'No specific submission recorded',
            'parties_involved': list(set(group['parties_involved']))  # Remove duplicates
        }
        enhanced_facts.append(enhanced_fact)
    
    return enhanced_facts

# Get enhanced timeline data with claimant and respondent submissions
def get_timeline_data():
    # Create enhanced timeline events with both parties' positions
    timeline_events = [
        {
            "event": "Club founded and officially registered in the Football Federation",
            "date": "1950-01-12",
            "isDisputed": False,
            "claimant_submission": "Athletic Club United was officially founded and registered with the National Football Federation on January 12, 1950, marking the beginning of its formal existence as a competitive sporting entity.",
            "respondent_submission": "No specific counter-submission recorded",
            "exhibits": ["C-1"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Statement of Appeal",
            "source_text": "Athletic Club United was officially founded and registered with the National Football Federation on January 12, 1950, marking the beginning of its formal existence as a competitive sporting entity.",
            "page": 15,
            "doc_name": "Statement of Appeal",
            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity.",
            "parties_involved": ["Appellant"]
        },
        {
            "event": "Operations ceased between 1975-1976",
            "date": "1975-1976",
            "isDisputed": True,
            "claimant_submission": "While there was a temporary administrative restructuring during 1975-1976 due to financial difficulties, the club's core operations and identity remained intact throughout this period, with no cessation of sporting activities.",
            "respondent_submission": "Complete cessation of all club operations occurred during the 1975-1976 season, with no team fielded in any competition and complete absence from federation records, constituting a clear break in continuity.",
            "exhibits": ["C-2", "R-1", "R-2"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Both parties - Statement of Appeal & Answer to PM",
            "source_text": "Complete cessation of all club operations occurred during the 1975-1976 season, with no team fielded in any competition and complete absence from federation records, constituting a clear break in continuity.",
            "page": 127,
            "doc_name": "Answer to Request for Provisional Measures",
            "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity.",
            "parties_involved": ["Appellant", "Respondent"]
        },
        {
            "event": "Club colors established as blue and white",
            "date": "1956-03-10",
            "isDisputed": True,
            "claimant_submission": "The club's official colors were formally established as royal blue and white on March 10, 1956, following a unanimous decision by the club's founding committee and ratified by the membership.",
            "respondent_submission": "The newly registered entity adopted a significantly different color scheme incorporating red and yellow as primary colors, abandoning the traditional blue and white entirely for the 1976-1977 season.",
            "exhibits": ["C-4", "R-4"],
            "argId": "1.2",
            "argTitle": "Club Colors Analysis",
            "source": "Appeal - Statement of Appeal",
            "source_text": "The club's official colors were formally established as royal blue and white on March 10, 1956, following a unanimous decision by the club's founding committee and ratified by the membership.",
            "page": 67,
            "doc_name": "Statement of Appeal",
            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity.",
            "parties_involved": ["Appellant", "Respondent"]
        },
        {
            "event": "First National Championship won",
            "date": "1955-05-20",
            "isDisputed": False,
            "claimant_submission": "Athletic Club United achieved its first National Championship victory on May 20, 1955, defeating rivals 3-1 in the final match held at National Stadium, establishing the club's competitive credentials.",
            "respondent_submission": "No specific counter-submission recorded",
            "exhibits": ["C-3"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Appeal Brief",
            "source_text": "Athletic Club United achieved its first National Championship victory on May 20, 1955, defeating rivals 3-1 in the final match held at National Stadium, establishing the club's competitive credentials.",
            "page": 42,
            "doc_name": "Appeal Brief",
            "doc_summary": "Comprehensive brief supporting the appeal with detailed arguments and evidence regarding club continuity and identity.",
            "parties_involved": ["Appellant"]
        },
        {
            "event": "Club registration formally terminated",
            "date": "1975-04-30",
            "isDisputed": True,
            "claimant_submission": "On April 30, 1975, the club's administrative operations were formally halted due to severe financial difficulties, with all staff terminated and offices closed indefinitely, but this was a temporary administrative measure that did not affect the club's legal identity.",
            "respondent_submission": "The club's registration with the National Football Federation was formally terminated on April 30, 1975, following failure to meet financial obligations and regulatory requirements, creating a complete legal break.",
            "exhibits": ["R-2"],
            "argId": "1.1.1",
            "argTitle": "Registration Gap Evidence",
            "source": "provisional measures - Answer to Request for PM",
            "source_text": "The club's registration with the National Football Federation was formally terminated on April 30, 1975, following failure to meet financial obligations and regulatory requirements.",
            "page": 158,
            "doc_name": "Answer to Request for Provisional Measures",
            "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity.",
            "parties_involved": ["Appellant", "Respondent"]
        },
        {
            "event": "New entity registered with similar name",
            "date": "1976-09-15",
            "isDisputed": True,
            "claimant_submission": "The registration in 1976 was a continuation of the same legal entity under identical management and ownership, maintaining all historical rights and obligations of the original club.",
            "respondent_submission": "A new sporting entity was registered on September 15, 1976, under the name 'Athletic Club United FC' - notably different from the original 'Athletic Club United' that had ceased operations, establishing a completely separate legal entity.",
            "exhibits": ["R-2"],
            "argId": "1.1.1",
            "argTitle": "Registration Gap Evidence",
            "source": "provisional measures - Answer to Request for PM",
            "source_text": "A new sporting entity was registered on September 15, 1976, under the name 'Athletic Club United FC' - notably different from the original 'Athletic Club United' that had ceased operations.",
            "page": 162,
            "doc_name": "Answer to Request for Provisional Measures",
            "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity.",
            "parties_involved": ["Appellant", "Respondent"]
        },
        {
            "event": "Federation officially recognizes club history spanning pre and post 1976",
            "date": "2010-05-18",
            "isDisputed": True,
            "claimant_submission": "The National Football Federation issued official recognition on May 18, 2010, acknowledging the club's continuous history from 1950 to present, including the period spanning 1975-1976, providing definitive administrative confirmation of sporting succession.",
            "respondent_submission": "The 2010 federation recognition was a purely administrative convenience that does not override the documented legal and operational discontinuity that occurred in 1975-1976.",
            "exhibits": ["C-10"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "admissibility - Reply to Objection to Admissibility",
            "source_text": "The National Football Federation issued official recognition on May 18, 2010, acknowledging the club's continuous history from 1950 to present, including the period spanning 1975-1976.",
            "page": 234,
            "doc_name": "Reply to Objection to Admissibility",
            "doc_summary": "Appellant's response to respondent's objections regarding the admissibility of certain evidence and arguments.",
            "parties_involved": ["Appellant", "Respondent"]
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

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Helper function to get evidence content
def get_evidence_content(fact):
    if not fact.get('exhibits') or len(fact['exhibits']) == 0:
        return []
    
    # Get evidence details from the argument data
    args_data = get_argument_data()
    evidence_content = []
    
    for exhibit_id in fact['exhibits']:
        # Search through all arguments to find evidence details
        def find_evidence(args):
            for arg_key in args:
                arg = args[arg_key]
                if arg.get('evidence'):
                    evidence = next((e for e in arg['evidence'] if e['id'] == exhibit_id), None)
                    if evidence:
                        return evidence
                if arg.get('children'):
                    child_evidence = find_evidence(arg['children'])
                    if child_evidence:
                        return child_evidence
            return None
        
        # Look in both claimant and respondent args
        evidence = find_evidence(args_data['claimantArgs']) or find_evidence(args_data['respondentArgs'])
        
        if evidence:
            evidence_content.append({
                'id': exhibit_id,
                'title': evidence['title'],
                'summary': evidence['summary']
            })
        else:
            evidence_content.append({
                'id': exhibit_id,
                'title': exhibit_id,
                'summary': 'Evidence details not available'
            })
    
    return evidence_content

# Enhanced Card View with improved styling
def render_streamlit_card_view(filtered_facts=None):
    # Get facts data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    # Sort by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("🔍 No facts found matching the selected criteria.")
        return
    
    # Display summary metrics
    total_facts = len(facts_data)
    disputed_facts = len([f for f in facts_data if f['isDisputed']])
    undisputed_facts = total_facts - disputed_facts
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Total Facts", total_facts, help="Total number of factual points")
    with col2:
        st.metric("⚠️ Disputed", disputed_facts, help="Facts contested by parties")
    with col3:
        st.metric("✅ Undisputed", undisputed_facts, help="Facts accepted by all parties")
    
    st.markdown("---")
    
    # Display each fact as an enhanced card
    for i, fact in enumerate(facts_data):
        # Create a more visually appealing card container
        with st.container():
            # Card header with enhanced styling
            col1, col2 = st.columns([4, 1])
            with col1:
                dispute_icon = "⚠️" if fact['isDisputed'] else "✅"
                st.markdown(f"### {dispute_icon} **{fact['date']}** - {fact['event']}")
            with col2:
                if fact['isDisputed']:
                    st.error("Disputed", icon="⚠️")
                else:
                    st.success("Undisputed", icon="✅")
            
            # Create expandable content with enhanced layout
            with st.expander("📖 View Details", expanded=False):
                # Use tabs for better organization
                tab1, tab2, tab3 = st.tabs(["📁 Evidence", "⚖️ Submissions", "📊 Metadata"])
                
                with tab1:
                    st.subheader("Evidence & Source References")
                    evidence_content = get_evidence_content(fact)
                    
                    if evidence_content:
                        for evidence in evidence_content:
                            with st.container():
                                st.markdown(f"#### 📄 **{evidence['id']}** - {evidence['title']}")
                                
                                # Enhanced info display
                                if fact.get('doc_summary'):
                                    st.info(f"**📋 Document Summary:** {fact['doc_summary']}")
                                
                                if fact.get('source_text'):
                                    st.markdown(f"**📝 Source Text:** *{fact['source_text']}*")
                                
                                # Reference information in columns
                                ref_col1, ref_col2, ref_col3 = st.columns([2, 2, 1])
                                with ref_col1:
                                    if fact.get('page'):
                                        st.markdown(f"**📄 Page:** {fact['page']}")
                                with ref_col2:
                                    if fact.get('paragraphs'):
                                        st.markdown(f"**📑 Paragraphs:** {fact['paragraphs']}")
                                with ref_col3:
                                    if st.button("📋 Copy", key=f"copy_{evidence['id']}_{i}", help="Copy reference"):
                                        st.success("✅ Copied!")
                                
                                st.markdown("---")
                    else:
                        st.warning("⚠️ No evidence references available for this fact")
                
                with tab2:
                    st.subheader("Party Submissions")
                    
                    # Enhanced submission display
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("#### 🔵 **Appellant Position**")
                        claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                        if claimant_text == 'No specific submission recorded':
                            st.info("💡 No submission provided")
                        else:
                            st.info(claimant_text)
                    
                    with col2:
                        st.markdown("#### 🔴 **Respondent Position**")
                        respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                        if respondent_text == 'No specific submission recorded':
                            st.warning("💡 No submission provided")
                        else:
                            st.warning(respondent_text)
                
                with tab3:
                    st.subheader("Case Metadata")
                    
                    meta_col1, meta_col2 = st.columns(2)
                    with meta_col1:
                        st.markdown(f"**🏷️ Argument ID:** {fact.get('argId', 'N/A')}")
                        st.markdown(f"**📂 Argument Title:** {fact.get('argTitle', 'N/A')}")
                    with meta_col2:
                        if fact.get('parties_involved'):
                            st.markdown(f"**👥 Parties Involved:** {', '.join(fact['parties_involved'])}")
                        st.markdown(f"**📖 Document:** {fact.get('doc_name', 'N/A')}")
            
            st.markdown("---")

# Enhanced Timeline View
def render_streamlit_timeline_view(filtered_facts=None):
    # Get facts data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    # Sort by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("🔍 No timeline events found matching the selected criteria.")
        return
    
    # Display summary
    total_events = len(facts_data)
    disputed_events = len([f for f in facts_data if f['isDisputed']])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📅 Timeline Events", total_events)
    with col2:
        st.metric("⚠️ Disputed Events", disputed_events)
    
    st.markdown("---")
    
    # Group by year for year markers
    events_by_year = {}
    for fact in facts_data:
        year = fact['date'].split('-')[0] if '-' in fact['date'] else fact['date'][:4]
        if year not in events_by_year:
            events_by_year[year] = []
        events_by_year[year].append(fact)
    
    # Display timeline events with enhanced styling
    for year, events in events_by_year.items():
        # Year marker with enhanced styling
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 15px; border-radius: 10px; text-align: center; 
                    font-size: 24px; font-weight: bold; margin: 20px 0;">
            📅 {year}
        </div>
        """, unsafe_allow_html=True)
        
        for i, fact in enumerate(events):
            # Enhanced timeline event container
            with st.container():
                # Event header with timeline styling
                col1, col2, col3 = st.columns([2, 4, 1])
                
                with col1:
                    st.markdown(f"**📅 {fact['date']}**")
                
                with col2:
                    st.markdown(f"### {fact['event']}")
                
                with col3:
                    if fact['isDisputed']:
                        st.error("⚠️ Disputed")
                    else:
                        st.success("✅ Agreed")
                
                # Enhanced content display
                with st.expander("🔍 View Event Details", expanded=False):
                    tab1, tab2 = st.tabs(["📁 Evidence", "⚖️ Positions"])
                    
                    with tab1:
                        evidence_content = get_evidence_content(fact)
                        if evidence_content:
                            for evidence in evidence_content:
                                st.markdown(f"**📄 {evidence['id']}** - {evidence['title']}")
                                st.caption(evidence['summary'])
                        else:
                            st.info("📝 No evidence references available")
                    
                    with tab2:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("**🔵 Appellant**")
                            claimant_text = fact.get('claimant_submission', 'No submission')
                            st.info(claimant_text if claimant_text != 'No specific submission recorded' else "No submission provided")
                        
                        with col2:
                            st.markdown("**🔴 Respondent**")
                            respondent_text = fact.get('respondent_submission', 'No submission')
                            st.warning(respondent_text if respondent_text != 'No specific submission recorded' else "No submission provided")
                
                if i < len(events) - 1:
                    st.markdown("---")

# Enhanced Document Categories View
def render_streamlit_docset_view(filtered_facts=None):
    # Get facts and document sets data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
        
    document_sets = get_document_sets()
    
    # Sort facts by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    # Group facts by document categories
    docs_with_facts = {}
    
    # Initialize all groups
    for ds in document_sets:
        if ds.get('isGroup'):
            docs_with_facts[ds['id']] = {
                'docset': ds,
                'facts': []
            }
    
    # Distribute facts to categories (same logic as before)
    for fact in facts_data:
        fact_assigned = False
        
        for ds in document_sets:
            if ds.get('isGroup'):
                for doc in ds.get('documents', []):
                    if fact.get('source') and doc['id'] + '.' in fact['source']:
                        docs_with_facts[ds['id']]['facts'].append({
                            **fact,
                            'documentName': doc['name']
                        })
                        fact_assigned = True
                        break
                if fact_assigned:
                    break
        
        if not fact_assigned:
            for ds in document_sets:
                if ds.get('isGroup'):
                    for doc in ds.get('documents', []):
                        parties = fact.get('parties_involved', [])
                        if (doc['party'] == 'Mixed' or 
                            (doc['party'] == 'Appellant' and 'Appellant' in parties) or
                            (doc['party'] == 'Respondent' and 'Respondent' in parties)):
                            docs_with_facts[ds['id']]['facts'].append({
                                **fact,
                                'documentName': doc['name']
                            })
                            fact_assigned = True
                            break
                    if fact_assigned:
                        break
    
    # Display document categories with enhanced styling
    for docset_id, doc_with_facts in docs_with_facts.items():
        docset = doc_with_facts['docset']
        facts = doc_with_facts['facts']
        
        # Enhanced document category header
        party_color = ("🔵" if docset['party'] == 'Appellant' else 
                      "🔴" if docset['party'] == 'Respondent' else "⚪")
        
        # Create an attractive header for each document category
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    color: white; padding: 15px; border-radius: 10px; margin: 10px 0;">
            <h3>📁 {party_color} {docset['name'].title()} ({len(facts)} facts)</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if facts:
            for i, fact in enumerate(facts):
                with st.container():
                    # Enhanced fact display
                    col1, col2, col3 = st.columns([2, 4, 1])
                    
                    with col1:
                        st.markdown(f"**📅 {fact['date']}**")
                    
                    with col2:
                        st.markdown(f"**{fact['event']}**")
                    
                    with col3:
                        if fact['isDisputed']:
                            st.error("⚠️")
                        else:
                            st.success("✅")
                    
                    # Simplified content display for document view
                    with st.expander("📖 Details", expanded=False):
                        if fact.get('source_text'):
                            st.markdown(f"**📝 Source:** *{fact['source_text']}*")
                        
                        if fact.get('doc_summary'):
                            st.info(f"**📋 Document:** {fact['doc_summary']}")
                        
                        # Quick reference info
                        if fact.get('page') or fact.get('paragraphs'):
                            ref_info = []
                            if fact.get('page'):
                                ref_info.append(f"Page {fact['page']}")
                            if fact.get('paragraphs'):
                                ref_info.append(f"¶{fact['paragraphs']}")
                            st.caption(f"📍 {' | '.join(ref_info)}")
                    
                    if i < len(facts) - 1:
                        st.markdown("---")
        else:
            st.info("🔍 No facts found in this document category.")
        
        st.markdown("<br>", unsafe_allow_html=True)

# Enhanced main app with improved styling
def main():
    # Enhanced sidebar with better styling
    with st.sidebar:
        # Enhanced logo and branding
        st.markdown("""
        <div style="text-align: center; padding: 20px 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; margin-bottom: 30px; color: white;">
            <div style="font-size: 48px; margin-bottom: 10px;">⚖️</div>
            <h1 style="margin: 0; font-weight: 700; color: white;">CaseLens</h1>
            <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.9;">Legal Analysis Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Navigation")
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Enhanced navigation buttons
        current_view = st.session_state.view
        
        if st.button("📑 Arguments Analysis", 
                    key="args_button", 
                    on_click=set_arguments_view, 
                    use_container_width=True,
                    type="primary" if current_view == "Arguments" else "secondary"):
            pass
        
        if st.button("📊 Facts Timeline", 
                    key="facts_button", 
                    on_click=set_facts_view, 
                    use_container_width=True,
                    type="primary" if current_view == "Facts" else "secondary"):
            pass
        
        if st.button("📁 Evidence Library", 
                    key="exhibits_button", 
                    on_click=set_exhibits_view, 
                    use_container_width=True,
                    type="primary" if current_view == "Exhibits" else "secondary"):
            pass
        
        # Enhanced sidebar info
        st.markdown("---")
        st.markdown("### 📈 Case Overview")
        
        # Get case statistics
        all_facts = get_all_facts()
        total_facts = len(all_facts)
        disputed_count = len([f for f in all_facts if f['isDisputed']])
        
        st.metric("Total Facts", total_facts, help="All factual points in the case")
        st.metric("Disputed", disputed_count, help="Facts contested by parties")
        st.metric("Consensus", total_facts - disputed_count, help="Facts agreed upon")
        
        # Case info
        st.markdown("---")
        st.markdown("### ℹ️ Case Information")
        st.markdown("**Case:** Athletic Club United v. Federation")
        st.markdown("**Issue:** Sporting Succession Rights")
        st.markdown("**Status:** Under Review")
    
    # Main content area with enhanced styling
    if st.session_state.view == "Facts":
        # Enhanced title with case context
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h1 style="color: #2c3e50; margin-bottom: 10px;">📊 Case Facts Analysis</h1>
            <p style="color: #7f8c8d; font-size: 18px;">Athletic Club United - Sporting Succession Dispute</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced view toggle section
        st.markdown("### 🎛️ View Controls")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Card View", 
                        use_container_width=True, 
                        type="primary" if st.session_state.current_view_type == "card" else "secondary",
                        help="Detailed card view of each fact"):
                st.session_state.current_view_type = "card"
                st.rerun()
        
        with col2:
            if st.button("📅 Timeline View", 
                        use_container_width=True,
                        type="primary" if st.session_state.current_view_type == "timeline" else "secondary",
                        help="Chronological timeline of events"):
                st.session_state.current_view_type = "timeline"
                st.rerun()
        
        with col3:
            if st.button("📁 Document Categories", 
                        use_container_width=True,
                        type="primary" if st.session_state.current_view_type == "docset" else "secondary",
                        help="Facts organized by document type"):
                st.session_state.current_view_type = "docset"
                st.rerun()
        
        st.markdown("---")
        
        # Enhanced filter section
        st.markdown("### 🔍 Filter Options")
        filter_col1, filter_col2 = st.columns([3, 1])
        
        with filter_col1:
            filter_option = st.selectbox(
                "Filter Facts by Dispute Status:",
                ["All Facts", "Disputed Facts", "Undisputed Facts"],
                index=0,
                help="Filter facts based on whether they are contested by the parties"
            )
        
        with filter_col2:
            # Add search functionality (placeholder)
            search_term = st.text_input("🔍 Search", placeholder="Search facts...", help="Search within fact descriptions")
        
        # Apply filters
        if filter_option == "All Facts":
            filtered_facts = get_all_facts()
        elif filter_option == "Disputed Facts":
            filtered_facts = [fact for fact in get_all_facts() if fact['isDisputed']]
        else:
            filtered_facts = [fact for fact in get_all_facts() if not fact['isDisputed']]
        
        # Apply search filter if provided
        if search_term:
            filtered_facts = [fact for fact in filtered_facts 
                            if search_term.lower() in fact['event'].lower() or 
                               search_term.lower() in fact.get('source_text', '').lower()]
        
        st.markdown("---")
        
        # Render the appropriate enhanced view
        render_view_content(st.session_state.current_view_type, filtered_facts)
    
    elif st.session_state.view == "Arguments":
        st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <h1 style="color: #2c3e50;">📑 Arguments Analysis</h1>
            <p style="color: #7f8c8d; font-size: 18px;">Coming Soon - Detailed argument structure and analysis</p>
            <div style="font-size: 64px; margin: 20px 0;">🚧</div>
        </div>
        """, unsafe_allow_html=True)
    
    elif st.session_state.view == "Exhibits":
        st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <h1 style="color: #2c3e50;">📁 Evidence Library</h1>
            <p style="color: #7f8c8d; font-size: 18px;">Coming Soon - Comprehensive evidence and exhibit management</p>
            <div style="font-size: 64px; margin: 20px 0;">📚</div>
        </div>
        """, unsafe_allow_html=True)

# Helper function to render the appropriate view content
def render_view_content(view_type, filtered_facts):
    if view_type == "card":
        render_streamlit_card_view(filtered_facts)
    elif view_type == "timeline":
        render_streamlit_timeline_view(filtered_facts)
    elif view_type == "docset":
        render_streamlit_docset_view(filtered_facts)

if __name__ == "__main__":
    main()
