import streamlit as st
import json
import streamlit.components.v1 as components

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
            "children": {
                "1.1": {
                    "id": "1.1",
                    "title": "Club Name Analysis",
                    "paragraphs": "20-45",
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
                    ],
                    "children": {}
                },
                "1.2": {
                    "id": "1.2",
                    "title": "Club Colors Analysis",
                    "paragraphs": "46-65",
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
                    "children": {}
                }
            }
        }
    }
    
    respondent_args = {
        "1": {
            "id": "1",
            "title": "Sporting Succession Rebuttal",
            "paragraphs": "200-218",
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
            "children": {}
        }
    }
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args
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

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    facts_data = get_all_facts()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    
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
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
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
    
    # Create the Card View HTML component
    if st.session_state.view == "Facts":
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    line-height: 1.5;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    background-color: #fff;
                }}
                
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                
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
                
                .disputed-badge {{
                    background-color: rgba(229, 62, 62, 0.1);
                    color: #e53e3e;
                }}
                
                .section-title {{
                    font-size: 1.5rem;
                    font-weight: 600;
                    margin-bottom: 1rem;
                    padding-bottom: 0.5rem;
                    border-bottom: 1px solid #eaeaea;
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
            </style>
        </head>
        <body>
            <div class="container">
                <div class="section-title">Case Facts</div>
                
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <div id="card-facts-container"></div>
            </div>
            
            <script>
                const factsData = {facts_json};
                const args_data = {args_json};
                
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
                        parties_involved: fact.parties_involved || [],
                        argId: fact.argId || '',
                        argTitle: fact.argTitle || '',
                        paragraphs: fact.paragraphs || ''
                    }};
                }}
                
                function getEvidenceContent(fact) {{
                    if (!fact.exhibits || fact.exhibits.length === 0) {{
                        return 'None';
                    }}
                    
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
                
                function switchFactsTab(tabType) {{
                    const allBtn = document.getElementById('all-facts-btn');
                    const disputedBtn = document.getElementById('disputed-facts-btn');
                    const undisputedBtn = document.getElementById('undisputed-facts-btn');
                    
                    allBtn.classList.remove('active');
                    disputedBtn.classList.remove('active');
                    undisputedBtn.classList.remove('active');
                    
                    if (tabType === 'all') {{
                        allBtn.classList.add('active');
                    }} else if (tabType === 'disputed') {{
                        disputedBtn.classList.add('active');
                    }} else {{
                        undisputedBtn.classList.add('active');
                    }}
                    
                    renderCardView(tabType);
                }}
                
                function renderCardView(tabType = 'all') {{
                    const container = document.getElementById('card-facts-container');
                    container.innerHTML = '';
                    
                    let filteredFacts = factsData.map(standardizeFactData);
                    if (tabType === 'disputed') {{
                        filteredFacts = filteredFacts.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = filteredFacts.filter(fact => !fact.isDisputed);
                    }}
                    
                    filteredFacts.sort((a, b) => {{
                        const dateA = a.date.split('-')[0];
                        const dateB = b.date.split('-')[0];
                        return new Date(dateA) - new Date(dateB);
                    }});
                    
                    filteredFacts.forEach((fact, index) => {{
                        const cardContainer = document.createElement('div');
                        cardContainer.className = `card-fact-container${{fact.isDisputed ? ' disputed' : ''}}`;
                        
                        const headerEl = document.createElement('div');
                        headerEl.className = `card-fact-header${{fact.isDisputed ? ' disputed' : ''}}`;
                        headerEl.onclick = () => toggleCardFact(index);
                        
                        const titleEl = document.createElement('div');
                        titleEl.className = 'card-fact-title';
                        
                        const dateEl = document.createElement('div');
                        dateEl.className = 'card-fact-date';
                        dateEl.textContent = fact.date;
                        titleEl.appendChild(dateEl);
                        
                        const eventEl = document.createElement('div');
                        eventEl.className = 'card-fact-event';
                        eventEl.textContent = fact.event;
                        titleEl.appendChild(eventEl);
                        
                        headerEl.appendChild(titleEl);
                        
                        const badgesEl = document.createElement('div');
                        badgesEl.className = 'card-fact-badges';
                        
                        if (fact.parties_involved && fact.parties_involved.length > 0) {{
                            fact.parties_involved.forEach(party => {{
                                const partyBadge = document.createElement('span');
                                partyBadge.className = `badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                                partyBadge.textContent = party;
                                badgesEl.appendChild(partyBadge);
                            }});
                        }}
                        
                        if (fact.isDisputed) {{
                            const disputedBadge = document.createElement('span');
                            disputedBadge.className = 'badge disputed-badge';
                            disputedBadge.textContent = 'Disputed';
                            badgesEl.appendChild(disputedBadge);
                        }}
                        
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
                        
                        const contentEl = document.createElement('div');
                        contentEl.className = 'card-fact-content';
                        contentEl.id = `card-fact-content-${{index}}`;
                        
                        const detailsEl = document.createElement('div');
                        detailsEl.className = 'card-fact-details';
                        
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
                        
                        if (fact.source_text && fact.source_text !== 'No specific submission recorded') {{
                            const sourceTextEl = document.createElement('div');
                            sourceTextEl.className = 'card-source-text';
                            sourceTextEl.innerHTML = `
                                <div class="submission-header">Source Text</div>
                                <div>${{fact.source_text}}</div>
                            `;
                            contentEl.appendChild(sourceTextEl);
                        }}
                        
                        if (fact.claimant_submission && fact.claimant_submission !== 'No specific submission recorded') {{
                            const claimantSubmissionEl = document.createElement('div');
                            claimantSubmissionEl.className = 'card-source-text claimant-submission';
                            claimantSubmissionEl.innerHTML = `
                                <div class="submission-header">Claimant Submission</div>
                                <div>${{fact.claimant_submission}}</div>
                            `;
                            contentEl.appendChild(claimantSubmissionEl);
                        }}
                        
                        if (fact.respondent_submission && fact.respondent_submission !== 'No specific submission recorded') {{
                            const respondentSubmissionEl = document.createElement('div');
                            respondentSubmissionEl.className = 'card-source-text respondent-submission';
                            respondentSubmissionEl.innerHTML = `
                                <div class="submission-header">Respondent Submission</div>
                                <div>${{fact.respondent_submission}}</div>
                            `;
                            contentEl.appendChild(respondentSubmissionEl);
                        }}
                        
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
                        
                        const statusExhibitsEl = document.createElement('div');
                        statusExhibitsEl.className = 'card-fact-details';
                        statusExhibitsEl.style.marginTop = '16px';
                        
                        const statusSection = document.createElement('div');
                        statusSection.className = 'card-detail-section';
                        statusSection.innerHTML = `
                            <div class="card-detail-label">Status</div>
                            <div class="card-detail-value">${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}</div>
                        `;
                        statusExhibitsEl.appendChild(statusSection);
                        
                        const evidenceSection = document.createElement('div');
                        evidenceSection.className = 'card-detail-section';
                        const evidenceContent = getEvidenceContent(fact);
                        
                        if (evidenceContent === 'None') {{
                            evidenceSection.innerHTML = `
                                <div class="card-detail-label">Evidence</div>
                                <div class="card-detail-value">None</div>
                            `;
                        }} else {{
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
                                                <div style="font-size: 12px; color: #666; line-height: 1.4;">${{evidence.summary}}</div>
                                            </div>
                                        </div>
                                    `).join('')}}
                                </div>
                            `;
                        }}
                        statusExhibitsEl.appendChild(evidenceSection);
                        
                        contentEl.appendChild(statusExhibitsEl);
                        cardContainer.appendChild(contentEl);
                        container.appendChild(cardContainer);
                    }});
                    
                    if (filteredFacts.length === 0) {{
                        container.innerHTML = '<p style="text-align: center; padding: 40px; color: #718096;">No facts found matching the selected criteria.</p>';
                    }}
                }}
                
                // Initialize on page load
                renderCardView('all');
            </script>
        </body>
        </html>
        """
        
        st.title("Case Facts")
        components.html(html_content, height=800, scrolling=True)
    
    elif st.session_state.view == "Arguments":
        st.title("Arguments")
        st.write("Arguments view would be implemented here.")
    
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.write("Exhibits view would be implemented here.")

if __name__ == "__main__":
    main()
