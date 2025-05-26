import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

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

# Streamlit Native Card View Implementation
def render_streamlit_card_view(filtered_facts=None):
    # Get facts data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    # Sort by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    # Add custom CSS for better card styling
    st.markdown("""
    <style>
    .fact-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .fact-card:hover {
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    .dispute-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        margin-left: 10px;
    }
    .disputed {
        background-color: #ffebee;
        color: #c62828;
        border: 1px solid #ffcdd2;
    }
    .undisputed {
        background-color: #e8f5e8;
        color: #2e7d32;
        border: 1px solid #a5d6a7;
    }
    .evidence-tag {
        display: inline-block;
        background-color: #f5f5f5;
        padding: 4px 8px;
        margin: 2px;
        border-radius: 8px;
        font-size: 11px;
        color: #666;
        border: 1px solid #ddd;
    }
    .submission-box {
        border-left: 4px solid;
        padding: 15px;
        margin: 10px 0;
        border-radius: 0 8px 8px 0;
        background-color: #fafafa;
    }
    .claimant-submission {
        border-left-color: #2196f3;
        background-color: #f3f9ff;
    }
    .respondent-submission {
        border-left-color: #f44336;
        background-color: #fff3f3;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display summary stats
    total_facts = len(facts_data)
    disputed_facts = len([f for f in facts_data if f['isDisputed']])
    undisputed_facts = total_facts - disputed_facts
    
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    with stats_col1:
        st.metric("Total Facts", total_facts)
    with stats_col2:
        st.metric("Disputed", disputed_facts, delta=None)
    with stats_col3:
        st.metric("Undisputed", undisputed_facts, delta=None)
    
    st.divider()
    
    # Display each fact as an enhanced card
    for i, fact in enumerate(facts_data):
        # Create enhanced card with custom styling
        dispute_status = "disputed" if fact['isDisputed'] else "undisputed"
        dispute_text = "Disputed" if fact['isDisputed'] else "Undisputed"
        dispute_icon = "🔴" if fact['isDisputed'] else "🟢"
        
        # Card header with date, title, and status
        st.markdown(f"""
        <div class="fact-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 15px;">
                <div>
                    <h3 style="margin: 0; color: #333;">📅 {fact['date']}</h3>
                    <h4 style="margin: 5px 0; color: #666;">{fact['event']}</h4>
                </div>
                <span class="dispute-badge {dispute_status}">{dispute_icon} {dispute_text}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Use expander for detailed content
        with st.expander("🔍 View Details", expanded=False):
            # Evidence & Source References section with improved styling
            st.markdown("### 📁 Evidence & Source References")
            evidence_content = get_evidence_content(fact)
            
            if evidence_content:
                # Display evidence tags
                evidence_tags = " ".join([f'<span class="evidence-tag">{ev["id"]}</span>' for ev in evidence_content])
                st.markdown(f"**Evidence:** {evidence_tags}", unsafe_allow_html=True)
                
                # Tabbed evidence details
                if len(evidence_content) > 1:
                    evidence_tabs = st.tabs([f"📄 {ev['id']}" for ev in evidence_content])
                    for idx, (tab, evidence) in enumerate(zip(evidence_tabs, evidence_content)):
                        with tab:
                            st.markdown(f"**{evidence['title']}**")
                            st.markdown(evidence['summary'])
                            
                            if fact.get('doc_summary'):
                                st.info(f"📋 **Document Summary:** {fact['doc_summary']}")
                            
                            # Reference info in columns
                            ref_col1, ref_col2 = st.columns([3, 1])
                            with ref_col1:
                                ref_items = []
                                if fact.get('page'):
                                    ref_items.append(f"Page {fact['page']}")
                                if fact.get('paragraphs'):
                                    ref_items.append(f"¶ {fact['paragraphs']}")
                                if ref_items:
                                    st.markdown(f"📍 **Reference:** {' | '.join(ref_items)}")
                            
                            with ref_col2:
                                if st.button(f"📋 Copy", key=f"copy_{evidence['id']}_{i}_{idx}"):
                                    st.success("Copied!")
                else:
                    evidence = evidence_content[0]
                    st.markdown(f"**{evidence['title']}**")
                    st.markdown(evidence['summary'])
                    
                    if fact.get('doc_summary'):
                        st.info(f"📋 **Document Summary:** {fact['doc_summary']}")
                    
                    ref_col1, ref_col2 = st.columns([3, 1])
                    with ref_col1:
                        ref_items = []
                        if fact.get('page'):
                            ref_items.append(f"Page {fact['page']}")
                        if fact.get('paragraphs'):
                            ref_items.append(f"¶ {fact['paragraphs']}")
                        if ref_items:
                            st.markdown(f"📍 **Reference:** {' | '.join(ref_items)}")
                    
                    with ref_col2:
                        if st.button(f"📋 Copy", key=f"copy_{evidence['id']}_{i}"):
                            st.success("Copied!")
            else:
                st.markdown("*No evidence references available*")
            
            st.divider()
            
            # Enhanced Party Submissions section
            st.markdown("### ⚖️ Party Submissions")
            
            # Side-by-side submissions
            sub_col1, sub_col2 = st.columns(2)
            
            with sub_col1:
                st.markdown("#### 🔵 Claimant Position")
                claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                if claimant_text == 'No specific submission recorded':
                    st.markdown('<div class="submission-box claimant-submission"><em>No submission provided</em></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="submission-box claimant-submission">{claimant_text}</div>', unsafe_allow_html=True)
            
            with sub_col2:
                st.markdown("#### 🔴 Respondent Position")
                respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                if respondent_text == 'No specific submission recorded':
                    st.markdown('<div class="submission-box respondent-submission"><em>No submission provided</em></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="submission-box respondent-submission">{respondent_text}</div>', unsafe_allow_html=True)
            
            # Additional metadata
            if fact.get('parties_involved'):
                st.markdown(f"**👥 Parties Involved:** {', '.join(fact['parties_involved'])}")
            
            if fact.get('argTitle'):
                st.markdown(f"**🏷️ Argument Category:** {fact['argTitle']}")
        
        # Add spacing between cards
        st.markdown("<br>", unsafe_allow_html=True)

# Streamlit Native Timeline View Implementation
def render_streamlit_timeline_view(filtered_facts=None):
    # Get facts data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    # Sort by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No timeline events found matching the selected criteria.")
        return
    
    # Add custom CSS for timeline styling
    st.markdown("""
    <style>
    .timeline-container {
        position: relative;
        padding-left: 30px;
    }
    .timeline-line {
        position: absolute;
        left: 15px;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(to bottom, #2196f3, #f44336);
        border-radius: 2px;
    }
    .timeline-event {
        position: relative;
        margin-bottom: 30px;
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #2196f3;
        margin-left: 20px;
    }
    .timeline-event.disputed {
        border-left-color: #f44336;
    }
    .timeline-dot {
        position: absolute;
        left: -35px;
        top: 20px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: white;
        border: 3px solid #2196f3;
        z-index: 1;
    }
    .timeline-dot.disputed {
        border-color: #f44336;
    }
    .year-marker {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 25px;
        border-radius: 25px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        margin: 30px 0 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .event-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 15px;
    }
    .event-date {
        background: #f8f9fa;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 12px;
        color: #666;
        border: 1px solid #e9ecef;
    }
    .event-title {
        font-size: 16px;
        font-weight: 600;
        color: #333;
        flex: 1;
        margin-right: 15px;
        line-height: 1.4;
    }
    .status-badge {
        padding: 4px 10px;
        border-radius: 15px;
        font-size: 11px;
        font-weight: bold;
        white-space: nowrap;
    }
    .status-disputed {
        background: #ffebee;
        color: #c62828;
        border: 1px solid #ffcdd2;
    }
    .status-undisputed {
        background: #e8f5e8;
        color: #2e7d32;
        border: 1px solid #a5d6a7;
    }
    .timeline-content {
        margin-top: 15px;
    }
    .party-positions {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 15px;
    }
    .position-card {
        padding: 12px;
        border-radius: 8px;
        border-left: 3px solid;
        font-size: 14px;
        line-height: 1.5;
    }
    .claimant-position {
        background: #f3f9ff;
        border-left-color: #2196f3;
    }
    .respondent-position {
        background: #fff3f3;
        border-left-color: #f44336;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Timeline summary
    total_events = len(facts_data)
    disputed_events = len([f for f in facts_data if f['isDisputed']])
    date_range = f"{facts_data[0]['date'].split('-')[0]} - {facts_data[-1]['date'].split('-')[0]}"
    
    summary_col1, summary_col2, summary_col3 = st.columns(3)
    with summary_col1:
        st.metric("📅 Timeline Events", total_events)
    with summary_col2:
        st.metric("⚡ Disputed Events", disputed_events)
    with summary_col3:
        st.metric("📊 Date Range", date_range)
    
    st.divider()
    
    # Group by year for year markers
    events_by_year = {}
    for fact in facts_data:
        year = fact['date'].split('-')[0] if '-' in fact['date'] else fact['date'][:4]
        if year not in events_by_year:
            events_by_year[year] = []
        events_by_year[year].append(fact)
    
    # Display timeline with enhanced styling
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    
    for year_idx, (year, events) in enumerate(events_by_year.items()):
        # Year marker with gradient
        st.markdown(f'<div class="year-marker">📅 {year}</div>', unsafe_allow_html=True)
        
        for event_idx, fact in enumerate(events):
            dispute_class = "disputed" if fact['isDisputed'] else ""
            status_class = "status-disputed" if fact['isDisputed'] else "status-undisputed"
            status_text = "🔴 Disputed" if fact['isDisputed'] else "🟢 Undisputed"
            
            # Timeline event with custom styling
            st.markdown(f"""
            <div class="timeline-event {dispute_class}">
                <div class="timeline-dot {dispute_class}"></div>
                <div class="event-header">
                    <div class="event-title">{fact['event']}</div>
                    <div>
                        <div class="event-date">{fact['date']}</div>
                        <div class="status-badge {status_class}" style="margin-top: 5px;">{status_text}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Event details in expander
            with st.expander("🔍 Event Details", expanded=False):
                # Evidence section
                st.markdown("#### 📁 Evidence & Documentation")
                evidence_content = get_evidence_content(fact)
                
                if evidence_content:
                    evidence_cols = st.columns(min(len(evidence_content), 3))
                    for idx, evidence in enumerate(evidence_content):
                        with evidence_cols[idx % 3]:
                            st.markdown(f"**📄 {evidence['id']}**")
                            st.caption(evidence['title'])
                            with st.expander("View Summary"):
                                st.write(evidence['summary'])
                else:
                    st.info("No evidence references available")
                
                st.divider()
                
                # Party positions in grid layout
                st.markdown("#### ⚖️ Party Positions")
                
                claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                
                # Use custom HTML for better positioning
                positions_html = f"""
                <div class="party-positions">
                    <div class="position-card claimant-position">
                        <strong>🔵 Claimant Position:</strong><br>
                        <em>{'No submission provided' if claimant_text == 'No specific submission recorded' else claimant_text}</em>
                    </div>
                    <div class="position-card respondent-position">
                        <strong>🔴 Respondent Position:</strong><br>
                        <em>{'No submission provided' if respondent_text == 'No specific submission recorded' else respondent_text}</em>
                    </div>
                </div>
                """
                st.markdown(positions_html, unsafe_allow_html=True)
                
                # Additional metadata
                if fact.get('doc_name') or fact.get('page'):
                    st.markdown("#### 📋 Source Information")
                    source_col1, source_col2 = st.columns(2)
                    with source_col1:
                        if fact.get('doc_name'):
                            st.markdown(f"**Document:** {fact['doc_name']}")
                        if fact.get('argTitle'):
                            st.markdown(f"**Category:** {fact['argTitle']}")
                    with source_col2:
                        if fact.get('page'):
                            st.markdown(f"**Page:** {fact['page']}")
                        if fact.get('paragraphs'):
                            st.markdown(f"**Paragraphs:** {fact['paragraphs']}")
            
            # Add spacing between events
            st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Streamlit Native Document Categories View Implementation  
def render_streamlit_docset_view(filtered_facts=None):
    # Get facts and document sets data
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
        
    document_sets = get_document_sets()
    
    # Sort facts by date
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    # Add custom CSS for document categories styling
    st.markdown("""
    <style>
    .docset-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 12px 12px 0 0;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0;
    }
    .docset-container {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        margin: 20px 0;
        overflow: hidden;
        box-shadow: 0 3px 12px rgba(0,0,0,0.1);
    }
    .docset-content {
        padding: 20px;
        background: #fafafa;
    }
    .fact-item {
        background: white;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .fact-item:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .fact-item.disputed {
        border-left-color: #f44336;
    }
    .fact-item.undisputed {
        border-left-color: #4caf50;
    }
    .fact-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .party-indicator {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 10px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .party-appellant {
        background: #e3f2fd;
        color: #1976d2;
        border: 1px solid #bbdefb;
    }
    .party-respondent {
        background: #ffebee;
        color: #d32f2f;
        border: 1px solid #ffcdd2;
    }
    .party-mixed {
        background: #f3e5f5;
        color: #7b1fa2;
        border: 1px solid #e1bee7;
    }
    .document-stats {
        background: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #e0e0e0;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
        margin-bottom: 20px;
    }
    .stat-card {
        background: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .expandable-content {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.3s ease;
    }
    .expandable-content.expanded {
        max-height: 1000px;
    }
    </style>
    """, unsafe_allow_html=True)
    
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
    
    # Calculate summary statistics
    total_facts = sum(len(doc_facts['facts']) for doc_facts in docs_with_facts.values())
    total_disputed = sum(len([f for f in doc_facts['facts'] if f['isDisputed']]) for doc_facts in docs_with_facts.values())
    categories_with_facts = len([d for d in docs_with_facts.values() if len(d['facts']) > 0])
    
    # Display summary statistics
    st.markdown("### 📊 Document Categories Overview")
    
    stats_html = f"""
    <div class="stats-grid">
        <div class="stat-card">
            <h3 style="margin: 0; color: #2196f3;">{total_facts}</h3>
            <p style="margin: 5px 0 0 0; color: #666;">Total Facts</p>
        </div>
        <div class="stat-card">
            <h3 style="margin: 0; color: #f44336;">{total_disputed}</h3>
            <p style="margin: 5px 0 0 0; color: #666;">Disputed Facts</p>
        </div>
        <div class="stat-card">
            <h3 style="margin: 0; color: #4caf50;">{total_facts - total_disputed}</h3>
            <p style="margin: 5px 0 0 0; color: #666;">Undisputed Facts</p>
        </div>
        <div class="stat-card">
            <h3 style="margin: 0; color: #ff9800;">{categories_with_facts}</h3>
            <p style="margin: 5px 0 0 0; color: #666;">Active Categories</p>
        </div>
    </div>
    """
    st.markdown(stats_html, unsafe_allow_html=True)
    
    st.divider()
    
    # Display document categories with enhanced styling
    for docset_id, doc_with_facts in docs_with_facts.items():
        docset = doc_with_facts['docset']
        facts = doc_with_facts['facts']
        
        # Document set header with party indicators
        party_colors = {
            'Appellant': 'party-appellant',
            'Respondent': 'party-respondent', 
            'Mixed': 'party-mixed'
        }
        party_class = party_colors.get(docset['party'], 'party-mixed')
        party_icon = "🔵" if docset['party'] == 'Appellant' else "🔴" if docset['party'] == 'Respondent' else "⚪"
        
        # Enhanced document category container
        st.markdown(f"""
        <div class="docset-container">
            <div class="docset-header">
                <div>
                    <span style="font-size: 18px;">📁 {docset['name'].title()}</span>
                    <span class="party-indicator {party_class}" style="margin-left: 15px;">{party_icon} {docset['party']}</span>
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 5px 12px; border-radius: 15px;">
                    {len(facts)} Facts
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Use expander for document category content
        with st.expander(f"📄 View {docset['name'].title()} Facts", expanded=False):
            if facts:
                # Show document list within category
                st.markdown("#### 📚 Documents in this category:")
                doc_cols = st.columns(min(len(docset.get('documents', [])), 4))
                for idx, doc in enumerate(docset.get('documents', [])):
                    with doc_cols[idx % 4]:
                        doc_party_class = party_colors.get(doc['party'], 'party-mixed')
                        st.markdown(f"""
                        <div style="padding: 8px; border-radius: 6px; background: #f8f9fa; margin: 5px 0; border-left: 3px solid #ddd;">
                            <div style="font-size: 12px; font-weight: bold;">{doc['name']}</div>
                            <span class="party-indicator {doc_party_class}" style="font-size: 9px;">{doc['party']}</span>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.divider()
                
                # Display facts in this category
                st.markdown("#### 📋 Facts from these documents:")
                
                for i, fact in enumerate(facts):
                    dispute_class = "disputed" if fact['isDisputed'] else "undisputed"
                    dispute_icon = "🔴" if fact['isDisputed'] else "🟢"
                    
                    # Enhanced fact item
                    st.markdown(f"""
                    <div class="fact-item {dispute_class}">
                        <div class="fact-header">
                            <div>
                                <strong style="color: #333;">{fact['date']} - {fact['event']}</strong>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px;">
                                <span style="font-size: 12px; color: #666;">
                                    {dispute_icon} {'Disputed' if fact['isDisputed'] else 'Undisputed'}
                                </span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Fact details in nested expander
                    with st.expander(f"🔍 View Fact Details", key=f"fact_{docset_id}_{i}"):
                        # Evidence section with tabs
                        evidence_content = get_evidence_content(fact)
                        
                        if evidence_content:
                            st.markdown("**📁 Evidence & Documentation**")
                            
                            if len(evidence_content) > 1:
                                evidence_tabs = st.tabs([f"📄 {ev['id']}" for ev in evidence_content])  
                                for tab, evidence in zip(evidence_tabs, evidence_content):
                                    with tab:
                                        st.markdown(f"**{evidence['title']}**")
                                        st.write(evidence['summary'])
                                        
                                        if fact.get('doc_summary'):
                                            st.info(f"📋 {fact['doc_summary']}")
                            else:
                                evidence = evidence_content[0]
                                st.markdown(f"**📄 {evidence['id']} - {evidence['title']}**")
                                st.write(evidence['summary'])
                                
                                if fact.get('doc_summary'):
                                    st.info(f"📋 {fact['doc_summary']}")
                        
                        st.divider()
                        
                        # Party submissions in columns
                        st.markdown("**⚖️ Party Positions**")
                        pos_col1, pos_col2 = st.columns(2)
                        
                        with pos_col1:
                            st.markdown("**🔵 Claimant**")
                            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                            if claimant_text == 'No specific submission recorded':
                                st.markdown("*No submission provided*")
                            else:
                                st.info(claimant_text)
                        
                        with pos_col2:
                            st.markdown("**🔴 Respondent**")
                            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                            if respondent_text == 'No specific submission recorded':
                                st.markdown("*No submission provided*")
                            else:
                                st.warning(respondent_text)
                        
                        # Reference information
                        if fact.get('page') or fact.get('paragraphs') or fact.get('documentName'):
                            st.markdown("**📍 Reference Information**")
                            ref_col1, ref_col2 = st.columns(2)
                            with ref_col1:
                                if fact.get('documentName'):
                                    st.markdown(f"**Document:** {fact['documentName']}")
                                if fact.get('page'):
                                    st.markdown(f"**Page:** {fact['page']}")
                            with ref_col2:
                                if fact.get('paragraphs'):
                                    st.markdown(f"**Paragraphs:** {fact['paragraphs']}")
                                if fact.get('argTitle'):
                                    st.markdown(f"**Category:** {fact['argTitle']}")
                    
                    # Add spacing between fact items
                    if i < len(facts) - 1:
                        st.markdown("<br>", unsafe_allow_html=True)
                        
            else:
                st.info("📭 No facts found in this document category.")
        
        # Add spacing between document categories
        st.markdown("<br>", unsafe_allow_html=True)

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
    
    # Create the facts view with native components
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # Create a simple header with view toggle using Streamlit components
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
        
        # Facts filter using selectbox instead of tabs to avoid nesting issues
        filter_option = st.selectbox(
            "Filter Facts:",
            ["All Facts", "Disputed Facts", "Undisputed Facts"],
            index=0
        )
        
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
        
        st.divider()
        
        # Render the appropriate native view based on current view type
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
