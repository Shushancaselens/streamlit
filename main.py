import streamlit as st
import json
import pandas as pd
import base64
from datetime import datetime

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'facts_filter' not in st.session_state:
    st.session_state.facts_filter = "All Facts"
if 'display_mode' not in st.session_state:
    st.session_state.display_mode = "Card View"

# Create data structures
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

# Get all facts from the data
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
            'parties_involved': list(set(group['parties_involved']))
        }
        enhanced_facts.append(enhanced_fact)
    
    return enhanced_facts

# Get document sets
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
            "name": "Provisional Measures",
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
            "name": "Admissibility",
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
            "name": "Challenge",
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

# Helper function to create CSV download link
def get_csv_download_link(df, filename="data.csv"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" target="_blank">Download CSV</a>'
    return href

# Helper function to get evidence details
def get_evidence_details(exhibits, args_data):
    evidence_details = []
    for exhibit_id in exhibits:
        # Search through all arguments to find evidence details
        def find_evidence(args):
            for arg_key in args:
                arg = args[arg_key]
                if 'evidence' in arg and arg['evidence']:
                    evidence = next((e for e in arg['evidence'] if e['id'] == exhibit_id), None)
                    if evidence:
                        return evidence
                if 'children' in arg and arg['children']:
                    child_evidence = find_evidence(arg['children'])
                    if child_evidence:
                        return child_evidence
            return None
        
        # Look in both claimant and respondent args
        evidence = find_evidence(args_data['claimantArgs']) or find_evidence(args_data['respondentArgs'])
        
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

# Main app
def main():
    # Sidebar with logo and navigation
    with st.sidebar:
        # Logo and title
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#whatsapp-mask)">
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Legal Analysis")
        
        # Navigation buttons
        if st.button("📑 Arguments", use_container_width=True):
            st.session_state.view = "Arguments"
        if st.button("📊 Facts", use_container_width=True):
            st.session_state.view = "Facts"
        if st.button("📁 Exhibits", use_container_width=True):
            st.session_state.view = "Exhibits"

    # Main content area
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # Get data
        facts_data = get_all_facts()
        args_data = get_argument_data()
        document_sets = get_document_sets()
        
        # Control section with native Streamlit components
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            # Facts filter dropdown
            facts_filter = st.selectbox(
                "Filter Facts:",
                ["All Facts", "Disputed Facts", "Undisputed Facts"],
                key="facts_filter_select"
            )
            st.session_state.facts_filter = facts_filter
        
        with col2:
            # Display mode dropdown
            display_mode = st.selectbox(
                "Display Mode:",
                ["Card View", "Table View", "Timeline View", "Document Categories"],
                key="display_mode_select"
            )
            st.session_state.display_mode = display_mode
        
        with col3:
            # Export options
            export_option = st.selectbox(
                "Export:",
                ["Select Export", "CSV", "JSON"],
                key="export_select"
            )
            
            if export_option != "Select Export":
                if st.button("Download", key="download_btn"):
                    # Filter facts based on current filter
                    filtered_facts = facts_data
                    if facts_filter == "Disputed Facts":
                        filtered_facts = [f for f in facts_data if f['isDisputed']]
                    elif facts_filter == "Undisputed Facts":
                        filtered_facts = [f for f in facts_data if not f['isDisputed']]
                    
                    if export_option == "CSV":
                        # Create DataFrame for CSV export
                        df_data = []
                        for fact in filtered_facts:
                            evidence_text = ', '.join([f"{ex}" for ex in fact.get('exhibits', [])])
                            df_data.append({
                                'Date': fact['date'],
                                'Event': fact['event'],
                                'Source_Text': fact.get('source_text', ''),
                                'Page': fact.get('page', ''),
                                'Document': fact.get('doc_name', ''),
                                'Doc_Summary': fact.get('doc_summary', ''),
                                'Claimant_Submission': fact.get('claimant_submission', 'No submission'),
                                'Respondent_Submission': fact.get('respondent_submission', 'No submission'),
                                'Status': 'Disputed' if fact['isDisputed'] else 'Undisputed',
                                'Evidence': evidence_text
                            })
                        
                        df = pd.DataFrame(df_data)
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv,
                            file_name=f"facts_{facts_filter.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
                            mime="text/csv"
                        )
                    
                    elif export_option == "JSON":
                        json_data = json.dumps(filtered_facts, indent=2)
                        st.download_button(
                            label="📥 Download JSON",
                            data=json_data,
                            file_name=f"facts_{facts_filter.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.json",
                            mime="application/json"
                        )
        
        st.divider()
        
        # Filter facts based on selection
        filtered_facts = facts_data
        if facts_filter == "Disputed Facts":
            filtered_facts = [f for f in facts_data if f['isDisputed']]
        elif facts_filter == "Undisputed Facts":
            filtered_facts = [f for f in facts_data if not f['isDisputed']]
        
        # Sort facts by date
        try:
            filtered_facts.sort(key=lambda x: datetime.strptime(x['date'].split('-')[0], '%Y') 
                              if x['date'] and x['date'] != 'present' 
                              else datetime.now())
        except:
            # Fallback sorting if date parsing fails
            filtered_facts.sort(key=lambda x: x['date'])
        
        # Display content based on selected mode
        if display_mode == "Card View":
            st.subheader(f"{facts_filter} - Card View")
            
            if not filtered_facts:
                st.info("No facts found matching the selected criteria.")
            else:
                for i, fact in enumerate(filtered_facts):
                    # Create expandable card for each fact
                    status_badge = "🔴 Disputed" if fact['isDisputed'] else "✅ Undisputed"
                    party_badges = " | ".join(fact.get('parties_involved', []))
                    
                    with st.expander(f"**{fact['date']}** - {fact['event']} ({status_badge})", expanded=False):
                        # Basic information
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write("**Document Information:**")
                            st.write(f"📄 **Document:** {fact.get('doc_name', 'N/A')}")
                            if fact.get('page'):
                                st.write(f"📖 **Page:** {fact['page']}")
                            st.write(f"⚖️ **Argument:** {fact.get('argId', '')}.{fact.get('argTitle', '')}")
                            if fact.get('paragraphs'):
                                st.write(f"📋 **Paragraphs:** {fact['paragraphs']}")
                        
                        with col2:
                            st.write("**Case Information:**")
                            st.write(f"👥 **Parties:** {party_badges}")
                            st.write(f"📍 **Status:** {status_badge}")
                            if fact.get('exhibits'):
                                st.write(f"📎 **Evidence:** {len(fact['exhibits'])} items")
                        
                        # Source text
                        if fact.get('source_text') and fact['source_text'] != 'No specific submission recorded':
                            st.write("**Source Text:**")
                            st.info(fact['source_text'])
                        
                        # Submissions
                        sub_col1, sub_col2 = st.columns(2)
                        
                        with sub_col1:
                            if fact.get('claimant_submission') and fact['claimant_submission'] != 'No specific submission recorded':
                                st.write("**🔵 Claimant Submission:**")
                                st.success(fact['claimant_submission'])
                        
                        with sub_col2:
                            if fact.get('respondent_submission') and fact['respondent_submission'] != 'No specific submission recorded':
                                st.write("**🔴 Respondent Submission:**")
                                st.error(fact['respondent_submission'])
                        
                        # Document summary
                        if fact.get('doc_summary'):
                            st.write("**Document Summary:**")
                            st.caption(fact['doc_summary'])
                        
                        # Evidence details
                        if fact.get('exhibits'):
                            st.write("**Evidence Details:**")
                            evidence_details = get_evidence_details(fact['exhibits'], args_data)
                            
                            for evidence in evidence_details:
                                with st.expander(f"📎 {evidence['id']}: {evidence['title']}", expanded=False):
                                    st.write(evidence['summary'])
        
        elif display_mode == "Table View":
            st.subheader(f"{facts_filter} - Table View")
            
            if not filtered_facts:
                st.info("No facts found matching the selected criteria.")
            else:
                # Create DataFrame for table display
                table_data = []
                for fact in filtered_facts:
                    evidence_text = ', '.join([f"{ex}" for ex in fact.get('exhibits', [])])
                    parties_text = ', '.join(fact.get('parties_involved', []))
                    
                    table_data.append({
                        'Date': fact['date'],
                        'Event': fact['event'],
                        'Document': fact.get('doc_name', ''),
                        'Page': fact.get('page', ''),
                        'Parties': parties_text,
                        'Status': 'Disputed' if fact['isDisputed'] else 'Undisputed',
                        'Evidence': evidence_text,
                        'Source Text': fact.get('source_text', '')[:100] + "..." if len(fact.get('source_text', '')) > 100 else fact.get('source_text', '')
                    })
                
                df = pd.DataFrame(table_data)
                
                # Display with styling
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Date": st.column_config.TextColumn("Date", width="small"),
                        "Event": st.column_config.TextColumn("Event", width="large"),
                        "Document": st.column_config.TextColumn("Document", width="medium"),
                        "Page": st.column_config.TextColumn("Page", width="small"),
                        "Parties": st.column_config.TextColumn("Parties", width="small"),
                        "Status": st.column_config.TextColumn("Status", width="small"),
                        "Evidence": st.column_config.TextColumn("Evidence", width="medium"),
                        "Source Text": st.column_config.TextColumn("Source Text", width="large")
                    }
                )
        
        elif display_mode == "Timeline View":
            st.subheader(f"{facts_filter} - Timeline View")
            
            if not filtered_facts:
                st.info("No facts found matching the selected criteria.")
            else:
                # Group facts by year
                facts_by_year = {}
                for fact in filtered_facts:
                    try:
                        year = fact['date'].split('-')[0] if fact['date'] != 'present' else '2024'
                        if year not in facts_by_year:
                            facts_by_year[year] = []
                        facts_by_year[year].append(fact)
                    except:
                        if 'Unknown' not in facts_by_year:
                            facts_by_year['Unknown'] = []
                        facts_by_year['Unknown'].append(fact)
                
                # Display timeline
                for year in sorted(facts_by_year.keys()):
                    st.markdown(f"## 📅 {year}")
                    
                    for fact in facts_by_year[year]:
                        status_icon = "🔴" if fact['isDisputed'] else "✅"
                        
                        with st.container():
                            st.markdown(f"""
                            <div style="border-left: 4px solid {'#ff4444' if fact['isDisputed'] else '#44ff44'}; 
                                        padding-left: 15px; margin: 10px 0; background-color: {'rgba(255,68,68,0.1)' if fact['isDisputed'] else 'rgba(68,255,68,0.1)'}; 
                                        border-radius: 5px; padding: 10px;">
                                <h4>{status_icon} {fact['date']} - {fact['event']}</h4>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Show details in expander
                            with st.expander("View Details", expanded=False):
                                if fact.get('source_text') and fact['source_text'] != 'No specific submission recorded':
                                    st.write("**Source:**")
                                    st.info(fact['source_text'])
                                
                                col1, col2 = st.columns(2)
                                with col1:
                                    if fact.get('claimant_submission') and fact['claimant_submission'] != 'No specific submission recorded':
                                        st.write("**🔵 Claimant:**")
                                        st.success(fact['claimant_submission'])
                                
                                with col2:
                                    if fact.get('respondent_submission') and fact['respondent_submission'] != 'No specific submission recorded':
                                        st.write("**🔴 Respondent:**")
                                        st.error(fact['respondent_submission'])
                                
                                if fact.get('exhibits'):
                                    st.write(f"**📎 Evidence:** {', '.join(fact['exhibits'])}")
        
        elif display_mode == "Document Categories":
            st.subheader(f"{facts_filter} - Document Categories")
            
            # Group facts by document category
            facts_by_category = {}
            
            for fact in filtered_facts:
                # Try to categorize based on document name
                category = "Other"
                doc_name = fact.get('doc_name', '').lower()
                
                if 'appeal' in doc_name:
                    category = "Appeal Documents"
                elif 'provisional' in doc_name or 'pm' in doc_name:
                    category = "Provisional Measures"
                elif 'admissibility' in doc_name:
                    category = "Admissibility Documents"
                elif 'challenge' in doc_name:
                    category = "Challenge Documents"
                
                if category not in facts_by_category:
                    facts_by_category[category] = []
                facts_by_category[category].append(fact)
            
            if not facts_by_category:
                st.info("No facts found matching the selected criteria.")
            else:
                # Display categories with native expanders
                for category, category_facts in facts_by_category.items():
                    with st.expander(f"📁 {category} ({len(category_facts)} facts)", expanded=True):
                        
                        if not category_facts:
                            st.info("No facts in this category.")
                            continue
                        
                        # Create mini table for each category
                        table_data = []
                        for fact in category_facts:
                            evidence_text = ', '.join([f"{ex}" for ex in fact.get('exhibits', [])])
                            
                            table_data.append({
                                'Date': fact['date'],
                                'Event': fact['event'][:80] + "..." if len(fact['event']) > 80 else fact['event'],
                                'Document': fact.get('doc_name', ''),
                                'Status': 'Disputed' if fact['isDisputed'] else 'Undisputed',
                                'Evidence': evidence_text
                            })
                        
                        if table_data:
                            df = pd.DataFrame(table_data)
                            st.dataframe(
                                df,
                                use_container_width=True,
                                hide_index=True,
                                column_config={
                                    "Date": st.column_config.TextColumn("Date", width="small"),
                                    "Event": st.column_config.TextColumn("Event", width="large"),
                                    "Document": st.column_config.TextColumn("Document", width="medium"),
                                    "Status": st.column_config.TextColumn("Status", width="small"),
                                    "Evidence": st.column_config.TextColumn("Evidence", width="medium")
                                }
                            )
        
        # Summary statistics
        st.divider()
        st.subheader("📊 Summary Statistics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Facts", len(facts_data))
        
        with col2:
            disputed_count = len([f for f in facts_data if f['isDisputed']])
            st.metric("Disputed Facts", disputed_count)
        
        with col3:
            undisputed_count = len([f for f in facts_data if not f['isDisputed']])
            st.metric("Undisputed Facts", undisputed_count)
        
        with col4:
            total_evidence = sum(len(f.get('exhibits', [])) for f in facts_data)
            st.metric("Total Evidence Items", total_evidence)

    elif st.session_state.view == "Arguments":
        st.title("Legal Arguments")
        st.info("Arguments view - Implementation pending")
        
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.info("Exhibits view - Implementation pending")

if __name__ == "__main__":
    main()
