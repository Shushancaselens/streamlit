import streamlit as st
import json
import pandas as pd
import base64
from datetime import datetime

# Set page config with better styling
st.set_page_config(
    page_title="CaseLens - Legal Analysis", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "CaseLens - Advanced Legal Case Analysis Tool"
    }
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 1rem;
        text-align: center;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 1rem;
    }
    
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 1.5rem 0 1rem 0;
        padding: 0.5rem 0;
        border-left: 4px solid #3498db;
        padding-left: 1rem;
    }
    
    .fact-card {
        border: 1px solid #e1e5e9;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        background: #f8f9fa;
    }
    
    .party-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    .appellant-badge {
        background-color: #e3f2fd;
        color: #1976d2;
        border: 1px solid #bbdefb;
    }
    
    .respondent-badge {
        background-color: #ffebee;
        color: #d32f2f;
        border: 1px solid #ffcdd2;
    }
    
    .disputed-indicator {
        background-color: #fff3e0;
        color: #f57c00;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .undisputed-indicator {
        background-color: #e8f5e8;
        color: #2e7d32;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .timeline-event {
        position: relative;
        padding-left: 2rem;
        margin-bottom: 2rem;
        border-left: 3px solid #3498db;
    }
    
    .timeline-event::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background-color: #3498db;
    }
    
    .evidence-tag {
        background-color: #f1f3f4;
        color: #5f6368;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
        margin: 0.25rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = "Facts"
if 'current_view' not in st.session_state:
    st.session_state.current_view = "Card View"
if 'selected_filter' not in st.session_state:
    st.session_state.selected_filter = "All Facts"

# Data functions (keeping the same data structure)
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
                'summary': evidence['summary']
            })
        else:
            evidence_content.append({
                'id': exhibit_id,
                'title': exhibit_id,
                'summary': 'Evidence details not available'
            })
    
    return evidence_content

# Improved UI Components
def render_header():
    st.markdown('<div class="main-header">⚖️ CaseLens Legal Analysis</div>', unsafe_allow_html=True)
    st.markdown("---")

def render_sidebar():
    with st.sidebar:
        st.markdown("### 🏛️ Case Navigation")
        
        # Navigation buttons with better styling
        sections = ["📊 Facts", "📑 Arguments", "📁 Exhibits"]
        current_section = st.radio(
            "Select Section:",
            sections,
            index=0,
            key="section_nav"
        )
        
        st.session_state.current_section = current_section.split(" ", 1)[1]  # Remove emoji
        
        st.markdown("---")
        
        # Case summary metrics
        facts_data = get_all_facts()
        total_facts = len(facts_data)
        disputed_facts = len([f for f in facts_data if f['isDisputed']])
        undisputed_facts = total_facts - disputed_facts
        
        st.markdown("### 📈 Case Summary")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Facts", total_facts)
            st.metric("Disputed", disputed_facts, delta=f"{disputed_facts/total_facts*100:.0f}%")
        with col2:
            st.metric("Undisputed", undisputed_facts, delta=f"{undisputed_facts/total_facts*100:.0f}%")
        
        st.markdown("---")
        
        # Quick filters
        st.markdown("### 🔍 Quick Filters")
        filter_options = ["All Facts", "Disputed Only", "Undisputed Only", "Appellant Claims", "Respondent Claims"]
        st.session_state.selected_filter = st.selectbox(
            "Filter by:",
            filter_options,
            key="fact_filter"
        )

