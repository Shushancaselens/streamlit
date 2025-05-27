def render_timeline_view(filtered_facts=None):
    """Renders a timeline view of the facts"""
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    # Custom CSS for timeline view
    st.markdown("""
    <style>
    .timeline {
        position: relative;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .timeline::after {
        content: '';
        position: absolute;
        width: 4px;
        background-color: #e2e8f0;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -2px;
    }
    
    .timeline-container {
        position: relative;
        width: 50%;
        padding: 10px 40px;
        background-color: inherit;
        box-sizing: border-box;
    }
    
    .timeline-container.left {
        left: 0;
    }
    
    .timeline-container.right {
        left: 50%;
    }
    
    .timeline-container::after {
        content: '';
        position: absolute;
        width: 16px;
        height: 16px;
        background-color: white;
        border: 3px solid #ef4444;
        top: 25px;
        border-radius: 50%;
        z-index: 1;
    }
    
    .timeline-container.disputed::after {
        border-color: #ef4444;
        background-color: #ef4444;
    }
    
    .timeline-container.undisputed::after {
        border-color: #10b981;
        background-color: #10b981;
    }
    
    .timeline-container.left::after {
        right: -12px;
    }
    
    .timeline-container.right::after {
        left: -12px;
    }
    
    .timeline-content {
        padding: 15px;
        background-color: white;
        position: relative;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .timeline-content:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .timeline-date {
        font-weight: 600;
        font-size: 0.875rem;
        color: #4b5563;
        margin-bottom: 5px;
    }
    
    .timeline-title {
        font-weight: 600;
        margin-bottom: 10px;
        color: #1f2937;
    }
    
    .timeline-badge {
        display: inline-block;
        font-size: 0.75rem;
        padding: 2px 8px;
        border-radius: 9999px;
        font-weight: 500;
        margin-right: 5px;
    }
    
    .timeline-badge.disputed {
        background-color: rgba(239, 68, 68, 0.1);
        color: #ef4444;
    }
    
    .timeline-badge.undisputed {
        background-color: rgba(16, 185, 129, 0.1);
        color: #10b981;
    }
    
    @media screen and (max-width: 600px) {
        .timeline::after {
            left: 31px;
        }
        
        .timeline-container {
            width: 100%;
            padding-left: 70px;
            padding-right: 25px;
        }
        
        .timeline-container.right {
            left: 0%;
        }
        
        .timeline-container.left::after, .timeline-container.right::after {
            left: 22px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Render timeline
    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    
    for i, fact in enumerate(facts_data):
        # Determine if this fact should be on the left or right
        position = "left" if i % 2 == 0 else "right"
        status_class = "disputed" if fact["isDisputed"] else "undisputed"
        
        # Render timeline item
        st.markdown(f"""
        <div class="timeline-container {position} {status_class}">
            <div class="timeline-content">
                <div class="timeline-date">{fact["date"]}</div>
                <div class="timeline-title">{fact["event"]}</div>
                <div>
                    <span class="timeline-badge {status_class}">
                        {"Disputed" if fact["isDisputed"] else "Undisputed"}
                    </span>
                    <span class="timeline-badge">
                        {', '.join(fact.get('parties_involved', []))}
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <details>
                        <summary style="cursor:pointer; color:#4299e1;">View details</summary>
                        <div style="margin-top: 10px; padding: 10px; background-color: #f9fafb; border-radius: 6px;">
                            <p><strong>Source Text:</strong> <em>{fact.get('source_text', 'Not available')}</em></p>
                            <p><strong>Exhibits:</strong> {', '.join(fact.get('exhibits', ['None']))}</p>
                            <p><strong>Document:</strong> {fact.get('doc_name', 'Not specified')}</p>
                        </div>
                    </details>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"
if 'current_tab_type' not in st.session_state:
    st.session_state.current_tab_type = "all"

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
                'summary': evidence['summary'],
                'citations': evidence.get('citations', [])
            })
        else:
            evidence_content.append({
                'id': exhibit_id,
                'title': exhibit_id,
                'summary': 'Evidence details not available',
                'citations': []
            })
    
    return evidence_content

