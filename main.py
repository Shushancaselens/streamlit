import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view and facts filter
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'facts_filter' not in st.session_state:
    st.session_state.facts_filter = "all"
if 'facts_view_type' not in st.session_state:
    st.session_state.facts_view_type = "card"

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
def render_streamlit_card_view():
    # Get facts data
    facts_data = get_all_facts()
    
    # Filter facts based on current filter
    if st.session_state.facts_filter == 'disputed':
        filtered_facts = [fact for fact in facts_data if fact['isDisputed']]
    elif st.session_state.facts_filter == 'undisputed':
        filtered_facts = [fact for fact in facts_data if not fact['isDisputed']]
    else:
        filtered_facts = facts_data
    
    # Sort by date
    filtered_facts.sort(key=lambda x: x['date'].split('-')[0])
    
    if not filtered_facts:
        st.info("No facts found matching the selected criteria.")
        return
    
    # Display each fact as a card using Streamlit expander
    for i, fact in enumerate(filtered_facts):
        # Create expander title with date and event
        expander_title = f"**{fact['date']}** - {fact['event']}"
        if fact['isDisputed']:
            expander_title += " 🔴"
        
        with st.expander(expander_title, expanded=False):
            # Evidence & Source References section
            st.subheader("📁 Evidence & Source References")
            evidence_content = get_evidence_content(fact)
            
            if evidence_content:
                for evidence in evidence_content:
                    with st.container():
                        st.markdown(f"**{evidence['id']}** - {evidence['title']}")
                        
                        # Document Summary
                        if fact.get('doc_summary'):
                            st.info(f"**Document Summary:** {fact['doc_summary']}")
                        
                        # Source Text
                        if fact.get('source_text'):
                            st.markdown(f"**Source Text:** *{fact['source_text']}*")
                        
                        # Reference information
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            ref_text = f"**Exhibit:** {evidence['id']}"
                            if fact.get('page'):
                                ref_text += f" | **Page:** {fact['page']}"
                            if fact.get('paragraphs'):
                                ref_text += f" | **Paragraphs:** {fact['paragraphs']}"
                            st.markdown(ref_text)
                        
                        with col2:
                            if st.button(f"📋 Copy Ref", key=f"copy_{evidence['id']}_{i}"):
                                ref_copy = f"Exhibit: {evidence['id']}"
                                if fact.get('page'):
                                    ref_copy += f", Page: {fact['page']}"
                                if fact.get('paragraphs'):
                                    ref_copy += f", Paragraphs: {fact['paragraphs']}"
                                st.success("Reference copied!")
                        
                        st.divider()
            else:
                st.markdown("*No evidence references available for this fact*")
            
            # Party Submissions section
            st.subheader("⚖️ Party Submissions")
            
            # Claimant submission
            st.markdown("**🔵 Claimant Submission**")
            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
            if claimant_text == 'No specific submission recorded':
                st.markdown("*No submission provided*")
            else:
                st.info(claimant_text)
            
            # Respondent submission
            st.markdown("**🔴 Respondent Submission**")
            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
            if respondent_text == 'No specific submission recorded':
                st.markdown("*No submission provided*")
            else:
                st.warning(respondent_text)
            
            # Status section
            st.subheader("📊 Status")
            status_col1, status_col2 = st.columns(2)
            
            with status_col1:
                if fact['isDisputed']:
                    st.error("**Status:** Disputed")
                else:
                    st.success("**Status:** Undisputed")
            
            with status_col2:
                if fact.get('parties_involved'):
                    st.markdown(f"**Parties:** {', '.join(fact['parties_involved'])}")

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
    
    # Create the facts view
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # View toggle buttons
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
        
        with col1:
            if st.button("Card View", type="primary" if st.session_state.facts_view_type == "card" else "secondary"):
                st.session_state.facts_view_type = "card"
                st.rerun()
        
        with col2:
            if st.button("Document Categories", type="primary" if st.session_state.facts_view_type == "docset" else "secondary"):
                st.session_state.facts_view_type = "docset"
                st.rerun()
        
        with col3:
            if st.button("Timeline View", type="primary" if st.session_state.facts_view_type == "timeline" else "secondary"):
                st.session_state.facts_view_type = "timeline"
                st.rerun()
        
        # Facts filter tabs
        tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
        
        with tab1:
            st.session_state.facts_filter = "all"
            if st.session_state.facts_view_type == "card":
                render_streamlit_card_view()
            else:
                # For non-card views, show the HTML component
                show_html_component(st.session_state.facts_view_type, args_json, facts_json, document_sets_json, timeline_json)
        
        with tab2:
            st.session_state.facts_filter = "disputed"
            if st.session_state.facts_view_type == "card":
                render_streamlit_card_view()
            else:
                show_html_component(st.session_state.facts_view_type, args_json, facts_json, document_sets_json, timeline_json)
        
        with tab3:
            st.session_state.facts_filter = "undisputed"
            if st.session_state.facts_view_type == "card":
                render_streamlit_card_view()
            else:
                show_html_component(st.session_state.facts_view_type, args_json, facts_json, document_sets_json, timeline_json)