def render_fact_card(fact, index):
    with st.container():
        # Card header with status and date
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown(f"### {fact['event']}")
        
        with col2:
            if fact['isDisputed']:
                st.markdown('<span class="disputed-indicator">⚠️ DISPUTED</span>', unsafe_allow_html=True)
            else:
                st.markdown('<span class="undisputed-indicator">✅ UNDISPUTED</span>', unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"**📅 {fact['date']}**")
        
        # Parties involved
        if fact.get('parties_involved'):
            party_tags = ""
            for party in fact['parties_involved']:
                if party == 'Appellant':
                    party_tags += '<span class="party-badge appellant-badge">🔵 Appellant</span>'
                else:
                    party_tags += '<span class="party-badge respondent-badge">🔴 Respondent</span>'
            st.markdown(party_tags, unsafe_allow_html=True)
        
        # Expandable details
        with st.expander("📋 View Details", expanded=False):
            # Tabs for different content
            tab1, tab2, tab3 = st.tabs(["📝 Submissions", "📁 Evidence", "ℹ️ Source"])
            
            with tab1:
                st.markdown("#### 🔵 Appellant Submission")
                if fact['claimant_submission'] != 'No specific submission recorded':
                    st.info(fact['claimant_submission'])
                else:
                    st.markdown("*No submission provided*")
                
                st.markdown("#### 🔴 Respondent Submission")
                if fact['respondent_submission'] != 'No specific submission recorded':
                    st.warning(fact['respondent_submission'])
                else:
                    st.markdown("*No submission provided*")
            
            with tab2:
                evidence_content = get_evidence_content(fact)
                if evidence_content:
                    for evidence in evidence_content:
                        st.markdown(f"**{evidence['id']}** - {evidence['title']}")
                        st.caption(evidence['summary'])
                        st.markdown('<span class="evidence-tag">📎 Evidence</span>', unsafe_allow_html=True)
                else:
                    st.info("No evidence references available")
            
            with tab3:
                info_col1, info_col2 = st.columns(2)
                with info_col1:
                    if fact.get('doc_name'):
                        st.markdown(f"**Document:** {fact['doc_name']}")
                    if fact.get('page'):
                        st.markdown(f"**Page:** {fact['page']}")
                with info_col2:
                    if fact.get('paragraphs'):
                        st.markdown(f"**Paragraphs:** {fact['paragraphs']}")
                    if fact.get('argId'):
                        st.markdown(f"**Argument ID:** {fact['argId']}")
        
        st.markdown("---")

