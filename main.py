import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
from datetime import datetime

# Set page config with enhanced settings
st.set_page_config(
    page_title="CaseLens - Legal Arguments Analysis", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "CaseLens - Professional Legal Case Analysis Tool"
    }
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main improvements */
    .main > div {
        padding-top: 2rem;
    }
    
    /* Enhanced card styling */
    .fact-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #4D68F9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .fact-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    }
    
    .disputed-card {
        border-left-color: #dc3545;
        background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
    }
    
    .undisputed-card {
        border-left-color: #28a745;
        background: linear-gradient(135deg, #f0fff4 0%, #ffffff 100%);
    }
    
    /* Status badges */
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;
        margin: 0.25rem;
    }
    
    .badge-disputed {
        background-color: #dc3545;
        color: white;
    }
    
    .badge-undisputed {
        background-color: #28a745;
        color: white;
    }
    
    .badge-appellant {
        background-color: #007bff;
        color: white;
    }
    
    .badge-respondent {
        background-color: #fd7e14;
        color: white;
    }
    
    /* Timeline enhancements */
    .timeline-container {
        position: relative;
        padding-left: 2rem;
    }
    
    .timeline-line {
        position: absolute;
        left: 1rem;
        top: 0;
        bottom: 0;
        width: 2px;
        background: linear-gradient(to bottom, #4D68F9, #28a745);
    }
    
    .timeline-dot {
        position: absolute;
        left: 0.5rem;
        width: 1rem;
        height: 1rem;
        border-radius: 50%;
        background: #4D68F9;
        border: 3px solid white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .timeline-dot.disputed {
        background: #dc3545;
    }
    
    /* Enhanced buttons */
    .stButton > button {
        border-radius: 8px;
        border: none;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Sidebar enhancements */
    .sidebar .stButton > button {
        width: 100%;
        margin-bottom: 0.5rem;
        text-align: left;
        justify-content: flex-start;
    }
    
    /* Evidence section styling */
    .evidence-section {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        border: 1px solid #dee2e6;
    }
    
    /* Party submission styling */
    .submission-section {
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        border: 1px solid #dee2e6;
    }
    
    .claimant-submission {
        background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 100%);
        border-left: 4px solid #2196f3;
    }
    
    .respondent-submission {
        background: linear-gradient(135deg, #fff3e0 0%, #ffffff 100%);
        border-left: 4px solid #ff9800;
    }
    
    /* Metrics styling */
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Enhanced typography */
    .section-header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 1rem 0 0.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #4D68F9;
    }
    
    .subsection-header {
        font-size: 1.1rem;
        font-weight: 500;
        color: #34495e;
        margin: 0.75rem 0 0.25rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"
if 'selected_parties' not in st.session_state:
    st.session_state.selected_parties = ["Appellant", "Respondent"]
if 'date_range' not in st.session_state:
    st.session_state.date_range = "all"

# Data functions (keeping all original functionality)
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

def get_all_facts():
    args_data = get_argument_data()
    facts = []
    
    def extract_facts(arg, party):
        if not arg:
            return
            
        if 'factualPoints' in arg and arg['factualPoints']:
            for point in arg['factualPoints']:
                fact = {
                    'event': point['point'],
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
                
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Appellant')
        
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
    
    enhanced_facts = []
    fact_groups = {}
    
    for fact in facts:
        key = f"{fact['date']}_{fact['event'][:50]}"
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
        
        if fact['party'] == 'Appellant':
            fact_groups[key]['claimant_submission'] = fact['source_text']
        else:
            fact_groups[key]['respondent_submission'] = fact['source_text']
        
        fact_groups[key]['parties_involved'].append(fact['party'])
        
        if fact['isDisputed']:
            fact_groups[key]['isDisputed'] = True
    
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
            'parties_involved': list(set(group['parties_involved']))
        }
        enhanced_facts.append(enhanced_fact)
    
    return enhanced_facts

def get_timeline_data():
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
    
    timeline_events.sort(key=lambda x: x['date'])
    return timeline_events

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

def get_evidence_content(fact):
    if not fact.get('exhibits') or len(fact['exhibits']) == 0:
        return []
    
    args_data = get_argument_data()
    evidence_content = []
    
    for exhibit_id in fact['exhibits']:
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

# Enhanced sidebar with better organization
def render_enhanced_sidebar():
    with st.sidebar:
        # Logo and branding
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 2rem;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="40" height="40">
              <mask id="logo-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#logo-mask)">
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 15px; font-weight: 700; color: #4D68F9; font-size: 1.8rem;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">📊 Case Analysis</div>', unsafe_allow_html=True)
        
        # Navigation buttons with enhanced styling
        nav_col1, nav_col2 = st.columns(2)
        
        with nav_col1:
            if st.button("📑 Arguments", key="args_btn", use_container_width=True,
                        type="primary" if st.session_state.view == "Arguments" else "secondary"):
                st.session_state.view = "Arguments"
                st.rerun()
        
        with nav_col2:
            if st.button("📊 Facts", key="facts_btn", use_container_width=True,
                        type="primary" if st.session_state.view == "Facts" else "secondary"):
                st.session_state.view = "Facts"
                st.rerun()
        
        if st.button("📁 Exhibits", key="exhibits_btn", use_container_width=True,
                    type="primary" if st.session_state.view == "Exhibits" else "secondary"):
            st.session_state.view = "Exhibits"
            st.rerun()
        
        # Enhanced filtering section
        if st.session_state.view == "Facts":
            st.markdown('<div class="section-header">🔍 Filters</div>', unsafe_allow_html=True)
            
            # Party filter with multiselect
            selected_parties = st.multiselect(
                "Select Parties:",
                ["Appellant", "Respondent"],
                default=st.session_state.selected_parties,
                key="party_filter"
            )
            st.session_state.selected_parties = selected_parties
            
            # Date range filter
            date_range = st.selectbox(
                "Date Range:",
                ["All Time", "1950s", "1970s-1980s", "2000s-Present"],
                key="date_filter"
            )
            st.session_state.date_range = date_range
            
            # Quick stats
            facts_data = get_all_facts()
            total_facts = len(facts_data)
            disputed_facts = len([f for f in facts_data if f['isDisputed']])
            undisputed_facts = total_facts - disputed_facts
            
            st.markdown('<div class="section-header">📈 Quick Stats</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Facts", total_facts)
                st.metric("Disputed", disputed_facts, delta=f"{(disputed_facts/total_facts*100):.1f}%")
            with col2:
                st.metric("Undisputed", undisputed_facts, delta=f"{(undisputed_facts/total_facts*100):.1f}%")

# Enhanced fact card component
def render_enhanced_fact_card(fact, index):
    card_class = "disputed-card" if fact['isDisputed'] else "undisputed-card"
    
    with st.container():
        st.markdown(f'<div class="fact-card {card_class}">', unsafe_allow_html=True)
        
        # Header with date, status, and parties
        header_col1, header_col2, header_col3 = st.columns([2, 1, 1])
        
        with header_col1:
            st.markdown(f"### 📅 {fact['date']}")
            st.markdown(f"**{fact['event']}**")
        
        with header_col2:
            status_class = "badge-disputed" if fact['isDisputed'] else "badge-undisputed"
            status_text = "Disputed" if fact['isDisputed'] else "Undisputed"
            st.markdown(f'<span class="status-badge {status_class}">{status_text}</span>', unsafe_allow_html=True)
        
        with header_col3:
            for party in fact.get('parties_involved', []):
                party_class = "badge-appellant" if party == "Appellant" else "badge-respondent"
                st.markdown(f'<span class="status-badge {party_class}">{party}</span>', unsafe_allow_html=True)
        
        # Expandable details
        with st.expander("View Details", expanded=False):
            # Evidence section with enhanced styling
            st.markdown('<div class="subsection-header">📁 Evidence & References</div>', unsafe_allow_html=True)
            
            evidence_content = get_evidence_content(fact)
            if evidence_content:
                for evidence in evidence_content:
                    st.markdown('<div class="evidence-section">', unsafe_allow_html=True)
                    st.markdown(f"**{evidence['id']}** - {evidence['title']}")
                    st.markdown(f"_{evidence['summary']}_")
                    
                    # Reference details
                    ref_col1, ref_col2 = st.columns([3, 1])
                    with ref_col1:
                        ref_parts = [f"**Exhibit:** {evidence['id']}"]
                        if fact.get('page'):
                            ref_parts.append(f"**Page:** {fact['page']}")
                        if fact.get('paragraphs'):
                            ref_parts.append(f"**Paragraphs:** {fact['paragraphs']}")
                        st.markdown(" | ".join(ref_parts))
                    
                    with ref_col2:
                        if st.button(f"📋 Copy", key=f"copy_{evidence['id']}_{index}"):
                            st.success("Copied!")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("No evidence references available")
            
            # Party submissions with enhanced styling
            st.markdown('<div class="subsection-header">⚖️ Party Submissions</div>', unsafe_allow_html=True)
            
            # Claimant submission
            st.markdown('<div class="submission-section claimant-submission">', unsafe_allow_html=True)
            st.markdown("**🔵 Appellant Submission**")
            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
            if claimant_text != 'No specific submission recorded':
                st.markdown(f"_{claimant_text}_")
            else:
                st.markdown("_No submission provided_")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Respondent submission
            st.markdown('<div class="submission-section respondent-submission">', unsafe_allow_html=True)
            st.markdown("**🔴 Respondent Submission**")
            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
            if respondent_text != 'No specific submission recorded':
                st.markdown(f"_{respondent_text}_")
            else:
                st.markdown("_No submission provided_")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Enhanced timeline component
def render_enhanced_timeline(facts_data):
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
    
    # Group by year
    events_by_year = {}
    for fact in facts_data:
        year = fact['date'].split('-')[0] if '-' in fact['date'] else fact['date'][:4]
        if year not in events_by_year:
            events_by_year[year] = []
        events_by_year[year].append(fact)
    
    for year, events in events_by_year.items():
        st.markdown(f"## 📅 {year}")
        
        for i, fact in enumerate(events):
            dot_class = "disputed" if fact['isDisputed'] else ""
            st.markdown(f'<div class="timeline-dot {dot_class}"></div>', unsafe_allow_html=True)
            
            # Event card
            render_enhanced_fact_card(fact, f"{year}_{i}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced card view
def render_enhanced_card_view(filtered_facts):
    if not filtered_facts:
        st.info("No facts found matching the selected criteria.")
        return
    
    # Sort by date
    filtered_facts.sort(key=lambda x: x['date'].split('-')[0] if '-' in x['date'] else x['date'][:4])
    
    for i, fact in enumerate(filtered_facts):
        render_enhanced_fact_card(fact, i)

# Enhanced document categories view
def render_enhanced_docset_view(filtered_facts):
    document_sets = get_document_sets()
    
    # Group facts by document categories
    docs_with_facts = {}
    
    for ds in document_sets:
        if ds.get('isGroup'):
            docs_with_facts[ds['id']] = {
                'docset': ds,
                'facts': []
            }
    
    # Distribute facts to categories
    for fact in filtered_facts:
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
        
        party_color = ("🔵" if docset['party'] == 'Appellant' else 
                      "🔴" if docset['party'] == 'Respondent' else "⚪")
        
        with st.expander(f"📁 {party_color} **{docset['name'].title()}** ({len(facts)} facts)", expanded=False):
            if facts:
                for i, fact in enumerate(facts):
                    render_enhanced_fact_card(fact, f"{docset_id}_{i}")
            else:
                st.info("No facts found in this document category.")

# Apply filters to facts
def apply_filters(facts_data):
    filtered_facts = facts_data.copy()
    
    # Filter by parties
    if st.session_state.selected_parties:
        filtered_facts = [
            fact for fact in filtered_facts 
            if any(party in fact.get('parties_involved', []) for party in st.session_state.selected_parties)
        ]
    
    # Filter by date range
    if st.session_state.date_range != "All Time":
        if st.session_state.date_range == "1950s":
            filtered_facts = [f for f in filtered_facts if f['date'].startswith('195')]
        elif st.session_state.date_range == "1970s-1980s":
            filtered_facts = [f for f in filtered_facts if f['date'].startswith('197') or f['date'].startswith('198')]
        elif st.session_state.date_range == "2000s-Present":
            filtered_facts = [f for f in filtered_facts if f['date'].startswith('20')]
    
    return filtered_facts

# Main application
def main():
    # Render enhanced sidebar
    render_enhanced_sidebar()
    
    # Main content area
    if st.session_state.view == "Facts":
        st.markdown('<div class="section-header">⚖️ Case Facts Analysis</div>', unsafe_allow_html=True)
        
        # View type selection with enhanced buttons
        view_col1, view_col2, view_col3, view_col4 = st.columns([2, 2, 2, 2])
        
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
        
        with view_col4:
            # Export functionality
            facts_data = get_all_facts()
            df = pd.DataFrame(facts_data)
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Export CSV",
                data=csv,
                file_name="case_facts.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        st.divider()
        
        # Filter tabs with enhanced styling
        filter_tab1, filter_tab2, filter_tab3 = st.tabs(["📊 All Facts", "🔴 Disputed Facts", "🟢 Undisputed Facts"])
        
        with filter_tab1:
            facts_data = get_all_facts()
            filtered_facts = apply_filters(facts_data)
            
            if st.session_state.current_view_type == "card":
                render_enhanced_card_view(filtered_facts)
            elif st.session_state.current_view_type == "timeline":
                render_enhanced_timeline(filtered_facts)
            elif st.session_state.current_view_type == "docset":
                render_enhanced_docset_view(filtered_facts)
        
        with filter_tab2:
            facts_data = [fact for fact in get_all_facts() if fact['isDisputed']]
            filtered_facts = apply_filters(facts_data)
            
            if st.session_state.current_view_type == "card":
                render_enhanced_card_view(filtered_facts)
            elif st.session_state.current_view_type == "timeline":
                render_enhanced_timeline(filtered_facts)
            elif st.session_state.current_view_type == "docset":
                render_enhanced_docset_view(filtered_facts)
        
        with filter_tab3:
            facts_data = [fact for fact in get_all_facts() if not fact['isDisputed']]
            filtered_facts = apply_filters(facts_data)
            
            if st.session_state.current_view_type == "card":
                render_enhanced_card_view(filtered_facts)
            elif st.session_state.current_view_type == "timeline":
                render_enhanced_timeline(filtered_facts)
            elif st.session_state.current_view_type == "docset":
                render_enhanced_docset_view(filtered_facts)
    
    elif st.session_state.view == "Arguments":
        st.markdown('<div class="section-header">📑 Legal Arguments</div>', unsafe_allow_html=True)
        st.info("Arguments view is under development. This will show the structured legal arguments from both parties.")
    
    elif st.session_state.view == "Exhibits":
        st.markdown('<div class="section-header">📁 Evidence & Exhibits</div>', unsafe_allow_html=True)
        st.info("Exhibits view is under development. This will show all evidence and exhibits referenced in the case.")

if __name__ == "__main__":
    main()

