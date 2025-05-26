import streamlit as st
import pandas as pd
import json
from datetime import datetime
import base64
import io

# Set page config
st.set_page_config(
    page_title="Legal Arguments Analysis", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .fact-card {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        background-color: white;
    }
    
    .fact-card.disputed {
        border-left: 4px solid #e53e3e;
        background-color: rgba(229, 62, 62, 0.02);
    }
    
    .badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 500;
        margin: 2px;
    }
    
    .appellant-badge {
        background-color: rgba(49, 130, 206, 0.1);
        color: #3182ce;
    }
    
    .respondent-badge {
        background-color: rgba(229, 62, 62, 0.1);
        color: #e53e3e;
    }
    
    .disputed-badge {
        background-color: rgba(229, 62, 62, 0.1);
        color: #e53e3e;
    }
    
    .evidence-badge {
        background-color: rgba(221, 107, 32, 0.1);
        color: #dd6b20;
    }
    
    .timeline-item {
        border-left: 4px solid #4299e1;
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    
    .timeline-item.disputed {
        border-left-color: #e53e3e;
    }
    
    .timeline-point {
        position: absolute;
        left: -8px;
        top: 10px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background-color: #4299e1;
    }
    
    .timeline-point.disputed {
        background-color: #e53e3e;
    }
    
    .submission-box {
        padding: 12px;
        border-radius: 6px;
        margin: 8px 0;
        border-left: 4px solid;
    }
    
    .claimant-submission {
        background-color: rgba(49, 130, 206, 0.03);
        border-left-color: #3182ce;
    }
    
    .respondent-submission {
        background-color: rgba(229, 62, 62, 0.03);
        border-left-color: #e53e3e;
    }
    
    .doc-info {
        background-color: #f8fafc;
        padding: 12px;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def get_argument_data():
    """Get the arguments data structure"""
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
                            ]
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
            ]
        }
    }
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args
    }

@st.cache_data
def get_all_facts():
    """Extract and standardize all facts from the argument data"""
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
                    'claimant_submission': point.get('source_text', '') if party == 'Appellant' else '',
                    'respondent_submission': point.get('source_text', '') if party == 'Respondent' else ''
                }
                facts.append(fact)
                
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    # Extract from claimant args
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Appellant')
        
    # Extract from respondent args
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
    
    # Enhance facts with both parties' submissions
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
        
        if fact['party'] == 'Appellant':
            fact_groups[key]['claimant_submission'] = fact['source_text']
        else:
            fact_groups[key]['respondent_submission'] = fact['source_text']
        
        fact_groups[key]['parties_involved'].append(fact['party'])
        
        if fact['isDisputed']:
            fact_groups[key]['isDisputed'] = True
    
    # Create enhanced facts
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

@st.cache_data
def get_timeline_data():
    """Get enhanced timeline data"""
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
            "source_text": "Athletic Club United achieved its first National Championship victory on May 20, 1955, defeating rivals 3-1 in the final match held at National Stadium, establishing the club's competitive credentials.",
            "page": 42,
            "doc_name": "Appeal Brief",
            "doc_summary": "Comprehensive brief supporting the appeal with detailed arguments and evidence regarding club continuity and identity.",
            "parties_involved": ["Appellant"]
        }
    ]
    
    # Sort events chronologically
    timeline_events.sort(key=lambda x: x['date'])
    return timeline_events

@st.cache_data
def get_document_sets():
    """Get document sets for categorization"""
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
        }
    ]

def get_evidence_details(exhibits, args_data):
    """Get detailed evidence information for given exhibit IDs"""
    if not exhibits:
        return []
    
    evidence_details = []
    
    def find_evidence(args, exhibit_id):
        for arg_key in args:
            arg = args[arg_key]
            if 'evidence' in arg:
                for evidence in arg['evidence']:
                    if evidence['id'] == exhibit_id:
                        return evidence
            if 'children' in arg:
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

def format_date(date_str):
    """Format date string for better display"""
    if '-' in date_str and len(date_str.split('-')) == 2:
        return date_str  # Range like "1975-1976"
    
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except:
        return date_str