def render_timeline_view(facts):
    st.markdown('<div class="section-header">📅 Timeline View</div>', unsafe_allow_html=True)
    
    # Sort facts by date
    sorted_facts = sorted(facts, key=lambda x: x['date'])
    
    # Group by year
    years = {}
    for fact in sorted_facts:
        year = fact['date'].split('-')[0] if '-' in fact['date'] else fact['date'][:4]
        if year not in years:
            years[year] = []
        years[year].append(fact)
    
    for year, year_facts in years.items():
        st.markdown(f"## 📆 {year}")
        
        for fact in year_facts:
            st.markdown('<div class="timeline-event">', unsafe_allow_html=True)
            
            # Event header
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{fact['date']}** - {fact['event']}")
            with col2:
                if fact['isDisputed']:
                    st.error("Disputed")
                else:
                    st.success("Undisputed")
            
            # Quick summary
            if fact.get('source_text'):
                with st.expander("View Details"):
                    st.info(fact['source_text'])
                    
                    # Evidence tags
                    if fact.get('exhibits'):
                        evidence_tags = " ".join([f'<span class="evidence-tag">{ex}</span>' for ex in fact['exhibits']])
                        st.markdown(evidence_tags, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")

def render_card_view(facts):
    st.markdown('<div class="section-header">📋 Card View</div>', unsafe_allow_html=True)
    
    if not facts:
        st.info("No facts match the current filter criteria.")
        return
    
    # Sort facts by date
    sorted_facts = sorted(facts, key=lambda x: x['date'])
    
    for i, fact in enumerate(sorted_facts):
        render_fact_card(fact, i)

def render_summary_view(facts):
    st.markdown('<div class="section-header">📊 Summary Dashboard</div>', unsafe_allow_html=True)
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    total_facts = len(facts)
    disputed = len([f for f in facts if f['isDisputed']])
    undisputed = total_facts - disputed
    unique_exhibits = len(set([ex for f in facts for ex in f.get('exhibits', [])]))
    
    with col1:
        st.metric("Total Facts", total_facts)
    with col2:
        st.metric("Disputed Facts", disputed, delta=f"{disputed/total_facts*100:.1f}%" if total_facts > 0 else "0%")
    with col3:
        st.metric("Undisputed Facts", undisputed, delta=f"{undisputed/total_facts*100:.1f}%" if total_facts > 0 else "0%")
    with col4:
        st.metric("Evidence Items", unique_exhibits)
    
    st.markdown("---")
    
    # Facts by year chart
    if facts:
        years_data = {}
        for fact in facts:
            year = fact['date'].split('-')[0] if '-' in fact['date'] else fact['date'][:4]
            if year not in years_data:
                years_data[year] = {'disputed': 0, 'undisputed': 0}
            if fact['isDisputed']:
                years_data[year]['disputed'] += 1
            else:
                years_data[year]['undisputed'] += 1
        
        # Create DataFrame for chart
        chart_data = []
        for year, data in years_data.items():
            chart_data.append({'Year': int(year), 'Disputed': data['disputed'], 'Undisputed': data['undisputed']})
        
        if chart_data:
            df = pd.DataFrame(chart_data)
            st.markdown("### 📈 Facts Distribution by Year")
            st.bar_chart(df.set_index('Year')[['Disputed', 'Undisputed']])

def filter_facts(facts, filter_type):
    if filter_type == "All Facts":
        return facts
    elif filter_type == "Disputed Only":
        return [f for f in facts if f['isDisputed']]
    elif filter_type == "Undisputed Only":
        return [f for f in facts if not f['isDisputed']]
    elif filter_type == "Appellant Claims":
        return [f for f in facts if 'Appellant' in f.get('parties_involved', [])]
    elif filter_type == "Respondent Claims":
        return [f for f in facts if 'Respondent' in f.get('parties_involved', [])]
    return facts

def main():
    render_header()
    render_sidebar()
    
    # Main content area
    if st.session_state.current_section == "Facts":
        facts_data = get_all_facts()
        filtered_facts = filter_facts(facts_data, st.session_state.selected_filter)
        
        # View selection tabs
        tab1, tab2, tab3 = st.tabs(["📋 Card View", "📅 Timeline", "📊 Summary"])
        
        with tab1:
            render_card_view(filtered_facts)
        
        with tab2:
            render_timeline_view(filtered_facts)
        
        with tab3:
            render_summary_view(filtered_facts)
    
    elif st.session_state.current_section == "Arguments":
        st.markdown('<div class="section-header">📑 Legal Arguments</div>', unsafe_allow_html=True)
        st.info("Arguments section - Coming soon! This will display the structured legal arguments from both parties.")
        
        # Placeholder for arguments structure
        args_data = get_argument_data()
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔵 Appellant Arguments")
            for arg_id, arg in args_data['claimantArgs'].items():
                with st.expander(f"{arg['title']} (¶{arg['paragraphs']})"):
                    for point in arg['overview']['points']:
                        st.markdown(f"• {point}")
        
        with col2:
            st.markdown("### 🔴 Respondent Arguments")
            for arg_id, arg in args_data['respondentArgs'].items():
                with st.expander(f"{arg['title']} (¶{arg['paragraphs']})"):
                    for point in arg['overview']['points']:
                        st.markdown(f"• {point}")
    
    elif st.session_state.current_section == "Exhibits":
        st.markdown('<div class="section-header">📁 Evidence & Exhibits</div>', unsafe_allow_html=True)
        st.info("Exhibits section - Coming soon! This will display all evidence and supporting documents.")
        
        # Show evidence summary
        facts_data = get_all_facts()
        all_exhibits = set()
        for fact in facts_data:
            all_exhibits.update(fact.get('exhibits', []))
        
        st.markdown(f"### Total Evidence Items: {len(all_exhibits)}")
        
        exhibit_cols = st.columns(3)
        for i, exhibit in enumerate(sorted(all_exhibits)):
            with exhibit_cols[i % 3]:
                st.markdown(f"**{exhibit}**")
                evidence_details = get_evidence_content({'exhibits': [exhibit]})
                if evidence_details:
                    st.caption(evidence_details[0]['title'])

if __name__ == "__main__":
    main()
