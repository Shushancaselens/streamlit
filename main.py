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

# Function to display cards
def display_cards(filtered_facts, i_offset=0):
    if not filtered_facts:
        st.info("No facts found matching the selected criteria.")
    else:
        # Sort by date
        filtered_facts.sort(key=lambda x: x['date'].split('-')[0])
        
        # Render each fact as a card
        for i, fact in enumerate(filtered_facts):
            # Create card using expander as the main container
            with st.expander(f"**{fact['date']}** - {fact.get('doc_name', 'Unknown Document')}", expanded=False):
                
                # Event title inside the card
                st.subheader(fact['event'])
                st.write(f"**Exhibits:** {len(fact.get('exhibits', []))}")
                
                # Evidence section
                evidence_content = get_evidence_content(fact)
                
                if evidence_content:
                    st.subheader("📄 Evidence & References")
                    
                    for evidence in evidence_content:
                        st.write(f"**{evidence['id']} - {evidence['title']}**")
                        
                        if fact.get('doc_summary'):
                            st.info(f"**Document:** {fact['doc_summary']}")
                        
                        if fact.get('source_text'):
                            st.write(f"**Source:** {fact['source_text']}")
                        
                        st.write(f"**Summary:** {evidence['summary']}")
                        
                        # Reference info
                        st.write(f"**Reference:** Exhibit {evidence['id']}, Page {fact.get('page', 'N/A')}, Paragraphs {fact.get('paragraphs', 'N/A')}")
                        
                        # Action buttons
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button(f"Preview {evidence['id']}", key=f"preview_{evidence['id']}_{i}_{i_offset}"):
                                st.success(f"Opening {evidence['id']}")
                        with col2:
                            if st.button(f"Copy Reference", key=f"copy_{evidence['id']}_{i}_{i_offset}"):
                                st.success("Reference copied!")
                        
                        st.write("---")
                else:
                    st.info("No evidence available")
                
                # Party submissions
                st.subheader("📝 Party Submissions")
                
                st.write("**🔵 Claimant:**")
                claimant_text = fact.get('claimant_submission', 'No submission recorded')
                if claimant_text == 'No specific submission recorded':
                    st.write("*No submission provided*")
                else:
                    st.write(claimant_text)
                
                st.write("**🔴 Respondent:**")
                respondent_text = fact.get('respondent_submission', 'No submission recorded')
                if respondent_text == 'No specific submission recorded':
                    st.write("*No submission provided*")
                else:
                    st.write(respondent_text)
                
                # Status info
                st.subheader("ℹ️ Case Information")
                st.write(f"**Argument ID:** {fact.get('argId', 'N/A')}")
                st.write(f"**Paragraphs:** {fact.get('paragraphs', 'N/A')}")
                
                status = "Disputed" if fact['isDisputed'] else "Undisputed"
                if fact['isDisputed']:
                    st.error(f"Status: {status}")
                else:
                    st.success(f"Status: {status}")
            
            st.write("")  # Simple spacing between cards

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
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    document_sets_json = json.dumps(document_sets)
    
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
    
    # Create the facts HTML component with embedded Streamlit for card view
    if st.session_state.view == "Facts":
        # Create HTML component that handles navigation and renders streamlit content for card view
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
                
                /* Card view will be handled by Streamlit - placeholder */
                #card-view-content {{
                    min-height: 400px;
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
                    </div>
                    
                    <div class="facts-header">
                        <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                        <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                        <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                    </div>
                    
                    <!-- Card View - Will be handled by Streamlit -->
                    <div id="card-view-content" class="facts-content active">
                        <div id="streamlit-card-container"></div>
                    </div>
                    
                    <!-- Document Sets View -->
                    <div id="docset-view-content" class="facts-content" style="display: none;">
                        <div id="document-sets-container"></div>
                    </div>
                </div>
            </div>
            
            <script>
                // Initialize data
                const factsData = {facts_json};
                const documentSets = {document_sets_json};
                let currentTab = 'all';
                let currentView = 'card';
                
                // Communication with Streamlit
                function notifyStreamlit(action, data) {{
                    // This would communicate with Streamlit to trigger re-renders
                    console.log('Notify Streamlit:', action, data);
                    
                    // For now, we'll handle the JavaScript parts and let Streamlit handle card rendering
                    if (action === 'tab_change') {{
                        currentTab = data.tab;
                        if (currentView !== 'card') {{
                            if (currentView === 'docset') {{
                                renderDocumentSets(currentTab);
                            }}
                        }}
                    }} else if (action === 'view_change') {{
                        currentView = data.view;
                        // Streamlit will handle card view, we handle others
                    }}
                }}
                
                // Tab switching
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
                    
                    // Notify about tab change
                    notifyStreamlit('tab_change', {{ tab: tabType }});
                }}
                
                // View switching
                function switchView(viewType) {{
                    const cardBtn = document.getElementById('card-view-btn');
                    const docsetBtn = document.getElementById('docset-view-btn');
                    
                    const cardContent = document.getElementById('card-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    // Remove active class from all buttons
                    cardBtn.classList.remove('active');
                    docsetBtn.classList.remove('active');
                    
                    // Hide all content
                    cardContent.style.display = 'none';
                    docsetContent.style.display = 'none';
                    
                    // Activate the selected view
                    if (viewType === 'card') {{
                        cardBtn.classList.add('active');
                        cardContent.style.display = 'block';
                        // Streamlit will handle card rendering
                    }} else if (viewType === 'docset') {{
                        docsetBtn.classList.add('active');
                        docsetContent.style.display = 'block';
                        renderDocumentSets(currentTab);
                    }}
                    
                    // Notify about view change
                    notifyStreamlit('view_change', {{ view: viewType }});
                }}
                
                // Standardize data structure
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
                        evidence: fact.evidence || [],
                        parties_involved: fact.parties_involved || [],
                        argId: fact.argId || '',
                        argTitle: fact.argTitle || '',
                        paragraphs: fact.paragraphs || ''
                    }};
                }}
                
                // Get evidence content
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
                
                // Toggle evidence expansion
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
                
                // Copy reference function
                function copyReference(exhibitId, page, paragraphs) {{
                    let referenceText = `Exhibit: ${{exhibitId}}`;
                    if (page && page !== 'N/A') {{
                        referenceText += `, Page: ${{page}}`;
                    }}
                    if (paragraphs && paragraphs !== 'N/A') {{
                        referenceText += `, Paragraphs: ${{paragraphs}}`;
                    }}
                    
                    navigator.clipboard.writeText(referenceText).then(() => {{
                        const notification = document.getElementById('copy-notification');
                        notification.textContent = 'Reference copied to clipboard!';
                        notification.classList.add('show');
                        
                        setTimeout(() => {{
                            notification.classList.remove('show');
                            notification.textContent = 'Content copied to clipboard!';
                        }}, 2000);
                    }}).catch(() => {{
                        const textarea = document.createElement('textarea');
                        textarea.value = referenceText;
                        document.body.appendChild(textarea);
                        textarea.select();
                        document.execCommand('copy');
                        document.body.removeChild(textarea);
                        
                        const notification = document.getElementById('copy-notification');
                        notification.textContent = 'Reference copied to clipboard!';
                        notification.classList.add('show');
                        
                        setTimeout(() => {{
                            notification.classList.remove('show');
                            notification.textContent = 'Content copied to clipboard!';
                        }}, 2000);
                    }});
                }}
                
                // Preview document function
                function previewDocument(exhibitId, documentTitle) {{
                    const notification = document.getElementById('copy-notification');
                    notification.textContent = `Opening preview for ${{exhibitId}}: ${{documentTitle}}`;
                    notification.classList.add('show');
                    
                    setTimeout(() => {{
                        notification.classList.remove('show');
                        notification.textContent = 'Content copied to clipboard!';
                    }}, 3000);
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
                
                // Export and copy functions
                function copyAllContent() {{
                    const notification = document.getElementById('copy-notification');
                    notification.classList.add('show');
                    setTimeout(() => {{ notification.classList.remove('show'); }}, 2000);
                }}
                
                function exportAsCsv() {{ alert("CSV export functionality would be implemented here"); }}
                function exportAsPdf() {{ alert("PDF export functionality would be implemented here"); }}
                function exportAsWord() {{ alert("Word export functionality would be implemented here"); }}
                
                // Render document sets view
                function renderDocumentSets(tabType = 'all') {{
                    const container = document.getElementById('document-sets-container');
                    container.innerHTML = '';
                    
                    let filteredFacts = factsData.map(standardizeFactData);
                    if (tabType === 'disputed') {{
                        filteredFacts = filteredFacts.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = filteredFacts.filter(fact => !fact.isDisputed);
                    }}
                    
                    const docsWithFacts = {{}};
                    
                    documentSets.forEach(ds => {{
                        if (ds.isGroup) {{
                            docsWithFacts[ds.id] = {{
                                docset: ds,
                                facts: []
                            }};
                        }}
                    }});
                    
                    // Distribute facts to categories
                    filteredFacts.forEach((fact, index) => {{
                        let factAssigned = false;
                        
                        documentSets.forEach(ds => {{
                            if (ds.isGroup && !factAssigned) {{
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
                            // Default assignment to first category
                            if (Object.keys(docsWithFacts).length > 0) {{
                                const firstKey = Object.keys(docsWithFacts)[0];
                                docsWithFacts[firstKey].facts.push(fact);
                            }}
                        }}
                    }});
                    
                    // Create document sets UI
                    Object.values(docsWithFacts).forEach(docWithFacts => {{
                        const docset = docWithFacts.docset;
                        const facts = docWithFacts.facts;
                        
                        const docsetEl = document.createElement('div');
                        docsetEl.className = 'docset-container';
                        
                        const headerHtml = `
                            <div class="docset-header" onclick="toggleDocSet('${{docset.id}}')">
                                <svg id="chevron-${{docset.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <svg class="folder-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                                </svg>
                                <span><strong>${{docset.name}}</strong></span>
                                <span style="margin-left: auto;">
                                    <span class="badge">${{facts.length}} facts</span>
                                </span>
                            </div>
                            <div id="docset-content-${{docset.id}}" class="docset-content">
                        `;
                        
                        let contentHtml = '';
                        
                        if (facts.length > 0) {{
                            contentHtml += '<div style="padding: 16px;">';
                            
                            facts.forEach((fact, factIndex) => {{
                                contentHtml += `
                                    <div style="border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
                                        <div style="padding: 16px; background-color: ${{fact.isDisputed ? 'rgba(229, 62, 62, 0.05)' : '#f8fafc'}};">
                                            <div style="display: flex; align-items: center; gap: 12px;">
                                                <div style="font-weight: 600; color: #2d3748; min-width: 120px;">${{fact.date}}</div>
                                                <div style="font-weight: 500; color: #1a202c; flex-grow: 1;">${{fact.event}}</div>
                                            </div>
                                        </div>
                                        <div style="padding: 20px; background-color: white;">
                                            <h4>Party Submissions</h4>
                                            <div style="background-color: rgba(49, 130, 206, 0.03); padding: 16px; border-radius: 6px; border-left: 4px solid #3182ce; margin: 10px 0;">
                                                <div style="font-weight: 600; color: #3182ce; margin-bottom: 6px;">CLAIMANT SUBMISSION</div>
                                                <div>${{fact.claimant_submission !== 'No specific submission recorded' ? fact.claimant_submission : '<em>No submission provided</em>'}}</div>
                                            </div>
                                            <div style="background-color: rgba(229, 62, 62, 0.03); padding: 16px; border-radius: 6px; border-left: 4px solid #e53e3e; margin: 10px 0;">
                                                <div style="font-weight: 600; color: #e53e3e; margin-bottom: 6px;">RESPONDENT SUBMISSION</div>
                                                <div>${{fact.respondent_submission !== 'No specific submission recorded' ? fact.respondent_submission : '<em>No submission provided</em>'}}</div>
                                            </div>
                                            <div style="margin-top: 16px;">
                                                <strong>Status:</strong> ${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}
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
                
                // Initialize
                document.addEventListener('DOMContentLoaded', function() {{
                    // Default to card view
                    currentView = 'card';
                    currentTab = 'all';
                }});
            </script>
        </body>
        </html>
        """
        
        # Add custom CSS to hide the HTML card content area since Streamlit will render it below
        st.markdown("""
        <style>
        #streamlit-card-container {
            display: none;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Render the main HTML component with navigation
        components.html(html_content, height=200, scrolling=False)
        
        # Initialize session state for current view if not exists
        if 'current_view' not in st.session_state:
            st.session_state.current_view = 'card'
        
        facts_data = get_all_facts()
        
        # Card view content using Streamlit native components
        
        if not filtered_facts:
            st.info("No facts found matching the selected criteria.")
        else:
            # Render each fact as a simple Streamlit card
            for i, fact in enumerate(filtered_facts):
                
                # Create card using expander as the main container
                with st.expander(f"**{fact['date']}** - {fact.get('doc_name', 'Unknown Document')}", expanded=False):
                    
                    # Event title inside the card
                    st.subheader(fact['event'])
                    st.write(f"**Exhibits:** {len(fact.get('exhibits', []))}")
                    
                    # Evidence section
                    evidence_content = get_evidence_content(fact)
                    
                    if evidence_content:
                        st.subheader("📄 Evidence & References")
                        
                        for evidence in evidence_content:
                            st.write(f"**{evidence['id']} - {evidence['title']}**")
                            
                            if fact.get('doc_summary'):
                                st.info(f"**Document:** {fact['doc_summary']}")
                            
                            if fact.get('source_text'):
                                st.write(f"**Source:** {fact['source_text']}")
                            
                            st.write(f"**Summary:** {evidence['summary']}")
                            
                            # Reference info
                            st.write(f"**Reference:** Exhibit {evidence['id']}, Page {fact.get('page', 'N/A')}, Paragraphs {fact.get('paragraphs', 'N/A')}")
                            
                            # Action buttons
                            col1, col2 = st.columns(2)
                            with col1:
                                if st.button(f"Preview {evidence['id']}", key=f"preview_{evidence['id']}_{i}"):
                                    st.success(f"Opening {evidence['id']}")
                            with col2:
                                if st.button(f"Copy Reference", key=f"copy_{evidence['id']}_{i}"):
                                    st.success("Reference copied!")
                            
                            st.write("---")
                    else:
                        st.info("No evidence available")
                    
                    # Party submissions
                    st.subheader("📝 Party Submissions")
                    
                    st.write("**🔵 Claimant:**")
                    claimant_text = fact.get('claimant_submission', 'No submission recorded')
                    if claimant_text == 'No specific submission recorded':
                        st.write("*No submission provided*")
                    else:
                        st.write(claimant_text)
                    
                    st.write("**🔴 Respondent:**")
                    respondent_text = fact.get('respondent_submission', 'No submission recorded')
                    if respondent_text == 'No specific submission recorded':
                        st.write("*No submission provided*")
                    else:
                        st.write(respondent_text)
                    
                    # Status info
                    st.subheader("ℹ️ Case Information")
                    st.write(f"**Argument ID:** {fact.get('argId', 'N/A')}")
                    st.write(f"**Paragraphs:** {fact.get('paragraphs', 'N/A')}")
                    
                    status = "Disputed" if fact['isDisputed'] else "Undisputed"
                    if fact['isDisputed']:
                        st.error(f"Status: {status}")
                    else:
                        st.success(f"Status: {status}")
                
                st.write("")  # Simple spacing between cards

if __name__ == "__main__":
    main()

