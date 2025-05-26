import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(
    page_title="CaseLens - Legal Analysis", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="⚖️"
)

# Enhanced CSS styling
st.markdown("""
<style>
    /* Main styling */
    .main {
        padding-top: 1rem;
    }
    
    /* Custom card styling */
    .fact-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border: 1px solid #e0e6ed;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .fact-card:hover {
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    /* Status badges */
    .status-badge {
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        text-align: center;
        display: inline-block;
        margin: 0.2rem;
    }
    
    .status-disputed {
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
    }
    
    .status-undisputed {
        background: linear-gradient(135deg, #51cf66, #40c057);
        color: white;
    }
    
    /* Party colors */
    .party-appellant {
        border-left: 4px solid #3b82f6;
        background: linear-gradient(90deg, rgba(59,130,246,0.05) 0%, transparent 100%);
    }
    
    .party-respondent {
        border-left: 4px solid #ef4444;
        background: linear-gradient(90deg, rgba(239,68,68,0.05) 0%, transparent 100%);
    }
    
    /* Timeline styling */
    .timeline-year {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        text-align: center;
        margin: 2rem 0 1rem 0;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102,126,234,0.3);
    }
    
    .timeline-event {
        border-left: 3px solid #e0e6ed;
        padding-left: 1.5rem;
        margin: 1.5rem 0;
        position: relative;
    }
    
    .timeline-event::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #3b82f6;
        border: 3px solid white;
        box-shadow: 0 0 0 3px #e0e6ed;
    }
    
    /* Sidebar styling */
    .sidebar-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }
    
    /* Button enhancements */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        margin-bottom: 8px;
        transition: all 0.3s ease;
        font-weight: 500;
        border: none;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102,126,234,0.3);
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    }
    
    /* View toggle buttons */
    .view-toggle {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 0.5rem;
        margin: 0.2rem;
        transition: all 0.3s ease;
    }
    
    .view-toggle:hover {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59,130,246,0.3);
    }
    
    /* Enhanced expander styling */
    .streamlit-expanderContent {
        background: rgba(248,249,250,0.5);
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Metric styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border: 1px solid #e0e6ed;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Info/warning/error styling */
    .stAlert {
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102,126,234,0.2);
    }
    
    /* Evidence section styling */
    .evidence-section {
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #2196f3;
    }
    
    /* Party submission styling */
    .submission-claimant {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 4px solid #2196f3;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .submission-respondent {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-left: 4px solid #f44336;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
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
        st.info("🔍 No facts found matching the selected criteria.")
        return
    
    # Show summary statistics
    total_facts = len(facts_data)
    disputed_facts = len([f for f in facts_data if f['isDisputed']])
    undisputed_facts = total_facts - disputed_facts
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Facts", total_facts)
    with col2:
        st.metric("🔴 Disputed", disputed_facts)
    with col3:
        st.metric("🟢 Undisputed", undisputed_facts)
    with col4:
        st.metric("📈 Dispute Rate", f"{(disputed_facts/total_facts*100):.1f}%")
    
    st.markdown("---")
    
    # Display each fact as an enhanced card
    for i, fact in enumerate(facts_data):
        # Create enhanced card container
        with st.container():
            # Card header with enhanced styling
            col1, col2, col3 = st.columns([6, 2, 1])
            
            with col1:
                st.markdown(f"### 📅 {fact['date']} - {fact['event']}")
            
            with col2:
                if fact['isDisputed']:
                    st.markdown('<div class="status-badge status-disputed">🔴 DISPUTED</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="status-badge status-undisputed">🟢 UNDISPUTED</div>', unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"**#{i+1}**")
            
            # Enhanced expander with better title
            expander_title = f"View Details - {fact['event'][:50]}{'...' if len(fact['event']) > 50 else ''}"
            
            with st.expander(expander_title, expanded=False):
                # Evidence & Source References section with enhanced styling
                st.markdown('<div class="evidence-section">', unsafe_allow_html=True)
                st.markdown("### 📁 Evidence & Source References")
                
                evidence_content = get_evidence_content(fact)
                
                if evidence_content:
                    for evidence in evidence_content:
                        st.markdown(f"**🔖 {evidence['id']}** - {evidence['title']}")
                        
                        # Document Summary with enhanced display
                        if fact.get('doc_summary'):
                            st.info(f"**📄 Document Summary:** {fact['doc_summary']}")
                        
                        # Source Text with better formatting
                        if fact.get('source_text'):
                            st.markdown(f"**📝 Source Text:** *{fact['source_text']}*")
                        
                        # Reference information with better layout
                        ref_col1, ref_col2 = st.columns([4, 1])
                        with ref_col1:
                            ref_text = f"**📎 Exhibit:** {evidence['id']}"
                            if fact.get('page'):
                                ref_text += f" | **📄 Page:** {fact['page']}"
                            if fact.get('paragraphs'):
                                ref_text += f" | **📋 Paragraphs:** {fact['paragraphs']}"
                            st.markdown(ref_text)
                        
                        with ref_col2:
                            if st.button(f"📋 Copy", key=f"copy_{evidence['id']}_{i}", help="Copy reference"):
                                st.success("✅ Copied!")
                        
                        st.markdown("---")
                else:
                    st.warning("⚠️ No evidence references available for this fact")
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Party Submissions section with enhanced styling
                st.markdown("### ⚖️ Party Submissions")
                
                # Enhanced submission display
                submission_col1, submission_col2 = st.columns(2)
                
                with submission_col1:
                    st.markdown('<div class="submission-claimant">', unsafe_allow_html=True)
                    st.markdown("#### 🔵 Appellant Submission")
                    claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                    if claimant_text == 'No specific submission recorded':
                        st.markdown("*No submission provided*")
                    else:
                        st.markdown(f"*{claimant_text}*")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with submission_col2:
                    st.markdown('<div class="submission-respondent">', unsafe_allow_html=True)
                    st.markdown("#### 🔴 Respondent Submission")
                    respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                    if respondent_text == 'No specific submission recorded':
                        st.markdown("*No submission provided*")
                    else:
                        st.markdown(f"*{respondent_text}*")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # Enhanced status section
                st.markdown("### 📊 Fact Status")
                status_col1, status_col2, status_col3 = st.columns(3)
                
                with status_col1:
                    if fact['isDisputed']:
                        st.error("🔴 **Status:** Disputed")
                    else:
                        st.success("🟢 **Status:** Undisputed")
                
                with status_col2:
                    if fact.get('parties_involved'):
                        parties_text = ', '.join(fact['parties_involved'])
                        st.info(f"👥 **Parties:** {parties_text}")
                
                with status_col3:
                    if fact.get('exhibits'):
                        exhibits_count = len(fact['exhibits'])
                        st.info(f"📎 **Exhibits:** {exhibits_count}")
            
            st.markdown("---")

# Enhanced Timeline View Implementation
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
    
    # Show summary statistics
    total_events = len(facts_data)
    disputed_events = len([f for f in facts_data if f['isDisputed']])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📅 Timeline Events", total_events)
    with col2:
        st.metric("⚖️ Disputed Events", disputed_events)
    
    st.markdown("---")
    
    # Group by year for enhanced year markers
    events_by_year = {}
    for fact in facts_data:
        year = fact['date'].split('-')[0] if '-' in fact['date'] else fact['date'][:4]
        if year not in events_by_year:
            events_by_year[year] = []
        events_by_year[year].append(fact)
    
    # Display enhanced timeline events
    for year, events in events_by_year.items():
        # Enhanced year marker
        st.markdown(f'<div class="timeline-year">📅 {year} ({len(events)} events)</div>', unsafe_allow_html=True)
        
        for i, fact in enumerate(events):
            # Enhanced timeline event container
            st.markdown('<div class="timeline-event">', unsafe_allow_html=True)
            
            # Event header with enhanced styling
            event_col1, event_col2, event_col3 = st.columns([5, 2, 1])
            
            with event_col1:
                st.markdown(f"**📆 {fact['date']} - {fact['event']}**")
            
            with event_col2:
                if fact['isDisputed']:
                    st.markdown('<div class="status-badge status-disputed">🔴 DISPUTED</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="status-badge status-undisputed">🟢 UNDISPUTED</div>', unsafe_allow_html=True)
            
            with event_col3:
                if fact.get('parties_involved'):
                    parties_count = len(fact['parties_involved'])
                    st.markdown(f"**👥 {parties_count}**")
            
            # Event details with enhanced styling
            with st.container():
                # Evidence section
                st.markdown("**📁 Evidence & Source References**")
                evidence_content = get_evidence_content(fact)
                
                if evidence_content:
                    for evidence in evidence_content:
                        st.markdown(f"📎 **{evidence['id']}** - {evidence['title']}")
                        if fact.get('doc_summary'):
                            st.info(f"📄 **Document:** {fact['doc_summary']}")
                        if fact.get('source_text'):
                            st.markdown(f"📝 *{fact['source_text']}*")
                else:
                    st.warning("⚠️ No evidence references available")
                
                # Enhanced party submissions
                st.markdown("**⚖️ Party Positions**")
                
                # Side-by-side submissions
                sub_col1, sub_col2 = st.columns(2)
                
                with sub_col1:
                    st.markdown("**🔵 Appellant Position**")
                    claimant_text = fact.get('claimant_submission', 'No submission provided')
                    if claimant_text == 'No specific submission recorded':
                        st.markdown("*No position recorded*")
                    else:
                        st.info(claimant_text)
                
                with sub_col2:
                    st.markdown("**🔴 Respondent Position**")
                    respondent_text = fact.get('respondent_submission', 'No submission provided')
                    if respondent_text == 'No specific submission recorded':
                        st.markdown("*No position recorded*")
                    else:
                        st.warning(respondent_text)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Separator between events
            if i < len(events) - 1:
                st.markdown("---")

# Enhanced Document Categories View Implementation  
def render_streamlit_docset_view(filtered_facts=None):
    # Get facts and document sets data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
        
    document_sets = get_document_sets()
    
    # Sort facts by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    # Show summary
    st.markdown("### 📂 Facts Organized by Document Categories")
    
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
    
    # Display enhanced document categories
    for docset_id, doc_with_facts in docs_with_facts.items():
        docset = doc_with_facts['docset']
        facts = doc_with_facts['facts']
        
        # Enhanced document set header
        party_color = ("🔵" if docset['party'] == 'Appellant' else 
                      "🔴" if docset['party'] == 'Respondent' else "⚪")
        
        disputed_count = len([f for f in facts if f['isDisputed']])
        
        # Enhanced expander title
        expander_title = f"📁 {party_color} **{docset['name'].upper()}** | {len(facts)} facts | {disputed_count} disputed"
        
        with st.expander(expander_title, expanded=False):
            if facts:
                # Document category summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("📊 Total Facts", len(facts))
                with col2:
                    st.metric("🔴 Disputed", disputed_count)
                with col3:
                    st.metric("🟢 Undisputed", len(facts) - disputed_count)
                
                st.markdown("---")
                
                for i, fact in enumerate(facts):
                    # Enhanced fact container
                    with st.container():
                        # Fact header with enhanced layout
                        fact_col1, fact_col2, fact_col3, fact_col4 = st.columns([3, 3, 1, 1])
                        
                        with fact_col1:
                            st.markdown(f"**📅 {fact['date']}**")
                        
                        with fact_col2:
                            st.markdown(f"**{fact['event'][:40]}{'...' if len(fact['event']) > 40 else ''}**")
                        
                        with fact_col3:
                            if fact['isDisputed']:
                                st.markdown("🔴")
                            else:
                                st.markdown("🟢")
                        
                        with fact_col4:
                            if fact.get('exhibits'):
                                st.markdown(f"📎 {len(fact['exhibits'])}")
                        
                        # Enhanced fact details
                        with st.container():
                            # Evidence section with better styling
                            st.markdown("**📎 Evidence References**")
                            evidence_content = get_evidence_content(fact)
                            
                            if evidence_content:
                                evidence_text = " | ".join([f"**{e['id']}**" for e in evidence_content])
                                st.markdown(evidence_text)
                                
                                if fact.get('doc_summary'):
                                    st.info(f"📄 {fact['doc_summary']}")
                            else:
                                st.warning("⚠️ No evidence references")
                            
                            # Compact party submissions
                            st.markdown("**⚖️ Party Positions**")
                            
                            # Compact side-by-side display
                            pos_col1, pos_col2 = st.columns(2)
                            
                            with pos_col1:
                                st.markdown("**🔵 Appellant**")
                                claimant_text = fact.get('claimant_submission', 'No submission')
                                if claimant_text == 'No specific submission recorded':
                                    st.markdown("*No position*")
                                else:
                                    truncated = claimant_text[:100] + '...' if len(claimant_text) > 100 else claimant_text
                                    st.info(truncated)
                            
                            with pos_col2:
                                st.markdown("**🔴 Respondent**")
                                respondent_text = fact.get('respondent_submission', 'No submission')
                                if respondent_text == 'No specific submission recorded':
                                    st.markdown("*No position*")
                                else:
                                    truncated = respondent_text[:100] + '...' if len(respondent_text) > 100 else respondent_text
                                    st.warning(truncated)
                        
                        # Separator between facts
                        if i < len(facts) - 1:
                            st.markdown("---")
            else:
                st.info("📭 No facts found in this document category.")

# Enhanced main application
def main():
    # Get the data
    args_data = get_argument_data()
    facts_data = get_all_facts()
    document_sets = get_document_sets()
    timeline_data = get_timeline_data()
    
    # Enhanced sidebar
    with st.sidebar:
        # Enhanced logo and header
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-bottom: 30px;">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 15px;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="45" height="45">
                  <mask id="caselens-mask" maskUnits="userSpaceOnUse">
                    <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
                  </mask>
                  <g mask="url(#caselens-mask)">
                    <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="white"/>
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="#667eea"/>
                  </g>
                </svg>
            </div>
            <h1 style="color: white; font-weight: 700; margin: 0; font-size: 28px;">CaseLens</h1>
            <p style="color: rgba(255,255,255,0.8); margin: 5px 0 0 0; font-size: 14px;">Legal Analysis Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation section
        st.markdown('<div class="section-header">📋 Navigation</div>', unsafe_allow_html=True)
        
        # Enhanced button handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Enhanced navigation buttons
        if st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True):
            pass
        if st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True):
            pass
        if st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True):
            pass
        
        # Case summary section
        st.markdown("---")
        st.markdown('<div class="section-header">📈 Case Summary</div>', unsafe_allow_html=True)
        
        total_facts = len(get_all_facts())
        disputed_facts = len([f for f in get_all_facts() if f['isDisputed']])
        
        st.metric("Total Facts", total_facts)
        st.metric("Disputed Facts", disputed_facts)
        st.metric("Dispute Rate", f"{(disputed_facts/total_facts*100):.1f}%")
    
    # Enhanced main content area
    if st.session_state.view == "Facts":
        # Enhanced header
        st.markdown('<div class="section-header">⚖️ Case Facts Analysis</div>', unsafe_allow_html=True)
        
        # Enhanced view toggle
        st.subheader("📋 View Options")
        view_col1, view_col2, view_col3 = st.columns(3)
        
        with view_col1:
            if st.button("📋 Card View", use_container_width=True, 
                        type="primary" if st.session_state.current_view_type == "card" else "secondary"):
                st.session_state.current_view_type = "card"
                st.rerun()
        
        with view_col2:
            if st.button("📅 Timeline View", use_container_width=True,
                        type="primary" if st.session_state.current_view_type == "timeline" else "secondary"):
                st.session_state.current_view_type = "timeline"
                st.rerun()
        
        with view_col3:
            if st.button("📁 Document Categories", use_container_width=True,
                        type="primary" if st.session_state.current_view_type == "docset" else "secondary"):
                st.session_state.current_view_type = "docset"
                st.rerun()
        
        st.markdown("---")
        
        # Enhanced filter section
        st.subheader("🔍 Filter Facts")
        filter_col1, filter_col2 = st.columns([3, 1])
        
        with filter_col1:
            filter_option = st.selectbox(
                "Select facts to display:",
                ["All Facts", "Disputed Facts", "Undisputed Facts"],
                index=0
            )
        
        with filter_col2:
            if st.button("🔄 Refresh", use_container_width=True):
                st.rerun()
        
        # Process filter selection
        if filter_option == "All Facts":
            st.session_state.current_tab_type = "all"
            filtered_facts = get_all_facts()
        elif filter_option == "Disputed Facts":
            st.session_state.current_tab_type = "disputed"
            filtered_facts = [fact for fact in get_all_facts() if fact['isDisputed']]
        else:
            st.session_state.current_tab_type = "undisputed"
            filtered_facts = [fact for fact in get_all_facts() if not fact['isDisputed']]
        
        st.markdown("---")
        
        # Render the appropriate enhanced view
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
