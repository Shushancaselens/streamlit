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

# Mock document content for preview functionality
def get_document_content():
    return {
        "Statement of Appeal": {
            "title": "Statement of Appeal",
            "content": """
            <h2>STATEMENT OF APPEAL</h2>
            <p><strong>Case No:</strong> CAS 2024/A/9876</p>
            <p><strong>Date:</strong> January 15, 2024</p>
            
            <h3>I. INTRODUCTION</h3>
            <p>The Appellant hereby submits this Statement of Appeal pursuant to Article 62 of the Code of Sports-related Arbitration...</p>
            
            <h3>II. FACTUAL BACKGROUND</h3>
            <p>Athletic Club United was officially founded and registered with the National Football Federation on January 12, 1950, under registration number NFF-1950-0047...</p>
            
            <h3>III. SPORTING SUCCESSION ARGUMENT</h3>
            <p>The club has maintained continuous operation under the same name 'Athletic Club United' since its official registration in 1950, as evidenced by uninterrupted participation in national competitions...</p>
            
            <h3>IV. LEGAL GROUNDS</h3>
            <p>Based on established CAS jurisprudence, particularly CAS 2016/A/4576, the criteria for sporting succession include:</p>
            <ul>
                <li>Continuous use of identifying elements</li>
                <li>Public recognition of the entity's identity</li>
                <li>Preservation of sporting records and achievements</li>
                <li>Consistent participation in competitions under the same identity</li>
            </ul>
            """,
            "pages": 45
        },
        "Answer to Request for Provisional Measures": {
            "title": "Answer to Request for Provisional Measures", 
            "content": """
            <h2>ANSWER TO REQUEST FOR PROVISIONAL MEASURES</h2>
            <p><strong>Case No:</strong> CAS 2024/A/9876</p>
            <p><strong>Date:</strong> February 22, 2024</p>
            
            <h3>I. PROCEDURAL BACKGROUND</h3>
            <p>The Respondent hereby responds to the Appellant's request for provisional measures dated February 1, 2024...</p>
            
            <h3>II. FACTUAL DISPUTES</h3>
            <p>The club's operations completely ceased during the 1975-1976 season, with no participation in any competitive events and complete absence from all official federation records during this period...</p>
            
            <h3>III. OPERATIONAL DISCONTINUITY</h3>
            <p>Complete cessation of all club operations occurred during the 1975-1976 season, with no team fielded in any competition and complete absence from federation records, constituting a clear break in continuity...</p>
            
            <h3>IV. LEGAL ANALYSIS</h3>
            <p>Pursuant to CAS 2017/A/5465, actual operational continuity (specifically participation in competitions) is the primary determinant of sporting succession...</p>
            """,
            "pages": 38
        },
        "Appeal Brief": {
            "title": "Appeal Brief",
            "content": """
            <h2>COMPREHENSIVE APPEAL BRIEF</h2>
            <p><strong>Case No:</strong> CAS 2024/A/9876</p>
            <p><strong>Date:</strong> March 10, 2024</p>
            
            <h3>I. EXECUTIVE SUMMARY</h3>
            <p>This comprehensive brief supports the appeal with detailed arguments and evidence regarding club continuity and identity...</p>
            
            <h3>II. CHAMPIONSHIP HISTORY</h3>
            <p>Athletic Club United achieved its first National Championship victory on May 20, 1955, defeating rivals 3-1 in the final match held at National Stadium...</p>
            
            <h3>III. EVIDENCE COMPILATION</h3>
            <p>The following exhibits demonstrate continuous operation and identity maintenance:</p>
            <ul>
                <li>Exhibit C-1: Historical Registration Documents</li>
                <li>Exhibit C-2: Competition Participation Records</li>
                <li>Exhibit C-3: Championship Certificates and Trophies</li>
                <li>Exhibit C-4: Media Coverage Archive</li>
            </ul>
            """,
            "pages": 67
        }
    }

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
            "source": "provisional messier - Answer to Request for PM",
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
            "source": "provisional messier - Answer to Request for PM",
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
            "id": "provisional_messier",
            "name": "provisional messier",
            "party": "Respondent",
            "category": "provisional messier",
            "isGroup": True,
            "documents": [
                {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "category": "provisional messier"},
                {"id": "4", "name": "4. Answer to PM", "party": "Respondent", "category": "provisional messier"}
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
    document_content = get_document_content()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    document_sets_json = json.dumps(document_sets)
    timeline_json = json.dumps(timeline_data)
    document_content_json = json.dumps(document_content)
    
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
                
                /* Table view with horizontal scroll */
                .table-view-container {{
                    overflow-x: auto;
                    border: 1px solid #dee2e6;
                    border-radius: 8px;
                    margin-top: 20px;
                }}
                
                .table-view {{
                    width: 100%;
                    min-width: 1200px; /* Ensure minimum width for readability */
                    border-collapse: collapse;
                    font-size: 14px; /* Normal readable size */
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
                    font-size: 13px; /* Normal readable size */
                    vertical-align: top;
                    line-height: 1.4;
                }}
                
                .table-view tr:hover {{
                    background-color: #f8f9fa;
                }}
                
                /* Column-specific widths for better readability */
                .table-view td:nth-child(1) {{ /* Date */
                    min-width: 120px;
                    white-space: nowrap;
                }}
                
                .table-view td:nth-child(2) {{ /* Event */
                    min-width: 250px;
                    max-width: 300px;
                }}
                
                .table-view td:nth-child(3) {{ /* Source Text */
                    min-width: 300px;
                    max-width: 400px;
                }}
                
                .table-view td:nth-child(4) {{ /* Page */
                    min-width: 80px;
                    white-space: nowrap;
                }}
                
                .table-view td:nth-child(5) {{ /* Document */
                    min-width: 200px;
                    max-width: 250px;
                    font-weight: 500;
                }}
                
                .table-view td:nth-child(6) {{ /* Doc Summary */
                    min-width: 250px;
                    max-width: 350px;
                    font-style: italic;
                    color: #666;
                }}
                
                .table-view td:nth-child(7) {{ /* Claimant Submission */
                    min-width: 300px;
                    max-width: 400px;
                }}
                
                .table-view td:nth-child(8) {{ /* Respondent Submission */
                    min-width: 300px;
                    max-width: 400px;
                }}
                
                .table-view td:nth-child(9) {{ /* Status */
                    min-width: 100px;
                    white-space: nowrap;
                }}
                
                .table-view td:nth-child(10) {{ /* Evidence */
                    min-width: 200px;
                    max-width: 300px;
                }}
                
                /* Text wrapping for content cells */
                .table-view td:nth-child(2),
                .table-view td:nth-child(3),
                .table-view td:nth-child(5),
                .table-view td:nth-child(6),
                .table-view td:nth-child(7),
                .table-view td:nth-child(8),
                .table-view td:nth-child(10) {{
                    word-wrap: break-word;
                    overflow-wrap: break-word;
                }}
                
                /* Horizontal scroll indicator */
                .table-view-container::-webkit-scrollbar {{
                    height: 8px;
                }}
                
                .table-view-container::-webkit-scrollbar-track {{
                    background: #f1f1f1;
                    border-radius: 4px;
                }}
                
                .table-view-container::-webkit-scrollbar-thumb {{
                    background: #c1c1c1;
                    border-radius: 4px;
                }}
                
                .table-view-container::-webkit-scrollbar-thumb:hover {{
                    background: #a8a8a8;
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
                
                .view-toggle button:nth-child(3) {{
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
                    display: block; /* Changed from 'none' to 'block' to be open by default */
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
                    transform: rotate(90deg); /* Start expanded by default */
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
                
                /* Document link styling */
                .document-link {{
                    color: #4299e1;
                    text-decoration: underline;
                    cursor: pointer;
                    font-weight: 500;
                    transition: color 0.2s;
                }}
                
                .document-link:hover {{
                    color: #2b6cb0;
                    text-decoration: none;
                }}
                
                /* Document preview modal */
                .document-modal {{
                    display: none;
                    position: fixed;
                    z-index: 1000;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0,0,0,0.5);
                    backdrop-filter: blur(4px);
                }}
                
                .document-modal-content {{
                    background-color: white;
                    margin: 2% auto;
                    padding: 0;
                    border-radius: 8px;
                    width: 90%;
                    max-width: 900px;
                    height: 90%;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                    display: flex;
                    flex-direction: column;
                }}
                
                .document-modal-header {{
                    padding: 20px;
                    border-bottom: 1px solid #e2e8f0;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    background-color: #f8fafc;
                }}
                
                .document-modal-title {{
                    font-size: 1.25rem;
                    font-weight: 600;
                    color: #1a202c;
                }}
                
                .document-modal-close {{
                    background: none;
                    border: none;
                    font-size: 24px;
                    cursor: pointer;
                    color: #718096;
                    padding: 4px 8px;
                    border-radius: 4px;
                    transition: background-color 0.2s;
                }}
                
                .document-modal-close:hover {{
                    background-color: #e2e8f0;
                    color: #4a5568;
                }}
                
                .document-modal-body {{
                    flex: 1;
                    padding: 20px;
                    overflow-y: auto;
                    line-height: 1.6;
                }}
                
                .document-modal-body h2 {{
                    color: #2d3748;
                    margin-top: 24px;
                    margin-bottom: 12px;
                }}
                
                .document-modal-body h3 {{
                    color: #4a5568;
                    margin-top: 20px;
                    margin-bottom: 10px;
                }}
                
                .document-modal-body p {{
                    margin-bottom: 12px;
                    color: #2d3748;
                }}
                
                .document-modal-body ul {{
                    margin-bottom: 12px;
                    padding-left: 20px;
                }}
                
                .document-modal-body li {{
                    margin-bottom: 4px;
                }}
                
                .document-modal-footer {{
                    padding: 16px 20px;
                    border-top: 1px solid #e2e8f0;
                    background-color: #f8fafc;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }}
                
                .document-meta {{
                    font-size: 14px;
                    color: #718096;
                }}
                
                /* Animation for modal */
                .document-modal.show {{
                    display: block;
                    animation: fadeIn 0.3s ease;
                }}
                
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
                
                .document-modal-content.show {{
                    animation: slideInFromTop 0.3s ease;
                }}
                
                @keyframes slideInFromTop {{
                    from {{
                        transform: translateY(-50px);
                        opacity: 0;
                    }}
                    to {{
                        transform: translateY(0);
                        opacity: 1;
                    }}
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
                        <button id="table-view-btn" onclick="switchView('table')">Table View</button>
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
                    
                    <!-- Table View -->
                    <div id="table-view-content" class="facts-content" style="display: none;">
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
                
                <!-- Document Preview Modal -->
                <div id="document-modal" class="document-modal">
                    <div class="document-modal-content">
                        <div class="document-modal-header">
                            <div class="document-modal-title" id="modal-title">Document Preview</div>
                            <button class="document-modal-close" onclick="closeDocumentModal()">&times;</button>
                        </div>
                        <div class="document-modal-body" id="modal-body">
                            <!-- Document content will be inserted here -->
                        </div>
                        <div class="document-modal-footer">
                            <div class="document-meta" id="modal-meta">
                                <!-- Document metadata will be inserted here -->
                            </div>
                            <button class="action-button" onclick="openInNewTab()">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                    <polyline points="15 3 21 3 21 9"></polyline>
                                    <line x1="10" y1="14" x2="21" y2="3"></line>
                                </svg>
                                Open in New Tab
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            
            <script>
                // Initialize data - ensure all views use the same core data structure
                const factsData = {facts_json};
                const documentSets = {document_sets_json};
                const timelineData = {timeline_json};
                const documentContent = {document_content_json};
                
                // Document preview functionality
                function openDocumentPreview(documentName) {{
                    const modal = document.getElementById('document-modal');
                    const modalTitle = document.getElementById('modal-title');
                    const modalBody = document.getElementById('modal-body');
                    const modalMeta = document.getElementById('modal-meta');
                    
                    // Find document content
                    const docContent = documentContent[documentName];
                    
                    if (!docContent) {{
                        alert('Document content not available for: ' + documentName);
                        return;
                    }}
                    
                    // Set modal content
                    modalTitle.textContent = docContent.title;
                    modalBody.innerHTML = docContent.content;
                    modalMeta.innerHTML = `Pages: ${{docContent.pages}} | Document: ${{docContent.title}}`;
                    
                    // Show modal with animation
                    modal.classList.add('show');
                    modal.querySelector('.document-modal-content').classList.add('show');
                    
                    // Prevent body scroll
                    document.body.style.overflow = 'hidden';
                }}
                
                function closeDocumentModal() {{
                    const modal = document.getElementById('document-modal');
                    modal.classList.remove('show');
                    modal.querySelector('.document-modal-content').classList.remove('show');
                    
                    // Restore body scroll
                    document.body.style.overflow = 'auto';
                }}
                
                function openInNewTab() {{
                    const modalTitle = document.getElementById('modal-title');
                    const modalBody = document.getElementById('modal-body');
                    
                    // Create new window with document content
                    const newWindow = window.open('', '_blank');
                    newWindow.document.write(`
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <title>${{modalTitle.textContent}}</title>
                            <style>
                                body {{
                                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                                    line-height: 1.6;
                                    max-width: 800px;
                                    margin: 0 auto;
                                    padding: 40px 20px;
                                    color: #2d3748;
                                }}
                                h2 {{ color: #2d3748; margin-top: 32px; margin-bottom: 16px; }}
                                h3 {{ color: #4a5568; margin-top: 24px; margin-bottom: 12px; }}
                                p {{ margin-bottom: 16px; }}
                                ul {{ margin-bottom: 16px; padding-left: 24px; }}
                                li {{ margin-bottom: 8px; }}
                                strong {{ color: #1a202c; }}
                            </style>
                        </head>
                        <body>
                            <h1>${{modalTitle.textContent}}</h1>
                            ${{modalBody.innerHTML}}
                        </body>
                        </html>
                    `);
                    newWindow.document.close();
                }}
                
                // Close modal when clicking outside
                window.onclick = function(event) {{
                    const modal = document.getElementById('document-modal');
                    if (event.target === modal) {{
                        closeDocumentModal();
                    }}
                }}
                
                // Close modal with Escape key
                document.addEventListener('keydown', function(event) {{
                    if (event.key === 'Escape') {{
                        closeDocumentModal();
                    }}
                }});
                
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
                
                // Function to create document links
                function createDocumentLink(documentName) {{
                    if (!documentName || documentName === 'N/A') {{
                        return documentName || 'N/A';
                    }}
                    
                    // Check if document exists in our content
                    if (documentContent[documentName]) {{
                        return `<span class="document-link" onclick="openDocumentPreview('${{documentName}}')">${{documentName}}</span>`;
                    }}
                    
                    // If not found, return as regular text
                    return documentName;
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
                
                // Switch view between table, card, timeline, and document sets
                function switchView(viewType) {{
                    const tableBtn = document.getElementById('table-view-btn');
                    const cardBtn = document.getElementById('card-view-btn');
                    const timelineBtn = document.getElementById('timeline-view-btn');
                    const docsetBtn = document.getElementById('docset-view-btn');
                    
                    const tableContent = document.getElementById('table-view-content');
                    const cardContent = document.getElementById('card-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    // Remove active class from all buttons
                    tableBtn.classList.remove('active');
                    cardBtn.classList.remove('active');
                    timelineBtn.classList.remove('active');
                    docsetBtn.classList.remove('active');
                    
                    // Hide all content
                    tableContent.style.display = 'none';
                    cardContent.style.display = 'none';
                    timelineContent.style.display = 'none';
                    docsetContent.style.display = 'none';
                    
                    // Activate the selected view
                    if (viewType === 'card') {{
                        cardBtn.classList.add('active');
                        cardContent.style.display = 'block';
                        renderCardView();
                    }} else if (viewType === 'table') {{
                        tableBtn.classList.add('active');
                        tableContent.style.display = 'block';
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
                    const tableContent = document.getElementById('table-view-content');
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
                    }} else if (tableContent.style.display !== 'none') {{
                        // Copy table data
                        const table = document.querySelector('.table-view');
                        const headers = Array.from(table.querySelectorAll('th'))
                            .map(th => th.textContent.trim())
                            .join('\\t');
                        
                        contentToCopy += 'Case Facts\\n\\n';
                        contentToCopy += headers + '\\n';
                        
                        // Get rows
                        const rows = table.querySelectorAll('tbody tr');
                        rows.forEach(row => {{
                            const rowText = Array.from(row.querySelectorAll('td'))
                                .map(td => td.textContent.trim())
                                .join('\\t');
                            
                            contentToCopy += rowText + '\\n';
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
                            
                            // Get facts from this document
                            const tableFacts = container.querySelectorAll('tbody tr');
                            tableFacts.forEach(fact => {{
                                const cells = Array.from(fact.querySelectorAll('td'));
                                const date = cells[1] ? cells[1].textContent : '';
                                const event = cells[2] ? cells[2].textContent : '';
                                const claimantSub = cells[6] ? cells[6].textContent : '';
                                const respondentSub = cells[7] ? cells[7].textContent : '';
                                
                                contentToCopy += `- ${{date}} | ${{event}}\\n`;
                                if (claimantSub && claimantSub !== 'No submission') {{
                                    contentToCopy += `  Claimant: ${{claimantSub}}\\n`;
                                }}
                                if (respondentSub && respondentSub !== 'No submission') {{
                                    contentToCopy += `  Respondent: ${{respondentSub}}\\n`;
                                }}
                            }});
                            
                            contentToCopy += '\\n';
                        }});
                    }}
                    
                    // Create a temporary textarea to copy the content
                    const textarea = document.createElement('textarea');
                    textarea.value = contentToCopy;
                    document.body.appendChild(textarea);
                    textarea.select();