# Function to show HTML component for non-card views
def show_html_component(view_type, args_json, facts_json, document_sets_json, timeline_json):
    # Create the HTML content for non-card views (timeline and document sets)
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
                padding: 4px 10px;
                border-radius: 12px;
                font-size: 13px;
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
            
            /* Copy reference button */
            .copy-reference-btn {{
                display: inline-flex;
                align-items: center;
                gap: 4px;
                padding: 4px 8px;
                background-color: #f7fafc;
                border: 1px solid #e2e8f0;
                border-radius: 4px;
                cursor: pointer;
                font-size: 11px;
                color: #4a5568;
                transition: all 0.2s;
                margin-left: 8px;
            }}
            
            .copy-reference-btn:hover {{
                background-color: #edf2f7;
                border-color: #cbd5e0;
                transform: translateY(-1px);
            }}
            
            .copy-reference-btn svg {{
                width: 12px;
                height: 12px;
            }}
            
            /* Reference container */
            .reference-container {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-top: 8px;
                padding: 8px;
                background-color: #f8fafc;
                border-radius: 4px;
                border-left: 3px solid #a0aec0;
            }}
            
            .reference-text {{
                font-size: 12px;
                color: #4a5568;
                font-weight: 500;
                flex-grow: 1;
                margin-right: 12px;
            }}
            
            /* Facts styling */
            .facts-container {{
                margin-top: 20px;
            }}
            
            .facts-content {{
                margin-top: 20px;
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
                font-size: 16px;
                color: #2d3748;
                font-weight: 500;
            }}
            
            .timeline-footer {{
                padding: 14px 18px;
                background-color: #f8fafc;
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                border-top: 1px solid #e2e8f0;
            }}
            
            .timeline-meta {{
                font-size: 14px;
                color: #718096;
                margin-top: 10px;
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
            
            /* Card styling for consistency */
            .card-detail-section {{
                background-color: #f7fafc;
                padding: 12px 16px;
                border-radius: 6px;
                border: 1px solid #e2e8f0;
            }}
            
            .card-detail-label {{
                font-weight: 600;
                color: #4a5568;
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                margin-bottom: 6px;
            }}
            
            .card-detail-value {{
                color: #2d3748;
                font-size: 15px;
                line-height: 1.5;
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
                font-size: 12px;
                letter-spacing: 0.05em;
                margin-bottom: 10px;
                color: inherit;
            }}
            
            .claimant-submission .submission-header {{
                color: #3182ce;
            }}
            
            .respondent-submission .submission-header {{
                color: #e53e3e;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="facts-content">
                <!-- Timeline View -->
                <div id="timeline-view-content" class="content-section {{"active" if view_type == "timeline" else ""}}">
                    <div class="timeline-container">
                        <div class="timeline-wrapper">
                            <div class="timeline-line"></div>
                            <div id="timeline-events"></div>
                        </div>
                    </div>
                </div>
                
                <!-- Document Sets View -->
                <div id="docset-view-content" class="content-section {{"active" if view_type == "docset" else ""}}">
                    <div id="document-sets-container"></div>
                </div>
            </div>
        </div>
        
        <script>
            // Initialize data
            const factsData = {facts_json};
            const documentSets = {document_sets_json};
            const timelineData = {timeline_json};
            
            // Helper functions
            function getEvidenceContent(fact) {{
                if (!fact.exhibits || fact.exhibits.length === 0) {{
                    return [];
                }}
                
                const args_data = {args_json};
                let evidenceContent = [];
                
                fact.exhibits.forEach(exhibitId => {{
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
            
            function formatDate(dateString) {{
                if (dateString.includes('-')) {{
                    return dateString;
                }}
                
                const date = new Date(dateString);
                if (isNaN(date)) {{
                    return dateString;
                }}
                
                const options = {{ year: 'numeric', month: 'short', day: 'numeric' }};
                return date.toLocaleDateString(undefined, options);
            }}
            
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
            
            function toggleEvidence(evidenceId, factIndex) {{
                const content = document.getElementById(`evidence-content-${{evidenceId}}-${{factIndex}}`);
                const icon = document.getElementById(`evidence-icon-${{evidenceId}}-${{factIndex}}`);
                
                if (content.style.display === 'none' || content.style.display === '') {{
                    content.style.display = 'block';
                    icon.textContent = '−';
                }} else {{
                    content.style.display = 'none';
                    icon.textContent = '+';
                }}
            }}
            
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
            
            // Render Timeline View
            function renderTimeline() {{
                const container = document.getElementById('timeline-events');
                container.innerHTML = '';
                
                let filteredData = factsData;
                
                // Sort by date
                filteredData.sort((a, b) => {{
                    const dateA = a.date.split('-')[0];
                    const dateB = b.date.split('-')[0];
                    return new Date(dateA) - new Date(dateB);
                }});
                
                let currentYear = '';
                let prevYear = '';
                
                filteredData.forEach(fact => {{
                    currentYear = getYear(fact.date);
                    if (currentYear && currentYear !== prevYear) {{
                        const yearMarker = document.createElement('div');
                        yearMarker.className = 'timeline-year-marker';
                        yearMarker.innerHTML = `
                            <div class="timeline-year">${{currentYear}}</div>
                            <div class="timeline-year-line"></div>
                        `;
                        container.appendChild(yearMarker);
                        prevYear = currentYear;
                    }}
                
                    const timelineItem = document.createElement('div');
                    timelineItem.className = 'timeline-item';
                    
                    const timelinePoint = document.createElement('div');
                    timelinePoint.className = `timeline-point${{fact.isDisputed ? ' disputed' : ''}}`;
                    timelineItem.appendChild(timelinePoint);
                    
                    const contentEl = document.createElement('div');
                    contentEl.className = 'timeline-content';
                    
                    const headerEl = document.createElement('div');
                    headerEl.className = `timeline-header${{fact.isDisputed ? ' timeline-header-disputed' : ''}}`;
                    
                    const titleEl = document.createElement('div');
                    titleEl.style.cssText = 'display: flex; align-items: center; gap: 12px; flex-grow: 1;';
                    
                    const dateEl = document.createElement('div');
                    dateEl.className = 'timeline-date';
                    dateEl.textContent = formatDate(fact.date);
                    titleEl.appendChild(dateEl);
                    
                    const eventEl = document.createElement('div');
                    eventEl.style.cssText = 'font-weight: 500; color: #1a202c; flex-grow: 1;';
                    eventEl.textContent = fact.event;
                    titleEl.appendChild(eventEl);
                    
                    headerEl.appendChild(titleEl);
                    contentEl.appendChild(headerEl);
                    
                    const bodyEl = document.createElement('div');
                    bodyEl.className = 'timeline-body';
                    
                    // Evidence section
                    const evidenceContent = getEvidenceContent(fact);
                    if (evidenceContent.length > 0) {{
                        const evidenceSection = document.createElement('div');
                        evidenceSection.className = 'card-detail-section';
                        evidenceSection.style.marginBottom = '16px';
                        
                        evidenceSection.innerHTML = `
                            <div class="card-detail-label">Evidence & Source References (${{evidenceContent.length}} items)</div>
                            <div class="card-detail-value">
                                ${{evidenceContent.map((evidence, evidenceIndex) => `
                                    <div style="margin-bottom: 14px; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
                                        <div onclick="toggleEvidence('${{evidence.id}}', 'timeline-${{evidenceIndex}}')" 
                                             style="padding: 10px 14px; background-color: rgba(221, 107, 32, 0.05); cursor: pointer; display: flex; align-items: center; justify-content: space-between; transition: background-color 0.2s;"
                                             onmouseover="this.style.backgroundColor='rgba(221, 107, 32, 0.1)'" 
                                             onmouseout="this.style.backgroundColor='rgba(221, 107, 32, 0.05)'">
                                            <div>
                                                <span style="font-weight: 600; color: #dd6b20; font-size: 14px;">${{evidence.id}}</span>
                                                <span style="margin-left: 10px; color: #4a5568; font-size: 14px;">${{evidence.title}}</span>
                                            </div>
                                            <span id="evidence-icon-${{evidence.id}}-timeline-${{evidenceIndex}}" 
                                                  style="width: 18px; height: 18px; background-color: #dd6b20; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold;">+</span>
                                        </div>
                                        <div id="evidence-content-${{evidence.id}}-timeline-${{evidenceIndex}}" 
                                             style="display: none; padding: 14px; background-color: white; border-top: 1px solid #e2e8f0;">
                                            <div style="font-weight: 600; color: #2d3748; font-size: 14px; margin-bottom: 8px;">Document: ${{evidence.id}} - ${{evidence.title}}</div>
                                            <div style="background-color: #f8fafc; padding: 10px; border-radius: 6px; border-left: 3px solid #4299e1; margin-bottom: 10px;">
                                                <div style="font-weight: 600; font-size: 12px; text-transform: uppercase; color: #4299e1; margin-bottom: 6px;">Document Summary</div>
                                                <div style="font-size: 14px; color: #4a5568; line-height: 1.5;">${{fact.doc_summary || 'No document summary available'}}</div>
                                            </div>
                                            <div style="background-color: #f0f9ff; padding: 10px; border-radius: 6px; border-left: 3px solid #0ea5e9; margin-bottom: 10px;">
                                                <div style="font-weight: 600; font-size: 12px; text-transform: uppercase; color: #0ea5e9; margin-bottom: 6px;">Source Text</div>
                                                <div style="font-size: 14px; color: #4a5568; line-height: 1.5;">${{fact.source_text || 'No source text available'}}</div>
                                            </div>
                                        </div>
                                    </div>
                                `).join('')}}
                            </div>
                        `;
                        bodyEl.appendChild(evidenceSection);
                    }}
                    
                    // Submissions
                    const claimantSubmissionEl = document.createElement('div');
                    claimantSubmissionEl.className = 'card-source-text claimant-submission';
                    claimantSubmissionEl.style.marginBottom = '16px';
                    const claimantText = fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' 
                        ? fact.claimant_submission 
                        : 'No submission provided';
                    claimantSubmissionEl.innerHTML = `
                        <div class="submission-header">Claimant Submission</div>
                        <div>${{claimantText}}</div>
                    `;
                    bodyEl.appendChild(claimantSubmissionEl);
                    
                    const respondentSubmissionEl = document.createElement('div');
                    respondentSubmissionEl.className = 'card-source-text respondent-submission';
                    respondentSubmissionEl.style.marginBottom = '16px';
                    const respondentText = fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' 
                        ? fact.respondent_submission 
                        : 'No submission provided';
                    respondentSubmissionEl.innerHTML = `
                        <div class="submission-header">Respondent Submission</div>
                        <div>${{respondentText}}</div>
                    `;
                    bodyEl.appendChild(respondentSubmissionEl);
                    
                    // Status
                    const statusSection = document.createElement('div');
                    statusSection.className = 'card-detail-section';
                    statusSection.innerHTML = `
                        <div class="card-detail-label">Status</div>
                        <div class="card-detail-value">${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}</div>
                    `;
                    bodyEl.appendChild(statusSection);
                    
                    contentEl.appendChild(bodyEl);
                    timelineItem.appendChild(contentEl);
                    container.appendChild(timelineItem);
                }});
            }}
            
            // Render Document Sets View
            function renderDocumentSets() {{
                const container = document.getElementById('document-sets-container');
                container.innerHTML = '';
                
                let filteredFacts = factsData;
                filteredFacts.sort((a, b) => {{
                    const dateA = a.date.split('-')[0];
                    const dateB = b.date.split('-')[0];
                    return new Date(dateA) - new Date(dateB);
                }});
                
                const docsWithFacts = {{}};
                
                documentSets.forEach(ds => {{
                    if (ds.isGroup) {{
                        docsWithFacts[ds.id] = {{
                            docset: ds,
                            facts: []
                        }};
                    }}
                }});
                
                filteredFacts.forEach((fact, index) => {{
                    let factAssigned = false;
                    
                    documentSets.forEach(ds => {{
                        if (ds.isGroup) {{
                            ds.documents.forEach(doc => {{
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
                
                Object.values(docsWithFacts).forEach(docWithFacts => {{
                    const docset = docWithFacts.docset;
                    const facts = docWithFacts.facts;
                    
                    const docsetEl = document.createElement('div');
                    docsetEl.className = 'docset-container';
                    
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
                        contentHtml += '<div style="padding: 16px;">';
                        
                        facts.forEach((fact, factIndex) => {{
                            const evidenceContent = getEvidenceContent(fact);
                            
                            contentHtml += `
                                <div style="margin-bottom: 16px; border: 1px solid #e2e8f0; border-radius: 8px; background-color: white; box-shadow: 0 1px 3px rgba(0,0,0,0.1); overflow: hidden;">
                                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px; background-color: ${{fact.isDisputed ? 'rgba(229, 62, 62, 0.05)' : '#f8fafc'}};">
                                        <div style="display: flex; align-items: center; flex-grow: 1; gap: 12px;">
                                            <div style="font-weight: 600; color: #2d3748; min-width: 120px;">${{fact.date}}</div>
                                            <div style="font-weight: 500; color: #1a202c; flex-grow: 1;">${{fact.event}}</div>
                                        </div>
                                    </div>
                                    <div style="padding: 20px; border-top: 1px solid #e2e8f0; background-color: white;">
                            `;
                            
                            // Evidence section
                            if (evidenceContent.length > 0) {{
                                contentHtml += `
                                    <div class="card-detail-section" style="margin-bottom: 16px;">
                                        <div class="card-detail-label">Evidence & Source References (${{evidenceContent.length}} items)</div>
                                        <div class="card-detail-value">
                                            ${{evidenceContent.map((evidence, evidenceIndex) => `
                                                <div style="margin-bottom: 14px; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
                                                    <div onclick="toggleEvidence('${{evidence.id}}', 'docset-${{docset.id}}-${{factIndex}}-${{evidenceIndex}}')" 
                                                         style="padding: 10px 14px; background-color: rgba(221, 107, 32, 0.05); cursor: pointer; display: flex; align-items: center; justify-content: space-between; transition: background-color 0.2s;"
                                                         onmouseover="this.style.backgroundColor='rgba(221, 107, 32, 0.1)'" 
                                                         onmouseout="this.style.backgroundColor='rgba(221, 107, 32, 0.05)'">
                                                        <div>
                                                            <span style="font-weight: 600; color: #dd6b20; font-size: 14px;">${{evidence.id}}</span>
                                                            <span style="margin-left: 10px; color: #4a5568; font-size: 14px;">${{evidence.title}}</span>
                                                        </div>
                                                        <span id="evidence-icon-${{evidence.id}}-docset-${{docset.id}}-${{factIndex}}-${{evidenceIndex}}" 
                                                              style="width: 18px; height: 18px; background-color: #dd6b20; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold;">+</span>
                                                    </div>
                                                    <div id="evidence-content-${{evidence.id}}-docset-${{docset.id}}-${{factIndex}}-${{evidenceIndex}}" 
                                                         style="display: none; padding: 14px; background-color: white; border-top: 1px solid #e2e8f0;">
                                                        <div style="font-weight: 600; color: #2d3748; font-size: 14px; margin-bottom: 8px;">Document: ${{evidence.id}} - ${{evidence.title}}</div>
                                                        <div style="background-color: #f8fafc; padding: 10px; border-radius: 6px; border-left: 3px solid #4299e1; margin-bottom: 10px;">
                                                            <div style="font-weight: 600; font-size: 12px; text-transform: uppercase; color: #4299e1; margin-bottom: 6px;">Document Summary</div>
                                                            <div style="font-size: 14px; color: #4a5568; line-height: 1.5;">${{fact.doc_summary || 'No document summary available'}}</div>
                                                        </div>
                                                        <div style="background-color: #f0f9ff; padding: 10px; border-radius: 6px; border-left: 3px solid #0ea5e9; margin-bottom: 10px;">
                                                            <div style="font-weight: 600; font-size: 12px; text-transform: uppercase; color: #0ea5e9; margin-bottom: 6px;">Source Text</div>
                                                            <div style="font-size: 14px; color: #4a5568; line-height: 1.5;">${{fact.source_text || 'No source text available'}}</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            `).join('')}}
                                        </div>
                                    </div>
                                `;
                            }}
                            
                            // Submissions
                            const claimantText = fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' 
                                ? fact.claimant_submission 
                                : 'No submission provided';
                            const respondentText = fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' 
                                ? fact.respondent_submission 
                                : 'No submission provided';
                            
                            contentHtml += `
                                <div style="margin-top: 16px;">
                                    <div class="card-source-text claimant-submission">
                                        <div class="submission-header">Claimant Submission</div>
                                        <div>${{claimantText}}</div>
                                    </div>
                                    <div class="card-source-text respondent-submission">
                                        <div class="submission-header">Respondent Submission</div>
                                        <div>${{respondentText}}</div>
                                    </div>
                                </div>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 16px 0;">
                                    <div class="card-detail-section">
                                        <div class="card-detail-label">Status</div>
                                        <div class="card-detail-value">${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}</div>
                                    </div>
                                </div>
                            `;
                            
                            contentHtml += `
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
            
            // Initialize based on view type
            document.addEventListener('DOMContentLoaded', function() {{
                if ('{view_type}' === 'timeline') {{
                    renderTimeline();
                }} else if ('{view_type}' === 'docset') {{
                    renderDocumentSets();
                }}
            }});
            
            // Initialize immediately
            if ('{view_type}' === 'timeline') {{
                renderTimeline();
            }} else if ('{view_type}' === 'docset') {{
                renderDocumentSets();
            }}
        </script>
    </body>
    </html>
    """
    
    # Render the HTML component
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