def render_fact_card(fact, args_data):
    """Render a single fact as a card"""
    disputed_class = "disputed" if fact['isDisputed'] else ""
    
    with st.container():
        st.markdown(f'<div class="fact-card {disputed_class}">', unsafe_allow_html=True)
        
        # Header with date and status badges
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{format_date(fact['date'])}** - {fact['event']}")
        
        with col2:
            badge_html = ""
            for party in fact.get('parties_involved', []):
                badge_class = "appellant-badge" if party == "Appellant" else "respondent-badge"
                badge_html += f'<span class="badge {badge_class}">{party}</span>'
            
            if fact['isDisputed']:
                badge_html += '<span class="badge disputed-badge">Disputed</span>'
            
            st.markdown(badge_html, unsafe_allow_html=True)
        
        # Expandable details
        with st.expander("View Details", expanded=False):
            # Document information
            st.markdown('<div class="doc-info">', unsafe_allow_html=True)
            doc_col1, doc_col2 = st.columns(2)
            with doc_col1:
                st.markdown(f"**Document:** {fact.get('doc_name', 'N/A')}")
                st.markdown(f"**Page:** {fact.get('page', 'N/A')}")
            with doc_col2:
                st.markdown(f"**Argument:** {fact.get('argId', '')}. {fact.get('argTitle', '')}")
                st.markdown(f"**Paragraphs:** {fact.get('paragraphs', 'N/A')}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Document summary
            if fact.get('doc_summary'):
                st.markdown(f"**Document Summary:** {fact['doc_summary']}")
            
            # Source text
            if fact.get('source_text') and fact['source_text'] != 'No specific submission recorded':
                st.markdown("**Source Text:**")
                st.info(fact['source_text'])
            
            # Submissions
            if fact.get('claimant_submission') and fact['claimant_submission'] != 'No specific submission recorded':
                st.markdown("**Claimant Submission:**")
                st.markdown(f'<div class="submission-box claimant-submission">{fact["claimant_submission"]}</div>', 
                          unsafe_allow_html=True)
            
            if fact.get('respondent_submission') and fact['respondent_submission'] != 'No specific submission recorded':
                st.markdown("**Respondent Submission:**")
                st.markdown(f'<div class="submission-box respondent-submission">{fact["respondent_submission"]}</div>', 
                          unsafe_allow_html=True)
            
            # Evidence
            if fact.get('exhibits'):
                st.markdown("**Evidence:**")
                evidence_details = get_evidence_details(fact['exhibits'], args_data)
                for evidence in evidence_details:
                    with st.expander(f"📁 {evidence['id']}: {evidence['title']}", expanded=False):
                        st.write(evidence['summary'])
        
        st.markdown('</div>', unsafe_allow_html=True)

def render_timeline_item(fact, args_data):
    """Render a single timeline item"""
    disputed_class = "disputed" if fact['isDisputed'] else ""
    
    st.markdown(f'<div class="timeline-item {disputed_class}">', unsafe_allow_html=True)
    st.markdown(f'<div class="timeline-point {disputed_class}"></div>', unsafe_allow_html=True)
    
    # Date and badges
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"**{format_date(fact['date'])}**")
    with col2:
        badge_html = ""
        for party in fact.get('parties_involved', []):
            badge_class = "appellant-badge" if party == "Appellant" else "respondent-badge"
            badge_html += f'<span class="badge {badge_class}">{party}</span>'
        
        if fact['isDisputed']:
            badge_html += '<span class="badge disputed-badge">Disputed</span>'
        
        st.markdown(badge_html, unsafe_allow_html=True)
    
    # Event description
    st.markdown(f"**{fact['event']}**")
    
    # Document info
    st.markdown('<div class="doc-info">', unsafe_allow_html=True)
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.markdown(f"**Document:** {fact.get('doc_name', 'N/A')}")
        st.markdown(f"**Page:** {fact.get('page', 'N/A')}")
    with info_col2:
        st.markdown(f"**Argument:** {fact.get('argId', '')}. {fact.get('argTitle', '')}")
        st.markdown(f"**Paragraphs:** {fact.get('paragraphs', 'N/A')}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Submissions side by side
    if (fact.get('claimant_submission', 'No specific submission recorded') != 'No specific submission recorded' or
        fact.get('respondent_submission', 'No specific submission recorded') != 'No specific submission recorded'):
        
        sub_col1, sub_col2 = st.columns(2)
        
        with sub_col1:
            if fact.get('claimant_submission', 'No specific submission recorded') != 'No specific submission recorded':
                st.markdown("**Claimant Position:**")
                st.markdown(f'<div class="submission-box claimant-submission">{fact["claimant_submission"]}</div>', 
                          unsafe_allow_html=True)
        
        with sub_col2:
            if fact.get('respondent_submission', 'No specific submission recorded') != 'No specific submission recorded':
                st.markdown("**Respondent Position:**")
                st.markdown(f'<div class="submission-box respondent-submission">{fact["respondent_submission"]}</div>', 
                          unsafe_allow_html=True)
    
    # Evidence
    if fact.get('exhibits'):
        with st.expander(f"Evidence ({len(fact['exhibits'])} items)", expanded=False):
            evidence_details = get_evidence_details(fact['exhibits'], args_data)
            for evidence in evidence_details:
                st.markdown(f"**{evidence['id']}: {evidence['title']}**")
                st.write(evidence['summary'])
                st.markdown("---")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

def create_downloadable_csv(facts_df, filename="facts.csv"):
    """Create a downloadable CSV"""
    csv = facts_df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV</a>'
    return href

# Sidebar
with st.sidebar:
    # Logo and title
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
          <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
        </svg>
        <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Legal Analysis")
    
    # View selection
    view_option = st.radio(
        "Select View:",
        ["📊 Facts", "📑 Arguments", "📁 Exhibits"],
        index=0
    )

# Main content
if view_option == "📊 Facts":
    st.title("Case Facts")
    
    # Get data
    facts_data = get_all_facts()
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    
    # Filter options
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        fact_filter = st.selectbox(
            "Filter Facts:",
            ["All Facts", "Disputed Facts", "Undisputed Facts"]
        )
    
    with col2:
        view_type = st.selectbox(
            "View Type:",
            ["Card View", "Table View", "Timeline View", "Document Categories"]
        )
    
    with col3:
        if st.button("📥 Export CSV"):
            # Filter facts based on selection
            if fact_filter == "Disputed Facts":
                filtered_facts = [f for f in facts_data if f['isDisputed']]
            elif fact_filter == "Undisputed Facts":
                filtered_facts = [f for f in facts_data if not f['isDisputed']]
            else:
                filtered_facts = facts_data
            
            # Create DataFrame
            df_data = []
            for fact in filtered_facts:
                evidence_text = ', '.join([f"{ex}" for ex in fact.get('exhibits', [])])
                df_data.append({
                    'Date': fact['date'],
                    'Event': fact['event'],
                    'Source Text': fact.get('source_text', ''),
                    'Page': fact.get('page', ''),
                    'Document': fact.get('doc_name', ''),
                    'Doc Summary': fact.get('doc_summary', ''),
                    'Claimant Submission': fact.get('claimant_submission', 'No submission'),
                    'Respondent Submission': fact.get('respondent_submission', 'No submission'),
                    'Status': 'Disputed' if fact['isDisputed'] else 'Undisputed',
                    'Evidence': evidence_text
                })
            
            df = pd.DataFrame(df_data)
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download Facts CSV",
                data=csv,
                file_name=f"case_facts_{fact_filter.lower().replace(' ', '_')}.csv",
                mime="text/csv"
            )
    
    # Filter facts based on selection
    if fact_filter == "Disputed Facts":
        filtered_facts = [f for f in facts_data if f['isDisputed']]
        filtered_timeline = [f for f in timeline_data if f['isDisputed']]
    elif fact_filter == "Undisputed Facts":
        filtered_facts = [f for f in facts_data if not f['isDisputed']]
        filtered_timeline = [f for f in timeline_data if not f['isDisputed']]
    else:
        filtered_facts = facts_data
        filtered_timeline = timeline_data
    
    # Sort by date
    filtered_facts.sort(key=lambda x: x['date'])
    filtered_timeline.sort(key=lambda x: x['date'])
    
    # Render based on view type
    if view_type == "Card View":
        st.markdown(f"### {fact_filter} ({len(filtered_facts)} items)")
        
        if not filtered_facts:
            st.info("No facts found matching the selected criteria.")
        else:
            for fact in filtered_facts:
                render_fact_card(fact, args_data)
    
    elif view_type == "Table View":
        st.markdown(f"### {fact_filter} ({len(filtered_facts)} items)")
        
        if not filtered_facts:
            st.info("No facts found matching the selected criteria.")
        else:
            # Create DataFrame for table view
            df_data = []
            for fact in filtered_facts:
                evidence_text = ', '.join([f"{ex}" for ex in fact.get('exhibits', [])])
                df_data.append({
                    'Date': fact['date'],
                    'Event': fact['event'],
                    'Source Text': fact.get('source_text', '')[:100] + "..." if len(fact.get('source_text', '')) > 100 else fact.get('source_text', ''),
                    'Page': fact.get('page', ''),
                    'Document': fact.get('doc_name', ''),
                    'Claimant Submission': (fact.get('claimant_submission', 'No submission')[:100] + "...") if len(fact.get('claimant_submission', '')) > 100 else fact.get('claimant_submission', 'No submission'),
                    'Respondent Submission': (fact.get('respondent_submission', 'No submission')[:100] + "...") if len(fact.get('respondent_submission', '')) > 100 else fact.get('respondent_submission', 'No submission'),
                    'Status': 'Disputed' if fact['isDisputed'] else 'Undisputed',
                    'Evidence': evidence_text
                })
            
            df = pd.DataFrame(df_data)
            
            # Display with formatting
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Date": st.column_config.TextColumn("Date", width="small"),
                    "Event": st.column_config.TextColumn("Event", width="medium"),
                    "Source Text": st.column_config.TextColumn("Source Text", width="large"),
                    "Page": st.column_config.TextColumn("Page", width="small"),
                    "Document": st.column_config.TextColumn("Document", width="medium"),
                    "Status": st.column_config.TextColumn("Status", width="small"),
                    "Evidence": st.column_config.TextColumn("Evidence", width="medium")
                }
            )
    
    elif view_type == "Timeline View":
        st.markdown(f"### Timeline - {fact_filter} ({len(filtered_timeline)} items)")
        
        if not filtered_timeline:
            st.info("No timeline events found matching the selected criteria.")
        else:
            # Group by year for better organization
            current_year = ""
            for fact in filtered_timeline:
                # Extract year from date
                year = fact['date'][:4] if fact['date'] else ""
                if year != current_year:
                    st.markdown(f"## {year}")
                    current_year = year
                
                render_timeline_item(fact, args_data)
    
    elif view_type == "Document Categories":
        st.markdown("### Facts by Document Category")
        
        document_sets = get_document_sets()
        
        # Group facts by document category
        for doc_set in document_sets:
            with st.expander(f"📁 {doc_set['name']} ({doc_set['party']})", expanded=False):
                # Filter facts that might belong to this category
                category_facts = []
                for fact in filtered_facts:
                    # Simple categorization based on document name or party
                    if (doc_set['name'].lower() in fact.get('doc_name', '').lower() or
                        any(party in fact.get('parties_involved', []) for party in ['Appellant', 'Respondent'])):
                        category_facts.append(fact)
                
                if not category_facts:
                    st.info("No facts found for this document category.")
                else:
                    st.markdown(f"**{len(category_facts)} facts found**")
                    
                    # Create mini table for this category
                    df_data = []
                    for fact in category_facts:
                        df_data.append({
                            'Date': fact['date'],
                            'Event': fact['event'][:80] + "..." if len(fact['event']) > 80 else fact['event'],
                            'Page': fact.get('page', ''),
                            'Status': 'Disputed' if fact['isDisputed'] else 'Undisputed',
                            'Evidence': ', '.join(fact.get('exhibits', []))
                        })
                    
                    if df_data:
                        df = pd.DataFrame(df_data)
                        st.dataframe(df, use_container_width=True, hide_index=True)

elif view_option == "📑 Arguments":
    st.title("Legal Arguments")
    st.info("Arguments view functionality would be implemented here, showing the structured argument tree with claims, evidence, and legal reasoning.")

elif view_option == "📁 Exhibits":
    st.title("Case Exhibits")
    st.info("Exhibits view functionality would be implemented here, showing all evidence documents organized by type and relevance.")

# Footer
st.markdown("---")
st.markdown("*CaseLens - Legal Analysis Tool*")
