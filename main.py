import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config with better theming
st.set_page_config(
    page_title="CaseLens - Legal Analysis", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.caselens.com/help',
        'Report a bug': "https://www.caselens.com/bug",
        'About': "CaseLens - Advanced Legal Case Analysis Platform"
    }
)

# Enhanced CSS styling
st.markdown("""
<style>
    /* Import modern fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Custom font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Enhanced sidebar */
    .css-1d391kg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 1rem;
    }
    
    /* Sidebar buttons with modern styling */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 56px;
        margin-bottom: 12px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: none;
        font-weight: 500;
        font-size: 16px;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        color: #1e293b;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0px);
    }
    
    /* Primary button styling */
    .stButton .stButton--primary button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    
    .stButton .stButton--primary button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.6);
    }
    
    /* View toggle buttons */
    .view-toggle-container {
        background: #f8fafc;
        border-radius: 16px;
        padding: 8px;
        margin-bottom: 24px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Enhanced cards */
    .fact-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .fact-card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        transform: translateY(-2px);
    }
    
    /* Status badges */
    .status-badge {
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .status-disputed {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        color: #dc2626;
        border: 1px solid #fecaca;
    }
    
    .status-undisputed {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        color: #16a34a;
        border: 1px solid #bbf7d0;
    }
    
    /* Party indicators */
    .party-indicator {
        display: inline-flex;
        align-items: center;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-right: 8px;
    }
    
    .party-appellant {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        color: #1d4ed8;
    }
    
    .party-respondent {
        background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%);
        color: #dc2626;
    }
    
    /* Enhanced timeline */
    .timeline-year {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        padding: 12px 24px;
        border-radius: 12px;
        margin: 24px 0 16px 0;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }
    
    .timeline-event {
        border-left: 4px solid #e2e8f0;
        padding-left: 24px;
        margin-bottom: 32px;
        position: relative;
    }
    
    .timeline-event::before {
        content: '';
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #3b82f6;
        position: absolute;
        left: -8px;
        top: 8px;
        box-shadow: 0 0 0 4px white, 0 0 0 6px #3b82f6;
    }
    
    /* Evidence section styling */
    .evidence-section {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 12px;
        padding: 20px;
        margin: 16px 0;
        border-left: 4px solid #0ea5e9;
    }
    
    .evidence-item {
        background: white;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
    }
    
    /* Submission styling */
    .submission-claimant {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 16px;
        margin: 12px 0;
    }
    
    .submission-respondent {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border-left: 4px solid #ef4444;
        border-radius: 8px;
        padding: 16px;
        margin: 12px 0;
    }
    
    /* Enhanced selectbox */
    .stSelectbox > div > div {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        background: white;
    }
    
    /* Enhanced expanders */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        font-weight: 500;
    }
    
    .streamlit-expanderContent {
        background: white;
        border-radius: 0 0 12px 12px;
        border: 1px solid #e2e8f0;
        border-top: none;
    }
    
    /* Title styling */
    .main-title {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    
    /* Divider styling */
    .stDivider {
        margin: 2rem 0;
    }
    
    /* Filter section */
    .filter-section {
        background: #f8fafc;
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 24px;
        border: 1px solid #e2e8f0;
    }
    
    /* Copy button */
    .copy-button {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 12px;
        transition: all 0.2s;
    }
    
    .copy-button:hover {
        background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
        transform: translateY(-1px);
    }
    
    /* Document category styling */
    .doc-category {
        background: linear-gradient(135deg, #fafafa 0%, #f4f4f5 100%);
        border-radius: 12px;
        margin-bottom: 16px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    
    /* Icon styling */
    .icon {
        font-size: 18px;
        margin-right: 8px;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }
        
        .fact-card {
            padding: 16px;
        }
        
        .timeline-event {
            padding-left: 16px;
        }
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

# Enhanced Streamlit Card View Implementation
def render_streamlit_card_view(filtered_facts=None):
    # Get facts data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    # Sort by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.markdown("""
        <div style="text-align: center; padding: 60px 20px; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 16px; margin: 20px 0;">
            <div style="font-size: 48px; margin-bottom: 16px;">📋</div>
            <h3 style="color: #64748b; margin-bottom: 8px;">No Facts Found</h3>
            <p style="color: #94a3b8;">No facts match the selected criteria. Try adjusting your filters.</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Display stats
    disputed_count = sum(1 for f in facts_data if f['isDisputed'])
    undisputed_count = len(facts_data) - disputed_count
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #93c5fd;">
            <div style="font-size: 24px; font-weight: 600; color: #1d4ed8;">{len(facts_data)}</div>
            <div style="font-size: 14px; color: #3730a3; font-weight: 500;">Total Facts</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #fca5a5;">
            <div style="font-size: 24px; font-weight: 600; color: #dc2626;">{disputed_count}</div>
            <div style="font-size: 14px; color: #991b1b; font-weight: 500;">Disputed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #86efac;">
            <div style="font-size: 24px; font-weight: 600; color: #16a34a;">{undisputed_count}</div>
            <div style="font-size: 14px; color: #166534; font-weight: 500;">Undisputed</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display each fact as an enhanced card
    for i, fact in enumerate(facts_data):
        # Create enhanced expander title with better formatting
        status_icon = "🔴" if fact['isDisputed'] else "🟢"
        
        expander_title = f"{status_icon} **{fact['date']}** • {fact['event']}"
        
        with st.expander(expander_title, expanded=False):
            # Create two columns for better layout
            left_col, right_col = st.columns([2, 1])
            
            with left_col:
                # Evidence & Source References section with enhanced styling
                st.markdown("""
                <div class="evidence-section">
                    <h4 style="margin: 0 0 16px 0; color: #0ea5e9; font-weight: 600;">
                        📁 Evidence & Source References
                    </h4>
                </div>
                """, unsafe_allow_html=True)
                
                evidence_content = get_evidence_content(fact)
                
                if evidence_content:
                    for evidence in evidence_content:
                        st.markdown(f"""
                        <div class="evidence-item">
                            <div style="font-weight: 600; color: #1e293b; margin-bottom: 8px;">
                                {evidence['id']} • {evidence['title']}
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Document Summary
                        if fact.get('doc_summary'):
                            st.markdown(f"""
                            <div style="background: #f0f9ff; padding: 12px; border-radius: 8px; margin: 8px 0; border-left: 3px solid #0ea5e9;">
                                <strong style="color: #0c4a6e;">Document Summary:</strong><br>
                                <span style="color: #075985;">{fact['doc_summary']}</span>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Source Text
                        if fact.get('source_text'):
                            st.markdown(f"""
                            <div style="background: #fafafa; padding: 12px; border-radius: 8px; margin: 8px 0; border-left: 3px solid #64748b;">
                                <strong style="color: #334155;">Source Text:</strong><br>
                                <em style="color: #475569;">{fact['source_text']}</em>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Reference information
                        ref_parts = []
                        if evidence['id']:
                            ref_parts.append(f"Exhibit: {evidence['id']}")
                        if fact.get('page'):
                            ref_parts.append(f"Page: {fact['page']}")
                        if fact.get('paragraphs'):
                            ref_parts.append(f"Paragraphs: {fact['paragraphs']}")
                        
                        if ref_parts:
                            st.markdown(f"""
                            <div style="background: #f8fafc; padding: 8px 12px; border-radius: 6px; margin: 8px 0; font-size: 13px; color: #64748b;">
                                {' | '.join(ref_parts)}
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="text-align: center; padding: 20px; color: #94a3b8; font-style: italic;">
                        No evidence references available for this fact
                    </div>
                    """, unsafe_allow_html=True)
            
            with right_col:
                # Status section with enhanced design
                st.markdown("""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0;">
                    <h4 style="margin: 0 0 16px 0; color: #1e293b; font-weight: 600;">📊 Status</h4>
                """, unsafe_allow_html=True)
                
                if fact['isDisputed']:
                    st.markdown("""
                    <div class="status-badge status-disputed" style="margin-bottom: 12px;">
                        Disputed
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="status-badge status-undisputed" style="margin-bottom: 12px;">
                        Undisputed
                    </div>
                    """, unsafe_allow_html=True)
                
                if fact.get('parties_involved'):
                    parties_html = ""
                    for party in fact['parties_involved']:
                        class_name = "party-appellant" if party == "Appellant" else "party-respondent"
                        parties_html += f'<span class="party-indicator {class_name}">{party}</span>'
                    
                    st.markdown(f"""
                    <div style="margin-top: 12px;">
                        <div style="font-size: 12px; color: #64748b; margin-bottom: 6px; font-weight: 500;">PARTIES INVOLVED</div>
                        {parties_html}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
            
            # Party Submissions section with enhanced styling
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <h4 style="color: #1e293b; font-weight: 600; margin-bottom: 16px;">
                ⚖️ Party Submissions
            </h4>
            """, unsafe_allow_html=True)
            
            # Claimant submission
            st.markdown("""
            <div style="font-weight: 600; color: #1d4ed8; margin-bottom: 8px; display: flex; align-items: center;">
                🔵 Claimant Submission
            </div>
            """, unsafe_allow_html=True)
            
            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
            if claimant_text == 'No specific submission recorded':
                st.markdown("""
                <div class="submission-claimant">
                    <em style="color: #64748b;">No submission provided</em>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="submission-claimant">
                    {claimant_text}
                </div>
                """, unsafe_allow_html=True)
            
            # Respondent submission
            st.markdown("""
            <div style="font-weight: 600; color: #dc2626; margin: 16px 0 8px 0; display: flex; align-items: center;">
                🔴 Respondent Submission
            </div>
            """, unsafe_allow_html=True)
            
            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
            if respondent_text == 'No specific submission recorded':
                st.markdown("""
                <div class="submission-respondent">
                    <em style="color: #64748b;">No submission provided</em>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="submission-respondent">
                    {respondent_text}
                </div>
                """, unsafe_allow_html=True)

# Enhanced Streamlit Timeline View Implementation
def render_streamlit_timeline_view(filtered_facts=None):
    # Get facts data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    # Sort by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.markdown("""
        <div style="text-align: center; padding: 60px 20px; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 16px; margin: 20px 0;">
            <div style="font-size: 48px; margin-bottom: 16px;">📅</div>
            <h3 style="color: #64748b; margin-bottom: 8px;">No Timeline Events</h3>
            <p style="color: #94a3b8;">No timeline events match the selected criteria.</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Group by year for year markers
    events_by_year = {}
    for fact in facts_data:
        year = fact['date'].split('-')[0] if '-' in fact['date'] else fact['date'][:4]
        if year not in events_by_year:
            events_by_year[year] = []
        events_by_year[year].append(fact)
    
    # Display timeline events with enhanced styling
    for year, events in events_by_year.items():
        # Enhanced year marker
        st.markdown(f"""
        <div class="timeline-year">
            <div style="font-size: 24px; font-weight: 700;">📅 {year}</div>
            <div style="font-size: 14px; opacity: 0.9;">{len(events)} event{'s' if len(events) != 1 else ''}</div>
        </div>
        """, unsafe_allow_html=True)
        
        for i, fact in enumerate(events):
            # Create enhanced timeline event container
            status_color = "#ef4444" if fact['isDisputed'] else "#22c55e"
            
            st.markdown(f"""
            <div class="timeline-event" style="border-left-color: {status_color};">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div>
                        <div style="font-size: 14px; color: #64748b; font-weight: 500;">{fact['date']}</div>
                        <div style="font-size: 18px; font-weight: 600; color: #1e293b; margin-top: 4px;">{fact['event']}</div>
                    </div>
                    <div>
            """, unsafe_allow_html=True)
            
            if fact['isDisputed']:
                st.markdown("""
                <span class="status-badge status-disputed">Disputed</span>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <span class="status-badge status-undisputed">Undisputed</span>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Evidence section with enhanced design
            st.markdown("""
            <div class="evidence-section">
                <h5 style="margin: 0 0 12px 0; color: #0ea5e9; font-weight: 600;">
                    📁 Evidence & Source References
                </h5>
            </div>
            """, unsafe_allow_html=True)
            
            evidence_content = get_evidence_content(fact)
            
            if evidence_content:
                for evidence in evidence_content:
                    st.markdown(f"""
                    <div class="evidence-item">
                        <strong style="color: #1e293b;">{evidence['id']}</strong> • {evidence['title']}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if fact.get('doc_summary'):
                        st.markdown(f"""
                        <div style="background: #f0f9ff; padding: 10px; border-radius: 6px; margin: 8px 0; border-left: 3px solid #0ea5e9; font-size: 14px;">
                            <strong style="color: #0c4a6e;">Document Summary:</strong> {fact['doc_summary']}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if fact.get('source_text'):
                        st.markdown(f"""
                        <div style="background: #fafafa; padding: 10px; border-radius: 6px; margin: 8px 0; border-left: 3px solid #64748b; font-size: 14px;">
                            <strong style="color: #334155;">Source Text:</strong> <em>{fact['source_text']}</em>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="color: #94a3b8; font-style: italic; font-size: 14px;">
                    No evidence references available
                </div>
                """, unsafe_allow_html=True)
            
            # Party submissions with enhanced styling
            st.markdown("""
            <div style="margin: 20px 0;">
                <h5 style="margin: 0 0 12px 0; color: #1e293b; font-weight: 600;">⚖️ Party Submissions</h5>
            </div>
            """, unsafe_allow_html=True)
            
            # Claimant submission
            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
            if claimant_text == 'No specific submission recorded':
                st.markdown("""
                <div class="submission-claimant">
                    <strong style="color: #1d4ed8;">🔵 Claimant:</strong><br>
                    <em style="color: #64748b;">No submission provided</em>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="submission-claimant">
                    <strong style="color: #1d4ed8;">🔵 Claimant:</strong><br>
                    {claimant_text}
                </div>
                """, unsafe_allow_html=True)
            
            # Respondent submission
            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
            if respondent_text == 'No specific submission recorded':
                st.markdown("""
                <div class="submission-respondent">
                    <strong style="color: #dc2626;">🔴 Respondent:</strong><br>
                    <em style="color: #64748b;">No submission provided</em>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="submission-respondent">
                    <strong style="color: #dc2626;">🔴 Respondent:</strong><br>
                    {respondent_text}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Add separator between events
            if i < len(events) - 1:
                st.markdown("""
                <div style="height: 2px; background: linear-gradient(90deg, transparent 0%, #e2e8f0 50%, transparent 100%); margin: 32px 0;"></div>
                """, unsafe_allow_html=True)

# Enhanced Streamlit Document Categories View Implementation  
def render_streamlit_docset_view(filtered_facts=None):
    # Get facts and document sets data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
        
    document_sets = get_document_sets()
    
    # Sort facts by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.markdown("""
        <div style="text-align: center; padding: 60px 20px; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 16px; margin: 20px 0;">
            <div style="font-size: 48px; margin-bottom: 16px;">📁</div>
            <h3 style="color: #64748b; margin-bottom: 8px;">No Documents</h3>
            <p style="color: #94a3b8;">No facts found in document categories matching the selected criteria.</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Group facts by document categories
    docs_with_facts = {}
    
    # Initialize all groups
    for ds in document_sets:
        if ds.get('isGroup'):
            docs_with_facts[ds['id']] = {
                'docset': ds,
                'facts': []
            }
    
    # Distribute facts to categories
    for fact in facts_data:
        fact_assigned = False
        
        # Try to assign based on source matching
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
        
        # If not assigned by source, assign by party matching
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
        
        # Enhanced document set header
        party_colors = {
            'Appellant': '🔵',
            'Respondent': '🔴',
            'Mixed': '⚪',
            'Shared': '🟡'
        }
        party_color = party_colors.get(docset['party'], '⚪')
        
        # Enhanced expander with better styling
        expander_title = f"📁 {party_color} **{docset['name'].title()}** • {len(facts)} fact{'s' if len(facts) != 1 else ''}"
        
        with st.expander(expander_title, expanded=False):
            if facts:
                # Display stats for this document category
                disputed_in_cat = sum(1 for f in facts if f['isDisputed'])
                undisputed_in_cat = len(facts) - disputed_in_cat
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%); padding: 12px; border-radius: 8px; text-align: center;">
                        <div style="font-size: 20px; font-weight: 600; color: #374151;">{len(facts)}</div>
                        <div style="font-size: 12px; color: #6b7280; font-weight: 500;">Total</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); padding: 12px; border-radius: 8px; text-align: center;">
                        <div style="font-size: 20px; font-weight: 600; color: #dc2626;">{disputed_in_cat}</div>
                        <div style="font-size: 12px; color: #991b1b; font-weight: 500;">Disputed</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px; text-align: center;">
                        <div style="font-size: 20px; font-weight: 600; color: #16a34a;">{undisputed_in_cat}</div>
                        <div style="font-size: 12px; color: #166534; font-weight: 500;">Undisputed</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                for i, fact in enumerate(facts):
                    # Enhanced fact container
                    status_color = "#fef2f2" if fact['isDisputed'] else "#f0fdf4"
                    border_color = "#fca5a5" if fact['isDisputed'] else "#86efac"
                    
                    st.markdown(f"""
                    <div style="background: {status_color}; border: 1px solid {border_color}; border-radius: 12px; padding: 20px; margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                            <div>
                                <div style="font-size: 14px; color: #64748b; font-weight: 500;">{fact['date']}</div>
                                <div style="font-size: 16px; font-weight: 600; color: #1e293b; margin-top: 4px;">{fact['event']}</div>
                            </div>
                            <div>
                    """, unsafe_allow_html=True)
                    
                    if fact['isDisputed']:
                        st.markdown('<span class="status-badge status-disputed">Disputed</span>', unsafe_allow_html=True)
                    else:
                        st.markdown('<span class="status-badge status-undisputed">Undisputed</span>', unsafe_allow_html=True)
                    
                    st.markdown("""
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Evidence section
                    st.markdown("""
                    <div style="margin-bottom: 16px;">
                        <h6 style="margin: 0 0 8px 0; color: #0ea5e9; font-weight: 600; font-size: 14px;">📁 Evidence & Source References</h6>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    evidence_content = get_evidence_content(fact)
                    
                    if evidence_content:
                        for evidence in evidence_content:
                            st.markdown(f"""
                            <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
                                <strong style="color: #1e293b; font-size: 14px;">{evidence['id']}</strong> • <span style="font-size: 14px;">{evidence['title']}</span>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            if fact.get('doc_summary'):
                                st.markdown(f"""
                                <div style="background: #f0f9ff; padding: 10px; border-radius: 6px; margin: 6px 0; border-left: 3px solid #0ea5e9; font-size: 13px;">
                                    <strong style="color: #0c4a6e;">Document Summary:</strong> {fact['doc_summary']}
                                </div>
                                """, unsafe_allow_html=True)
                            
                            if fact.get('source_text'):
                                st.markdown(f"""
                                <div style="background: #fafafa; padding: 10px; border-radius: 6px; margin: 6px 0; border-left: 3px solid #64748b; font-size: 13px;">
                                    <strong style="color: #334155;">Source Text:</strong> <em>{fact['source_text']}</em>
                                </div>
                                """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div style="color: #94a3b8; font-style: italic; font-size: 13px; text-align: center; padding: 10px;">
                            No evidence references available
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Party submissions
                    st.markdown("""
                    <div style="margin: 16px 0 8px 0;">
                        <h6 style="margin: 0; color: #1e293b; font-weight: 600; font-size: 14px;">⚖️ Party Submissions</h6>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Claimant submission
                    claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                    if claimant_text == 'No specific submission recorded':
                        st.markdown("""
                        <div style="background: #eff6ff; border-left: 3px solid #3b82f6; padding: 10px; border-radius: 6px; margin: 6px 0; font-size: 13px;">
                            <strong style="color: #1d4ed8;">🔵 Claimant:</strong><br>
                            <em style="color: #64748b;">No submission provided</em>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background: #eff6ff; border-left: 3px solid #3b82f6; padding: 10px; border-radius: 6px; margin: 6px 0; font-size: 13px;">
                            <strong style="color: #1d4ed8;">🔵 Claimant:</strong><br>
                            {claimant_text}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Respondent submission
                    respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                    if respondent_text == 'No specific submission recorded':
                        st.markdown("""
                        <div style="background: #fef2f2; border-left: 3px solid #ef4444; padding: 10px; border-radius: 6px; margin: 6px 0; font-size: 13px;">
                            <strong style="color: #dc2626;">🔴 Respondent:</strong><br>
                            <em style="color: #64748b;">No submission provided</em>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background: #fef2f2; border-left: 3px solid #ef4444; padding: 10px; border-radius: 6px; margin: 6px 0; font-size: 13px;">
                            <strong style="color: #dc2626;">🔴 Respondent:</strong><br>
                            {respondent_text}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Separator between facts
                    if i < len(facts) - 1:
                        st.markdown("""
                        <div style="height: 1px; background: linear-gradient(90deg, transparent 0%, #e2e8f0 50%, transparent 100%); margin: 20px 0;"></div>
                        """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="text-align: center; padding: 40px 20px; background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%); border-radius: 12px; margin: 20px 0;">
                    <div style="font-size: 36px; margin-bottom: 12px; opacity: 0.6;">📄</div>
                    <h4 style="color: #6b7280; margin-bottom: 8px;">No Facts Found</h4>
                    <p style="color: #9ca3af; margin: 0;">No facts found in this document category.</p>
                </div>
                """, unsafe_allow_html=True)

# Main app with enhanced UI
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
    
    # Enhanced sidebar with better styling
    with st.sidebar:
        # Enhanced logo and CaseLens text
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 32px; padding: 20px 0;">
            <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); border-radius: 12px; padding: 8px; margin-right: 12px; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="white">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                </svg>
            </div>
            <div>
                <h1 style="margin: 0; font-weight: 700; color: white; font-size: 28px; text-shadow: 0 2px 4px rgba(0,0,0,0.1);">CaseLens</h1>
                <div style="color: rgba(255,255,255,0.8); font-size: 12px; font-weight: 500; margin-top: 2px;">Legal Analysis Platform</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="color: rgba(255,255,255,0.9); font-size: 18px; font-weight: 600; margin-bottom: 24px; text-align: center;">
            Navigation
        </div>
        """, unsafe_allow_html=True)
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Enhanced navigation buttons
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
        
        # Additional sidebar information
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background: rgba(255,255,255,0.1); border-radius: 12px; padding: 16px; margin-top: 20px;">
            <div style="color: rgba(255,255,255,0.9); font-size: 14px; font-weight: 600; margin-bottom: 8px;">Case Overview</div>
            <div style="color: rgba(255,255,255,0.7); font-size: 12px; line-height: 1.4;">
                Athletic Club United<br>
                Sporting Succession Dispute<br>
                <span style="opacity: 0.8;">7 key events • 3 disputed facts</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Create the facts view with enhanced native components
    if st.session_state.view == "Facts":
        # Enhanced main title
        st.markdown("""
        <div style="text-align: center; margin-bottom: 32px;">
            <h1 class="main-title" style="font-size: 42px; margin-bottom: 8px;">Case Facts</h1>
            <p style="color: #64748b; font-size: 16px; margin: 0;">Comprehensive analysis of factual evidence and party submissions</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced view toggle with modern design
        st.markdown('<div class="view-toggle-container">', unsafe_allow_html=True)
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
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Enhanced filter section
        st.markdown('<div class="filter-section">', unsafe_allow_html=True)
        filter_option = st.selectbox(
            "🔍 Filter Facts:",
            ["All Facts", "Disputed Facts", "Undisputed Facts"],
            index=0
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Set current tab type based on selection
        if filter_option == "All Facts":
            st.session_state.current_tab_type = "all"
            filtered_facts = get_all_facts()
        elif filter_option == "Disputed Facts":
            st.session_state.current_tab_type = "disputed"
            filtered_facts = [fact for fact in get_all_facts() if fact['isDisputed']]
        else:
            st.session_state.current_tab_type = "undisputed"
            filtered_facts = [fact for fact in get_all_facts() if not fact['isDisputed']]
        
        # Render the appropriate enhanced view based on current view type
        render_view_content(st.session_state.current_view_type, filtered_facts)

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