def open_preview_in_new_tab(document_id, page=None):
    """Opens a preview of the document in a new tab"""
    # In a real application, this would generate a URL to a document viewer
    # For demonstration purposes, we'll create a simple HTML page
    preview_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Document Preview - {document_id}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; }}
            .document-header {{ background: #f1f5f9; padding: 15px; border-radius: 8px; margin-bottom: 20px; }}
            .document-content {{ border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; }}
            .page-indicator {{ position: fixed; bottom: 20px; right: 20px; background: #4D68F9; color: white; 
                             padding: 8px 15px; border-radius: 20px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="document-header">
            <h2>Document Preview</h2>
            <p><strong>Exhibit:</strong> {document_id}</p>
            {f"<p><strong>Page:</strong> {page}</p>" if page else ""}
        </div>
        <div class="document-content">
            <h3>Sample Document Content</h3>
            <p>This is a preview of document {document_id}. In a real application, the actual document content would be displayed here.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at justo vel libero faucibus dapibus.</p>
            <!-- More content would appear here -->
        </div>
        {f'<div class="page-indicator">Page {page}</div>' if page else ''}
    </body>
    </html>
    """
    
    # Encode the HTML as a data URI
    encoded_html = base64.b64encode(preview_html.encode()).decode()
    
    # Create JavaScript to open a new tab with the preview
    js = f"""
    <script>
    (function() {{
        window.open("data:text/html;base64,{encoded_html}", "_blank");
    }})();
    </script>
    """
    
    # Use Streamlit components to inject the JavaScript
    components.html(js, height=0, width=0)

def render_streamlit_card_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    # Custom CSS for improved information hierarchy
    st.markdown("""
    <style>
    .evidence-container {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        background-color: #f8fafc;
    }
    .evidence-header {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
    }
    .evidence-title {
        font-size: 16px;
        font-weight: 600;
        margin: 0;
        flex-grow: 1;
    }
    .evidence-id {
        display: inline-block;
        background-color: #4D68F9;
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        margin-right: 10px;
        font-weight: 600;
    }
    .evidence-summary {
        padding: 12px;
        background-color: white;
        border-radius: 6px;
        border-left: 4px solid #4D68F9;
        margin-bottom: 12px;
    }
    .source-text {
        padding: 12px;
        background-color: #eff6ff;
        border-radius: 6px;
        border-left: 4px solid #3b82f6;
        font-style: italic;
        margin-bottom: 12px;
    }
    .doc-summary {
        padding: 12px;
        background-color: #f0f9ff;
        border-radius: 6px;
        border-left: 4px solid #0ea5e9;
        margin-bottom: 12px;
    }
    .reference-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f1f5f9;
        padding: 8px 12px;
        border-radius: 6px;
    }
    .button-container {
        display: flex;
        gap: 8px;
    }
    /* Adjusted section headers to be smaller */
    .section-header {
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #475569;
    }
    .subsection-header {
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 8px;
        color: #64748b;
    }
    </style>
    """, unsafe_allow_html=True)
    
    for i, fact in enumerate(facts_data):
        expander_title = f"**{fact['date']}** - {fact['event']}"
        if fact['isDisputed']:
            expander_title += " 🔴"
        
        with st.expander(expander_title, expanded=False):
            st.markdown('<div class="section-header">Evidence & Source References</div>', unsafe_allow_html=True)
            evidence_content = get_evidence_content(fact)
            
            if evidence_content:
                for evidence in evidence_content:
                    # Use HTML for better formatted evidence container
                    st.markdown(f"""
                    <div class="evidence-container">
                        <div class="evidence-header">
                            <span class="evidence-id">{evidence['id']}</span>
                            <span class="evidence-title">{evidence['title']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Evidence summary
                    st.markdown('<div class="subsection-header">Summary</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="evidence-summary">{evidence["summary"]}</div>', unsafe_allow_html=True)
                    
                    # Document info 
                    if fact.get('doc_summary'):
                        st.markdown('<div class="subsection-header">Document Context</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="doc-summary"><strong>Document:</strong> {fact["doc_name"]}<br><strong>Summary:</strong> {fact["doc_summary"]}</div>', unsafe_allow_html=True)
                    
                    # Source text
                    if fact.get('source_text'):
                        st.markdown('<div class="subsection-header">Source Text</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="source-text">{fact["source_text"]}</div>', unsafe_allow_html=True)
                    
                    # Reference information and buttons
                    st.markdown('<div class="subsection-header">Reference Details</div>', unsafe_allow_html=True)
                    col1, col2 = st.columns([3, 2])
                    
                    with col1:
                        ref_details = []
                        ref_details.append(f"**Exhibit:** {evidence['id']}")
                        if fact.get('page'):
                            ref_details.append(f"**Page:** {fact['page']}")
                        if fact.get('paragraphs'):
                            ref_details.append(f"**Paragraphs:** {fact['paragraphs']}")
                        if evidence.get('citations'):
                            ref_details.append(f"**Citations:** {', '.join(evidence['citations'])}")
                        
                        st.markdown(" | ".join(ref_details))
                    
                    with col2:
                        current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                        copy_key = f"copy_card_{evidence['id']}_{i}_{current_tab}"
                        preview_key = f"preview_card_{evidence['id']}_{i}_{current_tab}"
                        
                        col_copy, col_preview = st.columns(2)
                        
                        with col_copy:
                            if st.button("Copy", key=copy_key, use_container_width=True):
                                ref_copy = f"Exhibit: {evidence['id']}"
                                if fact.get('page'):
                                    ref_copy += f", Page: {fact['page']}"
                                if fact.get('paragraphs'):
                                    ref_copy += f", Paragraphs: {fact['paragraphs']}"
                                st.success("Reference copied!")
                        
                        with col_preview:
                            if st.button("Preview", key=preview_key, use_container_width=True):
                                open_preview_in_new_tab(evidence['id'], fact.get('page'))
                    
                    st.divider()
            else:
                st.info("*No evidence references available for this fact*")
            
            st.markdown('<div class="section-header">Party Submissions</div>', unsafe_allow_html=True)
            
            st.markdown("**🔵 Claimant Submission**")
            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
            if claimant_text == 'No specific submission recorded':
                st.markdown("*No submission provided*")
            else:
                st.info(claimant_text)
            
            st.markdown("**🔴 Respondent Submission**")
            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
            if respondent_text == 'No specific submission recorded':
                st.markdown("*No submission provided*")
            else:
                st.warning(respondent_text)
            
            st.markdown('<div class="section-header">Status</div>', unsafe_allow_html=True)
            status_col1, status_col2 = st.columns(2)
            
            with status_col1:
                if fact['isDisputed']:
                    st.error("**Status:** Disputed")
                else:
                    st.success("**Status:** Undisputed")
            
            with status_col2:
                if fact.get('parties_involved'):
                    st.markdown(f"**Parties:** {', '.join(fact['parties_involved'])}")

def render_streamlit_table_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    table_data = []
    for fact in facts_data:
        table_data.append({
            'Date': fact['date'],
            'Event': fact['event'],
            'Status': '🔴 Disputed' if fact['isDisputed'] else '🟢 Undisputed',
            'Parties': ', '.join(fact.get('parties_involved', [])),
            'Exhibits': ', '.join(fact.get('exhibits', [])),
            'Page': fact.get('page', ''),
            'Document': fact.get('doc_name', '')
        })
    
    df = pd.DataFrame(table_data)
    
    st.dataframe(
        df,
        use_container_width=True,
        height=600,
        column_config={
            'Date': st.column_config.TextColumn('Date', width=120),
            'Event': st.column_config.TextColumn('Event', width=300),
            'Status': st.column_config.TextColumn('Status', width=120),
            'Parties': st.column_config.TextColumn('Parties', width=150),
            'Exhibits': st.column_config.TextColumn('Exhibits', width=120),
            'Page': st.column_config.TextColumn('Page', width=80),
            'Document': st.column_config.TextColumn('Document', width=200)
        }
    )

def render_streamlit_docset_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
        
    document_sets = get_document_sets()
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    # Custom CSS for improved information hierarchy
    st.markdown("""
    <style>
    .evidence-container {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        background-color: #f8fafc;
    }
    .evidence-header {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
    }
    .evidence-title {
        font-size: 16px;
        font-weight: 600;
        margin: 0;
        flex-grow: 1;
    }
    .evidence-id {
        display: inline-block;
        background-color: #4D68F9;
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        margin-right: 10px;
        font-weight: 600;
    }
    .evidence-summary {
        padding: 12px;
        background-color: white;
        border-radius: 6px;
        border-left: 4px solid #4D68F9;
        margin-bottom: 12px;
    }
    .source-text {
        padding: 12px;
        background-color: #eff6ff;
        border-radius: 6px;
        border-left: 4px solid #3b82f6;
        font-style: italic;
        margin-bottom: 12px;
    }
    .doc-summary {
        padding: 12px;
        background-color: #f0f9ff;
        border-radius: 6px;
        border-left: 4px solid #0ea5e9;
        margin-bottom: 12px;
    }
    .docset-fact-header {
        display: flex;
        align-items: center;
        padding: 8px 12px;
        background-color: #f1f5f9;
        border-radius: 6px;
        margin-bottom: 12px;
    }
    .reference-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f1f5f9;
        padding: 8px 12px;
        border-radius: 6px;
    }
    .button-container {
        display: flex;
        gap: 8px;
    }
    /* Adjusted section headers to be smaller */
    .section-header {
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #475569;
    }
    .subsection-header {
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 8px;
        color: #64748b;
    }
    </style>
    """, unsafe_allow_html=True)
    
    docs_with_facts = {}
    
    for ds in document_sets:
        if ds.get('isGroup'):
            docs_with_facts[ds['id']] = {
                'docset': ds,
                'facts': []
            }
    
    for fact in facts_data:
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
    
    for docset_id, doc_with_facts in docs_with_facts.items():
        docset = doc_with_facts['docset']
        facts = doc_with_facts['facts']
        
        party_color = ("🔵" if docset['party'] == 'Appellant' else 
                      "🔴" if docset['party'] == 'Respondent' else "⚪")
        
        with st.expander(f"📁 {party_color} **{docset['name']}** ({len(facts)} facts)", expanded=False):
            if facts:
                for i, fact in enumerate(facts):
                    with st.container():
                        # Fact header with improved styling
                        st.markdown(f"""
                        <div class="docset-fact-header">
                            <div style="width:20%; font-weight:bold;">{fact['date']}</div>
                            <div style="width:70%; font-weight:bold;">{fact['event']}</div>
                            <div style="width:10%; text-align:right;">
                                {"🔴" if fact['isDisputed'] else "🟢"}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        with st.container():
                            st.markdown('<div class="section-header">Evidence & Source References</div>', unsafe_allow_html=True)
                            evidence_content = get_evidence_content(fact)
                            
                            if evidence_content:
                                for evidence_idx, evidence in enumerate(evidence_content):
                                    # Use HTML for better formatted evidence container
                                    st.markdown(f"""
                                    <div class="evidence-container">
                                        <div class="evidence-header">
                                            <span class="evidence-id">{evidence['id']}</span>
                                            <span class="evidence-title">{evidence['title']}</span>
                                        </div>
                                    </div>
                                    """, unsafe_allow_html=True)
                                    
                                    # Evidence summary
                                    st.markdown('<div class="subsection-header">Summary</div>', unsafe_allow_html=True)
                                    st.markdown(f'<div class="evidence-summary">{evidence["summary"]}</div>', unsafe_allow_html=True)
                                    
                                    # Document info 
                                    if fact.get('doc_summary'):
                                        st.markdown('<div class="subsection-header">Document Context</div>', unsafe_allow_html=True)
                                        st.markdown(f'<div class="doc-summary"><strong>Document:</strong> {fact["doc_name"]}<br><strong>Summary:</strong> {fact["doc_summary"]}</div>', unsafe_allow_html=True)
                                    
                                    # Source text
                                    if fact.get('source_text'):
                                        st.markdown('<div class="subsection-header">Source Text</div>', unsafe_allow_html=True)
                                        st.markdown(f'<div class="source-text">{fact["source_text"]}</div>', unsafe_allow_html=True)
                                    
                                    # Reference information and buttons
                                    st.markdown('<div class="subsection-header">Reference Details</div>', unsafe_allow_html=True)
                                    col1, col2 = st.columns([3, 2])
                                    
                                    with col1:
                                        ref_details = []
                                        ref_details.append(f"**Exhibit:** {evidence['id']}")
                                        if fact.get('page'):
                                            ref_details.append(f"**Page:** {fact['page']}")
                                        if fact.get('paragraphs'):
                                            ref_details.append(f"**Paragraphs:** {fact['paragraphs']}")
                                        if evidence.get('citations'):
                                            ref_details.append(f"**Citations:** {', '.join(evidence['citations'])}")
                                        
                                        st.markdown(" | ".join(ref_details))
                                    
                                    with col2:
                                        current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                                        unique_copy_key = f"copy_docset_{docset_id}_{i}_{evidence_idx}_{evidence['id']}_{current_tab}"
                                        unique_preview_key = f"preview_docset_{docset_id}_{i}_{evidence_idx}_{evidence['id']}_{current_tab}"
                                        
                                        col_copy, col_preview = st.columns(2)
                                        
                                        with col_copy:
                                            if st.button("Copy", key=unique_copy_key, use_container_width=True):
                                                ref_copy = f"Exhibit: {evidence['id']}"
                                                if fact.get('page'):
                                                    ref_copy += f", Page: {fact['page']}"
                                                if fact.get('paragraphs'):
                                                    ref_copy += f", Paragraphs: {fact['paragraphs']}"
                                                st.success("Reference copied!")
                                        
                                        with col_preview:
                                            if st.button("Preview", key=unique_preview_key, use_container_width=True):
                                                open_preview_in_new_tab(evidence['id'], fact.get('page'))
                                    
                                    st.divider()
                            else:
                                st.info("*No evidence references available*")
                            
                            st.markdown('<div class="section-header">Party Submissions</div>', unsafe_allow_html=True)
                            
                            st.markdown("**🔵 Claimant Submission**")
                            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                            if claimant_text == 'No specific submission recorded':
                                st.markdown("*No submission provided*")
                            else:
                                st.info(claimant_text)
                            
                            st.markdown("**🔴 Respondent Submission**")
                            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                            if respondent_text == 'No specific submission recorded':
                                st.markdown("*No submission provided*")
                            else:
                                st.warning(respondent_text)
                        
                        if i < len(facts) - 1:
                            st.divider()
            else:
                st.info("No facts found in this document category.")

def render_view_content(view_type, filtered_facts):
    if view_type == "card":
        render_streamlit_card_view(filtered_facts)
    elif view_type == "table":
        render_streamlit_table_view(filtered_facts)
    elif view_type == "docset":
        render_streamlit_docset_view(filtered_facts)
    elif view_type == "timeline":
        render_timeline_view(filtered_facts)
    else:
        render_streamlit_card_view(filtered_facts)

def main():
    # Add Streamlit sidebar with navigation buttons
    with st.sidebar:
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
        
        st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
        
        # Custom CSS for sidebar button styling
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
        
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Create the facts view
    if st.session_state.view == "Facts":
        # Header with title and action buttons
        col_title, col_copy, col_export = st.columns([3, 1, 1])
        
        with col_title:
            st.title("Case Facts")
        
        with col_copy:
            if st.button("Copy", use_container_width=True, type="secondary"):
                st.success("Facts copied to clipboard!")
        
        with col_export:
            if st.button("Export", use_container_width=True, type="secondary"):
                st.success("Facts exported!")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Use the HTML-based view toggle
        html_view_toggle = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: transparent;
                }

                /* View toggle tabs styling */
                .view-toggle {
                    display: flex;
                    justify-content: center;
                    margin-bottom: 16px;
                }
                
                .view-toggle button {
                    padding: 8px 16px;
                    border: 1px solid #e2e8f0;
                    background-color: #f7fafc;
                    cursor: pointer;
                    font-size: 14px;
                    transition: all 0.2s ease;
                }
                
                .view-toggle button.active {
                    background-color: #ef4444;
                    color: white;
                    border-color: #ef4444;
                }
                
                .view-toggle button:hover:not(.active) {
                    background-color: #edf2f7;
                }
                
                .view-toggle button:first-child {
                    border-radius: 4px 0 0 4px;
                }
                
                .view-toggle button:nth-child(2) {
                    border-left: none;
                }
                
                .view-toggle button:nth-child(3) {
                    border-left: none;
                }
                
                .view-toggle button:last-child {
                    border-radius: 0 4px 4px 0;
                    border-left: none;
                }
            </style>
        </head>
        <body>
            <div class="view-toggle">
                <button id="card-view-btn" class="{}" onclick="switchView('card')">Card View</button>
                <button id="table-view-btn" class="{}" onclick="switchView('table')">Table View</button>
                <button id="docset-view-btn" class="{}" onclick="switchView('docset')">Document Categories</button>
                <button id="timeline-view-btn" class="{}" onclick="switchView('timeline')">Timeline View</button>
            </div>

            <script>
                // Switch view between tabs
                function switchView(viewType) {{
                    // Send the selected view to Streamlit
                    window.parent.postMessage({{
                        type: 'streamlit:setComponentValue',
                        value: viewType
                    }}, '*');
                }}
                
                // Initialize the active state based on current view
                document.addEventListener('DOMContentLoaded', function() {{
                    // This will be replaced by the formatted string
                }});
            </script>
        </body>
        </html>
        """.format(
            "active" if st.session_state.current_view_type == "card" else "",
            "active" if st.session_state.current_view_type == "table" else "",
            "active" if st.session_state.current_view_type == "docset" else "",
            "active" if st.session_state.current_view_type == "timeline" else ""
        )
        
        # Render the HTML component
        view_type = components.html(html_view_toggle, height=50)
        
        # Update the view type if the component returned a value
        if view_type and view_type != st.session_state.current_view_type:
            st.session_state.current_view_type = view_type
            st.rerun()
        
        # Facts filter using tabs - improved styling
        st.markdown("""
        <style>
        /* Improved tab styling with better spacing */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 40px;
            padding-top: 10px;
            padding-bottom: 10px;
            white-space: pre;
            margin-right: 10px;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: rgba(239, 68, 68, 0.1);
            border-bottom-color: #ef4444 !important;
        }
        
        /* Make tab panels have more space above them */
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
        
        with tab1:
            st.session_state.current_tab_type = "all"
            filtered_facts = get_all_facts()
            if st.session_state.current_view_type == 'timeline':
                render_timeline_view(filtered_facts)
            else:
                render_view_content(st.session_state.current_view_type, filtered_facts)
        
        with tab2:
            st.session_state.current_tab_type = "disputed"
            filtered_facts = [fact for fact in get_all_facts() if fact['isDisputed']]
            if st.session_state.current_view_type == 'timeline':
                render_timeline_view(filtered_facts)
            else:
                render_view_content(st.session_state.current_view_type, filtered_facts)
        
        with tab3:
            st.session_state.current_tab_type = "undisputed"
            filtered_facts = [fact for fact in get_all_facts() if not fact['isDisputed']]
            if st.session_state.current_view_type == 'timeline':
                render_timeline_view(filtered_facts)
            else:
                render_view_content(st.session_state.current_view_type, filtered_facts)

if __name__ == "__main__":
    main()
