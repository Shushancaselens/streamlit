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
                
                .view-toggle button:nth-child(2) {{
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
                    display: none; /* Changed to 'none' to be closed by default */
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
                    transform: rotate(0deg); /* Start collapsed by default */
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
                
                /* Card View styling */
                .card-fact-container {{
                    margin-bottom: 16px;
                    border: 1px solid #e2e8f0;
                    border-radius: 8px;
                    background-color: white;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                
                .card-fact-container.disputed {{
                    border-left: 4px solid #e53e3e;
                    background-color: rgba(229, 62, 62, 0.02);
                }}
                
                .card-fact-header {{
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    padding: 16px;
                    background-color: #f8fafc;
                    cursor: pointer;
                    transition: background-color 0.2s;
                }}
                
                .card-fact-header:hover {{
                    background-color: #e2e8f0;
                }}
                
                .card-fact-header.disputed {{
                    background-color: rgba(229, 62, 62, 0.05);
                }}
                
                .card-fact-header.disputed:hover {{
                    background-color: rgba(229, 62, 62, 0.1);
                }}
                
                .card-fact-title {{
                    display: flex;
                    align-items: center;
                    flex-grow: 1;
                    gap: 12px;
                }}
                
                .card-fact-date {{
                    font-weight: 600;
                    color: #2d3748;
                    min-width: 120px;
                }}
                
                .card-fact-event {{
                    font-weight: 500;
                    color: #1a202c;
                    flex-grow: 1;
                }}
                
                .card-fact-badges {{
                    display: flex;
                    gap: 6px;
                    align-items: center;
                }}
                
                .card-chevron {{
                    transition: transform 0.2s;
                    color: #718096;
                    margin-left: 8px;
                }}
                
                .card-chevron.expanded {{
                    transform: rotate(90deg);
                }}
                
                .card-fact-content {{
                    display: none;
                    padding: 20px;
                    border-top: 1px solid #e2e8f0;
                    background-color: white;
                }}
                
                .card-fact-content.show {{
                    display: block;
                }}
                
                .card-fact-details {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 20px;
                    margin-bottom: 16px;
                }}
                
                .card-detail-section {{
                    background-color: #f7fafc;
                    padding: 12px 16px;
                    border-radius: 6px;
                    border: 1px solid #e2e8f0;
                }}
                
                .card-detail-label {{
                    font-weight: 600;
                    color: #4a5568;
                    font-size: 12px;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                    margin-bottom: 4px;
                }}
                
                .card-detail-value {{
                    color: #2d3748;
                    font-size: 14px;
                    line-height: 1.4;
                }}
                
                .card-source-text {{
                    background-color: #f7fafc;
                    padding: 16px;
                    border-radius: 6px;
                    border-left: 4px solid #4299e1;
                    margin: 16px 0;
                    font-style: italic;
                    color: #4a5568;
                    line-height: 1.5;
                }}
                
                .card-source-text.claimant-submission {{
                    border-left-color: #3182ce;
                    background-color: rgba(49, 130, 206, 0.03);
                }}
                
                .card-source-text.respondent-submission {{
                    border-left-color: #e53e3e;
                    background-color: rgba(229, 62, 62, 0.03);
                }}
                
                .submission-header {{
                    font-weight: 600;
                    text-transform: uppercase;
                    font-size: 11px;
                    letter-spacing: 0.05em;
                    margin-bottom: 8px;
                    color: inherit;
                }}
                
                .claimant-submission .submission-header {{
                    color: #3182ce;
                }}
                
                .respondent-submission .submission-header {{
                    color: #e53e3e;
                }}
                
                .card-exhibits {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 6px;
                    margin-top: 12px;
                }}
                
                @media (max-width: 768px) {{
                    .card-fact-details {{
                        grid-template-columns: 1fr;
                    }}
                    
                    .card-fact-title {{
                        flex-direction: column;
                        align-items: flex-start;
                        gap: 8px;
                    }}
                    
                    .card-fact-date {{
                        min-width: auto;
                    }}
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
                
                /* Enhanced Evidence styling */
                .evidence-item {{
                    border: 1px solid #e2e8f0;
                    border-radius: 6px;
                    overflow: hidden;
                    margin-bottom: 6px;
                    transition: all 0.2s ease;
                }}
                
                .evidence-header {{
                    padding: 8px 12px;
                    background-color: rgba(221, 107, 32, 0.05);
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    transition: background-color 0.2s ease;
                }}
                
                .evidence-header:hover {{
                    background-color: rgba(221, 107, 32, 0.1);
                }}
                
                .evidence-content {{
                    display: none;
                    padding: 12px;
                    background-color: white;
                    border-top: 1px solid #e2e8f0;
                    animation: slideDown 0.2s ease;
                }}
                
                .evidence-icon {{
                    width: 16px;
                    height: 16px;
                    background-color: #dd6b20;
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 10px;
                    font-weight: bold;
                    transition: transform 0.2s ease;
                }}
                
                .evidence-badge {{
                    display: inline-flex;
                    align-items: center;
                    padding: 3px 6px;
                    background-color: rgba(221, 107, 32, 0.1);
                    color: #dd6b20;
                    border-radius: 12px;
                    cursor: pointer;
                    font-size: 10px;
                    font-weight: 600;
                    transition: background-color 0.2s ease;
                    margin: 2px;
                }}
                
                .evidence-badge:hover {{
                    background-color: rgba(221, 107, 32, 0.2);
                }}
                
                @keyframes slideDown {{
                    from {{
                        opacity: 0;
                        max-height: 0;
                    }}
                    to {{
                        opacity: 1;
                        max-height: 200px;
                    }}
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
                        <button id="card-view-btn" class="active" onclick="switchView('card')">Card View</button>
                        <button id="docset-view-btn" onclick="switchView('docset')">Document Categories</button>
                        <button id="timeline-view-btn" onclick="switchView('timeline')">Timeline View</button>
                    </div>
                    
                    <div class="facts-header">
                        <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                        <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                        <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                    </div>
                    
                    <!-- Card View -->
                    <div id="card-view-content" class="facts-content">
                        <div id="card-facts-container"></div>
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
                // Initialize data - ensure all views use the same core data structure
                const factsData = {facts_json};
                const documentSets = {document_sets_json};
                const timelineData = {timeline_json};
                
                // Standardize data structure across all views
                function standardizeFactData(fact) {{
                    return {{
                        date: fact.date,
                        event: fact.event,
                        source_text: fact.source_text || '',
                        page: fact.page || '',
                        doc_name: fact.doc_name || '',
                        doc_summary: fact.doc_summary || '',
                        claimant_submission: fact.claimant_submission || 'No specific submission recorded',
                        respondent_submission: fact.respondent_submission || 'No specific submission recorded',
                        isDisputed: fact.isDisputed,
                        exhibits: fact.exhibits || [],
                        evidence: fact.evidence || [], // Add evidence details
                        parties_involved: fact.parties_involved || [],
                        argId: fact.argId || '',
                        argTitle: fact.argTitle || '',
                        paragraphs: fact.paragraphs || ''
                    }};
                }}
                
                // Function to get evidence content with expandable functionality
                function getEvidenceContent(fact, viewType = 'card') {{
                    if (!fact.exhibits || fact.exhibits.length === 0) {{
                        return 'None';
                    }}
                    
                    // Get evidence details from the argument data
                    const args_data = {args_json};
                    let evidenceContent = [];
                    
                    fact.exhibits.forEach(exhibitId => {{
                        // Search through all arguments to find evidence details
                        function findEvidence(args) {{
                            for (const argKey in args) {{
                                const arg = args[argKey];
                                if (arg.evidence) {{
                                    const evidence = arg.evidence.find(e => e.id === exhibitId);
                                    if (evidence) {{
                                        return evidence;
                                    }}
                                }}
                                if (arg.children) {{
                                    const childEvidence = findEvidence(arg.children);
                                    if (childEvidence) return childEvidence;
                                }}
                            }}
                            return null;
                        }}
                        
                        // Look in both claimant and respondent args
                        let evidence = findEvidence(args_data.claimantArgs) || findEvidence(args_data.respondentArgs);
                        
                        if (evidence) {{
                            evidenceContent.push({{
                                id: exhibitId,
                                title: evidence.title,
                                summary: evidence.summary
                            }});
                        }} else {{
                            evidenceContent.push({{
                                id: exhibitId,
                                title: exhibitId,
                                summary: 'Evidence details not available'
                            }});
                        }}
                    }});
                    
                    return evidenceContent;
                }}
                
                // Toggle evidence expansion
                function toggleEvidence(evidenceId, factIndex) {{
                    const content = document.getElementById(`evidence-content-${{evidenceId}}-${{factIndex}}`);
                    const icon = document.getElementById(`evidence-icon-${{evidenceId}}-${{factIndex}}`);
                    
                    if (content.style.display === 'none' || content.style.display === '') {{
                        content.style.display = 'block';
                        icon.textContent = '−';
                        icon.style.transform = 'rotate(0deg)';
                    }} else {{
                        content.style.display = 'none';
                        icon.textContent = '+';
                        icon.style.transform = 'rotate(0deg)';
                    }}
                }}
                
                // Standardize timeline data to match facts structure
                function standardizeTimelineData(item) {{
                    return {{
                        date: item.date,
                        event: item.event,
                        source_text: item.source_text || '',
                        page: item.page || '',
                        doc_name: item.doc_name || '',
                        doc_summary: item.doc_summary || '',
                        claimant_submission: item.claimant_submission || 'No specific submission recorded',
                        respondent_submission: item.respondent_submission || 'No specific submission recorded',
                        isDisputed: item.isDisputed,
                        exhibits: item.exhibits || [],
                        evidence: item.evidence || [],
                        parties_involved: item.parties_involved || [],
                        argId: item.argId || '',
                        argTitle: item.argTitle || '',
                        paragraphs: item.paragraphs || ''
                    }};
                }}
                
                // Switch view between card, timeline, and document sets (removed table)
                function switchView(viewType) {{
                    const cardBtn = document.getElementById('card-view-btn');
                    const timelineBtn = document.getElementById('timeline-view-btn');
                    const docsetBtn = document.getElementById('docset-view-btn');
                    
                    const cardContent = document.getElementById('card-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    // Remove active class from all buttons
                    cardBtn.classList.remove('active');
                    timelineBtn.classList.remove('active');
                    docsetBtn.classList.remove('active');
                    
                    // Hide all content
                    cardContent.style.display = 'none';
                    timelineContent.style.display = 'none';
                    docsetContent.style.display = 'none';
                    
                    // Activate the selected view
                    if (viewType === 'card') {{
                        cardBtn.classList.add('active');
                        cardContent.style.display = 'block';
                        renderCardView();
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
                    const cardContent = document.getElementById('card-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    
                    if (cardContent.style.display !== 'none') {{
                        // Copy card data
                        contentToCopy += 'Case Facts (Card View)\\n\\n';
                        
                        const cardItems = document.querySelectorAll('.card-fact-container');
                        cardItems.forEach(card => {{
                            const dateEl = card.querySelector('.card-fact-date');
                            const eventEl = card.querySelector('.card-fact-event');
                            const partyEls = card.querySelectorAll('.badge');
                            const claimantSubmissionEl = card.querySelector('.card-source-text:nth-of-type(1) div:last-child');
                            const respondentSubmissionEl = card.querySelector('.card-source-text:nth-of-type(2) div:last-child');
                            
                            if (dateEl && eventEl) {{
                                const date = dateEl.textContent.trim();
                                const event = eventEl.textContent.trim();
                                const parties = Array.from(partyEls).map(el => el.textContent.trim()).filter(text => text !== 'Disputed').join(', ');
                                const claimantSubmission = claimantSubmissionEl ? claimantSubmissionEl.textContent.trim() : '';
                                const respondentSubmission = respondentSubmissionEl ? respondentSubmissionEl.textContent.trim() : '';
                                
                                contentToCopy += `${{date}} - ${{event}} (${{parties}})\\n`;
                                if (claimantSubmission) {{
                                    contentToCopy += `Claimant: ${{claimantSubmission}}\\n`;
                                }}
                                if (respondentSubmission) {{
                                    contentToCopy += `Respondent: ${{respondentSubmission}}\\n`;
                                }}
                                contentToCopy += '\\n';
                            }}
                        }});
                    }} else if (timelineContent.style.display !== 'none') {{
                        // Copy timeline data
                        contentToCopy += 'Case Timeline\\n\\n';
                        
                        const timelineItems = document.querySelectorAll('.timeline-item');
                        timelineItems.forEach(item => {{
                            const dateEl = item.querySelector('.timeline-date');
                            const factEl = item.querySelector('.timeline-fact');
                            const partyEls = item.querySelectorAll('.badge');
                            const claimantEl = item.querySelector('.timeline-source-text[style*="3182ce"]');
                            const respondentEl = item.querySelector('.timeline-source-text[style*="e53e3e"]');
                            
                            if (dateEl && factEl) {{
                                const date = dateEl.textContent.trim();
                                const fact = factEl.textContent.trim();
                                const parties = Array.from(partyEls).map(el => el.textContent.trim()).filter(text => text !== 'Disputed').join(', ');
                                
                                contentToCopy += `${{date}} - ${{fact}} (${{parties}})\\n`;
                                
                                if (claimantEl) {{
                                    const claimantText = claimantEl.textContent.replace('Claimant Submission:', '').trim();
                                    contentToCopy += `Claimant: ${{claimantText}}\\n`;
                                }}
                                
                                if (respondentEl) {{
                                    const respondentText = respondentEl.textContent.replace('Respondent Submission:', '').trim();
                                    contentToCopy += `Respondent: ${{respondentText}}\\n`;
                                }}
                                
                                contentToCopy += '\\n';
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
                    
                    // Get currently active tab filter
                    const allBtn = document.getElementById('all-facts-btn');
                    const disputedBtn = document.getElementById('disputed-facts-btn');
                    const undisputedBtn = document.getElementById('undisputed-facts-btn');
                    
                    let currentFacts = factsData.map(standardizeFactData);
                    if (disputedBtn.classList.contains('active')) {{
                        currentFacts = currentFacts.filter(fact => fact.isDisputed);
                    }} else if (undisputedBtn.classList.contains('active')) {{
                        currentFacts = currentFacts.filter(fact => !fact.isDisputed);
                    }}
                    
                    // Standard headers for all views
                    let headers = "Date,Event,Source Text,Page,Document,Doc Summary,Claimant Submission,Respondent Submission,Status,Evidence\\n";
                    let rows = '';
                    
                    currentFacts.forEach(fact => {{
                        const evidenceContent = getEvidenceContent(fact);
                        let evidenceText = 'None';
                        if (evidenceContent !== 'None') {{
                            evidenceText = evidenceContent.map(ev => `${{ev.id}}: ${{ev.title}} - ${{ev.summary}}`).join(' | ');
                        }}
                        
                        const sourceText = (fact.source_text || '').replace(/"/g, '""');
                        const docName = (fact.doc_name || '').replace(/"/g, '""');
                        const docSummary = (fact.doc_summary || '').replace(/"/g, '""');
                        const claimantSubmission = (fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' ? fact.claimant_submission : 'No submission').replace(/"/g, '""');
                        const respondentSubmission = (fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' ? fact.respondent_submission : 'No submission').replace(/"/g, '""');
                        const evidenceForCsv = evidenceText.replace(/"/g, '""');
                        
                        rows += `"${{fact.date}}","${{fact.event}}","${{sourceText}}","${{fact.page || ''}}","${{docName}}","${{docSummary}}","${{claimantSubmission}}","${{respondentSubmission}}","${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}","${{evidenceForCsv}}"\\n`;
                    }});
                    
                    const csvContent = headers + rows;
                    const encodedUri = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
                    const link = document.createElement("a");
                    link.setAttribute("href", encodedUri);
                    
                    // Set filename based on active view
                    let filename = "facts.csv";
                    const cardContent = document.getElementById('card-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    if (cardContent.style.display !== 'none') {{
                        filename = "facts_cards.csv";
                    }} else if (timelineContent.style.display !== 'none') {{
                        filename = "facts_timeline.csv";
                    }} else if (docsetContent.style.display !== 'none') {{
                        filename = "facts_documents.csv";
                    }}
                    
                    link.setAttribute("download", filename);
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
                    }} else if (tabType === 'disputed') {{
                        disputedBtn.classList.add('active');
                    }} else {{
                        undisputedBtn.classList.add('active');
                    }}
                    
                    // Update active view
                    const cardContent = document.getElementById('card-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    if (cardContent.style.display !== 'none') {{
                        renderCardView(tabType);
                    }} else if (timelineContent.style.display !== 'none') {{
                        renderTimeline(tabType);
                    }} else if (docsetContent.style.display !== 'none') {{
                        renderDocumentSets(tabType);
                    }}
                }}
                
                // Toggle card fact visibility
                function toggleCardFact(factIndex) {{
                    const content = document.getElementById(`card-fact-content-${{factIndex}}`);
                    const chevron = document.getElementById(`card-chevron-${{factIndex}}`);
                    
                    if (content.classList.contains('show')) {{
                        content.classList.remove('show');
                        chevron.classList.remove('expanded');
                    }} else {{
                        content.classList.add('show');
                        chevron.classList.add('expanded');
                    }}
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
                
                // Render card view with dropdown containers for each fact
                function renderCardView(tabType = 'all') {{
                    const container = document.getElementById('card-facts-container');
                    container.innerHTML = '';
                    
                    // Filter facts based on tab type and standardize
                    let filteredFacts = factsData.map(standardizeFactData);
                    if (tabType === 'disputed') {{
                        filteredFacts = filteredFacts.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = filteredFacts.filter(fact => !fact.isDisputed);
                    }}
                    
                    // Sort by date
                    filteredFacts.sort((a, b) => {{
                        const dateA = a.date.split('-')[0];
                        const dateB = b.date.split('-')[0];
                        return new Date(dateA) - new Date(dateB);
                    }});
                    
                    // Render each fact as a card
                    filteredFacts.forEach((fact, index) => {{
                        const cardContainer = document.createElement('div');
                        cardContainer.className = `card-fact-container${{fact.isDisputed ? ' disputed' : ''}}`;
                        
                        // Create card header
                        const headerEl = document.createElement('div');
                        headerEl.className = `card-fact-header${{fact.isDisputed ? ' disputed' : ''}}`;
                        headerEl.onclick = () => toggleCardFact(index);
                        
                        // Create title section
                        const titleEl = document.createElement('div');
                        titleEl.className = 'card-fact-title';
                        
                        // Date
                        const dateEl = document.createElement('div');
                        dateEl.className = 'card-fact-date';
                        dateEl.textContent = fact.date;
                        titleEl.appendChild(dateEl);
                        
                        // Event
                        const eventEl = document.createElement('div');
                        eventEl.className = 'card-fact-event';
                        eventEl.textContent = fact.event;
                        titleEl.appendChild(eventEl);
                        
                        headerEl.appendChild(titleEl);
                        
                        // Create badges section
                        const badgesEl = document.createElement('div');
                        badgesEl.className = 'card-fact-badges';
                        
                        // Parties involved badges
                        if (fact.parties_involved && fact.parties_involved.length > 0) {{
                            fact.parties_involved.forEach(party => {{
                                const partyBadge = document.createElement('span');
                                partyBadge.className = `badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                                partyBadge.textContent = party;
                                badgesEl.appendChild(partyBadge);
                            }});
                        }}
                        
                        // Disputed badge
                        if (fact.isDisputed) {{
                            const disputedBadge = document.createElement('span');
                            disputedBadge.className = 'badge disputed-badge';
                            disputedBadge.textContent = 'Disputed';
                            badgesEl.appendChild(disputedBadge);
                        }}
                        
                        // Chevron
                        const chevronEl = document.createElement('div');
                        chevronEl.className = 'card-chevron';
                        chevronEl.id = `card-chevron-${{index}}`;
                        chevronEl.innerHTML = `
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                        `;
                        
                        badgesEl.appendChild(chevronEl);
                        headerEl.appendChild(badgesEl);
                        cardContainer.appendChild(headerEl);
                        
                        // Create card content with standardized structure
                        const contentEl = document.createElement('div');
                        contentEl.className = 'card-fact-content';
                        contentEl.id = `card-fact-content-${{index}}`;
                        
                        // Create details grid
                        const detailsEl = document.createElement('div');
                        detailsEl.className = 'card-fact-details';
                        
                        // Document info
                        const docSection = document.createElement('div');
                        docSection.className = 'card-detail-section';
                        docSection.innerHTML = `
                            <div class="card-detail-label">Document</div>
                            <div class="card-detail-value">
                                <strong>${{fact.doc_name || 'N/A'}}</strong>
                                ${{fact.page ? '<br><small>Page ' + fact.page + '</small>' : ''}}
                            </div>
                        `;
                        detailsEl.appendChild(docSection);
                        
                        // Argument info
                        const argSection = document.createElement('div');
                        argSection.className = 'card-detail-section';
                        argSection.innerHTML = `
                            <div class="card-detail-label">Argument</div>
                            <div class="card-detail-value">
                                <strong>${{fact.argId}}. ${{fact.argTitle}}</strong>
                                ${{fact.paragraphs ? '<br><small>Paragraphs: ' + fact.paragraphs + '</small>' : ''}}
                            </div>
                        `;
                        detailsEl.appendChild(argSection);
                        
                        contentEl.appendChild(detailsEl);
                        
                        // Source Text (always show if available)
                        if (fact.source_text && fact.source_text !== 'No specific submission recorded') {{
                            const sourceTextEl = document.createElement('div');
                            sourceTextEl.className = 'card-source-text';
                            sourceTextEl.innerHTML = `
                                <div class="submission-header">Source Text</div>
                                <div>${{fact.source_text}}</div>
                            `;
                            contentEl.appendChild(sourceTextEl);
                        }}
                        
                        // Evidence section (moved here, under Source Text)
                        const evidenceContent = getEvidenceContent(fact);
                        if (evidenceContent !== 'None') {{
                            const evidenceSection = document.createElement('div');
                            evidenceSection.className = 'card-detail-section';
                            evidenceSection.style.marginTop = '16px';
                            evidenceSection.innerHTML = `
                                <div class="card-detail-label">Evidence (${{evidenceContent.length}} items)</div>
                                <div class="card-detail-value">
                                    ${{evidenceContent.map((evidence, evidenceIndex) => `
                                        <div style="margin-bottom: 6px; border: 1px solid #e2e8f0; border-radius: 6px; overflow: hidden;">
                                            <div onclick="toggleEvidence('${{evidence.id}}', '${{index}}-${{evidenceIndex}}')" 
                                                 style="padding: 8px 12px; background-color: rgba(221, 107, 32, 0.05); cursor: pointer; display: flex; align-items: center; justify-content: space-between; transition: background-color 0.2s;"
                                                 onmouseover="this.style.backgroundColor='rgba(221, 107, 32, 0.1)'" 
                                                 onmouseout="this.style.backgroundColor='rgba(221, 107, 32, 0.05)'">
                                                <div>
                                                    <span style="font-weight: 600; color: #dd6b20; font-size: 12px;">${{evidence.id}}</span>
                                                    <span style="margin-left: 8px; color: #4a5568; font-size: 12px;">${{evidence.title}}</span>
                                                </div>
                                                <span id="evidence-icon-${{evidence.id}}-${{index}}-${{evidenceIndex}}" 
                                                      style="width: 16px; height: 16px; background-color: #dd6b20; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: bold;">+</span>
                                            </div>
                                            <div id="evidence-content-${{evidence.id}}-${{index}}-${{evidenceIndex}}" 
                                                 style="display: none; padding: 12px; background-color: white; border-top: 1px solid #e2e8f0;">
                                                <div style="font-weight: 600; color: #dd6b20; font-size: 13px; margin-bottom: 6px;">${{evidence.title}}</div>
                                                <div style="font-size: 12px; color: #666; line-height: 1.4;">${{evidence.summary}}</div>
                                            </div>
                                        </div>
                                    `).join('')}}
                                </div>
                            `;
                            contentEl.appendChild(evidenceSection);
                        }}
                        
                        // Claimant Submission
                        if (fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded') {{
                            const claimantSubmissionEl = document.createElement('div');
                            claimantSubmissionEl.className = 'card-source-text claimant-submission';
                            claimantSubmissionEl.innerHTML = `
                                <div class="submission-header">*** CLAIMANT SUBMISSION ***</div>
                                <div>${{fact.claimant_submission}}</div>
                            `;
                            contentEl.appendChild(claimantSubmissionEl);
                        }}
                        
                        // Respondent Submission
                        if (fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded') {{
                            const respondentSubmissionEl = document.createElement('div');
                            respondentSubmissionEl.className = 'card-source-text respondent-submission';
                            respondentSubmissionEl.innerHTML = `
                                <div class="submission-header">*** RESPONDENT SUBMISSION ***</div>
                                <div>${{fact.respondent_submission}}</div>
                            `;
                            contentEl.appendChild(respondentSubmissionEl);
                        }}
                        
                        // Document summary
                        if (fact.doc_summary) {{
                            const summaryEl = document.createElement('div');
                            summaryEl.className = 'card-detail-section';
                            summaryEl.style.marginTop = '16px';
                            summaryEl.innerHTML = `
                                <div class="card-detail-label">Document Summary</div>
                                <div class="card-detail-value">${{fact.doc_summary}}</div>
                            `;
                            contentEl.appendChild(summaryEl);
                        }}
                        
                        // Status section (Evidence removed since it's now under Source Text)
                        const statusSection = document.createElement('div');
                        statusSection.className = 'card-fact-details';
                        statusSection.style.marginTop = '16px';
                        
                        // Status
                        const statusInfo = document.createElement('div');
                        statusInfo.className = 'card-detail-section';
                        statusInfo.innerHTML = `
                            <div class="card-detail-label">Status</div>
                            <div class="card-detail-value">${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}</div>
                        `;
                        statusSection.appendChild(statusInfo);
                        
                        contentEl.appendChild(statusSection);
                        cardContainer.appendChild(contentEl);
                        container.appendChild(cardContainer);
                    }});
                    
                    // If no facts found
                    if (filteredFacts.length === 0) {{
                        container.innerHTML = '<p style="text-align: center; padding: 40px; color: #718096;">No facts found matching the selected criteria.</p>';
                    }}
                }}
                
                // Render enhanced timeline view
                function renderTimeline(tabType = 'all') {{
                    const container = document.getElementById('timeline-events');
                    container.innerHTML = '';
                    
                    // Use factsData and standardize it, not separate timelineData
                    let filteredData = factsData.map(standardizeFactData);
                    if (tabType === 'disputed') {{
                        filteredData = filteredData.filter(item => item.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredData = filteredData.filter(item => !item.isDisputed);
                    }}
                    
                    // Sort by date
                    filteredData.sort((a, b) => {{
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
                        
                        // Parties involved badges
                        if (fact.parties_involved && fact.parties_involved.length > 0) {{
                            fact.parties_involved.forEach(party => {{
                                const partyBadge = document.createElement('span');
                                partyBadge.className = `badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                                partyBadge.textContent = party;
                                badgesEl.appendChild(partyBadge);
                            }});
                        }}
                        
                        // Status badge
                        const statusBadge = document.createElement('span');
                        statusBadge.className = `badge ${{fact.isDisputed ? 'disputed-badge' : 'shared-badge'}}`;
                        statusBadge.textContent = fact.isDisputed ? 'Disputed' : 'Undisputed';
                        badgesEl.appendChild(statusBadge);
                        
                        headerEl.appendChild(badgesEl);
                        contentEl.appendChild(headerEl);
                        
                        // Create timeline body
                        const bodyEl = document.createElement('div');
                        bodyEl.className = 'timeline-body';
                        
                        // Event content
                        const factContent = document.createElement('div');
                        factContent.className = 'timeline-fact';
                        factContent.textContent = fact.event;
                        bodyEl.appendChild(factContent);
                        
                        // Document and reference information section
                        const docInfoEl = document.createElement('div');
                        docInfoEl.className = 'timeline-meta';
                        docInfoEl.style.cssText = 'background-color: #f8fafc; padding: 12px; border-radius: 6px; margin: 12px 0; border: 1px solid #e2e8f0;';
                        docInfoEl.innerHTML = `
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 13px;">
                                <div><strong>Document:</strong> ${{fact.doc_name || 'N/A'}}</div>
                                <div><strong>Page:</strong> ${{fact.page || 'N/A'}}</div>
                                <div><strong>Argument:</strong> ${{fact.argId}}. ${{fact.argTitle}}</div>
                                <div><strong>Paragraphs:</strong> ${{fact.paragraphs || 'N/A'}}</div>
                            </div>
                            ${{fact.doc_summary ? '<div style="margin-top: 8px; font-style: italic; color: #666; font-size: 12px;"><strong>Document Summary:</strong> ' + fact.doc_summary + '</div>' : ''}}
                        `;
                        bodyEl.appendChild(docInfoEl);
                        
                        // Source Text (if different from submissions and available)
                        if (fact.source_text && fact.source_text !== 'No specific submission recorded' && 
                            fact.source_text !== fact.claimant_submission && fact.source_text !== fact.respondent_submission) {{
                            const sourceTextEl = document.createElement('div');
                            sourceTextEl.className = 'timeline-source-text';
                            sourceTextEl.style.cssText = 'font-style: italic; color: #4a5568; margin-top: 8px; padding: 12px; background-color: rgba(74, 85, 104, 0.05); border-left: 4px solid #4a5568; font-size: 13px; border-radius: 0 6px 6px 0;';
                            sourceTextEl.innerHTML = `<strong>Source Text:</strong><br>${{fact.source_text}}`;
                            bodyEl.appendChild(sourceTextEl);
                        }}
                        
                        // Add claimant submission
                        if (fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded') {{
                            const claimantTextEl = document.createElement('div');
                            claimantTextEl.className = 'timeline-source-text';
                            claimantTextEl.style.cssText = 'font-style: italic; color: #3182ce; margin-top: 8px; padding: 12px; background-color: rgba(49, 130, 206, 0.05); border-left: 4px solid #3182ce; font-size: 13px; border-radius: 0 6px 6px 0;';
                            claimantTextEl.innerHTML = `<strong>*** CLAIMANT SUBMISSION ***</strong><br>${{fact.claimant_submission}}`;
                            bodyEl.appendChild(claimantTextEl);
                        }}
                        
                        // Add respondent submission
                        if (fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded') {{
                            const respondentTextEl = document.createElement('div');
                            respondentTextEl.className = 'timeline-source-text';
                            respondentTextEl.style.cssText = 'font-style: italic; color: #e53e3e; margin-top: 8px; padding: 12px; background-color: rgba(229, 62, 62, 0.05); border-left: 4px solid #e53e3e; font-size: 13px; border-radius: 0 6px 6px 0;';
                            respondentTextEl.innerHTML = `<strong>*** RESPONDENT SUBMISSION ***</strong><br>${{fact.respondent_submission}}`;
                            bodyEl.appendChild(respondentTextEl);
                        }}
                        
                        contentEl.appendChild(bodyEl);
                        
                        // Add footer if there are exhibits - show expandable content
                        const evidenceContent = getEvidenceContent(fact);
                        if (evidenceContent !== 'None') {{
                            const footerEl = document.createElement('div');
                            footerEl.className = 'timeline-footer';
                            footerEl.style.cssText = 'padding: 12px 16px; background-color: #f8fafc; border-top: 1px solid #e2e8f0; display: block;';
                            
                            footerEl.innerHTML = `
                                <div style="font-weight: 600; color: #4a5568; font-size: 12px; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em;">Evidence (${{evidenceContent.length}} items)</div>
                                ${{evidenceContent.map((evidence, evidenceIndex) => `
                                    <div style="margin-bottom: 6px; border: 1px solid #e2e8f0; border-radius: 6px; overflow: hidden;">
                                        <div onclick="toggleEvidence('${{evidence.id}}', 'timeline-${{evidenceIndex}}')" 
                                             style="padding: 8px 12px; background-color: rgba(221, 107, 32, 0.05); cursor: pointer; display: flex; align-items: center; justify-content: space-between; transition: background-color 0.2s;"
                                             onmouseover="this.style.backgroundColor='rgba(221, 107, 32, 0.1)'" 
                                             onmouseout="this.style.backgroundColor='rgba(221, 107, 32, 0.05)'">
                                            <div>
                                                <span style="font-weight: 600; color: #dd6b20; font-size: 13px;">${{evidence.id}}</span>
                                                <span style="margin-left: 8px; color: #4a5568; font-size: 13px;">${{evidence.title}}</span>
                                            </div>
                                            <span id="evidence-icon-${{evidence.id}}-timeline-${{evidenceIndex}}" 
                                                  style="width: 18px; height: 18px; background-color: #dd6b20; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold;">+</span>
                                        </div>
                                        <div id="evidence-content-${{evidence.id}}-timeline-${{evidenceIndex}}" 
                                             style="display: none; padding: 12px; background-color: white; border-top: 1px solid #e2e8f0;">
                                            <div style="font-weight: 600; color: #dd6b20; font-size: 13px; margin-bottom: 6px;">${{evidence.title}}</div>
                                            <div style="font-size: 12px; color: #666; line-height: 1.4;">${{evidence.summary}}</div>
                                        </div>
                                    </div>
                                `).join('')}}
                            `;
                            
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
                
                // Render document sets view with improved evidence formatting
                function renderDocumentSets(tabType = 'all') {{
                    const container = document.getElementById('document-sets-container');
                    container.innerHTML = '';
                    
                    // Filter facts based on tab type and standardize
                    let filteredFacts = factsData.map(standardizeFactData);
                    if (tabType === 'disputed') {{
                        filteredFacts = filteredFacts.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = filteredFacts.filter(fact => !fact.isDisputed);
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
                                            (fact.parties_involved && fact.parties_involved.includes('Appellant') && doc.party === 'Appellant') ||
                                            (fact.parties_involved && fact.parties_involved.includes('Respondent') && doc.party === 'Respondent')) {{
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
                    
                    // Create document sets UI with card-style display instead of table
                    Object.values(docsWithFacts).forEach(docWithFacts => {{
                        const docset = docWithFacts.docset;
                        const facts = docWithFacts.facts;
                        
                        // Create document set container
                        const docsetEl = document.createElement('div');
                        docsetEl.className = 'docset-container';
                        
                        // Create folder header
                        const headerHtml = `
                            <div class="docset-header" onclick="toggleDocSet('${{docset.id}}')">
                                <svg id="chevron-${{docset.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
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
                            // Create card-style display for facts in this category
                            contentHtml += '<div style="padding: 16px;">';
                            
                            facts.forEach((fact, factIndex) => {{
                                const evidenceContent = getEvidenceContent(fact);
                                let evidenceHtml = 'None';
                                
                                if (evidenceContent !== 'None') {{
                                    evidenceHtml = evidenceContent.map((evidence, evidenceIndex) => `
                                        <div style="margin-bottom: 6px;">
                                            <span onclick="toggleEvidence('${{evidence.id}}', 'docset-${{docset.id}}-${{factIndex}}-${{evidenceIndex}}')" 
                                                  style="display: inline-flex; align-items: center; padding: 4px 8px; background-color: rgba(221, 107, 32, 0.1); color: #dd6b20; border-radius: 12px; cursor: pointer; font-size: 12px; font-weight: 600; margin: 2px 0;"
                                                  onmouseover="this.style.backgroundColor='rgba(221, 107, 32, 0.2)'" 
                                                  onmouseout="this.style.backgroundColor='rgba(221, 107, 32, 0.1)'">
                                                📁 ${{evidence.id}}: ${{evidence.title.length > 25 ? evidence.title.substring(0, 25) + '...' : evidence.title}}
                                                <span id="evidence-icon-${{evidence.id}}-docset-${{docset.id}}-${{factIndex}}-${{evidenceIndex}}" style="margin-left: 6px; font-size: 10px;">+</span>
                                            </span>
                                            <div id="evidence-content-${{evidence.id}}-docset-${{docset.id}}-${{factIndex}}-${{evidenceIndex}}" 
                                                 style="display: none; margin-top: 6px; padding: 8px; background-color: rgba(221, 107, 32, 0.05); border-left: 3px solid #dd6b20; border-radius: 0 4px 4px 0; font-size: 12px; color: #666; line-height: 1.4;">
                                                <div style="font-weight: 600; color: #dd6b20; font-size: 13px; margin-bottom: 4px;">${{evidence.title}}</div>
                                                <div>${{evidence.summary}}</div>
                                            </div>
                                        </div>
                                    `).join('');
                                }}
                                
                                contentHtml += `
                                    <div style="margin-bottom: 16px; border: 1px solid #e2e8f0; border-radius: 8px; background-color: white; box-shadow: 0 1px 3px rgba(0,0,0,0.1); overflow: hidden; ${{fact.isDisputed ? 'border-left: 4px solid #e53e3e; background-color: rgba(229, 62, 62, 0.02);' : ''}}">
                                        <div style="padding: 16px; background-color: #f8fafc; border-bottom: 1px solid #e2e8f0; ${{fact.isDisputed ? 'background-color: rgba(229, 62, 62, 0.05);' : ''}}">
                                            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                                                <div style="font-weight: 600; color: #2d3748;">${{fact.date}}</div>
                                                <div style="display: flex; gap: 6px;">
                                                    ${{fact.parties_involved && fact.parties_involved.length > 0 ? fact.parties_involved.map(party => `
                                                        <span class="badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">${{party}}</span>
                                                    `).join('') : ''}}
                                                    ${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : ''}}
                                                </div>
                                            </div>
                                            <div style="font-weight: 500; color: #1a202c; font-size: 15px;">${{fact.event}}</div>
                                        </div>
                                        <div style="padding: 16px;">
                                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                                                <div>
                                                    <div style="font-weight: 600; color: #4a5568; font-size: 12px; text-transform: uppercase; margin-bottom: 4px;">Document</div>
                                                    <div><strong>${{fact.doc_name || 'N/A'}}</strong> ${{fact.page ? '(Page ' + fact.page + ')' : ''}}</div>
                                                </div>
                                                <div>
                                                    <div style="font-weight: 600; color: #4a5568; font-size: 12px; text-transform: uppercase; margin-bottom: 4px;">Argument</div>
                                                    <div><strong>${{fact.argId}}. ${{fact.argTitle}}</strong></div>
                                                </div>
                                            </div>
                                            ${{fact.source_text && fact.source_text !== 'No specific submission recorded' ? `
                                                <div style="background-color: #f7fafc; padding: 12px; border-radius: 6px; border-left: 4px solid #4299e1; margin-bottom: 12px;">
                                                    <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #4299e1; margin-bottom: 6px;">Source Text</div>
                                                    <div style="font-style: italic; color: #4a5568; font-size: 13px;">${{fact.source_text}}</div>
                                                </div>
                                            ` : ''}}
                                            ${{evidenceHtml !== 'None' ? `
                                                <div style="background-color: #f7fafc; padding: 12px; border-radius: 6px; border-left: 4px solid #dd6b20; margin-bottom: 12px;">
                                                    <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #dd6b20; margin-bottom: 6px;">Evidence (${{evidenceContent.length}} items)</div>
                                                    <div>${{evidenceHtml}}</div>
                                                </div>
                                            ` : ''}}
                                            ${{fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' ? `
                                                <div style="background-color: rgba(49, 130, 206, 0.03); padding: 12px; border-radius: 6px; border-left: 4px solid #3182ce; margin-bottom: 12px;">
                                                    <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #3182ce; margin-bottom: 6px;">*** CLAIMANT SUBMISSION ***</div>
                                                    <div style="font-style: italic; color: #4a5568; font-size: 13px;">${{fact.claimant_submission}}</div>
                                                </div>
                                            ` : ''}}
                                            ${{fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' ? `
                                                <div style="background-color: rgba(229, 62, 62, 0.03); padding: 12px; border-radius: 6px; border-left: 4px solid #e53e3e; margin-bottom: 12px;">
                                                    <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #e53e3e; margin-bottom: 6px;">*** RESPONDENT SUBMISSION ***</div>
                                                    <div style="font-style: italic; color: #4a5568; font-size: 13px;">${{fact.respondent_submission}}</div>
                                                </div>
                                            ` : ''}}
                                            <div style="display: grid; grid-template-columns: 1fr; gap: 16px;">
                                                <div>
                                                    <div style="font-weight: 600; color: #4a5568; font-size: 12px; text-transform: uppercase; margin-bottom: 4px;">Status</div>
                                                    <div>${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                `;
                            }});
                            
                            contentHtml += '</div>';
                        }} else {{
                            contentHtml += '<p style="padding: 12px;">No facts found</p>';
                        }}
                        
                        contentHtml += '</div>';
                        docsetEl.innerHTML = headerHtml + contentHtml;
                        
                        container.appendChild(docsetEl);
                    }});
                }}
                
                // Initialize facts on page load
                document.addEventListener('DOMContentLoaded', function() {{
                    renderCardView('all');
                }});
                
                // Initialize card view immediately
                renderCardView('all');
            </script>
        </body>
        </html>
        """
        
        # Render the HTML component
        st.title("Case Facts")
        components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
