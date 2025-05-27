import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config with improved title and favicon
st.set_page_config(
    page_title="CaseLens | Legal Arguments Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"
if 'current_tab_type' not in st.session_state:
    st.session_state.current_tab_type = "all"

# Apply consistent styling with Streamlit native look
st.markdown("""
<style>
    /* Improve general text styling */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Enhance heading styles */
    h1, h2, h3, h4 {
        font-weight: 600 !important;
        letter-spacing: -0.01em !important;
    }
    
    h1 {
        font-size: 2.2rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Improve expander styling */
    .streamlit-expanderHeader {
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        padding: 0.75rem 1rem !important;
        border-radius: 0.5rem !important;
        background-color: #f8fafc !important;
        border: 1px solid rgba(0, 0, 0, 0.05) !important;
        margin-bottom: 0.5rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #f1f5f9 !important;
    }
    
    .streamlit-expanderContent {
        border-left: 1px solid rgba(0, 0, 0, 0.05) !important;
        border-right: 1px solid rgba(0, 0, 0, 0.05) !important;
        border-bottom: 1px solid rgba(0, 0, 0, 0.05) !important;
        border-radius: 0 0 0.5rem 0.5rem !important;
        padding: 1rem !important;
        margin-top: -0.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Improve button styling */
    .stButton > button {
        font-weight: 500 !important;
        border-radius: 0.5rem !important;
        transition: all 0.2s ease !important;
    }
    
    /* Improve tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
    }
    
    /* Style info boxes */
    .element-container .stAlert {
        border-radius: 0.5rem !important;
        border: 1px solid rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
    }
    
    /* Reduce cell padding in dataframes */
    .dataframe-container [data-testid="stDataFrame"] td, 
    .dataframe-container [data-testid="stDataFrame"] th {
        padding: 0.5rem 0.75rem !important;
    }
    
    /* Divider styling */
    hr {
        margin: 1.5rem 0 !important;
        border-color: rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Container styling */
    .evidence-container, .submission-container, .status-container {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8fafc;
        margin-bottom: 1rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    /* Consistent badge styling */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.85rem;
        font-weight: 500;
        margin-right: 0.5rem;
    }
    
    .badge-disputed {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    
    .badge-undisputed {
        background-color: #dcfce7;
        color: #15803d;
    }
    
    .badge-appellant {
        background-color: #dbeafe;
        color: #1e40af;
    }
    
    .badge-respondent {
        background-color: #ffedd5;
        color: #9a3412;
    }
    
    /* Logo styling */
    .logo-container {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .logo-text {
        margin-left: 0.75rem;
        font-weight: 600;
        color: #4338ca;
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

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

def render_streamlit_card_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    for i, fact in enumerate(facts_data):
        # Create a more visually appealing header for the expander
        date_display = f"**{fact['date']}**"
        status_icon = "🔴" if fact['isDisputed'] else "🟢"
        
        expander_title = f"{date_display} - {fact['event']} {status_icon}"
        
        with st.expander(expander_title, expanded=False):
            # Evidence and source references section
            st.markdown("### Evidence & Source References")
            evidence_content = get_evidence_content(fact)
            
            if evidence_content:
                for evidence in evidence_content:
                    with st.container():
                        # Evidence title with improved styling
                        st.markdown(f"#### {evidence['id']} - {evidence['title']}")
                        
                        # Document information in a styled container
                        if fact.get('doc_summary'):
                            with st.container():
                                st.markdown(f"**Document:** {fact['doc_name']}")
                                st.info(fact['doc_summary'])
                        
                        # Source text with better formatting
                        if fact.get('source_text'):
                            st.markdown("**Source Text:**")
                            st.markdown(f"<div style='padding: 0.75rem; background-color: #f1f5f9; border-radius: 0.5rem; font-style: italic;'>{fact['source_text']}</div>", unsafe_allow_html=True)
                        
                        # Reference information with better layout
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            ref_text = []
                            ref_text.append(f"**Exhibit:** {evidence['id']}")
                            if fact.get('page'):
                                ref_text.append(f"**Page:** {fact['page']}")
                            if fact.get('paragraphs'):
                                ref_text.append(f"**Paragraphs:** {fact['paragraphs']}")
                            
                            st.markdown(" | ".join(ref_text))
                        
                        with col2:
                            current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                            if st.button(f"📋 Copy Ref", key=f"copy_card_{evidence['id']}_{i}_{current_tab}", 
                                        help="Copy reference details to clipboard"):
                                ref_copy = f"Exhibit: {evidence['id']}"
                                if fact.get('page'):
                                    ref_copy += f", Page: {fact['page']}"
                                if fact.get('paragraphs'):
                                    ref_copy += f", Paragraphs: {fact['paragraphs']}"
                                st.success("Reference copied!")
                        
                        st.markdown("---")
            else:
                st.markdown("*No evidence references available for this fact*")
            
            # Party submissions section with improved styling
            st.markdown("### ⚖️ Party Submissions")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🔵 Appellant")
                claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                if claimant_text == 'No specific submission recorded':
                    st.markdown("*No submission provided*")
                else:
                    st.markdown(f"""
                    <div style="padding: 0.75rem; background-color: #dbeafe; border-radius: 0.5rem; border-left: 4px solid #2563eb;">
                        {claimant_text}
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### 🔴 Respondent")
                respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                if respondent_text == 'No specific submission recorded':
                    st.markdown("*No submission provided*")
                else:
                    st.markdown(f"""
                    <div style="padding: 0.75rem; background-color: #ffedd5; border-radius: 0.5rem; border-left: 4px solid #ea580c;">
                        {respondent_text}
                    </div>
                    """, unsafe_allow_html=True)
            
            # Status section with improved visual indicators
            st.markdown("### 📊 Status")
            
            status_col1, status_col2 = st.columns(2)
            
            with status_col1:
                if fact['isDisputed']:
                    st.markdown("""
                    <div style="display: inline-block; padding: 0.5rem 0.75rem; background-color: #fee2e2; border-radius: 0.5rem; color: #b91c1c; font-weight: 500;">
                        <span>⚠️ Disputed</span>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="display: inline-block; padding: 0.5rem 0.75rem; background-color: #dcfce7; border-radius: 0.5rem; color: #15803d; font-weight: 500;">
                        <span>✓ Undisputed</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            with status_col2:
                if fact.get('parties_involved'):
                    parties = fact.get('parties_involved', [])
                    party_badges = []
                    
                    for party in parties:
                        if party == "Appellant":
                            party_badges.append("""
                            <div style="display: inline-block; margin-right: 0.5rem; padding: 0.5rem 0.75rem; background-color: #dbeafe; border-radius: 0.5rem; color: #1e40af; font-weight: 500;">
                                <span>🔵 Appellant</span>
                            </div>
                            """)
                        else:
                            party_badges.append("""
                            <div style="display: inline-block; margin-right: 0.5rem; padding: 0.5rem 0.75rem; background-color: #ffedd5; border-radius: 0.5rem; color: #9a3412; font-weight: 500;">
                                <span>🔴 Respondent</span>
                            </div>
                            """)
                    
                    st.markdown("".join(party_badges), unsafe_allow_html=True)

def render_streamlit_table_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    # Improved table styling
    st.markdown("""
    <style>
    .dataframe-container {
        border-radius: 0.5rem;
        overflow: hidden;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .dataframe-container [data-testid="stDataFrame"] {
        border-radius: 0.5rem;
    }
    
    .dataframe-container th {
        background-color: #f8fafc !important;
        font-weight: 600 !important;
    }
    
    .dataframe-container tr:nth-child(even) {
        background-color: #f8fafc !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    table_data = []
    for fact in facts_data:
        # Improved status indicator
        status_display = '🔴 Disputed' if fact['isDisputed'] else '🟢 Undisputed'
        
        table_data.append({
            'Date': fact['date'],
            'Event': fact['event'],
            'Status': status_display,
            'Parties': ', '.join(fact.get('parties_involved', [])),
            'Exhibits': ', '.join(fact.get('exhibits', [])),
            'Page': fact.get('page', ''),
            'Document': fact.get('doc_name', '')
        })
    
    df = pd.DataFrame(table_data)
    
    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add download button for table data
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<div style="text-align: right; margin-top: 10px;"><a href="data:file/csv;base64,{b64}" download="case_facts.csv" style="text-decoration: none; color: #4338ca; font-size: 0.9rem; font-weight: 500;"><span style="vertical-align: middle;">📥 Download as CSV</span></a></div>'
    st.markdown(href, unsafe_allow_html=True)

def render_streamlit_docset_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
        
    document_sets = get_document_sets()
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
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
    
    # Create a grid layout for document categories
    cols = st.columns(2)
    col_idx = 0
    
    for docset_id, doc_with_facts in docs_with_facts.items():
        docset = doc_with_facts['docset']
        facts = doc_with_facts['facts']
        
        # Create party indicator with appropriate styling
        if docset['party'] == 'Appellant':
            party_indicator = """<span style="display: inline-block; margin-right: 0.5rem; width: 1rem; height: 1rem; border-radius: 50%; background-color: #3b82f6;"></span>"""
        elif docset['party'] == 'Respondent':
            party_indicator = """<span style="display: inline-block; margin-right: 0.5rem; width: 1rem; height: 1rem; border-radius: 50%; background-color: #ef4444;"></span>"""
        else:
            party_indicator = """<span style="display: inline-block; margin-right: 0.5rem; width: 1rem; height: 1rem; border-radius: 50%; background: linear-gradient(135deg, #3b82f6 50%, #ef4444 50%);"></span>"""
        
        with cols[col_idx]:
            with st.expander(f"📁 {party_indicator} **{docset['name'].title()}** ({len(facts)} facts)", expanded=False):
                if facts:
                    for i, fact in enumerate(facts):
                        with st.container():
                            # Improved fact header
                            st.markdown(f"""
                            <div style="display: flex; align-items: center; margin-bottom: 0.5rem; background-color: #f8fafc; padding: 0.75rem; border-radius: 0.5rem;">
                                <div style="min-width: 100px; font-weight: 600;">{fact['date']}</div>
                                <div style="flex-grow: 1; font-weight: 500; margin-left: 1rem;">{fact['event']}</div>
                                <div style="min-width: 30px; text-align: center;">{('🔴' if fact['isDisputed'] else '🟢')}</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Evidence section with improved styling
                            with st.container():
                                st.markdown("#### Evidence & References")
                                evidence_content = get_evidence_content(fact)
                                
                                if evidence_content:
                                    for evidence_idx, evidence in enumerate(evidence_content):
                                        with st.container():
                                            # Improved evidence card styling
                                            st.markdown(f"""
                                            <div style="padding: 0.75rem; background-color: #f8fafc; border-radius: 0.5rem; margin-bottom: 0.75rem; border-left: 3px solid #6366f1;">
                                                <div style="font-weight: 600; color: #4338ca; margin-bottom: 0.5rem;">{evidence['id']} - {evidence['title']}</div>
                                                <div style="font-size: 0.9rem; color: #64748b; margin-bottom: 0.5rem;">{evidence['summary']}</div>
                                            </div>
                                            """, unsafe_allow_html=True)
                                            
                                            if fact.get('source_text'):
                                                with st.expander("Show Source Text", expanded=False):
                                                    st.markdown(f"*{fact['source_text']}*")
                                            
                                            # Reference details with copy button
                                            col1, col2 = st.columns([3, 1])
                                            with col1:
                                                ref_details = []
                                                ref_details.append(f"**Exhibit:** {evidence['id']}")
                                                if fact.get('page'):
                                                    ref_details.append(f"**Page:** {fact['page']}")
                                                if fact.get('paragraphs'):
                                                    ref_details.append(f"**Paragraphs:** {fact['paragraphs']}")
                                                
                                                st.markdown(" | ".join(ref_details))
                                            
                                            with col2:
                                                current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                                                unique_key = f"copy_docset_{docset_id}_{i}_{evidence_idx}_{evidence['id']}_{current_tab}"
                                                if st.button(f"📋 Copy", key=unique_key):
                                                    ref_copy = f"Exhibit: {evidence['id']}"
                                                    if fact.get('page'):
                                                        ref_copy += f", Page: {fact['page']}"
                                                    if fact.get('paragraphs'):
                                                        ref_copy += f", Paragraphs: {fact['paragraphs']}"
                                                    st.success("Reference copied!")
                                else:
                                    st.markdown("""
                                    <div style="padding: 0.75rem; background-color: #f8fafc; border-radius: 0.5rem; color: #64748b; font-style: italic;">
                                        No evidence references available
                                    </div>
                                    """, unsafe_allow_html=True)
                            
                            # Party submissions with improved tabs
                            st.markdown("#### Party Submissions")
                            tabs = st.tabs(["🔵 Appellant", "🔴 Respondent"])
                            
                            with tabs[0]:
                                claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                                if claimant_text == 'No specific submission recorded':
                                    st.markdown("*No submission provided*")
                                else:
                                    st.markdown(f"""
                                    <div style="padding: 0.75rem; background-color: #dbeafe; border-radius: 0.5rem; border-left: 4px solid #2563eb;">
                                        {claimant_text}
                                    </div>
                                    """, unsafe_allow_html=True)
                            
                            with tabs[1]:
                                respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                                if respondent_text == 'No specific submission recorded':
                                    st.markdown("*No submission provided*")
                                else:
                                    st.markdown(f"""
                                    <div style="padding: 0.75rem; background-color: #ffedd5; border-radius: 0.5rem; border-left: 4px solid #ea580c;">
                                        {respondent_text}
                                    </div>
                                    """, unsafe_allow_html=True)
                            
                            if i < len(facts) - 1:
                                st.divider()
                else:
                    st.info("No facts found in this document category.")
        
        # Alternate columns for balanced layout
        col_idx = 1 - col_idx

def render_view_content(view_type, filtered_facts):
    if view_type == "card":
        render_streamlit_card_view(filtered_facts)
    elif view_type == "table":
        render_streamlit_table_view(filtered_facts)
    elif view_type == "docset":
        render_streamlit_docset_view(filtered_facts)
    else:
        render_streamlit_card_view(filtered_facts)

def main():
    # Add Streamlit sidebar with improved styling
    with st.sidebar:
        # Improved logo and branding
        st.markdown("""
        <div class="logo-container">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="38" height="38">
              <mask id="mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#mask)">
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4338ca"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <span class="logo-text">CaseLens</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top: 0;'>Legal Analysis</h3>", unsafe_allow_html=True)
        
        # Improved sidebar navigation
        st.markdown("""
        <style>
        .sidebar-nav-button {
            width: 100%;
            border-radius: 0.5rem;
            height: 3rem;
            margin-bottom: 0.75rem;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            padding: 0 1rem;
            background-color: white;
            border: 1px solid rgba(0, 0, 0, 0.05);
            cursor: pointer;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
            text-decoration: none;
            color: #1e293b;
        }
        
        .sidebar-nav-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            background-color: #f8fafc;
        }
        
        .sidebar-nav-button-icon {
            margin-right: 0.75rem;
            font-size: 1.2rem;
        }
        
        .sidebar-nav-button-text {
            font-weight: 500;
        }
        
        .sidebar-nav-button-active {
            background-color: #f1f5f9;
            border-left: 3px solid #4338ca;
        }
        </style>
        """, unsafe_allow_html=True)
        
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Arguments button
        args_active = "sidebar-nav-button-active" if st.session_state.view == "Arguments" else ""
        args_button = st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        if args_button:
            st.session_state.view = "Arguments"
            st.rerun()
            
        # Facts button    
        facts_active = "sidebar-nav-button-active" if st.session_state.view == "Facts" else ""
        facts_button = st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        if facts_button:
            st.session_state.view = "Facts"
            st.rerun()
            
        # Exhibits button
        exhibits_active = "sidebar-nav-button-active" if st.session_state.view == "Exhibits" else ""
        exhibits_button = st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
        if exhibits_button:
            st.session_state.view = "Exhibits"
            st.rerun()
        
        # Add case information
        st.markdown("---")
        st.markdown("### Case Information")
        st.markdown("""
        <div style="background-color: white; padding: 1rem; border-radius: 0.5rem; border: 1px solid rgba(0, 0, 0, 0.05);">
            <div style="font-weight: 600; margin-bottom: 0.5rem;">Athletic Club United v. Federation</div>
            <div style="font-size: 0.9rem; color: #64748b; margin-bottom: 0.5rem;">Case No. CAS 2024/A/8765</div>
            <div style="font-size: 0.9rem; color: #64748b;">Sporting Succession Dispute</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add helpful resources section
        st.markdown("### Resources")
        st.markdown("""
        <div style="font-size: 0.9rem; color: #64748b;">
            <div style="margin-bottom: 0.5rem;"><a href="#" style="text-decoration: none; color: #4338ca;">📄 Case Summary</a></div>
            <div style="margin-bottom: 0.5rem;"><a href="#" style="text-decoration: none; color: #4338ca;">🔍 Search Documents</a></div>
            <div><a href="#" style="text-decoration: none; color: #4338ca;">🧠 AI Analysis</a></div>
        </div>
        """, unsafe_allow_html=True)
    
    # Create the facts view with improved styling
    if st.session_state.view == "Facts":
        # Header with improved layout
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
            <h1 style="margin: 0;">Case Facts</h1>
            <div style="display: flex; gap: 0.75rem;">
                <button id="copy-btn" style="display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background-color: white; border: 1px solid rgba(0, 0, 0, 0.1); border-radius: 0.5rem; cursor: pointer; transition: all 0.2s; font-weight: 500;">
                    <span>📋 Copy</span>
                </button>
                <button id="export-btn" style="display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background-color: white; border: 1px solid rgba(0, 0, 0, 0.1); border-radius: 0.5rem; cursor: pointer; transition: all 0.2s; font-weight: 500;">
                    <span>📥 Export</span>
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons for copy and export
        col_actions = st.columns([6, 1, 1])
        
        with col_actions[1]:
            if st.button("📋 Copy", use_container_width=True, type="secondary", help="Copy facts to clipboard"):
                st.success("Facts copied to clipboard!")
        
        with col_actions[2]:
            if st.button("📥 Export", use_container_width=True, type="secondary", help="Export facts as PDF"):
                st.success("Facts exported!")
        
        # Improved view switcher with tabs-like appearance
        st.markdown("""
        <style>
        /* Custom view switcher styling */
        .view-switcher {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin: 1.5rem 0;
        }
        
        .view-option {
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
            min-width: 160px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }
        
        .view-option-active {
            background-color: #4338ca;
            color: white;
            box-shadow: 0 2px 4px rgba(67, 56, 202, 0.2);
        }
        
        .view-option-inactive {
            background-color: white;
            color: #64748b;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        
        .view-option-inactive:hover {
            background-color: #f8fafc;
            color: #334155;
            transform: translateY(-2px);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        </style>
        
        <div class="view-switcher">
            <div class="view-option {('view-option-active' if st.session_state.current_view_type == 'card' else 'view-option-inactive')}" id="card-view-option">
                <span>📇</span>
                <span>Card View</span>
            </div>
            <div class="view-option {('view-option-active' if st.session_state.current_view_type == 'table' else 'view-option-inactive')}" id="table-view-option">
                <span>📊</span>
                <span>Table View</span>
            </div>
            <div class="view-option {('view-option-active' if st.session_state.current_view_type == 'docset' else 'view-option-inactive')}" id="docset-view-option">
                <span>📁</span>
                <span>Document Categories</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # View switcher buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("Card View", 
                        type="primary" if st.session_state.current_view_type == "card" else "secondary",
                        key="card_view_btn",
                        use_container_width=True):
                st.session_state.current_view_type = "card"
                st.rerun()
        
        with col2:
            if st.button("Table View", 
                        type="primary" if st.session_state.current_view_type == "table" else "secondary",
                        key="table_view_btn",
                        use_container_width=True):
                st.session_state.current_view_type = "table"
                st.rerun()
        
        with col3:
            if st.button("Document Categories", 
                        type="primary" if st.session_state.current_view_type == "docset" else "secondary",
                        key="docset_view_btn",
                        use_container_width=True):
                st.session_state.current_view_type = "docset"
                st.rerun()
        
        # Improved filter tabs with badges
        tab_styles = """
        <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 0.5rem;
            padding: 0.75rem 1.25rem;
            font-weight: 500;
        }
        
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: #4338ca;
            border-radius: 0.5rem;
        }
        
        .tab-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 1.5rem;
            height: 1.5rem;
            padding: 0 0.5rem;
            border-radius: 9999px;
            background-color: #e2e8f0;
            color: #475569;
            font-size: 0.75rem;
            margin-left: 0.5rem;
        }
        </style>
        """
        
        st.markdown(tab_styles, unsafe_allow_html=True)
        
        # Count facts for badges
        all_facts = get_all_facts()
        disputed_facts = [fact for fact in all_facts if fact['isDisputed']]
        undisputed_facts = [fact for fact in all_facts if not fact['isDisputed']]
        
        # Custom tab labels with badges
        tab1_label = f"All Facts ({len(all_facts)})"
        tab2_label = f"Disputed Facts ({len(disputed_facts)})"
        tab3_label = f"Undisputed Facts ({len(undisputed_facts)})"
        
        # Facts filter tabs
        tab1, tab2, tab3 = st.tabs([tab1_label, tab2_label, tab3_label])
        
        with tab1:
            st.session_state.current_tab_type = "all"
            filtered_facts = all_facts
            render_view_content(st.session_state.current_view_type, filtered_facts)
        
        with tab2:
            st.session_state.current_tab_type = "disputed"
            filtered_facts = disputed_facts
            render_view_content(st.session_state.current_view_type, filtered_facts)
        
        with tab3:
            st.session_state.current_tab_type = "undisputed"
            filtered_facts = undisputed_facts
            render_view_content(st.session_state.current_view_type, filtered_facts)

if __name__ == "__main__":
    main()
