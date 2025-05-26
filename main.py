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

if 'facts_tab' not in st.session_state:
    st.session_state.facts_tab = "all"

if 'facts_view' not in st.session_state:
    st.session_state.facts_view = "card"

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

# Function to get evidence content
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

# Function to render party badge
def render_party_badge(party):
    if party == "Appellant":
        return f'<span style="background-color: rgba(49, 130, 206, 0.1); color: #3182ce; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">{party}</span>'
    elif party == "Respondent":
        return f'<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">{party}</span>'
    else:
        return f'<span style="background-color: rgba(128, 128, 128, 0.1); color: #666; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">{party}</span>'

# Function to render disputed badge
def render_disputed_badge():
    return '<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">Disputed</span>'

# Function to render evidence badge
def render_evidence_badge(evidence_item):
    return f'<span style="background-color: rgba(221, 107, 32, 0.1); color: #dd6b20; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">📁 {evidence_item["id"]}</span>'

# Native Streamlit Facts Card View
def render_native_facts_cards(facts_data, tab_type="all"):
    # Filter facts based on tab type
    filtered_facts = facts_data.copy()
    if tab_type == 'disputed':
        filtered_facts = [fact for fact in filtered_facts if fact['isDisputed']]
    elif tab_type == 'undisputed':
        filtered_facts = [fact for fact in filtered_facts if not fact['isDisputed']]
    
    # Sort by date
    filtered_facts.sort(key=lambda x: x['date'])
    
    if len(filtered_facts) == 0:
        st.info("No facts found matching the selected criteria.")
        return
    
    # Render each fact as a native Streamlit card
    for i, fact in enumerate(filtered_facts):
        # Create container with border styling for disputed facts
        if fact['isDisputed']:
            container_style = """
            <div style="border-left: 4px solid #e53e3e; background-color: rgba(229, 62, 62, 0.02); margin-bottom: 16px; border-radius: 8px;">
            """
        else:
            container_style = """
            <div style="border: 1px solid #e2e8f0; margin-bottom: 16px; border-radius: 8px; background-color: white;">
            """
        
        st.markdown(container_style, unsafe_allow_html=True)
        
        # Create expander with custom header
        header_badges = ""
        if fact.get('parties_involved'):
            for party in fact['parties_involved']:
                header_badges += " " + render_party_badge(party)
        
        if fact['isDisputed']:
            header_badges += " " + render_disputed_badge()
        
        expander_label = f"**{fact['date']}** - {fact['event']}"
        
        with st.expander(expander_label, expanded=False):
            # Display badges
            if header_badges:
                st.markdown(header_badges, unsafe_allow_html=True)
            
            # Create two columns for document info and argument info
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📄 Document Information**")
                st.markdown(f"**Document:** {fact.get('doc_name', 'N/A')}")
                if fact.get('page'):
                    st.markdown(f"**Page:** {fact['page']}")
                
            with col2:
                st.markdown("**⚖️ Argument Information**")
                st.markdown(f"**Argument:** {fact.get('argId', '')}. {fact.get('argTitle', '')}")
                if fact.get('paragraphs'):
                    st.markdown(f"**Paragraphs:** {fact['paragraphs']}")
            
            # Source Text
            if fact.get('source_text') and fact['source_text'] != 'No specific submission recorded':
                st.markdown("**📋 Source Text**")
                st.info(fact['source_text'])
            
            # Claimant Submission
            if fact.get('claimant_submission') and fact['claimant_submission'] != 'No specific submission recorded':
                st.markdown("**👤 Claimant Submission**")
                st.markdown(f'<div style="background-color: rgba(49, 130, 206, 0.03); border-left: 4px solid #3182ce; padding: 12px; font-style: italic; border-radius: 0 6px 6px 0;">{fact["claimant_submission"]}</div>', unsafe_allow_html=True)
            
            # Respondent Submission
            if fact.get('respondent_submission') and fact['respondent_submission'] != 'No specific submission recorded':
                st.markdown("**🏛️ Respondent Submission**")
                st.markdown(f'<div style="background-color: rgba(229, 62, 62, 0.03); border-left: 4px solid #e53e3e; padding: 12px; font-style: italic; border-radius: 0 6px 6px 0;">{fact["respondent_submission"]}</div>', unsafe_allow_html=True)
            
            # Document Summary
            if fact.get('doc_summary'):
                st.markdown("**📝 Document Summary**")
                st.markdown(f"_{fact['doc_summary']}_")
            
            # Status and Evidence
            col3, col4 = st.columns(2)
            
            with col3:
                st.markdown("**🔍 Status**")
                if fact['isDisputed']:
                    st.markdown(render_disputed_badge(), unsafe_allow_html=True)
                else:
                    st.markdown("Undisputed")
            
            with col4:
                st.markdown("**📁 Evidence**")
                evidence_content = get_evidence_content(fact)
                
                if evidence_content:
                    for evidence in evidence_content:
                        with st.expander(f"📁 {evidence['id']}: {evidence['title']}", expanded=False):
                            st.markdown(evidence['summary'])
                else:
                    st.markdown("None")
        
        st.markdown("</div>", unsafe_allow_html=True)

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
        
        # Create buttons with names
        if st.button("📑 Arguments", key="args_button", use_container_width=True):
            st.session_state.view = "Arguments"
            st.rerun()
            
        if st.button("📊 Facts", key="facts_button", use_container_width=True):
            st.session_state.view = "Facts"
            st.rerun()
            
        if st.button("📁 Exhibits", key="exhibits_button", use_container_width=True):
            st.session_state.view = "Exhibits"
            st.rerun()
    
    # Create the facts view with native Streamlit cards
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # Action buttons row
        col_actions1, col_actions2, col_actions3 = st.columns([1, 1, 4])
        
        with col_actions1:
            if st.button("📋 Copy", help="Copy facts to clipboard"):
                st.info("Copy functionality would be implemented here")
        
        with col_actions2:
            if st.button("📥 Export", help="Export facts"):
                st.info("Export functionality would be implemented here")
        
        # View toggle buttons
        st.markdown("### View Options")
        view_cols = st.columns(4)
        
        with view_cols[0]:
            if st.button("Card View", key="card_view", use_container_width=True, 
                        type="primary" if st.session_state.facts_view == "card" else "secondary"):
                st.session_state.facts_view = "card"
                st.rerun()
        
        with view_cols[1]:
            if st.button("Table View", key="table_view", use_container_width=True,
                        type="primary" if st.session_state.facts_view == "table" else "secondary"):
                st.session_state.facts_view = "table"
                st.rerun()
        
        with view_cols[2]:
            if st.button("Document Categories", key="docset_view", use_container_width=True,
                        type="primary" if st.session_state.facts_view == "docset" else "secondary"):
                st.session_state.facts_view = "docset"
                st.rerun()
        
        with view_cols[3]:
            if st.button("Timeline View", key="timeline_view", use_container_width=True,
                        type="primary" if st.session_state.facts_view == "timeline" else "secondary"):
                st.session_state.facts_view = "timeline"
                st.rerun()
        
        # Facts filter tabs
        st.markdown("### Filter Facts")
        tab_cols = st.columns(3)
        
        with tab_cols[0]:
            if st.button("All Facts", key="all_facts", use_container_width=True,
                        type="primary" if st.session_state.facts_tab == "all" else "secondary"):
                st.session_state.facts_tab = "all"
                st.rerun()
        
        with tab_cols[1]:
            if st.button("Disputed Facts", key="disputed_facts", use_container_width=True,
                        type="primary" if st.session_state.facts_tab == "disputed" else "secondary"):
                st.session_state.facts_tab = "disputed"
                st.rerun()
        
        with tab_cols[2]:
            if st.button("Undisputed Facts", key="undisputed_facts", use_container_width=True,
                        type="primary" if st.session_state.facts_tab == "undisputed" else "secondary"):
                st.session_state.facts_tab = "undisputed"
                st.rerun()
        
        st.markdown("---")
        
        # Render content based on selected view
        if st.session_state.facts_view == "card":
            # Native Streamlit Cards View
            render_native_facts_cards(facts_data, st.session_state.facts_tab)
            
        else:
            # For other views, use the original HTML components
            if st.session_state.facts_view == "table":
                view_type = "table"
            elif st.session_state.facts_view == "docset":
                view_type = "docset"
            elif st.session_state.facts_view == "timeline":
                view_type = "timeline"
            else:
                view_type = "table"
            
            # Create HTML component for other views
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
                        padding: 20px;
                        background-color: #fff;
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
                    
                    /* Table view with horizontal scroll */
                    .table-view-container {{
                        overflow-x: auto;
                        border: 1px solid #dee2e6;
                        border-radius: 8px;
                        margin-top: 20px;
                    }}
                    
                    .table-view {{
                        width: 100%;
                        min-width: 1200px;
                        border-collapse: collapse;
                        font-size: 14px;
                    }}
                    
                    .table-view th {{
                        padding: 12px;
                        text-align: left;
                        background-color: #f8f9fa;
                        border-bottom: 2px solid #dee2e6;
                        position: sticky;
                        top: 0;
                        cursor: pointer;
                        font-size: 13px;
                        white-space: nowrap;
                        z-index: 10;
                    }}
                    
                    .table-view th:hover {{
                        background-color: #e9ecef;
                    }}
                    
                    .table-view td {{
                        padding: 12px;
                        border-bottom: 1px solid #dee2e6;
                        font-size: 13px;
                        vertical-align: top;
                        line-height: 1.4;
                    }}
                    
                    .table-view tr:hover {{
                        background-color: #f8f9fa;
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
                    
                    .docset-content {{
                        display: none;
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
                        transform: rotate(0deg);
                    }}
                    
                    .chevron.expanded {{
                        transform: rotate(90deg);
                    }}
                </style>
            </head>
            <body>
                <div id="content-container"></div>
                
                <script>
                    // Initialize data
                    const factsData = {facts_json};
                    const documentSets = {document_sets_json};
                    const timelineData = {timeline_json};
                    const currentTab = '{st.session_state.facts_tab}';
                    const currentView = '{view_type}';
                    
                    // Filter facts based on current tab
                    function getFilteredFacts() {{
                        let filtered = factsData.slice();
                        if (currentTab === 'disputed') {{
                            filtered = filtered.filter(fact => fact.isDisputed);
                        }} else if (currentTab === 'undisputed') {{
                            filtered = filtered.filter(fact => !fact.isDisputed);
                        }}
                        return filtered;
                    }}
                    
                    // Render based on current view
                    function renderCurrentView() {{
                        const container = document.getElementById('content-container');
                        const filteredFacts = getFilteredFacts();
                        
                        if (currentView === 'table') {{
                            renderTableView(filteredFacts, container);
                        }} else if (currentView === 'timeline') {{
                            renderTimelineView(filteredFacts, container);
                        }} else if (currentView === 'docset') {{
                            renderDocumentSetsView(filteredFacts, container);
                        }}
                    }}
                    
                    // Table view rendering
                    function renderTableView(facts, container) {{
                        let html = `
                            <div class="table-view-container">
                                <table class="table-view">
                                    <thead>
                                        <tr>
                                            <th>Date</th>
                                            <th>Event</th>
                                            <th>Source Text</th>
                                            <th>Page</th>
                                            <th>Document</th>
                                            <th>Doc Summary</th>
                                            <th>Claimant Submission</th>
                                            <th>Respondent Submission</th>
                                            <th>Status</th>
                                            <th>Evidence</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                        `;
                        
                        facts.forEach(fact => {{
                            const claimantSub = fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' 
                                ? fact.claimant_submission : 'No submission';
                            const respondentSub = fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' 
                                ? fact.respondent_submission : 'No submission';
                            
                            html += `
                                <tr ${{fact.isDisputed ? 'class="disputed"' : ''}}>
                                    <td>${{fact.date}}</td>
                                    <td>${{fact.event}}</td>
                                    <td>${{fact.source_text || ''}}</td>
                                    <td>${{fact.page || ''}}</td>
                                    <td>${{fact.doc_name || ''}}</td>
                                    <td>${{fact.doc_summary || ''}}</td>
                                    <td>${{claimantSub}}</td>
                                    <td>${{respondentSub}}</td>
                                    <td>${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : 'Undisputed'}}</td>
                                    <td>${{(fact.exhibits && fact.exhibits.length > 0) ? fact.exhibits.join(', ') : 'None'}}</td>
                                </tr>
                            `;
                        }});
                        
                        html += `
                                    </tbody>
                                </table>
                            </div>
                        `;
                        
                        container.innerHTML = html;
                    }}
                    
                    // Timeline view rendering
                    function renderTimelineView(facts, container) {{
                        let html = `
                            <div class="timeline-container">
                                <div class="timeline-wrapper">
                                    <div class="timeline-line"></div>
                        `;
                        
                        facts.sort((a, b) => new Date(a.date) - new Date(b.date));
                        
                        facts.forEach(fact => {{
                            const formattedDate = new Date(fact.date).toLocaleDateString('en-US', {{
                                year: 'numeric',
                                month: 'short',
                                day: 'numeric'
                            }});
                            
                            html += `
                                <div class="timeline-item">
                                    <div class="timeline-point${{fact.isDisputed ? ' disputed' : ''}}"></div>
                                    <div class="timeline-content">
                                        <div class="timeline-header${{fact.isDisputed ? ' timeline-header-disputed' : ''}}">
                                            <div class="timeline-date">${{formattedDate}}</div>
                                            <div class="timeline-badges">
                                                ${{fact.parties_involved ? fact.parties_involved.map(party => 
                                                    `<span class="badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">${{party}}</span>`
                                                ).join('') : ''}}
                                                ${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : ''}}
                                            </div>
                                        </div>
                                        <div class="timeline-body">
                                            <div class="timeline-fact">${{fact.event}}</div>
                                            ${{fact.source_text ? `<div style="font-style: italic; margin-top: 8px; color: #666;">${{fact.source_text}}</div>` : ''}}
                                            <div class="timeline-meta">
                                                <span><strong>Document:</strong> ${{fact.doc_name || 'N/A'}}</span>
                                                <span><strong>Page:</strong> ${{fact.page || 'N/A'}}</span>
                                            </div>
                                        </div>
                                        ${{fact.exhibits && fact.exhibits.length > 0 ? `
                                            <div class="timeline-footer">
                                                ${{fact.exhibits.map(exhibit => `<span class="badge exhibit-badge">${{exhibit}}</span>`).join('')}}
                                            </div>
                                        ` : ''}}
                                    </div>
                                </div>
                            `;
                        }});
                        
                        html += `
                                </div>
                            </div>
                        `;
                        
                        container.innerHTML = html;
                    }}
                    
                    // Document sets view rendering
                    function renderDocumentSetsView(facts, container) {{
                        let html = '';
                        
                        documentSets.forEach(docset => {{
                            if (docset.isGroup) {{
                                const docsetFacts = facts.filter(fact => 
                                    fact.doc_name && docset.documents.some(doc => 
                                        fact.doc_name.toLowerCase().includes(doc.name.toLowerCase().substring(0, 10))
                                    )
                                );
                                
                                html += `
                                    <div class="docset-container" style="margin-bottom: 20px;">
                                        <div class="docset-header" onclick="toggleDocSet('${{docset.id}}')">
                                            <svg class="chevron" id="chevron-${{docset.id}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <polyline points="9 18 15 12 9 6"></polyline>
                                            </svg>
                                            <svg class="folder-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                                            </svg>
                                            <span><strong>${{docset.name}}</strong></span>
                                            <span style="margin-left: auto;">
                                                <span class="badge">${{docsetFacts.length}} facts</span>
                                            </span>
                                        </div>
                                        <div id="docset-content-${{docset.id}}" class="docset-content">
                                `;
                                
                                if (docsetFacts.length > 0) {{
                                    html += `
                                        <div class="table-view-container">
                                            <table class="table-view">
                                                <thead>
                                                    <tr>
                                                        <th>Date</th>
                                                        <th>Event</th>
                                                        <th>Status</th>
                                                        <th>Evidence</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                    `;
                                    
                                    docsetFacts.forEach(fact => {{
                                        html += `
                                            <tr ${{fact.isDisputed ? 'class="disputed"' : ''}}>
                                                <td>${{fact.date}}</td>
                                                <td>${{fact.event}}</td>
                                                <td>${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : 'Undisputed'}}</td>
                                                <td>${{(fact.exhibits && fact.exhibits.length > 0) ? fact.exhibits.join(', ') : 'None'}}</td>
                                            </tr>
                                        `;
                                    }});
                                    
                                    html += `
                                                </tbody>
                                            </table>
                                        </div>
                                    `;
                                }} else {{
                                    html += '<p style="padding: 12px;">No facts found</p>';
                                }}
                                
                                html += `
                                        </div>
                                    </div>
                                `;
                            }}
                        }});
                        
                        container.innerHTML = html;
                    }}
                    
                    // Toggle document set visibility
                    function toggleDocSet(docsetId) {{
                        const content = document.getElementById(`docset-content-${{docsetId}}`);
                        const chevron = document.getElementById(`chevron-${{docsetId}}`);
                        
                        if (content.style.display === 'none' || content.style.display === '') {{
                            content.style.display = 'block';
                            chevron.style.transform = 'rotate(90deg)';
                        }} else {{
                            content.style.display = 'none';
                            chevron.style.transform = 'rotate(0deg)';
                        }}
                    }}
                    
                    // Initialize
                    document.addEventListener('DOMContentLoaded', function() {{
                        renderCurrentView();
                    }});
                    
                    renderCurrentView();
                </script>
            </body>
            </html>
            """
            
            components.html(html_content, height=800, scrolling=True)
    
    # Other views would go here (Arguments, Exhibits)
    elif st.session_state.view == "Arguments":
        st.title("Arguments")
        st.info("Arguments view would be implemented here")
        
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.info("Exhibits view would be implemented here")

if __name__ == "__main__":
    main()
