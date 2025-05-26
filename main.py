import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

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
                        evidence_key = f"evidence_{i}_{j}"
                        if st.checkbox(f"📁 {evidence['id']}: {evidence['title']}", key=evidence_key):
                            st.markdown(f"*{evidence['summary']}*")
                else:
                    st.markdown("None")

# Main app
def main():
    # Get the data
    args_data = get_argument_data()
    facts_data = get_all_facts()
    
    # Add Streamlit sidebar with navigation buttons
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
    
    # Main content area
    if st.session_state.view == "Facts":
        # Create HTML tabs and cards container
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
                
                #streamlit-cards-container {{
                    margin-top: 20px;
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
                
                <div id="streamlit-cards-container">
                    <!-- Streamlit cards will be rendered here -->
                </div>
            </div>
            
            <script>
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
                    
                    // Send message to Streamlit (this would need a proper bridge)
                    // For now, we'll handle filtering in the Streamlit component
                    window.parent.postMessage({{
                        type: 'facts_filter_change',
                        filter: tabType
                    }}, '*');
                }}
            </script>
        </body>
        </html>
        """
        
        # Display HTML tabs
        components.html(html_content, height=150)
        
        # Filter facts based on current selection
        if st.session_state.facts_filter == "disputed":
            filtered_facts = [fact for fact in facts_data if fact['isDisputed']]
        elif st.session_state.facts_filter == "undisputed":
            filtered_facts = [fact for fact in facts_data if not fact['isDisputed']]
        else:
            filtered_facts = facts_data
        
        # Sort facts by date
        filtered_facts.sort(key=lambda x: x['date'].split('-')[0])
        
        # Add buttons for manual tab switching (since HTML->Streamlit communication is limited)
        st.markdown("**Filter Facts:**")
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("All Facts", key="all_facts_sync", use_container_width=True):
                st.session_state.facts_filter = "all"
                st.rerun()
        
        with col2:
            if st.button("Disputed Facts", key="disputed_facts_sync", use_container_width=True):
                st.session_state.facts_filter = "disputed"
                st.rerun()
        
        with col3:
            if st.button("Undisputed Facts", key="undisputed_facts_sync", use_container_width=True):
                st.session_state.facts_filter = "undisputed"
                st.rerun()
        
        st.markdown("---")
        
        # Render facts using native Streamlit components
        render_streamlit_cards(filtered_facts, args_data)
    
    elif st.session_state.view == "Arguments":
        st.title("Arguments")
        st.write("Arguments view would be implemented here.")
    
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.write("Exhibits view would be implemented here.")

if __name__ == "__main__":
    main()
