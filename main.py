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

if 'current_facts_view' not in st.session_state:
    st.session_state.current_facts_view = "card"

if 'facts_filter' not in st.session_state:
    st.session_state.facts_filter = "all"

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

def get_evidence_details(exhibits, args_data):
    """Get evidence details for given exhibit IDs"""
    evidence_details = []
    
    def find_evidence(args, exhibit_id):
        for arg_key in args:
            arg = args[arg_key]
            if 'evidence' in arg and arg['evidence']:
                for evidence in arg['evidence']:
                    if evidence['id'] == exhibit_id:
                        return evidence
            if 'children' in arg and arg['children']:
                child_evidence = find_evidence(arg['children'], exhibit_id)
                if child_evidence:
                    return child_evidence
        return None
    
    for exhibit_id in exhibits:
        evidence = (find_evidence(args_data['claimantArgs'], exhibit_id) or 
                   find_evidence(args_data['respondentArgs'], exhibit_id))
        
        if evidence:
            evidence_details.append({
                'id': exhibit_id,
                'title': evidence['title'],
                'summary': evidence['summary']
            })
        else:
            evidence_details.append({
                'id': exhibit_id,
                'title': exhibit_id,
                'summary': 'Evidence details not available'
            })
    
    return evidence_details

def render_streamlit_cards(filtered_facts, args_data):
    """Render facts as native Streamlit cards"""
    
    if not filtered_facts:
        st.info("No facts found matching the selected criteria.")
        return
    
    for i, fact in enumerate(filtered_facts):
        # Create card styling based on disputed status
        if fact['isDisputed']:
            card_container = st.container()
            with card_container:
                st.markdown("""
                <style>
                div[data-testid="stExpander"] > div:first-child {
                    border-left: 4px solid #e53e3e !important;
                    background-color: rgba(229, 62, 62, 0.02) !important;
                }
                </style>
                """, unsafe_allow_html=True)
        
        # Create the main expander for the fact
        with st.expander(f"**{fact['date']}** - {fact['event']}", expanded=False):
            
            # Add party badges
            badge_html = ""
            if fact['parties_involved']:
                for party in fact['parties_involved']:
                    if party == 'Appellant':
                        badge_html += '<span style="background-color: rgba(49, 130, 206, 0.1); color: #3182ce; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500; margin-right: 6px;">Appellant</span>'
                    else:
                        badge_html += '<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500; margin-right: 6px;">Respondent</span>'
            
            if fact['isDisputed']:
                badge_html += '<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">Disputed</span>'
            
            if badge_html:
                st.markdown(badge_html, unsafe_allow_html=True)
                st.markdown("---")
            
            # Create two columns for document and argument info
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📄 Document**")
                st.markdown(f"**{fact['doc_name'] or 'N/A'}**")
                if fact['page']:
                    st.markdown(f"*Page {fact['page']}*")
            
            with col2:
                st.markdown("**📋 Argument**")
                st.markdown(f"**{fact['argId']}. {fact['argTitle']}**")
                if fact['paragraphs']:
                    st.markdown(f"*Paragraphs: {fact['paragraphs']}*")
            
            # Source text
            if fact['source_text'] and fact['source_text'] != 'No specific submission recorded':
                st.markdown("**📝 Source Text:**")
                st.info(fact['source_text'])
            
            # Submissions
            if fact['claimant_submission'] and fact['claimant_submission'] != 'No specific submission recorded':
                st.markdown("**👤 Claimant Submission:**")
                st.markdown(f'<div style="background-color: rgba(49, 130, 206, 0.03); border-left: 4px solid #3182ce; padding: 12px; margin: 8px 0; border-radius: 0 6px 6px 0; font-style: italic;">{fact["claimant_submission"]}</div>', unsafe_allow_html=True)
            
            if fact['respondent_submission'] and fact['respondent_submission'] != 'No specific submission recorded':
                st.markdown("**👤 Respondent Submission:**")
                st.markdown(f'<div style="background-color: rgba(229, 62, 62, 0.03); border-left: 4px solid #e53e3e; padding: 12px; margin: 8px 0; border-radius: 0 6px 6px 0; font-style: italic;">{fact["respondent_submission"]}</div>', unsafe_allow_html=True)
            
            # Document summary
            if fact['doc_summary']:
                st.markdown("**📖 Document Summary:**")
                st.markdown(f"*{fact['doc_summary']}*")
            
            # Status and Evidence in two columns
            col3, col4 = st.columns([1, 2])
            
            with col3:
                st.markdown("**⚖️ Status**")
                if fact['isDisputed']:
                    st.markdown('<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 4px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">Disputed</span>', unsafe_allow_html=True)
                else:
                    st.markdown("Undisputed")
            
            with col4:
                st.markdown("**📎 Evidence**")
                if fact['exhibits']:
                    evidence_details = get_evidence_details(fact['exhibits'], args_data)
                    
                    # Use checkboxes instead of nested expanders to avoid the error
                    for j, evidence in enumerate(evidence_details):
                        evidence_key = f"evidence_{i}_{j}_{st.session_state.facts_filter}"
                        if st.checkbox(f"📁 {evidence['id']}: {evidence['title']}", key=evidence_key):
                            st.markdown(f"*{evidence['summary']}*")
                else:
                    st.markdown("None")

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
    
    # Create the facts HTML component
    if st.session_state.view == "Facts":
        # Create a container for view selection and filtering
        st.title("Case Facts")
        
        # View toggle buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("Card View", key="card_view_btn", 
                        type="primary" if st.session_state.current_facts_view == "card" else "secondary",
                        use_container_width=True):
                st.session_state.current_facts_view = "card"
                st.experimental_rerun()
        
        with col2:
            if st.button("Table View", key="table_view_btn",
                        type="primary" if st.session_state.current_facts_view == "table" else "secondary",
                        use_container_width=True):
                st.session_state.current_facts_view = "table"
                st.experimental_rerun()
        
        with col3:
            if st.button("Timeline View", key="timeline_view_btn",
                        type="primary" if st.session_state.current_facts_view == "timeline" else "secondary",
                        use_container_width=True):
                st.session_state.current_facts_view = "timeline"
                st.experimental_rerun()
        
        with col4:
            if st.button("Document Categories", key="docset_view_btn",
                        type="primary" if st.session_state.current_facts_view == "docset" else "secondary",
                        use_container_width=True):
                st.session_state.current_facts_view = "docset"
                st.experimental_rerun()
        
        # Facts filter tabs
        tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
        
        with tab1:
            st.session_state.facts_filter = "all"
            filtered_facts = facts_data
        
        with tab2:
            st.session_state.facts_filter = "disputed"
            filtered_facts = [fact for fact in facts_data if fact['isDisputed']]
        
        with tab3:
            st.session_state.facts_filter = "undisputed"
            filtered_facts = [fact for fact in facts_data if not fact['isDisputed']]
        
        # Sort facts by date
        filtered_facts.sort(key=lambda x: x['date'].split('-')[0])
        
        # Render based on selected view
        if st.session_state.current_facts_view == "card":
            # Use Streamlit native card view
            render_streamlit_cards(filtered_facts, args_data)
            
        else:
            # Use HTML component for other views
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
                    
                    /* Timeline styling */
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
                    
                    .timeline-meta {{
                        font-size: 13px;
                        color: #718096;
                        margin-top: 8px;
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
                    
                    <!-- Table View -->
                    <div id="table-view-content" class="facts-content" style="display: {'block' if st.session_state.current_facts_view == 'table' else 'none'};">
                        <div class="table-view-container">
                            <table class="table-view">
                                <thead>
                                    <tr>
                                        <th onclick="sortTable('facts-table-body', 0)">Date</th>
                                        <th onclick="sortTable('facts-table-body', 1)">Event</th>
                                        <th onclick="sortTable('facts-table-body', 2)">Source Text</th>
                                        <th onclick="sortTable('facts-table-body', 3)">Page</th>
                                        <th onclick="sortTable('facts-table-body', 4)">Document</th>
                                        <th onclick="sortTable('facts-table-body', 5)">Doc Summary</th>
                                        <th onclick="sortTable('facts-table-body', 6)">Claimant Submission</th>
                                        <th onclick="sortTable('facts-table-body', 7)">Respondent Submission</th>
                                        <th onclick="sortTable('facts-table-body', 8)">Status</th>
                                        <th onclick="sortTable('facts-table-body', 9)">Evidence</th>
                                    </tr>
                                </thead>
                                <tbody id="facts-table-body"></tbody>
                            </table>
                        </div>
                    </div>
                    
                    <!-- Timeline View -->
                    <div id="timeline-view-content" class="facts-content" style="display: {'block' if st.session_state.current_facts_view == 'timeline' else 'none'};">
                        <div class="timeline-container">
                            <div class="timeline-wrapper">
                                <div class="timeline-line"></div>
                                <div id="timeline-events"></div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Document Sets View -->
                    <div id="docset-view-content" class="facts-content" style="display: {'block' if st.session_state.current_facts_view == 'docset' else 'none'};">
                        <div id="document-sets-container"></div>
                    </div>
                </div>
                
                <script>
                    // Initialize data
                    const factsData = {facts_json};
                    const documentSets = {document_sets_json};
                    const timelineData = {timeline_json};
                    const currentFilter = '{st.session_state.facts_filter}';
                    
                    // Filter facts based on current selection
                    let filteredFacts = factsData;
                    if (currentFilter === 'disputed') {{
                        filteredFacts = factsData.filter(fact => fact.isDisputed);
                    }} else if (currentFilter === 'undisputed') {{
                        filteredFacts = factsData.filter(fact => !fact.isDisputed);
                    }}
                    
                    // Sort by date
                    filteredFacts.sort((a, b) => {{
                        const dateA = a.date.split('-')[0];
                        const dateB = b.date.split('-')[0];
                        return new Date(dateA) - new Date(dateB);
                    }});
                    
                    // Render views based on current selection
                    if ('{st.session_state.current_facts_view}' === 'table') {{
                        renderFacts(currentFilter);
                    }} else if ('{st.session_state.current_facts_view}' === 'timeline') {{
                        renderTimeline(currentFilter);
                    }} else if ('{st.session_state.current_facts_view}' === 'docset') {{
                        renderDocumentSets(currentFilter);
                    }}
                    
                    // Copy all content function
                    function copyAllContent() {{
                        let contentToCopy = 'Case Facts\\n\\n';
                        
                        filteredFacts.forEach(fact => {{
                            contentToCopy += `${{fact.date}} - ${{fact.event}}\\n`;
                            if (fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded') {{
                                contentToCopy += `Claimant: ${{fact.claimant_submission}}\\n`;
                            }}
                            if (fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded') {{
                                contentToCopy += `Respondent: ${{fact.respondent_submission}}\\n`;
                            }}
                            contentToCopy += '\\n';
                        }});
                        
                        const textarea = document.createElement('textarea');
                        textarea.value = contentToCopy;
                        document.body.appendChild(textarea);
                        textarea.select();
                        document.execCommand('copy');
                        document.body.removeChild(textarea);
                        
                        const notification = document.getElementById('copy-notification');
                        notification.classList.add('show');
                        setTimeout(() => notification.classList.remove('show'), 2000);
                    }}
                    
                    // Export functions
                    function exportAsCsv() {{
                        let csvContent = "Date,Event,Source Text,Page,Document,Doc Summary,Claimant Submission,Respondent Submission,Status,Evidence\\n";
                        
                        filteredFacts.forEach(fact => {{
                            const row = [
                                fact.date,
                                fact.event,
                                fact.source_text || '',
                                fact.page || '',
                                fact.doc_name || '',
                                fact.doc_summary || '',
                                fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' ? fact.claimant_submission : 'No submission',
                                fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' ? fact.respondent_submission : 'No submission',
                                fact.isDisputed ? 'Disputed' : 'Undisputed',
                                fact.exhibits ? fact.exhibits.join('; ') : 'None'
                            ].map(field => `"${{(field || '').replace(/"/g, '""')}}"`).join(',');
                            
                            csvContent += row + '\\n';
                        }});
                        
                        const encodedUri = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
                        const link = document.createElement("a");
                        link.setAttribute("href", encodedUri);
                        link.setAttribute("download", "facts.csv");
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
                    
                    // Sort table function
                    function sortTable(tableId, columnIndex) {{
                        const table = document.getElementById(tableId);
                        const rows = Array.from(table.rows);
                        let dir = 1;
                        
                        if (table.getAttribute('data-sort-column') === String(columnIndex) &&
                            table.getAttribute('data-sort-dir') === '1') {{
                            dir = -1;
                        }}
                        
                        rows.sort((a, b) => {{
                            const cellA = a.cells[columnIndex].textContent.trim();
                            const cellB = b.cells[columnIndex].textContent.trim();
                            
                            if (columnIndex === 0) {{
                                const dateA = new Date(cellA);
                                const dateB = new Date(cellB);
                                if (!isNaN(dateA) && !isNaN(dateB)) {{
                                    return dir * (dateA - dateB);
                                }}
                            }}
                            
                            return dir * cellA.localeCompare(cellB);
                        }});
                        
                        rows.forEach(row => table.appendChild(row));
                        table.setAttribute('data-sort-column', columnIndex);
                        table.setAttribute('data-sort-dir', dir);
                    }}
                    
                    // Format date for display
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
                    
                    // Render facts table
                    function renderFacts(type = 'all') {{
                        const tableBody = document.getElementById('facts-table-body');
                        tableBody.innerHTML = '';
                        
                        filteredFacts.forEach(fact => {{
                            const row = document.createElement('tr');
                            if (fact.isDisputed) {{
                                row.classList.add('disputed');
                            }}
                            
                            // Create cells
                            const cells = [
                                fact.date,
                                fact.event,
                                fact.source_text || '',
                                fact.page || '',
                                fact.doc_name || '',
                                fact.doc_summary || '',
                                fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' ? fact.claimant_submission : 'No submission',
                                fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' ? fact.respondent_submission : 'No submission',
                                fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : 'Undisputed',
                                fact.exhibits ? fact.exhibits.join(', ') : 'None'
                            ];
                            
                            cells.forEach((cellContent, index) => {{
                                const cell = document.createElement('td');
                                if (index === 8) {{ // Status column
                                    cell.innerHTML = cellContent;
                                }} else {{
                                    cell.textContent = cellContent;
                                    cell.title = cellContent;
                                }}
                                row.appendChild(cell);
                            }});
                            
                            tableBody.appendChild(row);
                        }});
                    }}
                    
                    // Render timeline view
                    function renderTimeline(tabType = 'all') {{
                        const container = document.getElementById('timeline-events');
                        container.innerHTML = '';
                        
                        let currentYear = '';
                        let prevYear = '';
                        
                        filteredFacts.forEach(fact => {{
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
                            
                            const dateEl = document.createElement('div');
                            dateEl.className = 'timeline-date';
                            dateEl.textContent = formatDate(fact.date);
                            headerEl.appendChild(dateEl);
                            
                            const badgesEl = document.createElement('div');
                            badgesEl.className = 'timeline-badges';
                            
                            if (fact.parties_involved && fact.parties_involved.length > 0) {{
                                fact.parties_involved.forEach(party => {{
                                    const partyBadge = document.createElement('span');
                                    partyBadge.className = `badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                                    partyBadge.textContent = party;
                                    badgesEl.appendChild(partyBadge);
                                }});
                            }}
                            
                            const statusBadge = document.createElement('span');
                            statusBadge.className = `badge ${{fact.isDisputed ? 'disputed-badge' : 'shared-badge'}}`;
                            statusBadge.textContent = fact.isDisputed ? 'Disputed' : 'Undisputed';
                            badgesEl.appendChild(statusBadge);
                            
                            headerEl.appendChild(badgesEl);
                            contentEl.appendChild(headerEl);
                            
                            const bodyEl = document.createElement('div');
                            bodyEl.className = 'timeline-body';
                            
                            const factContent = document.createElement('div');
                            factContent.className = 'timeline-fact';
                            factContent.textContent = fact.event;
                            bodyEl.appendChild(factContent);
                            
                            if (fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded') {{
                                const claimantTextEl = document.createElement('div');
                                claimantTextEl.style.cssText = 'font-style: italic; color: #3182ce; margin-top: 8px; padding: 12px; background-color: rgba(49, 130, 206, 0.05); border-left: 4px solid #3182ce; font-size: 13px; border-radius: 0 6px 6px 0;';
                                claimantTextEl.innerHTML = `<strong>Claimant:</strong><br>${{fact.claimant_submission}}`;
                                bodyEl.appendChild(claimantTextEl);
                            }}
                            
                            if (fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded') {{
                                const respondentTextEl = document.createElement('div');
                                respondentTextEl.style.cssText = 'font-style: italic; color: #e53e3e; margin-top: 8px; padding: 12px; background-color: rgba(229, 62, 62, 0.05); border-left: 4px solid #e53e3e; font-size: 13px; border-radius: 0 6px 6px 0;';
                                respondentTextEl.innerHTML = `<strong>Respondent:</strong><br>${{fact.respondent_submission}}`;
                                bodyEl.appendChild(respondentTextEl);
                            }}
                            
                            const metaEl = document.createElement('div');
                            metaEl.className = 'timeline-meta';
                            metaEl.innerHTML = `<span><strong>Document:</strong> ${{fact.doc_name || 'N/A'}}</span><span><strong>Page:</strong> ${{fact.page || 'N/A'}}</span>`;
                            bodyEl.appendChild(metaEl);
                            
                            contentEl.appendChild(bodyEl);
                            timelineItem.appendChild(contentEl);
                            container.appendChild(timelineItem);
                        }});
                        
                        if (filteredFacts.length === 0) {{
                            container.innerHTML = '<p>No timeline events found matching the selected criteria.</p>';
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
                    
                    // Render document sets view
                    function renderDocumentSets(tabType = 'all') {{
                        const container = document.getElementById('document-sets-container');
                        container.innerHTML = '';
                        
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
                            // Distribute facts to appropriate categories
                            let factAssigned = false;
                            
                            // Simple assignment based on document name
                            if (fact.doc_name && fact.doc_name.includes('Appeal')) {{
                                docsWithFacts['appeal'].facts.push(fact);
                                factAssigned = true;
                            }} else if (fact.doc_name && fact.doc_name.includes('Provisional')) {{
                                docsWithFacts['provisional_measures'].facts.push(fact);
                                factAssigned = true;
                            }} else if (fact.doc_name && fact.doc_name.includes('Admissibility')) {{
                                docsWithFacts['admissibility'].facts.push(fact);
                                factAssigned = true;
                            }} else {{
                                docsWithFacts['challenge'].facts.push(fact);
                                factAssigned = true;
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
                                contentHtml += `
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
                                                ${{facts.map(fact => `
                                                    <tr ${{fact.isDisputed ? 'class="disputed"' : ''}}>
                                                        <td>${{fact.date}}</td>
                                                        <td>${{fact.event}}</td>
                                                        <td title="${{fact.source_text || ''}}">${{fact.source_text || ''}}</td>
                                                        <td>${{fact.page || ''}}</td>
                                                        <td><strong>${{fact.doc_name || 'N/A'}}</strong></td>
                                                        <td title="${{fact.doc_summary || ''}}">${{fact.doc_summary || ''}}</td>
                                                        <td title="${{fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' ? fact.claimant_submission : 'No submission'}}">${{fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded' ? fact.claimant_submission : 'No submission'}}</td>
                                                        <td title="${{fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' ? fact.respondent_submission : 'No submission'}}">${{fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded' ? fact.respondent_submission : 'No submission'}}</td>
                                                        <td>${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : 'Undisputed'}}</td>
                                                        <td>${{fact.exhibits ? fact.exhibits.join(', ') : 'None'}}</td>
                                                    </tr>
                                                `).join('')}}
                                            </tbody>
                                        </table>
                                    </div>
                                `;
                            }} else {{
                                contentHtml += '<p style="padding: 12px;">No facts found</p>';
                            }}
                            
                            contentHtml += '</div>';
                            docsetEl.innerHTML = headerHtml + contentHtml;
                            container.appendChild(docsetEl);
                        }});
                    }}
                </script>
            </body>
            </html>
            """
            
            # Render the HTML component
            components.html(html_content, height=800, scrolling=True)
    
    elif st.session_state.view == "Arguments":
        st.title("Arguments")
        st.write("Arguments view would be implemented here.")
    
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.write("Exhibits view would be implemented here.")

if __name__ == "__main__":
    main()
